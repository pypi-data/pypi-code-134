"""
This plugin searches for AWS key IDs
"""
import hashlib
import hmac
import re
import string
import textwrap
from datetime import datetime
from typing import cast
from typing import List
from typing import Union

import requests

from ..constants import VerifiedResult
from ..util.code_snippet import CodeSnippet
from .base import RegexBasedDetector


class AWSKeyDetector(RegexBasedDetector):
    """Scans for AWS keys."""
    secret_type = 'AWS Access Key'

    secret_keyword = r'(?:key|pwd|pw|password|pass|token)'

    denylist = (
        re.compile(r'AKIA[0-9A-Z]{16}'),

        # This examines the variable name to identify AWS secret tokens.
        # The order is important since we want to prefer finding `AKIA`-based
        # keys (since they can be verified), rather than the secret tokens.

        re.compile(
            r'aws.{{0,20}}?{secret_keyword}.{{0,20}}?[\'\"]([0-9a-zA-Z/+]{{40}})[\'\"]'.format(
                secret_keyword=secret_keyword,
            ),
            flags=re.IGNORECASE,
        ),
    )

    def verify(       # type: ignore[override]  # noqa: F821
        self,
        secret: str,
        context: CodeSnippet,
    ) -> VerifiedResult:
        # As this verification process looks for multi-factor secrets, by assuming that
        # the identified secret token is the key ID (then looking for the corresponding secret).
        # we quit early if it fails our assumptions.
        if not self.denylist[0].match(secret):
            return VerifiedResult.UNVERIFIED
        secret_access_key_candidates = get_secret_access_keys(context)
        if not secret_access_key_candidates:
            return VerifiedResult.UNVERIFIED

        for candidate in secret_access_key_candidates:
            if verify_aws_secret_access_key(secret, candidate):
                return VerifiedResult.VERIFIED_TRUE

        return VerifiedResult.VERIFIED_FALSE


def get_secret_access_keys(content: CodeSnippet) -> List[str]:
    # AWS secret access keys are 40 characters long.
    # e.g. some_function('AKIA...', '[secret key]')
    # e.g. secret_access_key = '[secret key]'
    regex = re.compile(
        r'(=|,|\() *([\'"]?)([%s]{40})(\2)(\))?' % (
            re.escape(string.ascii_letters + string.digits + '+/=')
        ),
    )

    return [
        match[2]
        for line in content
        for match in regex.findall(line)
    ]


def verify_aws_secret_access_key(key: str, secret: str) -> bool:  # pragma: no cover
    """
    Using requests, because we don't want to require boto3 for this one
    optional verification step.

    Loosely based off:
    https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html
    """
    now = datetime.utcnow()
    amazon_datetime = now.strftime('%Y%m%dT%H%M%SZ')

    headers = {
        # This is a required header for the signing process
        'Host': 'sts.amazonaws.com',
        'X-Amz-Date': amazon_datetime,
    }
    body = {
        'Action': 'GetCallerIdentity',
        'Version': '2011-06-15',
    }

    # Step #1: Canonical Request
    signed_headers = ';'.join(
        map(
            lambda x: x.lower(),
            headers.keys(),
        ),
    )
    canonical_request = textwrap.dedent("""
        POST
        /

        {headers}

        {signed_headers}
        {hashed_payload}
    """)[1:-1].format(

        headers='\n'.join([
            '{}:{}'.format(header.lower(), value)
            for header, value in headers.items()
        ]),
        signed_headers=signed_headers,

        # Poor man's method, but works for this use case.
        hashed_payload=hashlib.sha256(
            '&'.join([
                '{}={}'.format(header, value)
                for header, value in body.items()
            ]).encode('utf-8'),
        ).hexdigest(),
    )

    # Step #2: String to Sign
    region = 'us-east-1'
    scope = '{request_date}/{region}/sts/aws4_request'.format(
        request_date=now.strftime('%Y%m%d'),

        # STS is a global service; this is just for latency control.
        region=region,
    )

    string_to_sign = textwrap.dedent("""
        AWS4-HMAC-SHA256
        {request_datetime}
        {scope}
        {hashed_canonical_request}
    """)[1:-1].format(
        request_datetime=amazon_datetime,
        scope=scope,
        hashed_canonical_request=hashlib.sha256(
            canonical_request.encode('utf-8'),
        ).hexdigest(),
    )

    # Step #3: Calculate signature
    signing_key = _sign(
        cast(
            bytes, _sign(
                cast(
                    bytes, _sign(
                        cast(
                            bytes, _sign(
                                'AWS4{}'.format(secret).encode('utf-8'),
                                now.strftime('%Y%m%d'),
                            ),
                        ),
                        region,
                    ),
                ),
                'sts',
            ),
        ),
        'aws4_request',
    )

    signature = _sign(
        cast(bytes, signing_key),
        string_to_sign,
        hex=True,
    )

    # Step #4: Add to request headers
    headers['Authorization'] = (
        'AWS4-HMAC-SHA256 '
        f'Credential={key}/{scope}, '
        f'SignedHeaders={signed_headers}, '
        f'Signature={cast(str, signature)}'
    )

    # Step #5: Finally send the request
    response = requests.post(
        'https://sts.amazonaws.com',
        headers=headers,
        data=body,
    )

    if response.status_code == 403:
        return False

    return True


def _sign(key: bytes, message: str, hex: bool = False) -> Union[str, bytes]:  # pragma: no cover
    value = hmac.new(key, message.encode('utf-8'), hashlib.sha256)
    if not hex:
        return value.digest()

    return value.hexdigest()
