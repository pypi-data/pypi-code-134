# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'Kind',
    'Type',
]


class Kind(str, Enum):
    """
    Responsibility role under which this Managed Network Group will be created
    """
    CONNECTIVITY = "Connectivity"


class Type(str, Enum):
    """
    Gets or sets the connectivity type of a network structure policy
    """
    HUB_AND_SPOKE_TOPOLOGY = "HubAndSpokeTopology"
    MESH_TOPOLOGY = "MeshTopology"
