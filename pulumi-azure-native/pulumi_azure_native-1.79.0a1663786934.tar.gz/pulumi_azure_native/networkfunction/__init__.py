# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from .. import _utilities
import typing
# Export this package's modules as members:
from ._enums import *
from .azure_traffic_collector import *
from .collector_policy import *
from .get_azure_traffic_collector import *
from .get_collector_policy import *
from ._inputs import *
from . import outputs

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_azure_native.networkfunction.v20210901preview as __v20210901preview
    v20210901preview = __v20210901preview
    import pulumi_azure_native.networkfunction.v20220501 as __v20220501
    v20220501 = __v20220501
    import pulumi_azure_native.networkfunction.v20220801 as __v20220801
    v20220801 = __v20220801
else:
    v20210901preview = _utilities.lazy_import('pulumi_azure_native.networkfunction.v20210901preview')
    v20220501 = _utilities.lazy_import('pulumi_azure_native.networkfunction.v20220501')
    v20220801 = _utilities.lazy_import('pulumi_azure_native.networkfunction.v20220801')

