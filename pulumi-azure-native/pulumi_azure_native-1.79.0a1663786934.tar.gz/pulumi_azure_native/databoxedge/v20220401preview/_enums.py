# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AccountType',
    'AddonType',
    'AzureContainerDataFormat',
    'ClientPermissionType',
    'DataBoxEdgeDeviceKind',
    'DataBoxEdgeDeviceStatus',
    'DataPolicy',
    'DataResidencyType',
    'DayOfWeek',
    'EncryptionAlgorithm',
    'MonitoringStatus',
    'MsiIdentityType',
    'PlatformType',
    'RoleStatus',
    'RoleTypes',
    'SSLStatus',
    'ShareAccessProtocol',
    'ShareAccessType',
    'ShareStatus',
    'ShipmentType',
    'SkuName',
    'SkuTier',
    'StorageAccountStatus',
    'TriggerEventType',
    'UserType',
]


class AccountType(str, Enum):
    """
    Type of storage accessed on the storage account.
    """
    GENERAL_PURPOSE_STORAGE = "GeneralPurposeStorage"
    BLOB_STORAGE = "BlobStorage"


class AddonType(str, Enum):
    """
    Addon type.
    """
    IOT_EDGE = "IotEdge"
    ARC_FOR_KUBERNETES = "ArcForKubernetes"


class AzureContainerDataFormat(str, Enum):
    """
    Storage format used for the file represented by the share.
    """
    BLOCK_BLOB = "BlockBlob"
    PAGE_BLOB = "PageBlob"
    AZURE_FILE = "AzureFile"


class ClientPermissionType(str, Enum):
    """
    Type of access to be allowed for the client.
    """
    NO_ACCESS = "NoAccess"
    READ_ONLY = "ReadOnly"
    READ_WRITE = "ReadWrite"


class DataBoxEdgeDeviceKind(str, Enum):
    """
    The kind of the device.
    """
    AZURE_DATA_BOX_GATEWAY = "AzureDataBoxGateway"
    AZURE_STACK_EDGE = "AzureStackEdge"
    AZURE_STACK_HUB = "AzureStackHub"
    AZURE_MODULAR_DATA_CENTRE = "AzureModularDataCentre"


class DataBoxEdgeDeviceStatus(str, Enum):
    """
    The status of the Data Box Edge/Gateway device.
    """
    READY_TO_SETUP = "ReadyToSetup"
    ONLINE = "Online"
    OFFLINE = "Offline"
    NEEDS_ATTENTION = "NeedsAttention"
    DISCONNECTED = "Disconnected"
    PARTIALLY_DISCONNECTED = "PartiallyDisconnected"
    MAINTENANCE = "Maintenance"


class DataPolicy(str, Enum):
    """
    Data policy of the storage Account.
    """
    CLOUD = "Cloud"
    LOCAL = "Local"


class DataResidencyType(str, Enum):
    """
    DataResidencyType enum
    """
    GEO_ZONE_REPLICATION = "GeoZoneReplication"
    ZONE_REPLICATION = "ZoneReplication"


class DayOfWeek(str, Enum):
    SUNDAY = "Sunday"
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"


class EncryptionAlgorithm(str, Enum):
    """
    The algorithm used to encrypt "Value".
    """
    NONE = "None"
    AES256 = "AES256"
    RSAE_S_PKCS1_V_1_5 = "RSAES_PKCS1_v_1_5"


class MonitoringStatus(str, Enum):
    """
    Current monitoring status of the share.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class MsiIdentityType(str, Enum):
    """
    Identity type
    """
    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"


class PlatformType(str, Enum):
    """
    Host OS supported by the Kubernetes role.
    """
    WINDOWS = "Windows"
    LINUX = "Linux"


class RoleStatus(str, Enum):
    """
    Role status.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class RoleTypes(str, Enum):
    """
    Role type.
    """
    IOT = "IOT"
    ASA = "ASA"
    FUNCTIONS = "Functions"
    COGNITIVE = "Cognitive"
    MEC = "MEC"
    CLOUD_EDGE_MANAGEMENT = "CloudEdgeManagement"
    KUBERNETES = "Kubernetes"


class SSLStatus(str, Enum):
    """
    Signifies whether SSL needs to be enabled or not.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class ShareAccessProtocol(str, Enum):
    """
    Access protocol to be used by the share.
    """
    SMB = "SMB"
    NFS = "NFS"


class ShareAccessType(str, Enum):
    """
    Type of access to be allowed for the user.
    """
    CHANGE = "Change"
    READ = "Read"
    CUSTOM = "Custom"


class ShareStatus(str, Enum):
    """
    Current status of the share.
    """
    OFFLINE = "Offline"
    UNKNOWN = "Unknown"
    OK = "OK"
    UPDATING = "Updating"
    NEEDS_ATTENTION = "NeedsAttention"


class ShipmentType(str, Enum):
    """
    ShipmentType of the order
    """
    NOT_APPLICABLE = "NotApplicable"
    SHIPPED_TO_CUSTOMER = "ShippedToCustomer"
    SELF_PICKUP = "SelfPickup"


class SkuName(str, Enum):
    """
    SKU name.
    """
    GATEWAY = "Gateway"
    EDGE = "Edge"
    TE_A_1_NODE = "TEA_1Node"
    TE_A_1_NODE_UPS = "TEA_1Node_UPS"
    TE_A_1_NODE_HEATER = "TEA_1Node_Heater"
    TE_A_1_NODE_UP_S_HEATER = "TEA_1Node_UPS_Heater"
    TE_A_4_NODE_HEATER = "TEA_4Node_Heater"
    TE_A_4_NODE_UP_S_HEATER = "TEA_4Node_UPS_Heater"
    TMA = "TMA"
    TDC = "TDC"
    TC_A_SMALL = "TCA_Small"
    GPU = "GPU"
    TC_A_LARGE = "TCA_Large"
    EDGE_P_BASE = "EdgeP_Base"
    EDGE_P_HIGH = "EdgeP_High"
    EDGE_P_R_BASE = "EdgePR_Base"
    EDGE_P_R_BASE_UPS = "EdgePR_Base_UPS"
    EP2_64_1_VP_U_W = "EP2_64_1VPU_W"
    EP2_128_1_T4_MX1_W = "EP2_128_1T4_Mx1_W"
    EP2_256_2_T4_W = "EP2_256_2T4_W"
    EDGE_M_R_MINI = "EdgeMR_Mini"
    RC_A_SMALL = "RCA_Small"
    RC_A_LARGE = "RCA_Large"
    RDC = "RDC"
    MANAGEMENT = "Management"
    EP2_64_MX1_W = "EP2_64_Mx1_W"
    EP2_128_GPU1_MX1_W = "EP2_128_GPU1_Mx1_W"
    EP2_256_GPU2_MX1 = "EP2_256_GPU2_Mx1"
    EDGE_M_R_TCP = "EdgeMR_TCP"


class SkuTier(str, Enum):
    """
    The SKU tier. This is based on the SKU name.
    """
    STANDARD = "Standard"


class StorageAccountStatus(str, Enum):
    """
    Current status of the storage account
    """
    OK = "OK"
    OFFLINE = "Offline"
    UNKNOWN = "Unknown"
    UPDATING = "Updating"
    NEEDS_ATTENTION = "NeedsAttention"


class TriggerEventType(str, Enum):
    """
    Trigger Kind.
    """
    FILE_EVENT = "FileEvent"
    PERIODIC_TIMER_EVENT = "PeriodicTimerEvent"


class UserType(str, Enum):
    """
    Type of the user.
    """
    SHARE = "Share"
    LOCAL_MANAGEMENT = "LocalManagement"
    ARM = "ARM"
