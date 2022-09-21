"""Module for managing Firebolt credentials."""

from typing import Optional

from firebolt.client.constants import DEFAULT_API_URL
from prefect.blocks.core import Block
from pydantic import Field, SecretStr, root_validator


class FireboltCredentials(Block):
    """
    Store credentials for authenticating with Firebolt.

    Attributes:
        username: The email address associated with your Firebolt user.
        password: The password used for connecting to Firebolt.
        token: Authentication token to use instead of username and password.
        api_endpoint: Firebolt API endpoint used for authentication.
        account_name: Name of the account to authenticate with.
            If not provided, the default account will be used.
    """

    _block_type_name = "Firebolt Credentials"
    _logo_url = "https://images.ctfassets.net/gm98wzqotmnx/3loU17IXqVIWl4aWQfqc78/3c7eefe5e8cf4eec870856f10d7fdcce/5e8a264ceaf4870c90478037_Favicon_128.svg.png?h=250"  # noqa

    @root_validator
    def _ensure_valid_auth_method(cls, values):
        """
        Checks to make sure that either username and password or a token is provided.
        """
        has_username = values.get("username") is not None
        has_password = values.get("password") is not None
        has_token = values.get("token") is not None

        # No auth details provided
        if not any([has_password, has_username, has_token]):
            raise ValueError(
                "You have not provided a username/password or token. "
                "Please provide either a username and password or a token."
            )
        # Username/password and token provided
        if (has_username or has_password) and has_token:
            raise ValueError(
                "You have provided both a username/password and a token. "
                "Please provide either a username and password or a token."
            )
        # Username/password not provided together
        if has_username ^ has_password:
            raise ValueError(
                "You have provided only a username or password. "
                "Please provide both a username and a password."
            )
        return values

    username: Optional[str] = Field(
        default=None,
        description="The email address associated with your Firebolt user.",
    )
    password: Optional[SecretStr] = Field(
        default=None, description="The password used for connecting to Firebolt."
    )
    token: Optional[SecretStr] = Field(
        default=None,
        description="Authentication token to use instead of username and password.",
    )
    api_endpoint: str = Field(
        default=DEFAULT_API_URL,
        title="API Endpoint",
        description="Firebolt API endpoint used for authentication.",
    )
    account_name: Optional[str] = Field(
        default=None,
        description="Name of the account to authenticate with. If not "
        "provided, the default account will be used.",
    )
