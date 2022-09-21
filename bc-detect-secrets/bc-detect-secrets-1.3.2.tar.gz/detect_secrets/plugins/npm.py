"""
This plugin searches for NPM tokens
"""
import re

from detect_secrets.plugins.base import RegexBasedDetector


class NpmDetector(RegexBasedDetector):
    """Scans for NPM tokens."""
    secret_type = 'NPM tokens'

    denylist = [
        # npmrc authToken
        # ref. https://stackoverflow.com/questions/53099434/using-auth-tokens-in-npmrc
        re.compile(r'\/\/.+\/:_authToken=\s*((npm_.+)|([A-Fa-f0-9-]{36})).*'),
    ]
