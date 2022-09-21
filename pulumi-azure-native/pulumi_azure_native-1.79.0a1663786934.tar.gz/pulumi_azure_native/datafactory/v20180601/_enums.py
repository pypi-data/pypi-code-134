# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AzureFunctionActivityMethod',
    'AzureSearchIndexWriteBehaviorType',
    'BigDataPoolReferenceType',
    'BlobEventTypes',
    'CassandraSourceReadConsistencyLevels',
    'CosmosDbConnectionMode',
    'CosmosDbServicePrincipalCredentialType',
    'CredentialReferenceType',
    'DataFlowComputeType',
    'DataFlowReferenceType',
    'DayOfWeek',
    'DaysOfWeek',
    'Db2AuthenticationType',
    'DependencyCondition',
    'DynamicsSinkWriteBehavior',
    'FactoryIdentityType',
    'FtpAuthenticationType',
    'GlobalParameterType',
    'GoogleAdWordsAuthenticationType',
    'GoogleBigQueryAuthenticationType',
    'HBaseAuthenticationType',
    'HDInsightActivityDebugInfoOption',
    'HiveAuthenticationType',
    'HiveServerType',
    'HiveThriftTransportProtocol',
    'HttpAuthenticationType',
    'ImpalaAuthenticationType',
    'IntegrationRuntimeEdition',
    'IntegrationRuntimeEntityReferenceType',
    'IntegrationRuntimeLicenseType',
    'IntegrationRuntimeSsisCatalogPricingTier',
    'IntegrationRuntimeType',
    'ManagedVirtualNetworkReferenceType',
    'MongoDbAuthenticationType',
    'NotebookParameterType',
    'NotebookReferenceType',
    'ODataAadServicePrincipalCredentialType',
    'ODataAuthenticationType',
    'ParameterType',
    'PhoenixAuthenticationType',
    'PolybaseSettingsRejectType',
    'PrestoAuthenticationType',
    'PublicNetworkAccess',
    'RecurrenceFrequency',
    'RestServiceAuthenticationType',
    'SalesforceSinkWriteBehavior',
    'SalesforceSourceReadBehavior',
    'SapCloudForCustomerSinkWriteBehavior',
    'SapHanaAuthenticationType',
    'ScriptActivityLogDestination',
    'ScriptActivityParameterDirection',
    'ScriptActivityParameterType',
    'ScriptType',
    'ServiceNowAuthenticationType',
    'SftpAuthenticationType',
    'SparkAuthenticationType',
    'SparkJobReferenceType',
    'SparkServerType',
    'SparkThriftTransportProtocol',
    'SqlAlwaysEncryptedAkvAuthType',
    'SsisLogLocationType',
    'SsisPackageLocationType',
    'StoredProcedureParameterType',
    'SybaseAuthenticationType',
    'TeamDeskAuthenticationType',
    'TeradataAuthenticationType',
    'TriggerReferenceType',
    'TumblingWindowFrequency',
    'Type',
    'VariableType',
    'WebActivityMethod',
    'WebAuthenticationType',
    'WebHookActivityMethod',
    'ZendeskAuthenticationType',
]


class AzureFunctionActivityMethod(str, Enum):
    """
    Rest API method for target endpoint.
    """
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    OPTIONS = "OPTIONS"
    HEAD = "HEAD"
    TRACE = "TRACE"


class AzureSearchIndexWriteBehaviorType(str, Enum):
    """
    Specify the write behavior when upserting documents into Azure Search Index.
    """
    MERGE = "Merge"
    UPLOAD = "Upload"


class BigDataPoolReferenceType(str, Enum):
    """
    Big data pool reference type.
    """
    BIG_DATA_POOL_REFERENCE = "BigDataPoolReference"


class BlobEventTypes(str, Enum):
    MICROSOFT_STORAGE_BLOB_CREATED = "Microsoft.Storage.BlobCreated"
    MICROSOFT_STORAGE_BLOB_DELETED = "Microsoft.Storage.BlobDeleted"


class CassandraSourceReadConsistencyLevels(str, Enum):
    """
    The consistency level specifies how many Cassandra servers must respond to a read request before returning data to the client application. Cassandra checks the specified number of Cassandra servers for data to satisfy the read request. Must be one of cassandraSourceReadConsistencyLevels. The default value is 'ONE'. It is case-insensitive.
    """
    ALL = "ALL"
    EAC_H_QUORUM = "EACH_QUORUM"
    QUORUM = "QUORUM"
    LOCA_L_QUORUM = "LOCAL_QUORUM"
    ONE = "ONE"
    TWO = "TWO"
    THREE = "THREE"
    LOCA_L_ONE = "LOCAL_ONE"
    SERIAL = "SERIAL"
    LOCA_L_SERIAL = "LOCAL_SERIAL"


class CosmosDbConnectionMode(str, Enum):
    """
    The connection mode used to access CosmosDB account. Type: string (or Expression with resultType string).
    """
    GATEWAY = "Gateway"
    DIRECT = "Direct"


class CosmosDbServicePrincipalCredentialType(str, Enum):
    """
    The service principal credential type to use in Server-To-Server authentication. 'ServicePrincipalKey' for key/secret, 'ServicePrincipalCert' for certificate. Type: string (or Expression with resultType string).
    """
    SERVICE_PRINCIPAL_KEY = "ServicePrincipalKey"
    SERVICE_PRINCIPAL_CERT = "ServicePrincipalCert"


class CredentialReferenceType(str, Enum):
    """
    Credential reference type.
    """
    CREDENTIAL_REFERENCE = "CredentialReference"


class DataFlowComputeType(str, Enum):
    """
    Compute type of the cluster which will execute data flow job.
    """
    GENERAL = "General"
    MEMORY_OPTIMIZED = "MemoryOptimized"
    COMPUTE_OPTIMIZED = "ComputeOptimized"


class DataFlowReferenceType(str, Enum):
    """
    Data flow reference type.
    """
    DATA_FLOW_REFERENCE = "DataFlowReference"


class DayOfWeek(str, Enum):
    """
    The day of the week.
    """
    SUNDAY = "Sunday"
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"


class DaysOfWeek(str, Enum):
    SUNDAY = "Sunday"
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"


class Db2AuthenticationType(str, Enum):
    """
    AuthenticationType to be used for connection. It is mutually exclusive with connectionString property.
    """
    BASIC = "Basic"


class DependencyCondition(str, Enum):
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    SKIPPED = "Skipped"
    COMPLETED = "Completed"


class DynamicsSinkWriteBehavior(str, Enum):
    """
    The write behavior for the operation.
    """
    UPSERT = "Upsert"


class FactoryIdentityType(str, Enum):
    """
    The identity type.
    """
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned,UserAssigned"


class FtpAuthenticationType(str, Enum):
    """
    The authentication type to be used to connect to the FTP server.
    """
    BASIC = "Basic"
    ANONYMOUS = "Anonymous"


class GlobalParameterType(str, Enum):
    """
    Global Parameter type.
    """
    OBJECT = "Object"
    STRING = "String"
    INT = "Int"
    FLOAT = "Float"
    BOOL = "Bool"
    ARRAY = "Array"


class GoogleAdWordsAuthenticationType(str, Enum):
    """
    The OAuth 2.0 authentication mechanism used for authentication. ServiceAuthentication can only be used on self-hosted IR.
    """
    SERVICE_AUTHENTICATION = "ServiceAuthentication"
    USER_AUTHENTICATION = "UserAuthentication"


class GoogleBigQueryAuthenticationType(str, Enum):
    """
    The OAuth 2.0 authentication mechanism used for authentication. ServiceAuthentication can only be used on self-hosted IR.
    """
    SERVICE_AUTHENTICATION = "ServiceAuthentication"
    USER_AUTHENTICATION = "UserAuthentication"


class HBaseAuthenticationType(str, Enum):
    """
    The authentication mechanism to use to connect to the HBase server.
    """
    ANONYMOUS = "Anonymous"
    BASIC = "Basic"


class HDInsightActivityDebugInfoOption(str, Enum):
    """
    Debug info option.
    """
    NONE = "None"
    ALWAYS = "Always"
    FAILURE = "Failure"


class HiveAuthenticationType(str, Enum):
    """
    The authentication method used to access the Hive server.
    """
    ANONYMOUS = "Anonymous"
    USERNAME = "Username"
    USERNAME_AND_PASSWORD = "UsernameAndPassword"
    WINDOWS_AZURE_HD_INSIGHT_SERVICE = "WindowsAzureHDInsightService"


class HiveServerType(str, Enum):
    """
    The type of Hive server.
    """
    HIVE_SERVER1 = "HiveServer1"
    HIVE_SERVER2 = "HiveServer2"
    HIVE_THRIFT_SERVER = "HiveThriftServer"


class HiveThriftTransportProtocol(str, Enum):
    """
    The transport protocol to use in the Thrift layer.
    """
    BINARY = "Binary"
    SASL = "SASL"
    HTT_P_ = "HTTP "


class HttpAuthenticationType(str, Enum):
    """
    The authentication type to be used to connect to the HTTP server.
    """
    BASIC = "Basic"
    ANONYMOUS = "Anonymous"
    DIGEST = "Digest"
    WINDOWS = "Windows"
    CLIENT_CERTIFICATE = "ClientCertificate"


class ImpalaAuthenticationType(str, Enum):
    """
    The authentication type to use.
    """
    ANONYMOUS = "Anonymous"
    SASLUSERNAME = "SASLUsername"
    USERNAME_AND_PASSWORD = "UsernameAndPassword"


class IntegrationRuntimeEdition(str, Enum):
    """
    The edition for the SSIS Integration Runtime
    """
    STANDARD = "Standard"
    ENTERPRISE = "Enterprise"


class IntegrationRuntimeEntityReferenceType(str, Enum):
    """
    The type of this referenced entity.
    """
    INTEGRATION_RUNTIME_REFERENCE = "IntegrationRuntimeReference"
    LINKED_SERVICE_REFERENCE = "LinkedServiceReference"


class IntegrationRuntimeLicenseType(str, Enum):
    """
    License type for bringing your own license scenario.
    """
    BASE_PRICE = "BasePrice"
    LICENSE_INCLUDED = "LicenseIncluded"


class IntegrationRuntimeSsisCatalogPricingTier(str, Enum):
    """
    The pricing tier for the catalog database. The valid values could be found in https://azure.microsoft.com/en-us/pricing/details/sql-database/
    """
    BASIC = "Basic"
    STANDARD = "Standard"
    PREMIUM = "Premium"
    PREMIUM_RS = "PremiumRS"


class IntegrationRuntimeType(str, Enum):
    """
    Type of integration runtime.
    """
    MANAGED = "Managed"
    SELF_HOSTED = "SelfHosted"


class ManagedVirtualNetworkReferenceType(str, Enum):
    """
    Managed Virtual Network reference type.
    """
    MANAGED_VIRTUAL_NETWORK_REFERENCE = "ManagedVirtualNetworkReference"


class MongoDbAuthenticationType(str, Enum):
    """
    The authentication type to be used to connect to the MongoDB database.
    """
    BASIC = "Basic"
    ANONYMOUS = "Anonymous"


class NotebookParameterType(str, Enum):
    """
    Notebook parameter type.
    """
    STRING = "string"
    INT = "int"
    FLOAT = "float"
    BOOL = "bool"


class NotebookReferenceType(str, Enum):
    """
    Synapse notebook reference type.
    """
    NOTEBOOK_REFERENCE = "NotebookReference"


class ODataAadServicePrincipalCredentialType(str, Enum):
    """
    Specify the credential type (key or cert) is used for service principal.
    """
    SERVICE_PRINCIPAL_KEY = "ServicePrincipalKey"
    SERVICE_PRINCIPAL_CERT = "ServicePrincipalCert"


class ODataAuthenticationType(str, Enum):
    """
    Type of authentication used to connect to the OData service.
    """
    BASIC = "Basic"
    ANONYMOUS = "Anonymous"
    WINDOWS = "Windows"
    AAD_SERVICE_PRINCIPAL = "AadServicePrincipal"
    MANAGED_SERVICE_IDENTITY = "ManagedServiceIdentity"


class ParameterType(str, Enum):
    """
    Parameter type.
    """
    OBJECT = "Object"
    STRING = "String"
    INT = "Int"
    FLOAT = "Float"
    BOOL = "Bool"
    ARRAY = "Array"
    SECURE_STRING = "SecureString"


class PhoenixAuthenticationType(str, Enum):
    """
    The authentication mechanism used to connect to the Phoenix server.
    """
    ANONYMOUS = "Anonymous"
    USERNAME_AND_PASSWORD = "UsernameAndPassword"
    WINDOWS_AZURE_HD_INSIGHT_SERVICE = "WindowsAzureHDInsightService"


class PolybaseSettingsRejectType(str, Enum):
    """
    Reject type.
    """
    VALUE = "value"
    PERCENTAGE = "percentage"


class PrestoAuthenticationType(str, Enum):
    """
    The authentication mechanism used to connect to the Presto server.
    """
    ANONYMOUS = "Anonymous"
    LDAP = "LDAP"


class PublicNetworkAccess(str, Enum):
    """
    Whether or not public network access is allowed for the data factory.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class RecurrenceFrequency(str, Enum):
    """
    The frequency.
    """
    NOT_SPECIFIED = "NotSpecified"
    MINUTE = "Minute"
    HOUR = "Hour"
    DAY = "Day"
    WEEK = "Week"
    MONTH = "Month"
    YEAR = "Year"


class RestServiceAuthenticationType(str, Enum):
    """
    Type of authentication used to connect to the REST service.
    """
    ANONYMOUS = "Anonymous"
    BASIC = "Basic"
    AAD_SERVICE_PRINCIPAL = "AadServicePrincipal"
    MANAGED_SERVICE_IDENTITY = "ManagedServiceIdentity"
    O_AUTH2_CLIENT_CREDENTIAL = "OAuth2ClientCredential"


class SalesforceSinkWriteBehavior(str, Enum):
    """
    The write behavior for the operation. Default is Insert.
    """
    INSERT = "Insert"
    UPSERT = "Upsert"


class SalesforceSourceReadBehavior(str, Enum):
    """
    The read behavior for the operation. Default is Query.
    """
    QUERY = "Query"
    QUERY_ALL = "QueryAll"


class SapCloudForCustomerSinkWriteBehavior(str, Enum):
    """
    The write behavior for the operation. Default is 'Insert'.
    """
    INSERT = "Insert"
    UPDATE = "Update"


class SapHanaAuthenticationType(str, Enum):
    """
    The authentication type to be used to connect to the SAP HANA server.
    """
    BASIC = "Basic"
    WINDOWS = "Windows"


class ScriptActivityLogDestination(str, Enum):
    """
    The destination of logs. Type: string.
    """
    ACTIVITY_OUTPUT = "ActivityOutput"
    EXTERNAL_STORE = "ExternalStore"


class ScriptActivityParameterDirection(str, Enum):
    """
    The direction of the parameter.
    """
    VALUE_INPUT = "Input"
    VALUE_OUTPUT = "Output"
    VALUE_INPUT_OUTPUT = "InputOutput"


class ScriptActivityParameterType(str, Enum):
    """
    The type of the parameter.
    """
    BOOLEAN = "Boolean"
    DATE_TIME = "DateTime"
    DATE_TIME_OFFSET = "DateTimeOffset"
    DECIMAL = "Decimal"
    DOUBLE = "Double"
    GUID = "Guid"
    INT16 = "Int16"
    INT32 = "Int32"
    INT64 = "Int64"
    SINGLE = "Single"
    STRING = "String"
    TIMESPAN = "Timespan"


class ScriptType(str, Enum):
    """
    The type of the query. Type: string.
    """
    QUERY = "Query"
    NON_QUERY = "NonQuery"


class ServiceNowAuthenticationType(str, Enum):
    """
    The authentication type to use.
    """
    BASIC = "Basic"
    O_AUTH2 = "OAuth2"


class SftpAuthenticationType(str, Enum):
    """
    The authentication type to be used to connect to the FTP server.
    """
    BASIC = "Basic"
    SSH_PUBLIC_KEY = "SshPublicKey"
    MULTI_FACTOR = "MultiFactor"


class SparkAuthenticationType(str, Enum):
    """
    The authentication method used to access the Spark server.
    """
    ANONYMOUS = "Anonymous"
    USERNAME = "Username"
    USERNAME_AND_PASSWORD = "UsernameAndPassword"
    WINDOWS_AZURE_HD_INSIGHT_SERVICE = "WindowsAzureHDInsightService"


class SparkJobReferenceType(str, Enum):
    """
    Synapse spark job reference type.
    """
    SPARK_JOB_DEFINITION_REFERENCE = "SparkJobDefinitionReference"


class SparkServerType(str, Enum):
    """
    The type of Spark server.
    """
    SHARK_SERVER = "SharkServer"
    SHARK_SERVER2 = "SharkServer2"
    SPARK_THRIFT_SERVER = "SparkThriftServer"


class SparkThriftTransportProtocol(str, Enum):
    """
    The transport protocol to use in the Thrift layer.
    """
    BINARY = "Binary"
    SASL = "SASL"
    HTT_P_ = "HTTP "


class SqlAlwaysEncryptedAkvAuthType(str, Enum):
    """
    Sql always encrypted AKV authentication type. Type: string (or Expression with resultType string).
    """
    SERVICE_PRINCIPAL = "ServicePrincipal"
    MANAGED_IDENTITY = "ManagedIdentity"
    USER_ASSIGNED_MANAGED_IDENTITY = "UserAssignedManagedIdentity"


class SsisLogLocationType(str, Enum):
    """
    The type of SSIS log location.
    """
    FILE = "File"


class SsisPackageLocationType(str, Enum):
    """
    The type of SSIS package location.
    """
    SSISDB = "SSISDB"
    FILE = "File"
    INLINE_PACKAGE = "InlinePackage"
    PACKAGE_STORE = "PackageStore"


class StoredProcedureParameterType(str, Enum):
    """
    Stored procedure parameter type.
    """
    STRING = "String"
    INT = "Int"
    INT64 = "Int64"
    DECIMAL = "Decimal"
    GUID = "Guid"
    BOOLEAN = "Boolean"
    DATE = "Date"


class SybaseAuthenticationType(str, Enum):
    """
    AuthenticationType to be used for connection.
    """
    BASIC = "Basic"
    WINDOWS = "Windows"


class TeamDeskAuthenticationType(str, Enum):
    """
    The authentication type to use.
    """
    BASIC = "Basic"
    TOKEN = "Token"


class TeradataAuthenticationType(str, Enum):
    """
    AuthenticationType to be used for connection.
    """
    BASIC = "Basic"
    WINDOWS = "Windows"


class TriggerReferenceType(str, Enum):
    """
    Trigger reference type.
    """
    TRIGGER_REFERENCE = "TriggerReference"


class TumblingWindowFrequency(str, Enum):
    """
    The frequency of the time windows.
    """
    MINUTE = "Minute"
    HOUR = "Hour"
    MONTH = "Month"


class Type(str, Enum):
    """
    Linked service reference type.
    """
    LINKED_SERVICE_REFERENCE = "LinkedServiceReference"


class VariableType(str, Enum):
    """
    Variable type.
    """
    STRING = "String"
    BOOL = "Bool"
    ARRAY = "Array"


class WebActivityMethod(str, Enum):
    """
    Rest API method for target endpoint.
    """
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"


class WebAuthenticationType(str, Enum):
    """
    Type of authentication used to connect to the web table source.
    """
    BASIC = "Basic"
    ANONYMOUS = "Anonymous"
    CLIENT_CERTIFICATE = "ClientCertificate"


class WebHookActivityMethod(str, Enum):
    """
    Rest API method for target endpoint.
    """
    POST = "POST"


class ZendeskAuthenticationType(str, Enum):
    """
    The authentication type to use.
    """
    BASIC = "Basic"
    TOKEN = "Token"
