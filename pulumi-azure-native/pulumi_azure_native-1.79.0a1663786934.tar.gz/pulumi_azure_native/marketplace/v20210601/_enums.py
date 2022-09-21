# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'Accessibility',
]


class Accessibility(str, Enum):
    """
    Plan accessibility
    """
    UNKNOWN = "Unknown"
    PUBLIC = "Public"
    PRIVATE_TENANT_ON_LEVEL = "PrivateTenantOnLevel"
    PRIVATE_SUBSCRIPTION_ON_LEVEL = "PrivateSubscriptionOnLevel"
