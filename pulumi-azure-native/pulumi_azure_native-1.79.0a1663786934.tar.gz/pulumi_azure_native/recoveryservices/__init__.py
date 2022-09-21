# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from .. import _utilities
import typing
# Export this package's modules as members:
from ._enums import *
from .get_private_endpoint_connection import *
from .get_protected_item import *
from .get_protection_container import *
from .get_protection_intent import *
from .get_protection_policy import *
from .get_recovery_point_access_token import *
from .get_replication_fabric import *
from .get_replication_migration_item import *
from .get_replication_network_mapping import *
from .get_replication_policy import *
from .get_replication_protected_item import *
from .get_replication_protection_container_mapping import *
from .get_replication_recovery_plan import *
from .get_replication_recovery_services_provider import *
from .get_replication_storage_classification_mapping import *
from .get_replicationv_center import *
from .get_resource_guard_proxy import *
from .get_vault import *
from .private_endpoint_connection import *
from .protected_item import *
from .protection_container import *
from .protection_intent import *
from .protection_policy import *
from .replication_fabric import *
from .replication_migration_item import *
from .replication_network_mapping import *
from .replication_policy import *
from .replication_protected_item import *
from .replication_protection_container_mapping import *
from .replication_recovery_plan import *
from .replication_recovery_services_provider import *
from .replication_storage_classification_mapping import *
from .replicationv_center import *
from .resource_guard_proxy import *
from .vault import *
from ._inputs import *
from . import outputs

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_azure_native.recoveryservices.v20160601 as __v20160601
    v20160601 = __v20160601
    import pulumi_azure_native.recoveryservices.v20160810 as __v20160810
    v20160810 = __v20160810
    import pulumi_azure_native.recoveryservices.v20161201 as __v20161201
    v20161201 = __v20161201
    import pulumi_azure_native.recoveryservices.v20170701 as __v20170701
    v20170701 = __v20170701
    import pulumi_azure_native.recoveryservices.v20180110 as __v20180110
    v20180110 = __v20180110
    import pulumi_azure_native.recoveryservices.v20180710 as __v20180710
    v20180710 = __v20180710
    import pulumi_azure_native.recoveryservices.v20181220 as __v20181220
    v20181220 = __v20181220
    import pulumi_azure_native.recoveryservices.v20190513 as __v20190513
    v20190513 = __v20190513
    import pulumi_azure_native.recoveryservices.v20190615 as __v20190615
    v20190615 = __v20190615
    import pulumi_azure_native.recoveryservices.v20200202 as __v20200202
    v20200202 = __v20200202
    import pulumi_azure_native.recoveryservices.v20201001 as __v20201001
    v20201001 = __v20201001
    import pulumi_azure_native.recoveryservices.v20201201 as __v20201201
    v20201201 = __v20201201
    import pulumi_azure_native.recoveryservices.v20210101 as __v20210101
    v20210101 = __v20210101
    import pulumi_azure_native.recoveryservices.v20210201 as __v20210201
    v20210201 = __v20210201
    import pulumi_azure_native.recoveryservices.v20210201preview as __v20210201preview
    v20210201preview = __v20210201preview
    import pulumi_azure_native.recoveryservices.v20210210 as __v20210210
    v20210210 = __v20210210
    import pulumi_azure_native.recoveryservices.v20210301 as __v20210301
    v20210301 = __v20210301
    import pulumi_azure_native.recoveryservices.v20210401 as __v20210401
    v20210401 = __v20210401
    import pulumi_azure_native.recoveryservices.v20210601 as __v20210601
    v20210601 = __v20210601
    import pulumi_azure_native.recoveryservices.v20210701 as __v20210701
    v20210701 = __v20210701
    import pulumi_azure_native.recoveryservices.v20210801 as __v20210801
    v20210801 = __v20210801
    import pulumi_azure_native.recoveryservices.v20211001 as __v20211001
    v20211001 = __v20211001
    import pulumi_azure_native.recoveryservices.v20211101 as __v20211101
    v20211101 = __v20211101
    import pulumi_azure_native.recoveryservices.v20211101preview as __v20211101preview
    v20211101preview = __v20211101preview
    import pulumi_azure_native.recoveryservices.v20211115 as __v20211115
    v20211115 = __v20211115
    import pulumi_azure_native.recoveryservices.v20211201 as __v20211201
    v20211201 = __v20211201
    import pulumi_azure_native.recoveryservices.v20220101 as __v20220101
    v20220101 = __v20220101
    import pulumi_azure_native.recoveryservices.v20220131preview as __v20220131preview
    v20220131preview = __v20220131preview
    import pulumi_azure_native.recoveryservices.v20220201 as __v20220201
    v20220201 = __v20220201
    import pulumi_azure_native.recoveryservices.v20220301 as __v20220301
    v20220301 = __v20220301
    import pulumi_azure_native.recoveryservices.v20220401 as __v20220401
    v20220401 = __v20220401
    import pulumi_azure_native.recoveryservices.v20220501 as __v20220501
    v20220501 = __v20220501
    import pulumi_azure_native.recoveryservices.v20220601preview as __v20220601preview
    v20220601preview = __v20220601preview
    import pulumi_azure_native.recoveryservices.v20220801 as __v20220801
    v20220801 = __v20220801
else:
    v20160601 = _utilities.lazy_import('pulumi_azure_native.recoveryservices.v20160601')
    v20160810 = _utilities.lazy_import('pulumi_azure_native.recoveryservices.v20160810')
    v20161201 = _utilities.lazy_import('pulumi_azure_native.recoveryservices.v20161201')
    v20170701 = _utilities.lazy_import('pulumi_azure_native.recoveryservices.v20170701')
    v20180110 = _utilities.lazy_import('pulumi_azure_native.recoveryservices.v20180110')
    v20180710 = _utilities.lazy_import('pulumi_azure_native.recoveryservices.v20180710')
    v20181220 = _utilities.lazy_import('pulumi_azure_native.recoveryservices.v20181220')
    v20190513 = _utilities.lazy_import('pulumi_azure_native.recoveryservices.v20190513')
    v20190615 = _utilities.lazy_import('pulumi_azure_native.recoveryservices.v20190615')
    v20200202 = _utilities.lazy_import('pulumi_azure_native.recoveryservices.v20200202')
    v20201001 = _utilities.lazy_import('pulumi_azure_native.recoveryservices.v20201001')
    v20201201 = _utilities.lazy_import('pulumi_azure_native.recoveryservices.v20201201')
    v20210101 = _utilities.lazy_import('pulumi_azure_native.recoveryservices.v20210101')
    v20210201 = _utilities.lazy_import('pulumi_azure_native.recoveryservices.v20210201')
    v20210201preview = _utilities.lazy_import('pulumi_azure_native.recoveryservices.v20210201preview')
    v20210210 = _utilities.lazy_import('pulumi_azure_native.recoveryservices.v20210210')
    v20210301 = _utilities.lazy_import('pulumi_azure_native.recoveryservices.v20210301')
    v20210401 = _utilities.lazy_import('pulumi_azure_native.recoveryservices.v20210401')
    v20210601 = _utilities.lazy_import('pulumi_azure_native.recoveryservices.v20210601')
    v20210701 = _utilities.lazy_import('pulumi_azure_native.recoveryservices.v20210701')
    v20210801 = _utilities.lazy_import('pulumi_azure_native.recoveryservices.v20210801')
    v20211001 = _utilities.lazy_import('pulumi_azure_native.recoveryservices.v20211001')
    v20211101 = _utilities.lazy_import('pulumi_azure_native.recoveryservices.v20211101')
    v20211101preview = _utilities.lazy_import('pulumi_azure_native.recoveryservices.v20211101preview')
    v20211115 = _utilities.lazy_import('pulumi_azure_native.recoveryservices.v20211115')
    v20211201 = _utilities.lazy_import('pulumi_azure_native.recoveryservices.v20211201')
    v20220101 = _utilities.lazy_import('pulumi_azure_native.recoveryservices.v20220101')
    v20220131preview = _utilities.lazy_import('pulumi_azure_native.recoveryservices.v20220131preview')
    v20220201 = _utilities.lazy_import('pulumi_azure_native.recoveryservices.v20220201')
    v20220301 = _utilities.lazy_import('pulumi_azure_native.recoveryservices.v20220301')
    v20220401 = _utilities.lazy_import('pulumi_azure_native.recoveryservices.v20220401')
    v20220501 = _utilities.lazy_import('pulumi_azure_native.recoveryservices.v20220501')
    v20220601preview = _utilities.lazy_import('pulumi_azure_native.recoveryservices.v20220601preview')
    v20220801 = _utilities.lazy_import('pulumi_azure_native.recoveryservices.v20220801')

