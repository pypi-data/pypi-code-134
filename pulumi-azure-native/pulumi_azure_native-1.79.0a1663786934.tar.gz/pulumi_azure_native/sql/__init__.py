# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from .. import _utilities
import typing
# Export this package's modules as members:
from ._enums import *
from .backup_short_term_retention_policy import *
from .data_masking_policy import *
from .database import *
from .database_advisor import *
from .database_blob_auditing_policy import *
from .database_security_alert_policy import *
from .database_vulnerability_assessment import *
from .database_vulnerability_assessment_rule_baseline import *
from .disaster_recovery_configuration import *
from .distributed_availability_group import *
from .elastic_pool import *
from .encryption_protector import *
from .extended_database_blob_auditing_policy import *
from .extended_server_blob_auditing_policy import *
from .failover_group import *
from .firewall_rule import *
from .geo_backup_policy import *
from .get_backup_short_term_retention_policy import *
from .get_data_masking_policy import *
from .get_database import *
from .get_database_advisor import *
from .get_database_blob_auditing_policy import *
from .get_database_security_alert_policy import *
from .get_database_vulnerability_assessment import *
from .get_database_vulnerability_assessment_rule_baseline import *
from .get_disaster_recovery_configuration import *
from .get_distributed_availability_group import *
from .get_elastic_pool import *
from .get_encryption_protector import *
from .get_extended_database_blob_auditing_policy import *
from .get_extended_server_blob_auditing_policy import *
from .get_failover_group import *
from .get_firewall_rule import *
from .get_geo_backup_policy import *
from .get_i_pv6_firewall_rule import *
from .get_instance_failover_group import *
from .get_instance_pool import *
from .get_job import *
from .get_job_agent import *
from .get_job_credential import *
from .get_job_step import *
from .get_job_target_group import *
from .get_long_term_retention_policy import *
from .get_managed_database import *
from .get_managed_database_sensitivity_label import *
from .get_managed_database_vulnerability_assessment import *
from .get_managed_database_vulnerability_assessment_rule_baseline import *
from .get_managed_instance import *
from .get_managed_instance_administrator import *
from .get_managed_instance_azure_ad_only_authentication import *
from .get_managed_instance_key import *
from .get_managed_instance_private_endpoint_connection import *
from .get_managed_instance_vulnerability_assessment import *
from .get_managed_server_dns_alias import *
from .get_outbound_firewall_rule import *
from .get_private_endpoint_connection import *
from .get_sensitivity_label import *
from .get_server import *
from .get_server_advisor import *
from .get_server_azure_ad_administrator import *
from .get_server_azure_ad_only_authentication import *
from .get_server_blob_auditing_policy import *
from .get_server_communication_link import *
from .get_server_dns_alias import *
from .get_server_key import *
from .get_server_security_alert_policy import *
from .get_server_trust_certificate import *
from .get_server_trust_group import *
from .get_server_vulnerability_assessment import *
from .get_sync_agent import *
from .get_sync_group import *
from .get_sync_member import *
from .get_transparent_data_encryption import *
from .get_virtual_network_rule import *
from .get_workload_classifier import *
from .get_workload_group import *
from .i_pv6_firewall_rule import *
from .instance_failover_group import *
from .instance_pool import *
from .job import *
from .job_agent import *
from .job_credential import *
from .job_step import *
from .job_target_group import *
from .long_term_retention_policy import *
from .managed_database import *
from .managed_database_sensitivity_label import *
from .managed_database_vulnerability_assessment import *
from .managed_database_vulnerability_assessment_rule_baseline import *
from .managed_instance import *
from .managed_instance_administrator import *
from .managed_instance_azure_ad_only_authentication import *
from .managed_instance_key import *
from .managed_instance_private_endpoint_connection import *
from .managed_instance_vulnerability_assessment import *
from .managed_server_dns_alias import *
from .outbound_firewall_rule import *
from .private_endpoint_connection import *
from .sensitivity_label import *
from .server import *
from .server_advisor import *
from .server_azure_ad_administrator import *
from .server_azure_ad_only_authentication import *
from .server_blob_auditing_policy import *
from .server_communication_link import *
from .server_dns_alias import *
from .server_key import *
from .server_security_alert_policy import *
from .server_trust_certificate import *
from .server_trust_group import *
from .server_vulnerability_assessment import *
from .sync_agent import *
from .sync_group import *
from .sync_member import *
from .transparent_data_encryption import *
from .virtual_network_rule import *
from .workload_classifier import *
from .workload_group import *
from ._inputs import *
from . import outputs

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_azure_native.sql.v20140401 as __v20140401
    v20140401 = __v20140401
    import pulumi_azure_native.sql.v20150501preview as __v20150501preview
    v20150501preview = __v20150501preview
    import pulumi_azure_native.sql.v20170301preview as __v20170301preview
    v20170301preview = __v20170301preview
    import pulumi_azure_native.sql.v20171001preview as __v20171001preview
    v20171001preview = __v20171001preview
    import pulumi_azure_native.sql.v20180601preview as __v20180601preview
    v20180601preview = __v20180601preview
    import pulumi_azure_native.sql.v20190601preview as __v20190601preview
    v20190601preview = __v20190601preview
    import pulumi_azure_native.sql.v20200202preview as __v20200202preview
    v20200202preview = __v20200202preview
    import pulumi_azure_native.sql.v20200801preview as __v20200801preview
    v20200801preview = __v20200801preview
    import pulumi_azure_native.sql.v20201101preview as __v20201101preview
    v20201101preview = __v20201101preview
    import pulumi_azure_native.sql.v20210201preview as __v20210201preview
    v20210201preview = __v20210201preview
    import pulumi_azure_native.sql.v20210501preview as __v20210501preview
    v20210501preview = __v20210501preview
    import pulumi_azure_native.sql.v20210801preview as __v20210801preview
    v20210801preview = __v20210801preview
    import pulumi_azure_native.sql.v20211101 as __v20211101
    v20211101 = __v20211101
    import pulumi_azure_native.sql.v20211101preview as __v20211101preview
    v20211101preview = __v20211101preview
    import pulumi_azure_native.sql.v20220201preview as __v20220201preview
    v20220201preview = __v20220201preview
else:
    v20140401 = _utilities.lazy_import('pulumi_azure_native.sql.v20140401')
    v20150501preview = _utilities.lazy_import('pulumi_azure_native.sql.v20150501preview')
    v20170301preview = _utilities.lazy_import('pulumi_azure_native.sql.v20170301preview')
    v20171001preview = _utilities.lazy_import('pulumi_azure_native.sql.v20171001preview')
    v20180601preview = _utilities.lazy_import('pulumi_azure_native.sql.v20180601preview')
    v20190601preview = _utilities.lazy_import('pulumi_azure_native.sql.v20190601preview')
    v20200202preview = _utilities.lazy_import('pulumi_azure_native.sql.v20200202preview')
    v20200801preview = _utilities.lazy_import('pulumi_azure_native.sql.v20200801preview')
    v20201101preview = _utilities.lazy_import('pulumi_azure_native.sql.v20201101preview')
    v20210201preview = _utilities.lazy_import('pulumi_azure_native.sql.v20210201preview')
    v20210501preview = _utilities.lazy_import('pulumi_azure_native.sql.v20210501preview')
    v20210801preview = _utilities.lazy_import('pulumi_azure_native.sql.v20210801preview')
    v20211101 = _utilities.lazy_import('pulumi_azure_native.sql.v20211101')
    v20211101preview = _utilities.lazy_import('pulumi_azure_native.sql.v20211101preview')
    v20220201preview = _utilities.lazy_import('pulumi_azure_native.sql.v20220201preview')

