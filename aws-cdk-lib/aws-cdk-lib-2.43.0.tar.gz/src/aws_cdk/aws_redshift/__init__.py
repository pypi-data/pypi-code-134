'''
# Amazon Redshift Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_redshift as redshift
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Redshift construct libraries](https://constructs.dev/search?q=redshift)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Redshift resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Redshift.html) directly.

> An experimental construct library for this service is available in preview. Since it is not stable yet, it is distributed
> as a separate package so that you can pin its version independently of the rest of the CDK. See the package:
>
> <span class="package-reference">@aws-cdk/aws-redshift-alpha</span>

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Redshift](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Redshift.html).

(Read the [CDK Contributing Guide](https://github.com/aws/aws-cdk/blob/main/CONTRIBUTING.md) and submit an RFC if you are interested in contributing to this construct library.)

<!--END CFNONLY DISCLAIMER-->
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from .._jsii import *

import constructs
from .. import (
    CfnResource as _CfnResource_9df397a6,
    CfnTag as _CfnTag_f6864754,
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556)
class CfnCluster(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_redshift.CfnCluster",
):
    '''A CloudFormation ``AWS::Redshift::Cluster``.

    Specifies a cluster. A *cluster* is a fully managed data warehouse that consists of a set of compute nodes.

    To create a cluster in Virtual Private Cloud (VPC), you must provide a cluster subnet group name. The cluster subnet group identifies the subnets of your VPC that Amazon Redshift uses when creating the cluster. For more information about managing clusters, go to `Amazon Redshift Clusters <https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html>`_ in the *Amazon Redshift Cluster Management Guide* .

    :cloudformationResource: AWS::Redshift::Cluster
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_redshift as redshift
        
        cfn_cluster = redshift.CfnCluster(self, "MyCfnCluster",
            cluster_type="clusterType",
            db_name="dbName",
            master_username="masterUsername",
            master_user_password="masterUserPassword",
            node_type="nodeType",
        
            # the properties below are optional
            allow_version_upgrade=False,
            aqua_configuration_status="aquaConfigurationStatus",
            automated_snapshot_retention_period=123,
            availability_zone="availabilityZone",
            availability_zone_relocation=False,
            availability_zone_relocation_status="availabilityZoneRelocationStatus",
            classic=False,
            cluster_identifier="clusterIdentifier",
            cluster_parameter_group_name="clusterParameterGroupName",
            cluster_security_groups=["clusterSecurityGroups"],
            cluster_subnet_group_name="clusterSubnetGroupName",
            cluster_version="clusterVersion",
            defer_maintenance=False,
            defer_maintenance_duration=123,
            defer_maintenance_end_time="deferMaintenanceEndTime",
            defer_maintenance_start_time="deferMaintenanceStartTime",
            destination_region="destinationRegion",
            elastic_ip="elasticIp",
            encrypted=False,
            enhanced_vpc_routing=False,
            hsm_client_certificate_identifier="hsmClientCertificateIdentifier",
            hsm_configuration_identifier="hsmConfigurationIdentifier",
            iam_roles=["iamRoles"],
            kms_key_id="kmsKeyId",
            logging_properties=redshift.CfnCluster.LoggingPropertiesProperty(
                bucket_name="bucketName",
        
                # the properties below are optional
                s3_key_prefix="s3KeyPrefix"
            ),
            maintenance_track_name="maintenanceTrackName",
            manual_snapshot_retention_period=123,
            number_of_nodes=123,
            owner_account="ownerAccount",
            port=123,
            preferred_maintenance_window="preferredMaintenanceWindow",
            publicly_accessible=False,
            resource_action="resourceAction",
            revision_target="revisionTarget",
            rotate_encryption_key=False,
            snapshot_cluster_identifier="snapshotClusterIdentifier",
            snapshot_copy_grant_name="snapshotCopyGrantName",
            snapshot_copy_manual=False,
            snapshot_copy_retention_period=123,
            snapshot_identifier="snapshotIdentifier",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            vpc_security_group_ids=["vpcSecurityGroupIds"]
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        cluster_type: builtins.str,
        db_name: builtins.str,
        master_username: builtins.str,
        master_user_password: builtins.str,
        node_type: builtins.str,
        allow_version_upgrade: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        aqua_configuration_status: typing.Optional[builtins.str] = None,
        automated_snapshot_retention_period: typing.Optional[jsii.Number] = None,
        availability_zone: typing.Optional[builtins.str] = None,
        availability_zone_relocation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        availability_zone_relocation_status: typing.Optional[builtins.str] = None,
        classic: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        cluster_identifier: typing.Optional[builtins.str] = None,
        cluster_parameter_group_name: typing.Optional[builtins.str] = None,
        cluster_security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        cluster_subnet_group_name: typing.Optional[builtins.str] = None,
        cluster_version: typing.Optional[builtins.str] = None,
        defer_maintenance: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        defer_maintenance_duration: typing.Optional[jsii.Number] = None,
        defer_maintenance_end_time: typing.Optional[builtins.str] = None,
        defer_maintenance_start_time: typing.Optional[builtins.str] = None,
        destination_region: typing.Optional[builtins.str] = None,
        elastic_ip: typing.Optional[builtins.str] = None,
        encrypted: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        enhanced_vpc_routing: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        hsm_client_certificate_identifier: typing.Optional[builtins.str] = None,
        hsm_configuration_identifier: typing.Optional[builtins.str] = None,
        iam_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        logging_properties: typing.Optional[typing.Union[typing.Union["CfnCluster.LoggingPropertiesProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        maintenance_track_name: typing.Optional[builtins.str] = None,
        manual_snapshot_retention_period: typing.Optional[jsii.Number] = None,
        number_of_nodes: typing.Optional[jsii.Number] = None,
        owner_account: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        publicly_accessible: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        resource_action: typing.Optional[builtins.str] = None,
        revision_target: typing.Optional[builtins.str] = None,
        rotate_encryption_key: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        snapshot_cluster_identifier: typing.Optional[builtins.str] = None,
        snapshot_copy_grant_name: typing.Optional[builtins.str] = None,
        snapshot_copy_manual: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        snapshot_copy_retention_period: typing.Optional[jsii.Number] = None,
        snapshot_identifier: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[str, typing.Any]]]] = None,
        vpc_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::Redshift::Cluster``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param cluster_type: The type of the cluster. When cluster type is specified as. - ``single-node`` , the *NumberOfNodes* parameter is not required. - ``multi-node`` , the *NumberOfNodes* parameter is required. Valid Values: ``multi-node`` | ``single-node`` Default: ``multi-node``
        :param db_name: The name of the first database to be created when the cluster is created. To create additional databases after the cluster is created, connect to the cluster with a SQL client and use SQL commands to create a database. For more information, go to `Create a Database <https://docs.aws.amazon.com/redshift/latest/dg/t_creating_database.html>`_ in the Amazon Redshift Database Developer Guide. Default: ``dev`` Constraints: - Must contain 1 to 64 alphanumeric characters. - Must contain only lowercase letters. - Cannot be a word that is reserved by the service. A list of reserved words can be found in `Reserved Words <https://docs.aws.amazon.com/redshift/latest/dg/r_pg_keywords.html>`_ in the Amazon Redshift Database Developer Guide.
        :param master_username: The user name associated with the admin user account for the cluster that is being created. Constraints: - Must be 1 - 128 alphanumeric characters. The user name can't be ``PUBLIC`` . - First character must be a letter. - Cannot be a reserved word. A list of reserved words can be found in `Reserved Words <https://docs.aws.amazon.com/redshift/latest/dg/r_pg_keywords.html>`_ in the Amazon Redshift Database Developer Guide.
        :param master_user_password: The password associated with the admin user account for the cluster that is being created. Constraints: - Must be between 8 and 64 characters in length. - Must contain at least one uppercase letter. - Must contain at least one lowercase letter. - Must contain one number. - Can be any printable ASCII character (ASCII code 33-126) except ' (single quote), " (double quote), , /, or @.
        :param node_type: The node type to be provisioned for the cluster. For information about node types, go to `Working with Clusters <https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#how-many-nodes>`_ in the *Amazon Redshift Cluster Management Guide* . Valid Values: ``ds2.xlarge`` | ``ds2.8xlarge`` | ``dc1.large`` | ``dc1.8xlarge`` | ``dc2.large`` | ``dc2.8xlarge`` | ``ra3.xlplus`` | ``ra3.4xlarge`` | ``ra3.16xlarge``
        :param allow_version_upgrade: If ``true`` , major version upgrades can be applied during the maintenance window to the Amazon Redshift engine that is running on the cluster. When a new major version of the Amazon Redshift engine is released, you can request that the service automatically apply upgrades during the maintenance window to the Amazon Redshift engine that is running on your cluster. Default: ``true``
        :param aqua_configuration_status: The value represents how the cluster is configured to use AQUA (Advanced Query Accelerator) when it is created. Possible values include the following. - enabled - Use AQUA if it is available for the current AWS Region and Amazon Redshift node type. - disabled - Don't use AQUA. - auto - Amazon Redshift determines whether to use AQUA.
        :param automated_snapshot_retention_period: The number of days that automated snapshots are retained. If the value is 0, automated snapshots are disabled. Even if automated snapshots are disabled, you can still create manual snapshots when you want with `CreateClusterSnapshot <https://docs.aws.amazon.com/redshift/latest/APIReference/API_CreateClusterSnapshot.html>`_ in the *Amazon Redshift API Reference* . Default: ``1`` Constraints: Must be a value from 0 to 35.
        :param availability_zone: The EC2 Availability Zone (AZ) in which you want Amazon Redshift to provision the cluster. For example, if you have several EC2 instances running in a specific Availability Zone, then you might want the cluster to be provisioned in the same zone in order to decrease network latency. Default: A random, system-chosen Availability Zone in the region that is specified by the endpoint. Example: ``us-east-2d`` Constraint: The specified Availability Zone must be in the same region as the current endpoint.
        :param availability_zone_relocation: The option to enable relocation for an Amazon Redshift cluster between Availability Zones after the cluster is created.
        :param availability_zone_relocation_status: Describes the status of the Availability Zone relocation operation.
        :param classic: A boolean value indicating whether the resize operation is using the classic resize process. If you don't provide this parameter or set the value to ``false`` , the resize type is elastic.
        :param cluster_identifier: A unique identifier for the cluster. You use this identifier to refer to the cluster for any subsequent cluster operations such as deleting or modifying. The identifier also appears in the Amazon Redshift console. Constraints: - Must contain from 1 to 63 alphanumeric characters or hyphens. - Alphabetic characters must be lowercase. - First character must be a letter. - Cannot end with a hyphen or contain two consecutive hyphens. - Must be unique for all clusters within an AWS account . Example: ``myexamplecluster``
        :param cluster_parameter_group_name: The name of the parameter group to be associated with this cluster. Default: The default Amazon Redshift cluster parameter group. For information about the default parameter group, go to `Working with Amazon Redshift Parameter Groups <https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html>`_ Constraints: - Must be 1 to 255 alphanumeric characters or hyphens. - First character must be a letter. - Cannot end with a hyphen or contain two consecutive hyphens.
        :param cluster_security_groups: A list of security groups to be associated with this cluster. Default: The default cluster security group for Amazon Redshift.
        :param cluster_subnet_group_name: The name of a cluster subnet group to be associated with this cluster. If this parameter is not provided the resulting cluster will be deployed outside virtual private cloud (VPC).
        :param cluster_version: The version of the Amazon Redshift engine software that you want to deploy on the cluster. The version selected runs on all the nodes in the cluster. Constraints: Only version 1.0 is currently available. Example: ``1.0``
        :param defer_maintenance: ``AWS::Redshift::Cluster.DeferMaintenance``.
        :param defer_maintenance_duration: ``AWS::Redshift::Cluster.DeferMaintenanceDuration``.
        :param defer_maintenance_end_time: ``AWS::Redshift::Cluster.DeferMaintenanceEndTime``.
        :param defer_maintenance_start_time: ``AWS::Redshift::Cluster.DeferMaintenanceStartTime``.
        :param destination_region: The destination region that snapshots are automatically copied to when cross-region snapshot copy is enabled.
        :param elastic_ip: The Elastic IP (EIP) address for the cluster. Constraints: The cluster must be provisioned in EC2-VPC and publicly-accessible through an Internet gateway. For more information about provisioning clusters in EC2-VPC, go to `Supported Platforms to Launch Your Cluster <https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#cluster-platforms>`_ in the Amazon Redshift Cluster Management Guide.
        :param encrypted: If ``true`` , the data in the cluster is encrypted at rest. Default: false
        :param enhanced_vpc_routing: An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see `Enhanced VPC Routing <https://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html>`_ in the Amazon Redshift Cluster Management Guide. If this option is ``true`` , enhanced VPC routing is enabled. Default: false
        :param hsm_client_certificate_identifier: Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.
        :param hsm_configuration_identifier: Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.
        :param iam_roles: A list of AWS Identity and Access Management (IAM) roles that can be used by the cluster to access other AWS services. You must supply the IAM roles in their Amazon Resource Name (ARN) format. The maximum number of IAM roles that you can associate is subject to a quota. For more information, go to `Quotas and limits <https://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-limits.html>`_ in the *Amazon Redshift Cluster Management Guide* .
        :param kms_key_id: The AWS Key Management Service (KMS) key ID of the encryption key that you want to use to encrypt data in the cluster.
        :param logging_properties: Specifies logging information, such as queries and connection attempts, for the specified Amazon Redshift cluster.
        :param maintenance_track_name: An optional parameter for the name of the maintenance track for the cluster. If you don't provide a maintenance track name, the cluster is assigned to the ``current`` track.
        :param manual_snapshot_retention_period: The default number of days to retain a manual snapshot. If the value is -1, the snapshot is retained indefinitely. This setting doesn't change the retention period of existing snapshots. The value must be either -1 or an integer between 1 and 3,653.
        :param number_of_nodes: The number of compute nodes in the cluster. This parameter is required when the *ClusterType* parameter is specified as ``multi-node`` . For information about determining how many nodes you need, go to `Working with Clusters <https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#how-many-nodes>`_ in the *Amazon Redshift Cluster Management Guide* . If you don't specify this parameter, you get a single-node cluster. When requesting a multi-node cluster, you must specify the number of nodes that you want in the cluster. Default: ``1`` Constraints: Value must be at least 1 and no more than 100.
        :param owner_account: The AWS account used to create or copy the snapshot. Required if you are restoring a snapshot you do not own, optional if you own the snapshot.
        :param port: The port number on which the cluster accepts incoming connections. The cluster is accessible only via the JDBC and ODBC connection strings. Part of the connection string requires the port on which the cluster will listen for incoming connections. Default: ``5439`` Valid Values: ``1150-65535``
        :param preferred_maintenance_window: The weekly time range (in UTC) during which automated cluster maintenance can occur. Format: ``ddd:hh24:mi-ddd:hh24:mi`` Default: A 30-minute window selected at random from an 8-hour block of time per region, occurring on a random day of the week. For more information about the time blocks for each region, see `Maintenance Windows <https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#rs-maintenance-windows>`_ in Amazon Redshift Cluster Management Guide. Valid Days: Mon | Tue | Wed | Thu | Fri | Sat | Sun Constraints: Minimum 30-minute window.
        :param publicly_accessible: If ``true`` , the cluster can be accessed from a public network.
        :param resource_action: ``AWS::Redshift::Cluster.ResourceAction``.
        :param revision_target: ``AWS::Redshift::Cluster.RevisionTarget``.
        :param rotate_encryption_key: ``AWS::Redshift::Cluster.RotateEncryptionKey``.
        :param snapshot_cluster_identifier: The name of the cluster the source snapshot was created from. This parameter is required if your IAM user has a policy containing a snapshot resource element that specifies anything other than * for the cluster name.
        :param snapshot_copy_grant_name: The name of the snapshot copy grant.
        :param snapshot_copy_manual: Indicates whether to apply the snapshot retention period to newly copied manual snapshots instead of automated snapshots.
        :param snapshot_copy_retention_period: The number of days to retain automated snapshots in the destination AWS Region after they are copied from the source AWS Region . By default, this only changes the retention period of copied automated snapshots. If you decrease the retention period for automated snapshots that are copied to a destination AWS Region , Amazon Redshift deletes any existing automated snapshots that were copied to the destination AWS Region and that fall outside of the new retention period. Constraints: Must be at least 1 and no more than 35 for automated snapshots. If you specify the ``manual`` option, only newly copied manual snapshots will have the new retention period. If you specify the value of -1 newly copied manual snapshots are retained indefinitely. Constraints: The number of days must be either -1 or an integer between 1 and 3,653 for manual snapshots.
        :param snapshot_identifier: The name of the snapshot from which to create the new cluster. This parameter isn't case sensitive. Example: ``my-snapshot-id``
        :param tags: A list of tag instances.
        :param vpc_security_group_ids: A list of Virtual Private Cloud (VPC) security groups to be associated with the cluster. Default: The default VPC security group is associated with the cluster.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnCluster.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnClusterProps(
            cluster_type=cluster_type,
            db_name=db_name,
            master_username=master_username,
            master_user_password=master_user_password,
            node_type=node_type,
            allow_version_upgrade=allow_version_upgrade,
            aqua_configuration_status=aqua_configuration_status,
            automated_snapshot_retention_period=automated_snapshot_retention_period,
            availability_zone=availability_zone,
            availability_zone_relocation=availability_zone_relocation,
            availability_zone_relocation_status=availability_zone_relocation_status,
            classic=classic,
            cluster_identifier=cluster_identifier,
            cluster_parameter_group_name=cluster_parameter_group_name,
            cluster_security_groups=cluster_security_groups,
            cluster_subnet_group_name=cluster_subnet_group_name,
            cluster_version=cluster_version,
            defer_maintenance=defer_maintenance,
            defer_maintenance_duration=defer_maintenance_duration,
            defer_maintenance_end_time=defer_maintenance_end_time,
            defer_maintenance_start_time=defer_maintenance_start_time,
            destination_region=destination_region,
            elastic_ip=elastic_ip,
            encrypted=encrypted,
            enhanced_vpc_routing=enhanced_vpc_routing,
            hsm_client_certificate_identifier=hsm_client_certificate_identifier,
            hsm_configuration_identifier=hsm_configuration_identifier,
            iam_roles=iam_roles,
            kms_key_id=kms_key_id,
            logging_properties=logging_properties,
            maintenance_track_name=maintenance_track_name,
            manual_snapshot_retention_period=manual_snapshot_retention_period,
            number_of_nodes=number_of_nodes,
            owner_account=owner_account,
            port=port,
            preferred_maintenance_window=preferred_maintenance_window,
            publicly_accessible=publicly_accessible,
            resource_action=resource_action,
            revision_target=revision_target,
            rotate_encryption_key=rotate_encryption_key,
            snapshot_cluster_identifier=snapshot_cluster_identifier,
            snapshot_copy_grant_name=snapshot_copy_grant_name,
            snapshot_copy_manual=snapshot_copy_manual,
            snapshot_copy_retention_period=snapshot_copy_retention_period,
            snapshot_identifier=snapshot_identifier,
            tags=tags,
            vpc_security_group_ids=vpc_security_group_ids,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnCluster.inspect)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnCluster._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrDeferMaintenanceIdentifier")
    def attr_defer_maintenance_identifier(self) -> builtins.str:
        '''
        :cloudformationAttribute: DeferMaintenanceIdentifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDeferMaintenanceIdentifier"))

    @builtins.property
    @jsii.member(jsii_name="attrEndpointAddress")
    def attr_endpoint_address(self) -> builtins.str:
        '''The connection endpoint for the Amazon Redshift cluster.

        For example: ``examplecluster.cg034hpkmmjt.us-east-1.redshift.amazonaws.com`` .

        :cloudformationAttribute: Endpoint.Address
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEndpointAddress"))

    @builtins.property
    @jsii.member(jsii_name="attrEndpointPort")
    def attr_endpoint_port(self) -> builtins.str:
        '''The port number on which the Amazon Redshift cluster accepts connections.

        For example: ``5439`` .

        :cloudformationAttribute: Endpoint.Port
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEndpointPort"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''A unique identifier for the cluster.

        You use this identifier to refer to the cluster for any subsequent cluster operations such as deleting or modifying. The identifier also appears in the Amazon Redshift console.

        Example: ``myexamplecluster``

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''A list of tag instances.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="clusterType")
    def cluster_type(self) -> builtins.str:
        '''The type of the cluster. When cluster type is specified as.

        - ``single-node`` , the *NumberOfNodes* parameter is not required.
        - ``multi-node`` , the *NumberOfNodes* parameter is required.

        Valid Values: ``multi-node`` | ``single-node``

        Default: ``multi-node``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-clustertype
        '''
        return typing.cast(builtins.str, jsii.get(self, "clusterType"))

    @cluster_type.setter
    def cluster_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCluster, "cluster_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterType", value)

    @builtins.property
    @jsii.member(jsii_name="dbName")
    def db_name(self) -> builtins.str:
        '''The name of the first database to be created when the cluster is created.

        To create additional databases after the cluster is created, connect to the cluster with a SQL client and use SQL commands to create a database. For more information, go to `Create a Database <https://docs.aws.amazon.com/redshift/latest/dg/t_creating_database.html>`_ in the Amazon Redshift Database Developer Guide.

        Default: ``dev``

        Constraints:

        - Must contain 1 to 64 alphanumeric characters.
        - Must contain only lowercase letters.
        - Cannot be a word that is reserved by the service. A list of reserved words can be found in `Reserved Words <https://docs.aws.amazon.com/redshift/latest/dg/r_pg_keywords.html>`_ in the Amazon Redshift Database Developer Guide.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-dbname
        '''
        return typing.cast(builtins.str, jsii.get(self, "dbName"))

    @db_name.setter
    def db_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCluster, "db_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dbName", value)

    @builtins.property
    @jsii.member(jsii_name="masterUsername")
    def master_username(self) -> builtins.str:
        '''The user name associated with the admin user account for the cluster that is being created.

        Constraints:

        - Must be 1 - 128 alphanumeric characters. The user name can't be ``PUBLIC`` .
        - First character must be a letter.
        - Cannot be a reserved word. A list of reserved words can be found in `Reserved Words <https://docs.aws.amazon.com/redshift/latest/dg/r_pg_keywords.html>`_ in the Amazon Redshift Database Developer Guide.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-masterusername
        '''
        return typing.cast(builtins.str, jsii.get(self, "masterUsername"))

    @master_username.setter
    def master_username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCluster, "master_username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "masterUsername", value)

    @builtins.property
    @jsii.member(jsii_name="masterUserPassword")
    def master_user_password(self) -> builtins.str:
        '''The password associated with the admin user account for the cluster that is being created.

        Constraints:

        - Must be between 8 and 64 characters in length.
        - Must contain at least one uppercase letter.
        - Must contain at least one lowercase letter.
        - Must contain one number.
        - Can be any printable ASCII character (ASCII code 33-126) except ' (single quote), " (double quote), , /, or @.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-masteruserpassword
        '''
        return typing.cast(builtins.str, jsii.get(self, "masterUserPassword"))

    @master_user_password.setter
    def master_user_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCluster, "master_user_password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "masterUserPassword", value)

    @builtins.property
    @jsii.member(jsii_name="nodeType")
    def node_type(self) -> builtins.str:
        '''The node type to be provisioned for the cluster.

        For information about node types, go to `Working with Clusters <https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#how-many-nodes>`_ in the *Amazon Redshift Cluster Management Guide* .

        Valid Values: ``ds2.xlarge`` | ``ds2.8xlarge`` | ``dc1.large`` | ``dc1.8xlarge`` | ``dc2.large`` | ``dc2.8xlarge`` | ``ra3.xlplus`` | ``ra3.4xlarge`` | ``ra3.16xlarge``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-nodetype
        '''
        return typing.cast(builtins.str, jsii.get(self, "nodeType"))

    @node_type.setter
    def node_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCluster, "node_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodeType", value)

    @builtins.property
    @jsii.member(jsii_name="allowVersionUpgrade")
    def allow_version_upgrade(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''If ``true`` , major version upgrades can be applied during the maintenance window to the Amazon Redshift engine that is running on the cluster.

        When a new major version of the Amazon Redshift engine is released, you can request that the service automatically apply upgrades during the maintenance window to the Amazon Redshift engine that is running on your cluster.

        Default: ``true``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-allowversionupgrade
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "allowVersionUpgrade"))

    @allow_version_upgrade.setter
    def allow_version_upgrade(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCluster, "allow_version_upgrade").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowVersionUpgrade", value)

    @builtins.property
    @jsii.member(jsii_name="aquaConfigurationStatus")
    def aqua_configuration_status(self) -> typing.Optional[builtins.str]:
        '''The value represents how the cluster is configured to use AQUA (Advanced Query Accelerator) when it is created.

        Possible values include the following.

        - enabled - Use AQUA if it is available for the current AWS Region and Amazon Redshift node type.
        - disabled - Don't use AQUA.
        - auto - Amazon Redshift determines whether to use AQUA.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-aquaconfigurationstatus
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aquaConfigurationStatus"))

    @aqua_configuration_status.setter
    def aqua_configuration_status(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCluster, "aqua_configuration_status").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aquaConfigurationStatus", value)

    @builtins.property
    @jsii.member(jsii_name="automatedSnapshotRetentionPeriod")
    def automated_snapshot_retention_period(self) -> typing.Optional[jsii.Number]:
        '''The number of days that automated snapshots are retained.

        If the value is 0, automated snapshots are disabled. Even if automated snapshots are disabled, you can still create manual snapshots when you want with `CreateClusterSnapshot <https://docs.aws.amazon.com/redshift/latest/APIReference/API_CreateClusterSnapshot.html>`_ in the *Amazon Redshift API Reference* .

        Default: ``1``

        Constraints: Must be a value from 0 to 35.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-automatedsnapshotretentionperiod
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "automatedSnapshotRetentionPeriod"))

    @automated_snapshot_retention_period.setter
    def automated_snapshot_retention_period(
        self,
        value: typing.Optional[jsii.Number],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCluster, "automated_snapshot_retention_period").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "automatedSnapshotRetentionPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="availabilityZone")
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''The EC2 Availability Zone (AZ) in which you want Amazon Redshift to provision the cluster.

        For example, if you have several EC2 instances running in a specific Availability Zone, then you might want the cluster to be provisioned in the same zone in order to decrease network latency.

        Default: A random, system-chosen Availability Zone in the region that is specified by the endpoint.

        Example: ``us-east-2d``

        Constraint: The specified Availability Zone must be in the same region as the current endpoint.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-availabilityzone
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityZone"))

    @availability_zone.setter
    def availability_zone(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCluster, "availability_zone").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilityZone", value)

    @builtins.property
    @jsii.member(jsii_name="availabilityZoneRelocation")
    def availability_zone_relocation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''The option to enable relocation for an Amazon Redshift cluster between Availability Zones after the cluster is created.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-availabilityzonerelocation
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "availabilityZoneRelocation"))

    @availability_zone_relocation.setter
    def availability_zone_relocation(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCluster, "availability_zone_relocation").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilityZoneRelocation", value)

    @builtins.property
    @jsii.member(jsii_name="availabilityZoneRelocationStatus")
    def availability_zone_relocation_status(self) -> typing.Optional[builtins.str]:
        '''Describes the status of the Availability Zone relocation operation.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-availabilityzonerelocationstatus
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityZoneRelocationStatus"))

    @availability_zone_relocation_status.setter
    def availability_zone_relocation_status(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCluster, "availability_zone_relocation_status").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilityZoneRelocationStatus", value)

    @builtins.property
    @jsii.member(jsii_name="classic")
    def classic(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A boolean value indicating whether the resize operation is using the classic resize process.

        If you don't provide this parameter or set the value to ``false`` , the resize type is elastic.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-classic
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "classic"))

    @classic.setter
    def classic(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCluster, "classic").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "classic", value)

    @builtins.property
    @jsii.member(jsii_name="clusterIdentifier")
    def cluster_identifier(self) -> typing.Optional[builtins.str]:
        '''A unique identifier for the cluster.

        You use this identifier to refer to the cluster for any subsequent cluster operations such as deleting or modifying. The identifier also appears in the Amazon Redshift console.

        Constraints:

        - Must contain from 1 to 63 alphanumeric characters or hyphens.
        - Alphabetic characters must be lowercase.
        - First character must be a letter.
        - Cannot end with a hyphen or contain two consecutive hyphens.
        - Must be unique for all clusters within an AWS account .

        Example: ``myexamplecluster``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-clusteridentifier
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterIdentifier"))

    @cluster_identifier.setter
    def cluster_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCluster, "cluster_identifier").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="clusterParameterGroupName")
    def cluster_parameter_group_name(self) -> typing.Optional[builtins.str]:
        '''The name of the parameter group to be associated with this cluster.

        Default: The default Amazon Redshift cluster parameter group. For information about the default parameter group, go to `Working with Amazon Redshift Parameter Groups <https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html>`_

        Constraints:

        - Must be 1 to 255 alphanumeric characters or hyphens.
        - First character must be a letter.
        - Cannot end with a hyphen or contain two consecutive hyphens.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-clusterparametergroupname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterParameterGroupName"))

    @cluster_parameter_group_name.setter
    def cluster_parameter_group_name(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCluster, "cluster_parameter_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterParameterGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="clusterSecurityGroups")
    def cluster_security_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of security groups to be associated with this cluster.

        Default: The default cluster security group for Amazon Redshift.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-clustersecuritygroups
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "clusterSecurityGroups"))

    @cluster_security_groups.setter
    def cluster_security_groups(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCluster, "cluster_security_groups").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterSecurityGroups", value)

    @builtins.property
    @jsii.member(jsii_name="clusterSubnetGroupName")
    def cluster_subnet_group_name(self) -> typing.Optional[builtins.str]:
        '''The name of a cluster subnet group to be associated with this cluster.

        If this parameter is not provided the resulting cluster will be deployed outside virtual private cloud (VPC).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-clustersubnetgroupname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterSubnetGroupName"))

    @cluster_subnet_group_name.setter
    def cluster_subnet_group_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCluster, "cluster_subnet_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterSubnetGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="clusterVersion")
    def cluster_version(self) -> typing.Optional[builtins.str]:
        '''The version of the Amazon Redshift engine software that you want to deploy on the cluster.

        The version selected runs on all the nodes in the cluster.

        Constraints: Only version 1.0 is currently available.

        Example: ``1.0``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-clusterversion
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterVersion"))

    @cluster_version.setter
    def cluster_version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCluster, "cluster_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterVersion", value)

    @builtins.property
    @jsii.member(jsii_name="deferMaintenance")
    def defer_maintenance(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''``AWS::Redshift::Cluster.DeferMaintenance``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-defermaintenance
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "deferMaintenance"))

    @defer_maintenance.setter
    def defer_maintenance(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCluster, "defer_maintenance").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deferMaintenance", value)

    @builtins.property
    @jsii.member(jsii_name="deferMaintenanceDuration")
    def defer_maintenance_duration(self) -> typing.Optional[jsii.Number]:
        '''``AWS::Redshift::Cluster.DeferMaintenanceDuration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-defermaintenanceduration
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "deferMaintenanceDuration"))

    @defer_maintenance_duration.setter
    def defer_maintenance_duration(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCluster, "defer_maintenance_duration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deferMaintenanceDuration", value)

    @builtins.property
    @jsii.member(jsii_name="deferMaintenanceEndTime")
    def defer_maintenance_end_time(self) -> typing.Optional[builtins.str]:
        '''``AWS::Redshift::Cluster.DeferMaintenanceEndTime``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-defermaintenanceendtime
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deferMaintenanceEndTime"))

    @defer_maintenance_end_time.setter
    def defer_maintenance_end_time(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCluster, "defer_maintenance_end_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deferMaintenanceEndTime", value)

    @builtins.property
    @jsii.member(jsii_name="deferMaintenanceStartTime")
    def defer_maintenance_start_time(self) -> typing.Optional[builtins.str]:
        '''``AWS::Redshift::Cluster.DeferMaintenanceStartTime``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-defermaintenancestarttime
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deferMaintenanceStartTime"))

    @defer_maintenance_start_time.setter
    def defer_maintenance_start_time(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCluster, "defer_maintenance_start_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deferMaintenanceStartTime", value)

    @builtins.property
    @jsii.member(jsii_name="destinationRegion")
    def destination_region(self) -> typing.Optional[builtins.str]:
        '''The destination region that snapshots are automatically copied to when cross-region snapshot copy is enabled.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-destinationregion
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationRegion"))

    @destination_region.setter
    def destination_region(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCluster, "destination_region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationRegion", value)

    @builtins.property
    @jsii.member(jsii_name="elasticIp")
    def elastic_ip(self) -> typing.Optional[builtins.str]:
        '''The Elastic IP (EIP) address for the cluster.

        Constraints: The cluster must be provisioned in EC2-VPC and publicly-accessible through an Internet gateway. For more information about provisioning clusters in EC2-VPC, go to `Supported Platforms to Launch Your Cluster <https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#cluster-platforms>`_ in the Amazon Redshift Cluster Management Guide.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-elasticip
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "elasticIp"))

    @elastic_ip.setter
    def elastic_ip(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCluster, "elastic_ip").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "elasticIp", value)

    @builtins.property
    @jsii.member(jsii_name="encrypted")
    def encrypted(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''If ``true`` , the data in the cluster is encrypted at rest.

        Default: false

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-encrypted
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "encrypted"))

    @encrypted.setter
    def encrypted(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCluster, "encrypted").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encrypted", value)

    @builtins.property
    @jsii.member(jsii_name="enhancedVpcRouting")
    def enhanced_vpc_routing(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''An option that specifies whether to create the cluster with enhanced VPC routing enabled.

        To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see `Enhanced VPC Routing <https://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html>`_ in the Amazon Redshift Cluster Management Guide.

        If this option is ``true`` , enhanced VPC routing is enabled.

        Default: false

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-enhancedvpcrouting
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "enhancedVpcRouting"))

    @enhanced_vpc_routing.setter
    def enhanced_vpc_routing(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCluster, "enhanced_vpc_routing").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enhancedVpcRouting", value)

    @builtins.property
    @jsii.member(jsii_name="hsmClientCertificateIdentifier")
    def hsm_client_certificate_identifier(self) -> typing.Optional[builtins.str]:
        '''Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-hsmclientcertificateidentifier
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hsmClientCertificateIdentifier"))

    @hsm_client_certificate_identifier.setter
    def hsm_client_certificate_identifier(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCluster, "hsm_client_certificate_identifier").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hsmClientCertificateIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="hsmConfigurationIdentifier")
    def hsm_configuration_identifier(self) -> typing.Optional[builtins.str]:
        '''Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-hsmconfigurationidentifier
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hsmConfigurationIdentifier"))

    @hsm_configuration_identifier.setter
    def hsm_configuration_identifier(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCluster, "hsm_configuration_identifier").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hsmConfigurationIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="iamRoles")
    def iam_roles(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of AWS Identity and Access Management (IAM) roles that can be used by the cluster to access other AWS services.

        You must supply the IAM roles in their Amazon Resource Name (ARN) format.

        The maximum number of IAM roles that you can associate is subject to a quota. For more information, go to `Quotas and limits <https://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-limits.html>`_ in the *Amazon Redshift Cluster Management Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-iamroles
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "iamRoles"))

    @iam_roles.setter
    def iam_roles(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCluster, "iam_roles").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iamRoles", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''The AWS Key Management Service (KMS) key ID of the encryption key that you want to use to encrypt data in the cluster.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-kmskeyid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCluster, "kms_key_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="loggingProperties")
    def logging_properties(
        self,
    ) -> typing.Optional[typing.Union["CfnCluster.LoggingPropertiesProperty", _IResolvable_da3f097b]]:
        '''Specifies logging information, such as queries and connection attempts, for the specified Amazon Redshift cluster.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-loggingproperties
        '''
        return typing.cast(typing.Optional[typing.Union["CfnCluster.LoggingPropertiesProperty", _IResolvable_da3f097b]], jsii.get(self, "loggingProperties"))

    @logging_properties.setter
    def logging_properties(
        self,
        value: typing.Optional[typing.Union["CfnCluster.LoggingPropertiesProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCluster, "logging_properties").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loggingProperties", value)

    @builtins.property
    @jsii.member(jsii_name="maintenanceTrackName")
    def maintenance_track_name(self) -> typing.Optional[builtins.str]:
        '''An optional parameter for the name of the maintenance track for the cluster.

        If you don't provide a maintenance track name, the cluster is assigned to the ``current`` track.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-maintenancetrackname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maintenanceTrackName"))

    @maintenance_track_name.setter
    def maintenance_track_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCluster, "maintenance_track_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maintenanceTrackName", value)

    @builtins.property
    @jsii.member(jsii_name="manualSnapshotRetentionPeriod")
    def manual_snapshot_retention_period(self) -> typing.Optional[jsii.Number]:
        '''The default number of days to retain a manual snapshot.

        If the value is -1, the snapshot is retained indefinitely. This setting doesn't change the retention period of existing snapshots.

        The value must be either -1 or an integer between 1 and 3,653.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-manualsnapshotretentionperiod
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "manualSnapshotRetentionPeriod"))

    @manual_snapshot_retention_period.setter
    def manual_snapshot_retention_period(
        self,
        value: typing.Optional[jsii.Number],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCluster, "manual_snapshot_retention_period").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "manualSnapshotRetentionPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="numberOfNodes")
    def number_of_nodes(self) -> typing.Optional[jsii.Number]:
        '''The number of compute nodes in the cluster.

        This parameter is required when the *ClusterType* parameter is specified as ``multi-node`` .

        For information about determining how many nodes you need, go to `Working with Clusters <https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#how-many-nodes>`_ in the *Amazon Redshift Cluster Management Guide* .

        If you don't specify this parameter, you get a single-node cluster. When requesting a multi-node cluster, you must specify the number of nodes that you want in the cluster.

        Default: ``1``

        Constraints: Value must be at least 1 and no more than 100.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-numberofnodes
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "numberOfNodes"))

    @number_of_nodes.setter
    def number_of_nodes(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCluster, "number_of_nodes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numberOfNodes", value)

    @builtins.property
    @jsii.member(jsii_name="ownerAccount")
    def owner_account(self) -> typing.Optional[builtins.str]:
        '''The AWS account used to create or copy the snapshot.

        Required if you are restoring a snapshot you do not own, optional if you own the snapshot.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-owneraccount
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ownerAccount"))

    @owner_account.setter
    def owner_account(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCluster, "owner_account").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ownerAccount", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> typing.Optional[jsii.Number]:
        '''The port number on which the cluster accepts incoming connections.

        The cluster is accessible only via the JDBC and ODBC connection strings. Part of the connection string requires the port on which the cluster will listen for incoming connections.

        Default: ``5439``

        Valid Values: ``1150-65535``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-port
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "port"))

    @port.setter
    def port(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCluster, "port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> typing.Optional[builtins.str]:
        '''The weekly time range (in UTC) during which automated cluster maintenance can occur.

        Format: ``ddd:hh24:mi-ddd:hh24:mi``

        Default: A 30-minute window selected at random from an 8-hour block of time per region, occurring on a random day of the week. For more information about the time blocks for each region, see `Maintenance Windows <https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#rs-maintenance-windows>`_ in Amazon Redshift Cluster Management Guide.

        Valid Days: Mon | Tue | Wed | Thu | Fri | Sat | Sun

        Constraints: Minimum 30-minute window.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-preferredmaintenancewindow
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preferredMaintenanceWindow"))

    @preferred_maintenance_window.setter
    def preferred_maintenance_window(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCluster, "preferred_maintenance_window").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preferredMaintenanceWindow", value)

    @builtins.property
    @jsii.member(jsii_name="publiclyAccessible")
    def publicly_accessible(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''If ``true`` , the cluster can be accessed from a public network.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-publiclyaccessible
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "publiclyAccessible"))

    @publicly_accessible.setter
    def publicly_accessible(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCluster, "publicly_accessible").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publiclyAccessible", value)

    @builtins.property
    @jsii.member(jsii_name="resourceAction")
    def resource_action(self) -> typing.Optional[builtins.str]:
        '''``AWS::Redshift::Cluster.ResourceAction``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-resourceaction
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceAction"))

    @resource_action.setter
    def resource_action(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCluster, "resource_action").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceAction", value)

    @builtins.property
    @jsii.member(jsii_name="revisionTarget")
    def revision_target(self) -> typing.Optional[builtins.str]:
        '''``AWS::Redshift::Cluster.RevisionTarget``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-revisiontarget
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "revisionTarget"))

    @revision_target.setter
    def revision_target(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCluster, "revision_target").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "revisionTarget", value)

    @builtins.property
    @jsii.member(jsii_name="rotateEncryptionKey")
    def rotate_encryption_key(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''``AWS::Redshift::Cluster.RotateEncryptionKey``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-rotateencryptionkey
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "rotateEncryptionKey"))

    @rotate_encryption_key.setter
    def rotate_encryption_key(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCluster, "rotate_encryption_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rotateEncryptionKey", value)

    @builtins.property
    @jsii.member(jsii_name="snapshotClusterIdentifier")
    def snapshot_cluster_identifier(self) -> typing.Optional[builtins.str]:
        '''The name of the cluster the source snapshot was created from.

        This parameter is required if your IAM user has a policy containing a snapshot resource element that specifies anything other than * for the cluster name.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-snapshotclusteridentifier
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snapshotClusterIdentifier"))

    @snapshot_cluster_identifier.setter
    def snapshot_cluster_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCluster, "snapshot_cluster_identifier").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotClusterIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="snapshotCopyGrantName")
    def snapshot_copy_grant_name(self) -> typing.Optional[builtins.str]:
        '''The name of the snapshot copy grant.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-snapshotcopygrantname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snapshotCopyGrantName"))

    @snapshot_copy_grant_name.setter
    def snapshot_copy_grant_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCluster, "snapshot_copy_grant_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotCopyGrantName", value)

    @builtins.property
    @jsii.member(jsii_name="snapshotCopyManual")
    def snapshot_copy_manual(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates whether to apply the snapshot retention period to newly copied manual snapshots instead of automated snapshots.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-snapshotcopymanual
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "snapshotCopyManual"))

    @snapshot_copy_manual.setter
    def snapshot_copy_manual(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCluster, "snapshot_copy_manual").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotCopyManual", value)

    @builtins.property
    @jsii.member(jsii_name="snapshotCopyRetentionPeriod")
    def snapshot_copy_retention_period(self) -> typing.Optional[jsii.Number]:
        '''The number of days to retain automated snapshots in the destination AWS Region after they are copied from the source AWS Region .

        By default, this only changes the retention period of copied automated snapshots.

        If you decrease the retention period for automated snapshots that are copied to a destination AWS Region , Amazon Redshift deletes any existing automated snapshots that were copied to the destination AWS Region and that fall outside of the new retention period.

        Constraints: Must be at least 1 and no more than 35 for automated snapshots.

        If you specify the ``manual`` option, only newly copied manual snapshots will have the new retention period.

        If you specify the value of -1 newly copied manual snapshots are retained indefinitely.

        Constraints: The number of days must be either -1 or an integer between 1 and 3,653 for manual snapshots.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-snapshotcopyretentionperiod
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "snapshotCopyRetentionPeriod"))

    @snapshot_copy_retention_period.setter
    def snapshot_copy_retention_period(
        self,
        value: typing.Optional[jsii.Number],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCluster, "snapshot_copy_retention_period").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotCopyRetentionPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="snapshotIdentifier")
    def snapshot_identifier(self) -> typing.Optional[builtins.str]:
        '''The name of the snapshot from which to create the new cluster. This parameter isn't case sensitive.

        Example: ``my-snapshot-id``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-snapshotidentifier
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snapshotIdentifier"))

    @snapshot_identifier.setter
    def snapshot_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCluster, "snapshot_identifier").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of Virtual Private Cloud (VPC) security groups to be associated with the cluster.

        Default: The default VPC security group is associated with the cluster.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-vpcsecuritygroupids
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "vpcSecurityGroupIds"))

    @vpc_security_group_ids.setter
    def vpc_security_group_ids(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnCluster, "vpc_security_group_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcSecurityGroupIds", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_redshift.CfnCluster.EndpointProperty",
        jsii_struct_bases=[],
        name_mapping={"address": "address", "port": "port"},
    )
    class EndpointProperty:
        def __init__(
            self,
            *,
            address: typing.Optional[builtins.str] = None,
            port: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes a connection endpoint.

            :param address: The DNS address of the Cluster.
            :param port: The port that the database engine is listening on.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-cluster-endpoint.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_redshift as redshift
                
                endpoint_property = redshift.CfnCluster.EndpointProperty(
                    address="address",
                    port="port"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnCluster.EndpointProperty.__init__)
                check_type(argname="argument address", value=address, expected_type=type_hints["address"])
                check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            self._values: typing.Dict[str, typing.Any] = {}
            if address is not None:
                self._values["address"] = address
            if port is not None:
                self._values["port"] = port

        @builtins.property
        def address(self) -> typing.Optional[builtins.str]:
            '''The DNS address of the Cluster.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-cluster-endpoint.html#cfn-redshift-cluster-endpoint-address
            '''
            result = self._values.get("address")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def port(self) -> typing.Optional[builtins.str]:
            '''The port that the database engine is listening on.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-cluster-endpoint.html#cfn-redshift-cluster-endpoint-port
            '''
            result = self._values.get("port")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EndpointProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_redshift.CfnCluster.LoggingPropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={"bucket_name": "bucketName", "s3_key_prefix": "s3KeyPrefix"},
    )
    class LoggingPropertiesProperty:
        def __init__(
            self,
            *,
            bucket_name: builtins.str,
            s3_key_prefix: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies logging information, such as queries and connection attempts, for the specified Amazon Redshift cluster.

            :param bucket_name: The name of an existing S3 bucket where the log files are to be stored. Constraints: - Must be in the same region as the cluster - The cluster must have read bucket and put object permissions
            :param s3_key_prefix: The prefix applied to the log file names. Constraints: - Cannot exceed 512 characters - Cannot contain spaces( ), double quotes ("), single quotes ('), a backslash (), or control characters. The hexadecimal codes for invalid characters are: - x00 to x20 - x22 - x27 - x5c - x7f or larger

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-cluster-loggingproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_redshift as redshift
                
                logging_properties_property = redshift.CfnCluster.LoggingPropertiesProperty(
                    bucket_name="bucketName",
                
                    # the properties below are optional
                    s3_key_prefix="s3KeyPrefix"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnCluster.LoggingPropertiesProperty.__init__)
                check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
                check_type(argname="argument s3_key_prefix", value=s3_key_prefix, expected_type=type_hints["s3_key_prefix"])
            self._values: typing.Dict[str, typing.Any] = {
                "bucket_name": bucket_name,
            }
            if s3_key_prefix is not None:
                self._values["s3_key_prefix"] = s3_key_prefix

        @builtins.property
        def bucket_name(self) -> builtins.str:
            '''The name of an existing S3 bucket where the log files are to be stored.

            Constraints:

            - Must be in the same region as the cluster
            - The cluster must have read bucket and put object permissions

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-cluster-loggingproperties.html#cfn-redshift-cluster-loggingproperties-bucketname
            '''
            result = self._values.get("bucket_name")
            assert result is not None, "Required property 'bucket_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_key_prefix(self) -> typing.Optional[builtins.str]:
            '''The prefix applied to the log file names.

            Constraints:

            - Cannot exceed 512 characters
            - Cannot contain spaces( ), double quotes ("), single quotes ('), a backslash (), or control characters. The hexadecimal codes for invalid characters are:
            - x00 to x20
            - x22
            - x27
            - x5c
            - x7f or larger

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-cluster-loggingproperties.html#cfn-redshift-cluster-loggingproperties-s3keyprefix
            '''
            result = self._values.get("s3_key_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoggingPropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556)
class CfnClusterParameterGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_redshift.CfnClusterParameterGroup",
):
    '''A CloudFormation ``AWS::Redshift::ClusterParameterGroup``.

    Describes a parameter group.

    :cloudformationResource: AWS::Redshift::ClusterParameterGroup
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clusterparametergroup.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_redshift as redshift
        
        cfn_cluster_parameter_group = redshift.CfnClusterParameterGroup(self, "MyCfnClusterParameterGroup",
            description="description",
            parameter_group_family="parameterGroupFamily",
        
            # the properties below are optional
            parameters=[redshift.CfnClusterParameterGroup.ParameterProperty(
                parameter_name="parameterName",
                parameter_value="parameterValue"
            )],
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        description: builtins.str,
        parameter_group_family: builtins.str,
        parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnClusterParameterGroup.ParameterProperty", typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::Redshift::ClusterParameterGroup``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param description: The description of the parameter group.
        :param parameter_group_family: The name of the cluster parameter group family that this cluster parameter group is compatible with.
        :param parameters: An array of parameters to be modified. A maximum of 20 parameters can be modified in a single request. For each parameter to be modified, you must supply at least the parameter name and parameter value; other name-value pairs of the parameter are optional. For the workload management (WLM) configuration, you must supply all the name-value pairs in the wlm_json_configuration parameter.
        :param tags: The list of tags for the cluster parameter group.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnClusterParameterGroup.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnClusterParameterGroupProps(
            description=description,
            parameter_group_family=parameter_group_family,
            parameters=parameters,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnClusterParameterGroup.inspect)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnClusterParameterGroup._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrParameterGroupName")
    def attr_parameter_group_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: ParameterGroupName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrParameterGroupName"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''The list of tags for the cluster parameter group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clusterparametergroup.html#cfn-redshift-clusterparametergroup-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        '''The description of the parameter group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clusterparametergroup.html#cfn-redshift-clusterparametergroup-description
        '''
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnClusterParameterGroup, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="parameterGroupFamily")
    def parameter_group_family(self) -> builtins.str:
        '''The name of the cluster parameter group family that this cluster parameter group is compatible with.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clusterparametergroup.html#cfn-redshift-clusterparametergroup-parametergroupfamily
        '''
        return typing.cast(builtins.str, jsii.get(self, "parameterGroupFamily"))

    @parameter_group_family.setter
    def parameter_group_family(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnClusterParameterGroup, "parameter_group_family").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameterGroupFamily", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnClusterParameterGroup.ParameterProperty", _IResolvable_da3f097b]]]]:
        '''An array of parameters to be modified. A maximum of 20 parameters can be modified in a single request.

        For each parameter to be modified, you must supply at least the parameter name and parameter value; other name-value pairs of the parameter are optional.

        For the workload management (WLM) configuration, you must supply all the name-value pairs in the wlm_json_configuration parameter.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clusterparametergroup.html#cfn-redshift-clusterparametergroup-parameters
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnClusterParameterGroup.ParameterProperty", _IResolvable_da3f097b]]]], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnClusterParameterGroup.ParameterProperty", _IResolvable_da3f097b]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnClusterParameterGroup, "parameters").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_redshift.CfnClusterParameterGroup.ParameterProperty",
        jsii_struct_bases=[],
        name_mapping={
            "parameter_name": "parameterName",
            "parameter_value": "parameterValue",
        },
    )
    class ParameterProperty:
        def __init__(
            self,
            *,
            parameter_name: builtins.str,
            parameter_value: builtins.str,
        ) -> None:
            '''Describes a parameter in a cluster parameter group.

            :param parameter_name: The name of the parameter.
            :param parameter_value: The value of the parameter. If ``ParameterName`` is ``wlm_json_configuration`` , then the maximum size of ``ParameterValue`` is 8000 characters.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-clusterparametergroup-parameter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_redshift as redshift
                
                parameter_property = redshift.CfnClusterParameterGroup.ParameterProperty(
                    parameter_name="parameterName",
                    parameter_value="parameterValue"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnClusterParameterGroup.ParameterProperty.__init__)
                check_type(argname="argument parameter_name", value=parameter_name, expected_type=type_hints["parameter_name"])
                check_type(argname="argument parameter_value", value=parameter_value, expected_type=type_hints["parameter_value"])
            self._values: typing.Dict[str, typing.Any] = {
                "parameter_name": parameter_name,
                "parameter_value": parameter_value,
            }

        @builtins.property
        def parameter_name(self) -> builtins.str:
            '''The name of the parameter.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-clusterparametergroup-parameter.html#cfn-redshift-clusterparametergroup-parameter-parametername
            '''
            result = self._values.get("parameter_name")
            assert result is not None, "Required property 'parameter_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def parameter_value(self) -> builtins.str:
            '''The value of the parameter.

            If ``ParameterName`` is ``wlm_json_configuration`` , then the maximum size of ``ParameterValue`` is 8000 characters.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-clusterparametergroup-parameter.html#cfn-redshift-clusterparametergroup-parameter-parametervalue
            '''
            result = self._values.get("parameter_value")
            assert result is not None, "Required property 'parameter_value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_redshift.CfnClusterParameterGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "parameter_group_family": "parameterGroupFamily",
        "parameters": "parameters",
        "tags": "tags",
    },
)
class CfnClusterParameterGroupProps:
    def __init__(
        self,
        *,
        description: builtins.str,
        parameter_group_family: builtins.str,
        parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnClusterParameterGroup.ParameterProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnClusterParameterGroup``.

        :param description: The description of the parameter group.
        :param parameter_group_family: The name of the cluster parameter group family that this cluster parameter group is compatible with.
        :param parameters: An array of parameters to be modified. A maximum of 20 parameters can be modified in a single request. For each parameter to be modified, you must supply at least the parameter name and parameter value; other name-value pairs of the parameter are optional. For the workload management (WLM) configuration, you must supply all the name-value pairs in the wlm_json_configuration parameter.
        :param tags: The list of tags for the cluster parameter group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clusterparametergroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_redshift as redshift
            
            cfn_cluster_parameter_group_props = redshift.CfnClusterParameterGroupProps(
                description="description",
                parameter_group_family="parameterGroupFamily",
            
                # the properties below are optional
                parameters=[redshift.CfnClusterParameterGroup.ParameterProperty(
                    parameter_name="parameterName",
                    parameter_value="parameterValue"
                )],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnClusterParameterGroupProps.__init__)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument parameter_group_family", value=parameter_group_family, expected_type=type_hints["parameter_group_family"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "parameter_group_family": parameter_group_family,
        }
        if parameters is not None:
            self._values["parameters"] = parameters
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def description(self) -> builtins.str:
        '''The description of the parameter group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clusterparametergroup.html#cfn-redshift-clusterparametergroup-description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parameter_group_family(self) -> builtins.str:
        '''The name of the cluster parameter group family that this cluster parameter group is compatible with.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clusterparametergroup.html#cfn-redshift-clusterparametergroup-parametergroupfamily
        '''
        result = self._values.get("parameter_group_family")
        assert result is not None, "Required property 'parameter_group_family' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnClusterParameterGroup.ParameterProperty, _IResolvable_da3f097b]]]]:
        '''An array of parameters to be modified. A maximum of 20 parameters can be modified in a single request.

        For each parameter to be modified, you must supply at least the parameter name and parameter value; other name-value pairs of the parameter are optional.

        For the workload management (WLM) configuration, you must supply all the name-value pairs in the wlm_json_configuration parameter.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clusterparametergroup.html#cfn-redshift-clusterparametergroup-parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnClusterParameterGroup.ParameterProperty, _IResolvable_da3f097b]]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The list of tags for the cluster parameter group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clusterparametergroup.html#cfn-redshift-clusterparametergroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnClusterParameterGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_redshift.CfnClusterProps",
    jsii_struct_bases=[],
    name_mapping={
        "cluster_type": "clusterType",
        "db_name": "dbName",
        "master_username": "masterUsername",
        "master_user_password": "masterUserPassword",
        "node_type": "nodeType",
        "allow_version_upgrade": "allowVersionUpgrade",
        "aqua_configuration_status": "aquaConfigurationStatus",
        "automated_snapshot_retention_period": "automatedSnapshotRetentionPeriod",
        "availability_zone": "availabilityZone",
        "availability_zone_relocation": "availabilityZoneRelocation",
        "availability_zone_relocation_status": "availabilityZoneRelocationStatus",
        "classic": "classic",
        "cluster_identifier": "clusterIdentifier",
        "cluster_parameter_group_name": "clusterParameterGroupName",
        "cluster_security_groups": "clusterSecurityGroups",
        "cluster_subnet_group_name": "clusterSubnetGroupName",
        "cluster_version": "clusterVersion",
        "defer_maintenance": "deferMaintenance",
        "defer_maintenance_duration": "deferMaintenanceDuration",
        "defer_maintenance_end_time": "deferMaintenanceEndTime",
        "defer_maintenance_start_time": "deferMaintenanceStartTime",
        "destination_region": "destinationRegion",
        "elastic_ip": "elasticIp",
        "encrypted": "encrypted",
        "enhanced_vpc_routing": "enhancedVpcRouting",
        "hsm_client_certificate_identifier": "hsmClientCertificateIdentifier",
        "hsm_configuration_identifier": "hsmConfigurationIdentifier",
        "iam_roles": "iamRoles",
        "kms_key_id": "kmsKeyId",
        "logging_properties": "loggingProperties",
        "maintenance_track_name": "maintenanceTrackName",
        "manual_snapshot_retention_period": "manualSnapshotRetentionPeriod",
        "number_of_nodes": "numberOfNodes",
        "owner_account": "ownerAccount",
        "port": "port",
        "preferred_maintenance_window": "preferredMaintenanceWindow",
        "publicly_accessible": "publiclyAccessible",
        "resource_action": "resourceAction",
        "revision_target": "revisionTarget",
        "rotate_encryption_key": "rotateEncryptionKey",
        "snapshot_cluster_identifier": "snapshotClusterIdentifier",
        "snapshot_copy_grant_name": "snapshotCopyGrantName",
        "snapshot_copy_manual": "snapshotCopyManual",
        "snapshot_copy_retention_period": "snapshotCopyRetentionPeriod",
        "snapshot_identifier": "snapshotIdentifier",
        "tags": "tags",
        "vpc_security_group_ids": "vpcSecurityGroupIds",
    },
)
class CfnClusterProps:
    def __init__(
        self,
        *,
        cluster_type: builtins.str,
        db_name: builtins.str,
        master_username: builtins.str,
        master_user_password: builtins.str,
        node_type: builtins.str,
        allow_version_upgrade: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        aqua_configuration_status: typing.Optional[builtins.str] = None,
        automated_snapshot_retention_period: typing.Optional[jsii.Number] = None,
        availability_zone: typing.Optional[builtins.str] = None,
        availability_zone_relocation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        availability_zone_relocation_status: typing.Optional[builtins.str] = None,
        classic: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        cluster_identifier: typing.Optional[builtins.str] = None,
        cluster_parameter_group_name: typing.Optional[builtins.str] = None,
        cluster_security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        cluster_subnet_group_name: typing.Optional[builtins.str] = None,
        cluster_version: typing.Optional[builtins.str] = None,
        defer_maintenance: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        defer_maintenance_duration: typing.Optional[jsii.Number] = None,
        defer_maintenance_end_time: typing.Optional[builtins.str] = None,
        defer_maintenance_start_time: typing.Optional[builtins.str] = None,
        destination_region: typing.Optional[builtins.str] = None,
        elastic_ip: typing.Optional[builtins.str] = None,
        encrypted: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        enhanced_vpc_routing: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        hsm_client_certificate_identifier: typing.Optional[builtins.str] = None,
        hsm_configuration_identifier: typing.Optional[builtins.str] = None,
        iam_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        logging_properties: typing.Optional[typing.Union[typing.Union[CfnCluster.LoggingPropertiesProperty, typing.Dict[str, typing.Any]], _IResolvable_da3f097b]] = None,
        maintenance_track_name: typing.Optional[builtins.str] = None,
        manual_snapshot_retention_period: typing.Optional[jsii.Number] = None,
        number_of_nodes: typing.Optional[jsii.Number] = None,
        owner_account: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        publicly_accessible: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        resource_action: typing.Optional[builtins.str] = None,
        revision_target: typing.Optional[builtins.str] = None,
        rotate_encryption_key: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        snapshot_cluster_identifier: typing.Optional[builtins.str] = None,
        snapshot_copy_grant_name: typing.Optional[builtins.str] = None,
        snapshot_copy_manual: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        snapshot_copy_retention_period: typing.Optional[jsii.Number] = None,
        snapshot_identifier: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[str, typing.Any]]]] = None,
        vpc_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnCluster``.

        :param cluster_type: The type of the cluster. When cluster type is specified as. - ``single-node`` , the *NumberOfNodes* parameter is not required. - ``multi-node`` , the *NumberOfNodes* parameter is required. Valid Values: ``multi-node`` | ``single-node`` Default: ``multi-node``
        :param db_name: The name of the first database to be created when the cluster is created. To create additional databases after the cluster is created, connect to the cluster with a SQL client and use SQL commands to create a database. For more information, go to `Create a Database <https://docs.aws.amazon.com/redshift/latest/dg/t_creating_database.html>`_ in the Amazon Redshift Database Developer Guide. Default: ``dev`` Constraints: - Must contain 1 to 64 alphanumeric characters. - Must contain only lowercase letters. - Cannot be a word that is reserved by the service. A list of reserved words can be found in `Reserved Words <https://docs.aws.amazon.com/redshift/latest/dg/r_pg_keywords.html>`_ in the Amazon Redshift Database Developer Guide.
        :param master_username: The user name associated with the admin user account for the cluster that is being created. Constraints: - Must be 1 - 128 alphanumeric characters. The user name can't be ``PUBLIC`` . - First character must be a letter. - Cannot be a reserved word. A list of reserved words can be found in `Reserved Words <https://docs.aws.amazon.com/redshift/latest/dg/r_pg_keywords.html>`_ in the Amazon Redshift Database Developer Guide.
        :param master_user_password: The password associated with the admin user account for the cluster that is being created. Constraints: - Must be between 8 and 64 characters in length. - Must contain at least one uppercase letter. - Must contain at least one lowercase letter. - Must contain one number. - Can be any printable ASCII character (ASCII code 33-126) except ' (single quote), " (double quote), , /, or @.
        :param node_type: The node type to be provisioned for the cluster. For information about node types, go to `Working with Clusters <https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#how-many-nodes>`_ in the *Amazon Redshift Cluster Management Guide* . Valid Values: ``ds2.xlarge`` | ``ds2.8xlarge`` | ``dc1.large`` | ``dc1.8xlarge`` | ``dc2.large`` | ``dc2.8xlarge`` | ``ra3.xlplus`` | ``ra3.4xlarge`` | ``ra3.16xlarge``
        :param allow_version_upgrade: If ``true`` , major version upgrades can be applied during the maintenance window to the Amazon Redshift engine that is running on the cluster. When a new major version of the Amazon Redshift engine is released, you can request that the service automatically apply upgrades during the maintenance window to the Amazon Redshift engine that is running on your cluster. Default: ``true``
        :param aqua_configuration_status: The value represents how the cluster is configured to use AQUA (Advanced Query Accelerator) when it is created. Possible values include the following. - enabled - Use AQUA if it is available for the current AWS Region and Amazon Redshift node type. - disabled - Don't use AQUA. - auto - Amazon Redshift determines whether to use AQUA.
        :param automated_snapshot_retention_period: The number of days that automated snapshots are retained. If the value is 0, automated snapshots are disabled. Even if automated snapshots are disabled, you can still create manual snapshots when you want with `CreateClusterSnapshot <https://docs.aws.amazon.com/redshift/latest/APIReference/API_CreateClusterSnapshot.html>`_ in the *Amazon Redshift API Reference* . Default: ``1`` Constraints: Must be a value from 0 to 35.
        :param availability_zone: The EC2 Availability Zone (AZ) in which you want Amazon Redshift to provision the cluster. For example, if you have several EC2 instances running in a specific Availability Zone, then you might want the cluster to be provisioned in the same zone in order to decrease network latency. Default: A random, system-chosen Availability Zone in the region that is specified by the endpoint. Example: ``us-east-2d`` Constraint: The specified Availability Zone must be in the same region as the current endpoint.
        :param availability_zone_relocation: The option to enable relocation for an Amazon Redshift cluster between Availability Zones after the cluster is created.
        :param availability_zone_relocation_status: Describes the status of the Availability Zone relocation operation.
        :param classic: A boolean value indicating whether the resize operation is using the classic resize process. If you don't provide this parameter or set the value to ``false`` , the resize type is elastic.
        :param cluster_identifier: A unique identifier for the cluster. You use this identifier to refer to the cluster for any subsequent cluster operations such as deleting or modifying. The identifier also appears in the Amazon Redshift console. Constraints: - Must contain from 1 to 63 alphanumeric characters or hyphens. - Alphabetic characters must be lowercase. - First character must be a letter. - Cannot end with a hyphen or contain two consecutive hyphens. - Must be unique for all clusters within an AWS account . Example: ``myexamplecluster``
        :param cluster_parameter_group_name: The name of the parameter group to be associated with this cluster. Default: The default Amazon Redshift cluster parameter group. For information about the default parameter group, go to `Working with Amazon Redshift Parameter Groups <https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html>`_ Constraints: - Must be 1 to 255 alphanumeric characters or hyphens. - First character must be a letter. - Cannot end with a hyphen or contain two consecutive hyphens.
        :param cluster_security_groups: A list of security groups to be associated with this cluster. Default: The default cluster security group for Amazon Redshift.
        :param cluster_subnet_group_name: The name of a cluster subnet group to be associated with this cluster. If this parameter is not provided the resulting cluster will be deployed outside virtual private cloud (VPC).
        :param cluster_version: The version of the Amazon Redshift engine software that you want to deploy on the cluster. The version selected runs on all the nodes in the cluster. Constraints: Only version 1.0 is currently available. Example: ``1.0``
        :param defer_maintenance: ``AWS::Redshift::Cluster.DeferMaintenance``.
        :param defer_maintenance_duration: ``AWS::Redshift::Cluster.DeferMaintenanceDuration``.
        :param defer_maintenance_end_time: ``AWS::Redshift::Cluster.DeferMaintenanceEndTime``.
        :param defer_maintenance_start_time: ``AWS::Redshift::Cluster.DeferMaintenanceStartTime``.
        :param destination_region: The destination region that snapshots are automatically copied to when cross-region snapshot copy is enabled.
        :param elastic_ip: The Elastic IP (EIP) address for the cluster. Constraints: The cluster must be provisioned in EC2-VPC and publicly-accessible through an Internet gateway. For more information about provisioning clusters in EC2-VPC, go to `Supported Platforms to Launch Your Cluster <https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#cluster-platforms>`_ in the Amazon Redshift Cluster Management Guide.
        :param encrypted: If ``true`` , the data in the cluster is encrypted at rest. Default: false
        :param enhanced_vpc_routing: An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see `Enhanced VPC Routing <https://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html>`_ in the Amazon Redshift Cluster Management Guide. If this option is ``true`` , enhanced VPC routing is enabled. Default: false
        :param hsm_client_certificate_identifier: Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.
        :param hsm_configuration_identifier: Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.
        :param iam_roles: A list of AWS Identity and Access Management (IAM) roles that can be used by the cluster to access other AWS services. You must supply the IAM roles in their Amazon Resource Name (ARN) format. The maximum number of IAM roles that you can associate is subject to a quota. For more information, go to `Quotas and limits <https://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-limits.html>`_ in the *Amazon Redshift Cluster Management Guide* .
        :param kms_key_id: The AWS Key Management Service (KMS) key ID of the encryption key that you want to use to encrypt data in the cluster.
        :param logging_properties: Specifies logging information, such as queries and connection attempts, for the specified Amazon Redshift cluster.
        :param maintenance_track_name: An optional parameter for the name of the maintenance track for the cluster. If you don't provide a maintenance track name, the cluster is assigned to the ``current`` track.
        :param manual_snapshot_retention_period: The default number of days to retain a manual snapshot. If the value is -1, the snapshot is retained indefinitely. This setting doesn't change the retention period of existing snapshots. The value must be either -1 or an integer between 1 and 3,653.
        :param number_of_nodes: The number of compute nodes in the cluster. This parameter is required when the *ClusterType* parameter is specified as ``multi-node`` . For information about determining how many nodes you need, go to `Working with Clusters <https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#how-many-nodes>`_ in the *Amazon Redshift Cluster Management Guide* . If you don't specify this parameter, you get a single-node cluster. When requesting a multi-node cluster, you must specify the number of nodes that you want in the cluster. Default: ``1`` Constraints: Value must be at least 1 and no more than 100.
        :param owner_account: The AWS account used to create or copy the snapshot. Required if you are restoring a snapshot you do not own, optional if you own the snapshot.
        :param port: The port number on which the cluster accepts incoming connections. The cluster is accessible only via the JDBC and ODBC connection strings. Part of the connection string requires the port on which the cluster will listen for incoming connections. Default: ``5439`` Valid Values: ``1150-65535``
        :param preferred_maintenance_window: The weekly time range (in UTC) during which automated cluster maintenance can occur. Format: ``ddd:hh24:mi-ddd:hh24:mi`` Default: A 30-minute window selected at random from an 8-hour block of time per region, occurring on a random day of the week. For more information about the time blocks for each region, see `Maintenance Windows <https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#rs-maintenance-windows>`_ in Amazon Redshift Cluster Management Guide. Valid Days: Mon | Tue | Wed | Thu | Fri | Sat | Sun Constraints: Minimum 30-minute window.
        :param publicly_accessible: If ``true`` , the cluster can be accessed from a public network.
        :param resource_action: ``AWS::Redshift::Cluster.ResourceAction``.
        :param revision_target: ``AWS::Redshift::Cluster.RevisionTarget``.
        :param rotate_encryption_key: ``AWS::Redshift::Cluster.RotateEncryptionKey``.
        :param snapshot_cluster_identifier: The name of the cluster the source snapshot was created from. This parameter is required if your IAM user has a policy containing a snapshot resource element that specifies anything other than * for the cluster name.
        :param snapshot_copy_grant_name: The name of the snapshot copy grant.
        :param snapshot_copy_manual: Indicates whether to apply the snapshot retention period to newly copied manual snapshots instead of automated snapshots.
        :param snapshot_copy_retention_period: The number of days to retain automated snapshots in the destination AWS Region after they are copied from the source AWS Region . By default, this only changes the retention period of copied automated snapshots. If you decrease the retention period for automated snapshots that are copied to a destination AWS Region , Amazon Redshift deletes any existing automated snapshots that were copied to the destination AWS Region and that fall outside of the new retention period. Constraints: Must be at least 1 and no more than 35 for automated snapshots. If you specify the ``manual`` option, only newly copied manual snapshots will have the new retention period. If you specify the value of -1 newly copied manual snapshots are retained indefinitely. Constraints: The number of days must be either -1 or an integer between 1 and 3,653 for manual snapshots.
        :param snapshot_identifier: The name of the snapshot from which to create the new cluster. This parameter isn't case sensitive. Example: ``my-snapshot-id``
        :param tags: A list of tag instances.
        :param vpc_security_group_ids: A list of Virtual Private Cloud (VPC) security groups to be associated with the cluster. Default: The default VPC security group is associated with the cluster.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_redshift as redshift
            
            cfn_cluster_props = redshift.CfnClusterProps(
                cluster_type="clusterType",
                db_name="dbName",
                master_username="masterUsername",
                master_user_password="masterUserPassword",
                node_type="nodeType",
            
                # the properties below are optional
                allow_version_upgrade=False,
                aqua_configuration_status="aquaConfigurationStatus",
                automated_snapshot_retention_period=123,
                availability_zone="availabilityZone",
                availability_zone_relocation=False,
                availability_zone_relocation_status="availabilityZoneRelocationStatus",
                classic=False,
                cluster_identifier="clusterIdentifier",
                cluster_parameter_group_name="clusterParameterGroupName",
                cluster_security_groups=["clusterSecurityGroups"],
                cluster_subnet_group_name="clusterSubnetGroupName",
                cluster_version="clusterVersion",
                defer_maintenance=False,
                defer_maintenance_duration=123,
                defer_maintenance_end_time="deferMaintenanceEndTime",
                defer_maintenance_start_time="deferMaintenanceStartTime",
                destination_region="destinationRegion",
                elastic_ip="elasticIp",
                encrypted=False,
                enhanced_vpc_routing=False,
                hsm_client_certificate_identifier="hsmClientCertificateIdentifier",
                hsm_configuration_identifier="hsmConfigurationIdentifier",
                iam_roles=["iamRoles"],
                kms_key_id="kmsKeyId",
                logging_properties=redshift.CfnCluster.LoggingPropertiesProperty(
                    bucket_name="bucketName",
            
                    # the properties below are optional
                    s3_key_prefix="s3KeyPrefix"
                ),
                maintenance_track_name="maintenanceTrackName",
                manual_snapshot_retention_period=123,
                number_of_nodes=123,
                owner_account="ownerAccount",
                port=123,
                preferred_maintenance_window="preferredMaintenanceWindow",
                publicly_accessible=False,
                resource_action="resourceAction",
                revision_target="revisionTarget",
                rotate_encryption_key=False,
                snapshot_cluster_identifier="snapshotClusterIdentifier",
                snapshot_copy_grant_name="snapshotCopyGrantName",
                snapshot_copy_manual=False,
                snapshot_copy_retention_period=123,
                snapshot_identifier="snapshotIdentifier",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                vpc_security_group_ids=["vpcSecurityGroupIds"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnClusterProps.__init__)
            check_type(argname="argument cluster_type", value=cluster_type, expected_type=type_hints["cluster_type"])
            check_type(argname="argument db_name", value=db_name, expected_type=type_hints["db_name"])
            check_type(argname="argument master_username", value=master_username, expected_type=type_hints["master_username"])
            check_type(argname="argument master_user_password", value=master_user_password, expected_type=type_hints["master_user_password"])
            check_type(argname="argument node_type", value=node_type, expected_type=type_hints["node_type"])
            check_type(argname="argument allow_version_upgrade", value=allow_version_upgrade, expected_type=type_hints["allow_version_upgrade"])
            check_type(argname="argument aqua_configuration_status", value=aqua_configuration_status, expected_type=type_hints["aqua_configuration_status"])
            check_type(argname="argument automated_snapshot_retention_period", value=automated_snapshot_retention_period, expected_type=type_hints["automated_snapshot_retention_period"])
            check_type(argname="argument availability_zone", value=availability_zone, expected_type=type_hints["availability_zone"])
            check_type(argname="argument availability_zone_relocation", value=availability_zone_relocation, expected_type=type_hints["availability_zone_relocation"])
            check_type(argname="argument availability_zone_relocation_status", value=availability_zone_relocation_status, expected_type=type_hints["availability_zone_relocation_status"])
            check_type(argname="argument classic", value=classic, expected_type=type_hints["classic"])
            check_type(argname="argument cluster_identifier", value=cluster_identifier, expected_type=type_hints["cluster_identifier"])
            check_type(argname="argument cluster_parameter_group_name", value=cluster_parameter_group_name, expected_type=type_hints["cluster_parameter_group_name"])
            check_type(argname="argument cluster_security_groups", value=cluster_security_groups, expected_type=type_hints["cluster_security_groups"])
            check_type(argname="argument cluster_subnet_group_name", value=cluster_subnet_group_name, expected_type=type_hints["cluster_subnet_group_name"])
            check_type(argname="argument cluster_version", value=cluster_version, expected_type=type_hints["cluster_version"])
            check_type(argname="argument defer_maintenance", value=defer_maintenance, expected_type=type_hints["defer_maintenance"])
            check_type(argname="argument defer_maintenance_duration", value=defer_maintenance_duration, expected_type=type_hints["defer_maintenance_duration"])
            check_type(argname="argument defer_maintenance_end_time", value=defer_maintenance_end_time, expected_type=type_hints["defer_maintenance_end_time"])
            check_type(argname="argument defer_maintenance_start_time", value=defer_maintenance_start_time, expected_type=type_hints["defer_maintenance_start_time"])
            check_type(argname="argument destination_region", value=destination_region, expected_type=type_hints["destination_region"])
            check_type(argname="argument elastic_ip", value=elastic_ip, expected_type=type_hints["elastic_ip"])
            check_type(argname="argument encrypted", value=encrypted, expected_type=type_hints["encrypted"])
            check_type(argname="argument enhanced_vpc_routing", value=enhanced_vpc_routing, expected_type=type_hints["enhanced_vpc_routing"])
            check_type(argname="argument hsm_client_certificate_identifier", value=hsm_client_certificate_identifier, expected_type=type_hints["hsm_client_certificate_identifier"])
            check_type(argname="argument hsm_configuration_identifier", value=hsm_configuration_identifier, expected_type=type_hints["hsm_configuration_identifier"])
            check_type(argname="argument iam_roles", value=iam_roles, expected_type=type_hints["iam_roles"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument logging_properties", value=logging_properties, expected_type=type_hints["logging_properties"])
            check_type(argname="argument maintenance_track_name", value=maintenance_track_name, expected_type=type_hints["maintenance_track_name"])
            check_type(argname="argument manual_snapshot_retention_period", value=manual_snapshot_retention_period, expected_type=type_hints["manual_snapshot_retention_period"])
            check_type(argname="argument number_of_nodes", value=number_of_nodes, expected_type=type_hints["number_of_nodes"])
            check_type(argname="argument owner_account", value=owner_account, expected_type=type_hints["owner_account"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument preferred_maintenance_window", value=preferred_maintenance_window, expected_type=type_hints["preferred_maintenance_window"])
            check_type(argname="argument publicly_accessible", value=publicly_accessible, expected_type=type_hints["publicly_accessible"])
            check_type(argname="argument resource_action", value=resource_action, expected_type=type_hints["resource_action"])
            check_type(argname="argument revision_target", value=revision_target, expected_type=type_hints["revision_target"])
            check_type(argname="argument rotate_encryption_key", value=rotate_encryption_key, expected_type=type_hints["rotate_encryption_key"])
            check_type(argname="argument snapshot_cluster_identifier", value=snapshot_cluster_identifier, expected_type=type_hints["snapshot_cluster_identifier"])
            check_type(argname="argument snapshot_copy_grant_name", value=snapshot_copy_grant_name, expected_type=type_hints["snapshot_copy_grant_name"])
            check_type(argname="argument snapshot_copy_manual", value=snapshot_copy_manual, expected_type=type_hints["snapshot_copy_manual"])
            check_type(argname="argument snapshot_copy_retention_period", value=snapshot_copy_retention_period, expected_type=type_hints["snapshot_copy_retention_period"])
            check_type(argname="argument snapshot_identifier", value=snapshot_identifier, expected_type=type_hints["snapshot_identifier"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument vpc_security_group_ids", value=vpc_security_group_ids, expected_type=type_hints["vpc_security_group_ids"])
        self._values: typing.Dict[str, typing.Any] = {
            "cluster_type": cluster_type,
            "db_name": db_name,
            "master_username": master_username,
            "master_user_password": master_user_password,
            "node_type": node_type,
        }
        if allow_version_upgrade is not None:
            self._values["allow_version_upgrade"] = allow_version_upgrade
        if aqua_configuration_status is not None:
            self._values["aqua_configuration_status"] = aqua_configuration_status
        if automated_snapshot_retention_period is not None:
            self._values["automated_snapshot_retention_period"] = automated_snapshot_retention_period
        if availability_zone is not None:
            self._values["availability_zone"] = availability_zone
        if availability_zone_relocation is not None:
            self._values["availability_zone_relocation"] = availability_zone_relocation
        if availability_zone_relocation_status is not None:
            self._values["availability_zone_relocation_status"] = availability_zone_relocation_status
        if classic is not None:
            self._values["classic"] = classic
        if cluster_identifier is not None:
            self._values["cluster_identifier"] = cluster_identifier
        if cluster_parameter_group_name is not None:
            self._values["cluster_parameter_group_name"] = cluster_parameter_group_name
        if cluster_security_groups is not None:
            self._values["cluster_security_groups"] = cluster_security_groups
        if cluster_subnet_group_name is not None:
            self._values["cluster_subnet_group_name"] = cluster_subnet_group_name
        if cluster_version is not None:
            self._values["cluster_version"] = cluster_version
        if defer_maintenance is not None:
            self._values["defer_maintenance"] = defer_maintenance
        if defer_maintenance_duration is not None:
            self._values["defer_maintenance_duration"] = defer_maintenance_duration
        if defer_maintenance_end_time is not None:
            self._values["defer_maintenance_end_time"] = defer_maintenance_end_time
        if defer_maintenance_start_time is not None:
            self._values["defer_maintenance_start_time"] = defer_maintenance_start_time
        if destination_region is not None:
            self._values["destination_region"] = destination_region
        if elastic_ip is not None:
            self._values["elastic_ip"] = elastic_ip
        if encrypted is not None:
            self._values["encrypted"] = encrypted
        if enhanced_vpc_routing is not None:
            self._values["enhanced_vpc_routing"] = enhanced_vpc_routing
        if hsm_client_certificate_identifier is not None:
            self._values["hsm_client_certificate_identifier"] = hsm_client_certificate_identifier
        if hsm_configuration_identifier is not None:
            self._values["hsm_configuration_identifier"] = hsm_configuration_identifier
        if iam_roles is not None:
            self._values["iam_roles"] = iam_roles
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if logging_properties is not None:
            self._values["logging_properties"] = logging_properties
        if maintenance_track_name is not None:
            self._values["maintenance_track_name"] = maintenance_track_name
        if manual_snapshot_retention_period is not None:
            self._values["manual_snapshot_retention_period"] = manual_snapshot_retention_period
        if number_of_nodes is not None:
            self._values["number_of_nodes"] = number_of_nodes
        if owner_account is not None:
            self._values["owner_account"] = owner_account
        if port is not None:
            self._values["port"] = port
        if preferred_maintenance_window is not None:
            self._values["preferred_maintenance_window"] = preferred_maintenance_window
        if publicly_accessible is not None:
            self._values["publicly_accessible"] = publicly_accessible
        if resource_action is not None:
            self._values["resource_action"] = resource_action
        if revision_target is not None:
            self._values["revision_target"] = revision_target
        if rotate_encryption_key is not None:
            self._values["rotate_encryption_key"] = rotate_encryption_key
        if snapshot_cluster_identifier is not None:
            self._values["snapshot_cluster_identifier"] = snapshot_cluster_identifier
        if snapshot_copy_grant_name is not None:
            self._values["snapshot_copy_grant_name"] = snapshot_copy_grant_name
        if snapshot_copy_manual is not None:
            self._values["snapshot_copy_manual"] = snapshot_copy_manual
        if snapshot_copy_retention_period is not None:
            self._values["snapshot_copy_retention_period"] = snapshot_copy_retention_period
        if snapshot_identifier is not None:
            self._values["snapshot_identifier"] = snapshot_identifier
        if tags is not None:
            self._values["tags"] = tags
        if vpc_security_group_ids is not None:
            self._values["vpc_security_group_ids"] = vpc_security_group_ids

    @builtins.property
    def cluster_type(self) -> builtins.str:
        '''The type of the cluster. When cluster type is specified as.

        - ``single-node`` , the *NumberOfNodes* parameter is not required.
        - ``multi-node`` , the *NumberOfNodes* parameter is required.

        Valid Values: ``multi-node`` | ``single-node``

        Default: ``multi-node``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-clustertype
        '''
        result = self._values.get("cluster_type")
        assert result is not None, "Required property 'cluster_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def db_name(self) -> builtins.str:
        '''The name of the first database to be created when the cluster is created.

        To create additional databases after the cluster is created, connect to the cluster with a SQL client and use SQL commands to create a database. For more information, go to `Create a Database <https://docs.aws.amazon.com/redshift/latest/dg/t_creating_database.html>`_ in the Amazon Redshift Database Developer Guide.

        Default: ``dev``

        Constraints:

        - Must contain 1 to 64 alphanumeric characters.
        - Must contain only lowercase letters.
        - Cannot be a word that is reserved by the service. A list of reserved words can be found in `Reserved Words <https://docs.aws.amazon.com/redshift/latest/dg/r_pg_keywords.html>`_ in the Amazon Redshift Database Developer Guide.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-dbname
        '''
        result = self._values.get("db_name")
        assert result is not None, "Required property 'db_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def master_username(self) -> builtins.str:
        '''The user name associated with the admin user account for the cluster that is being created.

        Constraints:

        - Must be 1 - 128 alphanumeric characters. The user name can't be ``PUBLIC`` .
        - First character must be a letter.
        - Cannot be a reserved word. A list of reserved words can be found in `Reserved Words <https://docs.aws.amazon.com/redshift/latest/dg/r_pg_keywords.html>`_ in the Amazon Redshift Database Developer Guide.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-masterusername
        '''
        result = self._values.get("master_username")
        assert result is not None, "Required property 'master_username' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def master_user_password(self) -> builtins.str:
        '''The password associated with the admin user account for the cluster that is being created.

        Constraints:

        - Must be between 8 and 64 characters in length.
        - Must contain at least one uppercase letter.
        - Must contain at least one lowercase letter.
        - Must contain one number.
        - Can be any printable ASCII character (ASCII code 33-126) except ' (single quote), " (double quote), , /, or @.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-masteruserpassword
        '''
        result = self._values.get("master_user_password")
        assert result is not None, "Required property 'master_user_password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def node_type(self) -> builtins.str:
        '''The node type to be provisioned for the cluster.

        For information about node types, go to `Working with Clusters <https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#how-many-nodes>`_ in the *Amazon Redshift Cluster Management Guide* .

        Valid Values: ``ds2.xlarge`` | ``ds2.8xlarge`` | ``dc1.large`` | ``dc1.8xlarge`` | ``dc2.large`` | ``dc2.8xlarge`` | ``ra3.xlplus`` | ``ra3.4xlarge`` | ``ra3.16xlarge``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-nodetype
        '''
        result = self._values.get("node_type")
        assert result is not None, "Required property 'node_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allow_version_upgrade(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''If ``true`` , major version upgrades can be applied during the maintenance window to the Amazon Redshift engine that is running on the cluster.

        When a new major version of the Amazon Redshift engine is released, you can request that the service automatically apply upgrades during the maintenance window to the Amazon Redshift engine that is running on your cluster.

        Default: ``true``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-allowversionupgrade
        '''
        result = self._values.get("allow_version_upgrade")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def aqua_configuration_status(self) -> typing.Optional[builtins.str]:
        '''The value represents how the cluster is configured to use AQUA (Advanced Query Accelerator) when it is created.

        Possible values include the following.

        - enabled - Use AQUA if it is available for the current AWS Region and Amazon Redshift node type.
        - disabled - Don't use AQUA.
        - auto - Amazon Redshift determines whether to use AQUA.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-aquaconfigurationstatus
        '''
        result = self._values.get("aqua_configuration_status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def automated_snapshot_retention_period(self) -> typing.Optional[jsii.Number]:
        '''The number of days that automated snapshots are retained.

        If the value is 0, automated snapshots are disabled. Even if automated snapshots are disabled, you can still create manual snapshots when you want with `CreateClusterSnapshot <https://docs.aws.amazon.com/redshift/latest/APIReference/API_CreateClusterSnapshot.html>`_ in the *Amazon Redshift API Reference* .

        Default: ``1``

        Constraints: Must be a value from 0 to 35.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-automatedsnapshotretentionperiod
        '''
        result = self._values.get("automated_snapshot_retention_period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''The EC2 Availability Zone (AZ) in which you want Amazon Redshift to provision the cluster.

        For example, if you have several EC2 instances running in a specific Availability Zone, then you might want the cluster to be provisioned in the same zone in order to decrease network latency.

        Default: A random, system-chosen Availability Zone in the region that is specified by the endpoint.

        Example: ``us-east-2d``

        Constraint: The specified Availability Zone must be in the same region as the current endpoint.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-availabilityzone
        '''
        result = self._values.get("availability_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def availability_zone_relocation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''The option to enable relocation for an Amazon Redshift cluster between Availability Zones after the cluster is created.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-availabilityzonerelocation
        '''
        result = self._values.get("availability_zone_relocation")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def availability_zone_relocation_status(self) -> typing.Optional[builtins.str]:
        '''Describes the status of the Availability Zone relocation operation.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-availabilityzonerelocationstatus
        '''
        result = self._values.get("availability_zone_relocation_status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def classic(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A boolean value indicating whether the resize operation is using the classic resize process.

        If you don't provide this parameter or set the value to ``false`` , the resize type is elastic.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-classic
        '''
        result = self._values.get("classic")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def cluster_identifier(self) -> typing.Optional[builtins.str]:
        '''A unique identifier for the cluster.

        You use this identifier to refer to the cluster for any subsequent cluster operations such as deleting or modifying. The identifier also appears in the Amazon Redshift console.

        Constraints:

        - Must contain from 1 to 63 alphanumeric characters or hyphens.
        - Alphabetic characters must be lowercase.
        - First character must be a letter.
        - Cannot end with a hyphen or contain two consecutive hyphens.
        - Must be unique for all clusters within an AWS account .

        Example: ``myexamplecluster``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-clusteridentifier
        '''
        result = self._values.get("cluster_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cluster_parameter_group_name(self) -> typing.Optional[builtins.str]:
        '''The name of the parameter group to be associated with this cluster.

        Default: The default Amazon Redshift cluster parameter group. For information about the default parameter group, go to `Working with Amazon Redshift Parameter Groups <https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html>`_

        Constraints:

        - Must be 1 to 255 alphanumeric characters or hyphens.
        - First character must be a letter.
        - Cannot end with a hyphen or contain two consecutive hyphens.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-clusterparametergroupname
        '''
        result = self._values.get("cluster_parameter_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cluster_security_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of security groups to be associated with this cluster.

        Default: The default cluster security group for Amazon Redshift.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-clustersecuritygroups
        '''
        result = self._values.get("cluster_security_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def cluster_subnet_group_name(self) -> typing.Optional[builtins.str]:
        '''The name of a cluster subnet group to be associated with this cluster.

        If this parameter is not provided the resulting cluster will be deployed outside virtual private cloud (VPC).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-clustersubnetgroupname
        '''
        result = self._values.get("cluster_subnet_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cluster_version(self) -> typing.Optional[builtins.str]:
        '''The version of the Amazon Redshift engine software that you want to deploy on the cluster.

        The version selected runs on all the nodes in the cluster.

        Constraints: Only version 1.0 is currently available.

        Example: ``1.0``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-clusterversion
        '''
        result = self._values.get("cluster_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def defer_maintenance(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''``AWS::Redshift::Cluster.DeferMaintenance``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-defermaintenance
        '''
        result = self._values.get("defer_maintenance")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def defer_maintenance_duration(self) -> typing.Optional[jsii.Number]:
        '''``AWS::Redshift::Cluster.DeferMaintenanceDuration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-defermaintenanceduration
        '''
        result = self._values.get("defer_maintenance_duration")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def defer_maintenance_end_time(self) -> typing.Optional[builtins.str]:
        '''``AWS::Redshift::Cluster.DeferMaintenanceEndTime``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-defermaintenanceendtime
        '''
        result = self._values.get("defer_maintenance_end_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def defer_maintenance_start_time(self) -> typing.Optional[builtins.str]:
        '''``AWS::Redshift::Cluster.DeferMaintenanceStartTime``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-defermaintenancestarttime
        '''
        result = self._values.get("defer_maintenance_start_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def destination_region(self) -> typing.Optional[builtins.str]:
        '''The destination region that snapshots are automatically copied to when cross-region snapshot copy is enabled.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-destinationregion
        '''
        result = self._values.get("destination_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def elastic_ip(self) -> typing.Optional[builtins.str]:
        '''The Elastic IP (EIP) address for the cluster.

        Constraints: The cluster must be provisioned in EC2-VPC and publicly-accessible through an Internet gateway. For more information about provisioning clusters in EC2-VPC, go to `Supported Platforms to Launch Your Cluster <https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#cluster-platforms>`_ in the Amazon Redshift Cluster Management Guide.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-elasticip
        '''
        result = self._values.get("elastic_ip")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encrypted(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''If ``true`` , the data in the cluster is encrypted at rest.

        Default: false

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-encrypted
        '''
        result = self._values.get("encrypted")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def enhanced_vpc_routing(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''An option that specifies whether to create the cluster with enhanced VPC routing enabled.

        To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see `Enhanced VPC Routing <https://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html>`_ in the Amazon Redshift Cluster Management Guide.

        If this option is ``true`` , enhanced VPC routing is enabled.

        Default: false

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-enhancedvpcrouting
        '''
        result = self._values.get("enhanced_vpc_routing")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def hsm_client_certificate_identifier(self) -> typing.Optional[builtins.str]:
        '''Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-hsmclientcertificateidentifier
        '''
        result = self._values.get("hsm_client_certificate_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def hsm_configuration_identifier(self) -> typing.Optional[builtins.str]:
        '''Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-hsmconfigurationidentifier
        '''
        result = self._values.get("hsm_configuration_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iam_roles(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of AWS Identity and Access Management (IAM) roles that can be used by the cluster to access other AWS services.

        You must supply the IAM roles in their Amazon Resource Name (ARN) format.

        The maximum number of IAM roles that you can associate is subject to a quota. For more information, go to `Quotas and limits <https://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-limits.html>`_ in the *Amazon Redshift Cluster Management Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-iamroles
        '''
        result = self._values.get("iam_roles")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''The AWS Key Management Service (KMS) key ID of the encryption key that you want to use to encrypt data in the cluster.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-kmskeyid
        '''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def logging_properties(
        self,
    ) -> typing.Optional[typing.Union[CfnCluster.LoggingPropertiesProperty, _IResolvable_da3f097b]]:
        '''Specifies logging information, such as queries and connection attempts, for the specified Amazon Redshift cluster.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-loggingproperties
        '''
        result = self._values.get("logging_properties")
        return typing.cast(typing.Optional[typing.Union[CfnCluster.LoggingPropertiesProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def maintenance_track_name(self) -> typing.Optional[builtins.str]:
        '''An optional parameter for the name of the maintenance track for the cluster.

        If you don't provide a maintenance track name, the cluster is assigned to the ``current`` track.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-maintenancetrackname
        '''
        result = self._values.get("maintenance_track_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def manual_snapshot_retention_period(self) -> typing.Optional[jsii.Number]:
        '''The default number of days to retain a manual snapshot.

        If the value is -1, the snapshot is retained indefinitely. This setting doesn't change the retention period of existing snapshots.

        The value must be either -1 or an integer between 1 and 3,653.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-manualsnapshotretentionperiod
        '''
        result = self._values.get("manual_snapshot_retention_period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def number_of_nodes(self) -> typing.Optional[jsii.Number]:
        '''The number of compute nodes in the cluster.

        This parameter is required when the *ClusterType* parameter is specified as ``multi-node`` .

        For information about determining how many nodes you need, go to `Working with Clusters <https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#how-many-nodes>`_ in the *Amazon Redshift Cluster Management Guide* .

        If you don't specify this parameter, you get a single-node cluster. When requesting a multi-node cluster, you must specify the number of nodes that you want in the cluster.

        Default: ``1``

        Constraints: Value must be at least 1 and no more than 100.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-numberofnodes
        '''
        result = self._values.get("number_of_nodes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def owner_account(self) -> typing.Optional[builtins.str]:
        '''The AWS account used to create or copy the snapshot.

        Required if you are restoring a snapshot you do not own, optional if you own the snapshot.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-owneraccount
        '''
        result = self._values.get("owner_account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''The port number on which the cluster accepts incoming connections.

        The cluster is accessible only via the JDBC and ODBC connection strings. Part of the connection string requires the port on which the cluster will listen for incoming connections.

        Default: ``5439``

        Valid Values: ``1150-65535``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-port
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def preferred_maintenance_window(self) -> typing.Optional[builtins.str]:
        '''The weekly time range (in UTC) during which automated cluster maintenance can occur.

        Format: ``ddd:hh24:mi-ddd:hh24:mi``

        Default: A 30-minute window selected at random from an 8-hour block of time per region, occurring on a random day of the week. For more information about the time blocks for each region, see `Maintenance Windows <https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#rs-maintenance-windows>`_ in Amazon Redshift Cluster Management Guide.

        Valid Days: Mon | Tue | Wed | Thu | Fri | Sat | Sun

        Constraints: Minimum 30-minute window.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-preferredmaintenancewindow
        '''
        result = self._values.get("preferred_maintenance_window")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def publicly_accessible(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''If ``true`` , the cluster can be accessed from a public network.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-publiclyaccessible
        '''
        result = self._values.get("publicly_accessible")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def resource_action(self) -> typing.Optional[builtins.str]:
        '''``AWS::Redshift::Cluster.ResourceAction``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-resourceaction
        '''
        result = self._values.get("resource_action")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def revision_target(self) -> typing.Optional[builtins.str]:
        '''``AWS::Redshift::Cluster.RevisionTarget``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-revisiontarget
        '''
        result = self._values.get("revision_target")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rotate_encryption_key(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''``AWS::Redshift::Cluster.RotateEncryptionKey``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-rotateencryptionkey
        '''
        result = self._values.get("rotate_encryption_key")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def snapshot_cluster_identifier(self) -> typing.Optional[builtins.str]:
        '''The name of the cluster the source snapshot was created from.

        This parameter is required if your IAM user has a policy containing a snapshot resource element that specifies anything other than * for the cluster name.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-snapshotclusteridentifier
        '''
        result = self._values.get("snapshot_cluster_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def snapshot_copy_grant_name(self) -> typing.Optional[builtins.str]:
        '''The name of the snapshot copy grant.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-snapshotcopygrantname
        '''
        result = self._values.get("snapshot_copy_grant_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def snapshot_copy_manual(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates whether to apply the snapshot retention period to newly copied manual snapshots instead of automated snapshots.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-snapshotcopymanual
        '''
        result = self._values.get("snapshot_copy_manual")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def snapshot_copy_retention_period(self) -> typing.Optional[jsii.Number]:
        '''The number of days to retain automated snapshots in the destination AWS Region after they are copied from the source AWS Region .

        By default, this only changes the retention period of copied automated snapshots.

        If you decrease the retention period for automated snapshots that are copied to a destination AWS Region , Amazon Redshift deletes any existing automated snapshots that were copied to the destination AWS Region and that fall outside of the new retention period.

        Constraints: Must be at least 1 and no more than 35 for automated snapshots.

        If you specify the ``manual`` option, only newly copied manual snapshots will have the new retention period.

        If you specify the value of -1 newly copied manual snapshots are retained indefinitely.

        Constraints: The number of days must be either -1 or an integer between 1 and 3,653 for manual snapshots.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-snapshotcopyretentionperiod
        '''
        result = self._values.get("snapshot_copy_retention_period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def snapshot_identifier(self) -> typing.Optional[builtins.str]:
        '''The name of the snapshot from which to create the new cluster. This parameter isn't case sensitive.

        Example: ``my-snapshot-id``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-snapshotidentifier
        '''
        result = self._values.get("snapshot_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of tag instances.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def vpc_security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of Virtual Private Cloud (VPC) security groups to be associated with the cluster.

        Default: The default VPC security group is associated with the cluster.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html#cfn-redshift-cluster-vpcsecuritygroupids
        '''
        result = self._values.get("vpc_security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnClusterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnClusterSecurityGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_redshift.CfnClusterSecurityGroup",
):
    '''A CloudFormation ``AWS::Redshift::ClusterSecurityGroup``.

    Specifies a new Amazon Redshift security group. You use security groups to control access to non-VPC clusters.

    For information about managing security groups, go to `Amazon Redshift Cluster Security Groups <https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-security-groups.html>`_ in the *Amazon Redshift Cluster Management Guide* .

    :cloudformationResource: AWS::Redshift::ClusterSecurityGroup
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clustersecuritygroup.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_redshift as redshift
        
        cfn_cluster_security_group = redshift.CfnClusterSecurityGroup(self, "MyCfnClusterSecurityGroup",
            description="description",
        
            # the properties below are optional
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        description: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::Redshift::ClusterSecurityGroup``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param description: A description for the security group.
        :param tags: Specifies an arbitrary set of tags (key–value pairs) to associate with this security group. Use tags to manage your resources.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnClusterSecurityGroup.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnClusterSecurityGroupProps(description=description, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnClusterSecurityGroup.inspect)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnClusterSecurityGroup._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''Specifies an arbitrary set of tags (key–value pairs) to associate with this security group.

        Use tags to manage your resources.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clustersecuritygroup.html#cfn-redshift-clustersecuritygroup-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        '''A description for the security group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clustersecuritygroup.html#cfn-redshift-clustersecuritygroup-description
        '''
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnClusterSecurityGroup, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)


@jsii.implements(_IInspectable_c2943556)
class CfnClusterSecurityGroupIngress(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_redshift.CfnClusterSecurityGroupIngress",
):
    '''A CloudFormation ``AWS::Redshift::ClusterSecurityGroupIngress``.

    Adds an inbound (ingress) rule to an Amazon Redshift security group. Depending on whether the application accessing your cluster is running on the Internet or an Amazon EC2 instance, you can authorize inbound access to either a Classless Interdomain Routing (CIDR)/Internet Protocol (IP) range or to an Amazon EC2 security group. You can add as many as 20 ingress rules to an Amazon Redshift security group.

    If you authorize access to an Amazon EC2 security group, specify *EC2SecurityGroupName* and *EC2SecurityGroupOwnerId* . The Amazon EC2 security group and Amazon Redshift cluster must be in the same AWS Region .

    If you authorize access to a CIDR/IP address range, specify *CIDRIP* . For an overview of CIDR blocks, see the Wikipedia article on `Classless Inter-Domain Routing <https://docs.aws.amazon.com/http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing>`_ .

    You must also associate the security group with a cluster so that clients running on these IP addresses or the EC2 instance are authorized to connect to the cluster. For information about managing security groups, go to `Working with Security Groups <https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-security-groups.html>`_ in the *Amazon Redshift Cluster Management Guide* .

    :cloudformationResource: AWS::Redshift::ClusterSecurityGroupIngress
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clustersecuritygroupingress.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_redshift as redshift
        
        cfn_cluster_security_group_ingress = redshift.CfnClusterSecurityGroupIngress(self, "MyCfnClusterSecurityGroupIngress",
            cluster_security_group_name="clusterSecurityGroupName",
        
            # the properties below are optional
            cidrip="cidrip",
            ec2_security_group_name="ec2SecurityGroupName",
            ec2_security_group_owner_id="ec2SecurityGroupOwnerId"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        cluster_security_group_name: builtins.str,
        cidrip: typing.Optional[builtins.str] = None,
        ec2_security_group_name: typing.Optional[builtins.str] = None,
        ec2_security_group_owner_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::Redshift::ClusterSecurityGroupIngress``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param cluster_security_group_name: The name of the security group to which the ingress rule is added.
        :param cidrip: The IP range to be added the Amazon Redshift security group.
        :param ec2_security_group_name: The EC2 security group to be added the Amazon Redshift security group.
        :param ec2_security_group_owner_id: The AWS account number of the owner of the security group specified by the *EC2SecurityGroupName* parameter. The AWS Access Key ID is not an acceptable value. Example: ``111122223333`` Conditional. If you specify the ``EC2SecurityGroupName`` property, you must specify this property.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnClusterSecurityGroupIngress.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnClusterSecurityGroupIngressProps(
            cluster_security_group_name=cluster_security_group_name,
            cidrip=cidrip,
            ec2_security_group_name=ec2_security_group_name,
            ec2_security_group_owner_id=ec2_security_group_owner_id,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnClusterSecurityGroupIngress.inspect)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnClusterSecurityGroupIngress._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="clusterSecurityGroupName")
    def cluster_security_group_name(self) -> builtins.str:
        '''The name of the security group to which the ingress rule is added.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clustersecuritygroupingress.html#cfn-redshift-clustersecuritygroupingress-clustersecuritygroupname
        '''
        return typing.cast(builtins.str, jsii.get(self, "clusterSecurityGroupName"))

    @cluster_security_group_name.setter
    def cluster_security_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnClusterSecurityGroupIngress, "cluster_security_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterSecurityGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="cidrip")
    def cidrip(self) -> typing.Optional[builtins.str]:
        '''The IP range to be added the Amazon Redshift security group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clustersecuritygroupingress.html#cfn-redshift-clustersecuritygroupingress-cidrip
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cidrip"))

    @cidrip.setter
    def cidrip(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnClusterSecurityGroupIngress, "cidrip").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cidrip", value)

    @builtins.property
    @jsii.member(jsii_name="ec2SecurityGroupName")
    def ec2_security_group_name(self) -> typing.Optional[builtins.str]:
        '''The EC2 security group to be added the Amazon Redshift security group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clustersecuritygroupingress.html#cfn-redshift-clustersecuritygroupingress-ec2securitygroupname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ec2SecurityGroupName"))

    @ec2_security_group_name.setter
    def ec2_security_group_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnClusterSecurityGroupIngress, "ec2_security_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ec2SecurityGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="ec2SecurityGroupOwnerId")
    def ec2_security_group_owner_id(self) -> typing.Optional[builtins.str]:
        '''The AWS account number of the owner of the security group specified by the *EC2SecurityGroupName* parameter.

        The AWS Access Key ID is not an acceptable value.

        Example: ``111122223333``

        Conditional. If you specify the ``EC2SecurityGroupName`` property, you must specify this property.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clustersecuritygroupingress.html#cfn-redshift-clustersecuritygroupingress-ec2securitygroupownerid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ec2SecurityGroupOwnerId"))

    @ec2_security_group_owner_id.setter
    def ec2_security_group_owner_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnClusterSecurityGroupIngress, "ec2_security_group_owner_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ec2SecurityGroupOwnerId", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_redshift.CfnClusterSecurityGroupIngressProps",
    jsii_struct_bases=[],
    name_mapping={
        "cluster_security_group_name": "clusterSecurityGroupName",
        "cidrip": "cidrip",
        "ec2_security_group_name": "ec2SecurityGroupName",
        "ec2_security_group_owner_id": "ec2SecurityGroupOwnerId",
    },
)
class CfnClusterSecurityGroupIngressProps:
    def __init__(
        self,
        *,
        cluster_security_group_name: builtins.str,
        cidrip: typing.Optional[builtins.str] = None,
        ec2_security_group_name: typing.Optional[builtins.str] = None,
        ec2_security_group_owner_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnClusterSecurityGroupIngress``.

        :param cluster_security_group_name: The name of the security group to which the ingress rule is added.
        :param cidrip: The IP range to be added the Amazon Redshift security group.
        :param ec2_security_group_name: The EC2 security group to be added the Amazon Redshift security group.
        :param ec2_security_group_owner_id: The AWS account number of the owner of the security group specified by the *EC2SecurityGroupName* parameter. The AWS Access Key ID is not an acceptable value. Example: ``111122223333`` Conditional. If you specify the ``EC2SecurityGroupName`` property, you must specify this property.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clustersecuritygroupingress.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_redshift as redshift
            
            cfn_cluster_security_group_ingress_props = redshift.CfnClusterSecurityGroupIngressProps(
                cluster_security_group_name="clusterSecurityGroupName",
            
                # the properties below are optional
                cidrip="cidrip",
                ec2_security_group_name="ec2SecurityGroupName",
                ec2_security_group_owner_id="ec2SecurityGroupOwnerId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnClusterSecurityGroupIngressProps.__init__)
            check_type(argname="argument cluster_security_group_name", value=cluster_security_group_name, expected_type=type_hints["cluster_security_group_name"])
            check_type(argname="argument cidrip", value=cidrip, expected_type=type_hints["cidrip"])
            check_type(argname="argument ec2_security_group_name", value=ec2_security_group_name, expected_type=type_hints["ec2_security_group_name"])
            check_type(argname="argument ec2_security_group_owner_id", value=ec2_security_group_owner_id, expected_type=type_hints["ec2_security_group_owner_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "cluster_security_group_name": cluster_security_group_name,
        }
        if cidrip is not None:
            self._values["cidrip"] = cidrip
        if ec2_security_group_name is not None:
            self._values["ec2_security_group_name"] = ec2_security_group_name
        if ec2_security_group_owner_id is not None:
            self._values["ec2_security_group_owner_id"] = ec2_security_group_owner_id

    @builtins.property
    def cluster_security_group_name(self) -> builtins.str:
        '''The name of the security group to which the ingress rule is added.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clustersecuritygroupingress.html#cfn-redshift-clustersecuritygroupingress-clustersecuritygroupname
        '''
        result = self._values.get("cluster_security_group_name")
        assert result is not None, "Required property 'cluster_security_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cidrip(self) -> typing.Optional[builtins.str]:
        '''The IP range to be added the Amazon Redshift security group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clustersecuritygroupingress.html#cfn-redshift-clustersecuritygroupingress-cidrip
        '''
        result = self._values.get("cidrip")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ec2_security_group_name(self) -> typing.Optional[builtins.str]:
        '''The EC2 security group to be added the Amazon Redshift security group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clustersecuritygroupingress.html#cfn-redshift-clustersecuritygroupingress-ec2securitygroupname
        '''
        result = self._values.get("ec2_security_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ec2_security_group_owner_id(self) -> typing.Optional[builtins.str]:
        '''The AWS account number of the owner of the security group specified by the *EC2SecurityGroupName* parameter.

        The AWS Access Key ID is not an acceptable value.

        Example: ``111122223333``

        Conditional. If you specify the ``EC2SecurityGroupName`` property, you must specify this property.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clustersecuritygroupingress.html#cfn-redshift-clustersecuritygroupingress-ec2securitygroupownerid
        '''
        result = self._values.get("ec2_security_group_owner_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnClusterSecurityGroupIngressProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_redshift.CfnClusterSecurityGroupProps",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "tags": "tags"},
)
class CfnClusterSecurityGroupProps:
    def __init__(
        self,
        *,
        description: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnClusterSecurityGroup``.

        :param description: A description for the security group.
        :param tags: Specifies an arbitrary set of tags (key–value pairs) to associate with this security group. Use tags to manage your resources.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clustersecuritygroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_redshift as redshift
            
            cfn_cluster_security_group_props = redshift.CfnClusterSecurityGroupProps(
                description="description",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnClusterSecurityGroupProps.__init__)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def description(self) -> builtins.str:
        '''A description for the security group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clustersecuritygroup.html#cfn-redshift-clustersecuritygroup-description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Specifies an arbitrary set of tags (key–value pairs) to associate with this security group.

        Use tags to manage your resources.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clustersecuritygroup.html#cfn-redshift-clustersecuritygroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnClusterSecurityGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnClusterSubnetGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_redshift.CfnClusterSubnetGroup",
):
    '''A CloudFormation ``AWS::Redshift::ClusterSubnetGroup``.

    Specifies an Amazon Redshift subnet group. You must provide a list of one or more subnets in your existing Amazon Virtual Private Cloud ( Amazon VPC ) when creating Amazon Redshift subnet group.

    For information about subnet groups, go to `Amazon Redshift Cluster Subnet Groups <https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-cluster-subnet-groups.html>`_ in the *Amazon Redshift Cluster Management Guide* .

    :cloudformationResource: AWS::Redshift::ClusterSubnetGroup
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clustersubnetgroup.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_redshift as redshift
        
        cfn_cluster_subnet_group = redshift.CfnClusterSubnetGroup(self, "MyCfnClusterSubnetGroup",
            description="description",
            subnet_ids=["subnetIds"],
        
            # the properties below are optional
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        description: builtins.str,
        subnet_ids: typing.Sequence[builtins.str],
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::Redshift::ClusterSubnetGroup``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param description: A description for the subnet group.
        :param subnet_ids: An array of VPC subnet IDs. A maximum of 20 subnets can be modified in a single request.
        :param tags: Specifies an arbitrary set of tags (key–value pairs) to associate with this subnet group. Use tags to manage your resources.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnClusterSubnetGroup.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnClusterSubnetGroupProps(
            description=description, subnet_ids=subnet_ids, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnClusterSubnetGroup.inspect)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnClusterSubnetGroup._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''Specifies an arbitrary set of tags (key–value pairs) to associate with this subnet group.

        Use tags to manage your resources.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clustersubnetgroup.html#cfn-redshift-clustersubnetgroup-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        '''A description for the subnet group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clustersubnetgroup.html#cfn-redshift-clustersubnetgroup-description
        '''
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnClusterSubnetGroup, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.List[builtins.str]:
        '''An array of VPC subnet IDs.

        A maximum of 20 subnets can be modified in a single request.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clustersubnetgroup.html#cfn-redshift-clustersubnetgroup-subnetids
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnClusterSubnetGroup, "subnet_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetIds", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_redshift.CfnClusterSubnetGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "subnet_ids": "subnetIds",
        "tags": "tags",
    },
)
class CfnClusterSubnetGroupProps:
    def __init__(
        self,
        *,
        description: builtins.str,
        subnet_ids: typing.Sequence[builtins.str],
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnClusterSubnetGroup``.

        :param description: A description for the subnet group.
        :param subnet_ids: An array of VPC subnet IDs. A maximum of 20 subnets can be modified in a single request.
        :param tags: Specifies an arbitrary set of tags (key–value pairs) to associate with this subnet group. Use tags to manage your resources.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clustersubnetgroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_redshift as redshift
            
            cfn_cluster_subnet_group_props = redshift.CfnClusterSubnetGroupProps(
                description="description",
                subnet_ids=["subnetIds"],
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnClusterSubnetGroupProps.__init__)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "subnet_ids": subnet_ids,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def description(self) -> builtins.str:
        '''A description for the subnet group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clustersubnetgroup.html#cfn-redshift-clustersubnetgroup-description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subnet_ids(self) -> typing.List[builtins.str]:
        '''An array of VPC subnet IDs.

        A maximum of 20 subnets can be modified in a single request.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clustersubnetgroup.html#cfn-redshift-clustersubnetgroup-subnetids
        '''
        result = self._values.get("subnet_ids")
        assert result is not None, "Required property 'subnet_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Specifies an arbitrary set of tags (key–value pairs) to associate with this subnet group.

        Use tags to manage your resources.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clustersubnetgroup.html#cfn-redshift-clustersubnetgroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnClusterSubnetGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnEndpointAccess(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_redshift.CfnEndpointAccess",
):
    '''A CloudFormation ``AWS::Redshift::EndpointAccess``.

    Creates a Redshift-managed VPC endpoint.

    :cloudformationResource: AWS::Redshift::EndpointAccess
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-endpointaccess.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_redshift as redshift
        
        cfn_endpoint_access = redshift.CfnEndpointAccess(self, "MyCfnEndpointAccess",
            cluster_identifier="clusterIdentifier",
            endpoint_name="endpointName",
            subnet_group_name="subnetGroupName",
            vpc_security_group_ids=["vpcSecurityGroupIds"],
        
            # the properties below are optional
            resource_owner="resourceOwner"
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        cluster_identifier: builtins.str,
        endpoint_name: builtins.str,
        subnet_group_name: builtins.str,
        vpc_security_group_ids: typing.Sequence[builtins.str],
        resource_owner: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::Redshift::EndpointAccess``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param cluster_identifier: The cluster identifier of the cluster associated with the endpoint.
        :param endpoint_name: The name of the endpoint.
        :param subnet_group_name: The subnet group name where Amazon Redshift chooses to deploy the endpoint.
        :param vpc_security_group_ids: The security group that defines the ports, protocols, and sources for inbound traffic that you are authorizing into your endpoint.
        :param resource_owner: The AWS account ID of the owner of the cluster.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnEndpointAccess.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEndpointAccessProps(
            cluster_identifier=cluster_identifier,
            endpoint_name=endpoint_name,
            subnet_group_name=subnet_group_name,
            vpc_security_group_ids=vpc_security_group_ids,
            resource_owner=resource_owner,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnEndpointAccess.inspect)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnEndpointAccess._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAddress")
    def attr_address(self) -> builtins.str:
        '''The DNS address of the endpoint.

        :cloudformationAttribute: Address
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAddress"))

    @builtins.property
    @jsii.member(jsii_name="attrEndpointCreateTime")
    def attr_endpoint_create_time(self) -> builtins.str:
        '''The time (UTC) that the endpoint was created.

        :cloudformationAttribute: EndpointCreateTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEndpointCreateTime"))

    @builtins.property
    @jsii.member(jsii_name="attrEndpointStatus")
    def attr_endpoint_status(self) -> builtins.str:
        '''The status of the endpoint.

        :cloudformationAttribute: EndpointStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEndpointStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrPort")
    def attr_port(self) -> jsii.Number:
        '''The port number on which the cluster accepts incoming connections.

        :cloudformationAttribute: Port
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrPort"))

    @builtins.property
    @jsii.member(jsii_name="attrVpcSecurityGroups")
    def attr_vpc_security_groups(self) -> _IResolvable_da3f097b:
        '''
        :cloudformationAttribute: VpcSecurityGroups
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrVpcSecurityGroups"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="clusterIdentifier")
    def cluster_identifier(self) -> builtins.str:
        '''The cluster identifier of the cluster associated with the endpoint.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-endpointaccess.html#cfn-redshift-endpointaccess-clusteridentifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "clusterIdentifier"))

    @cluster_identifier.setter
    def cluster_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnEndpointAccess, "cluster_identifier").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="endpointName")
    def endpoint_name(self) -> builtins.str:
        '''The name of the endpoint.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-endpointaccess.html#cfn-redshift-endpointaccess-endpointname
        '''
        return typing.cast(builtins.str, jsii.get(self, "endpointName"))

    @endpoint_name.setter
    def endpoint_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnEndpointAccess, "endpoint_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpointName", value)

    @builtins.property
    @jsii.member(jsii_name="subnetGroupName")
    def subnet_group_name(self) -> builtins.str:
        '''The subnet group name where Amazon Redshift chooses to deploy the endpoint.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-endpointaccess.html#cfn-redshift-endpointaccess-subnetgroupname
        '''
        return typing.cast(builtins.str, jsii.get(self, "subnetGroupName"))

    @subnet_group_name.setter
    def subnet_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnEndpointAccess, "subnet_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> typing.List[builtins.str]:
        '''The security group that defines the ports, protocols, and sources for inbound traffic that you are authorizing into your endpoint.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-endpointaccess.html#cfn-redshift-endpointaccess-vpcsecuritygroupids
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "vpcSecurityGroupIds"))

    @vpc_security_group_ids.setter
    def vpc_security_group_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnEndpointAccess, "vpc_security_group_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcSecurityGroupIds", value)

    @builtins.property
    @jsii.member(jsii_name="resourceOwner")
    def resource_owner(self) -> typing.Optional[builtins.str]:
        '''The AWS account ID of the owner of the cluster.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-endpointaccess.html#cfn-redshift-endpointaccess-resourceowner
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceOwner"))

    @resource_owner.setter
    def resource_owner(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnEndpointAccess, "resource_owner").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceOwner", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_redshift.CfnEndpointAccess.VpcSecurityGroupProperty",
        jsii_struct_bases=[],
        name_mapping={
            "status": "status",
            "vpc_security_group_id": "vpcSecurityGroupId",
        },
    )
    class VpcSecurityGroupProperty:
        def __init__(
            self,
            *,
            status: typing.Optional[builtins.str] = None,
            vpc_security_group_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The security groups associated with the endpoint.

            :param status: The status of the endpoint.
            :param vpc_security_group_id: The identifier of the VPC security group.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-endpointaccess-vpcsecuritygroup.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_redshift as redshift
                
                vpc_security_group_property = redshift.CfnEndpointAccess.VpcSecurityGroupProperty(
                    status="status",
                    vpc_security_group_id="vpcSecurityGroupId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(CfnEndpointAccess.VpcSecurityGroupProperty.__init__)
                check_type(argname="argument status", value=status, expected_type=type_hints["status"])
                check_type(argname="argument vpc_security_group_id", value=vpc_security_group_id, expected_type=type_hints["vpc_security_group_id"])
            self._values: typing.Dict[str, typing.Any] = {}
            if status is not None:
                self._values["status"] = status
            if vpc_security_group_id is not None:
                self._values["vpc_security_group_id"] = vpc_security_group_id

        @builtins.property
        def status(self) -> typing.Optional[builtins.str]:
            '''The status of the endpoint.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-endpointaccess-vpcsecuritygroup.html#cfn-redshift-endpointaccess-vpcsecuritygroup-status
            '''
            result = self._values.get("status")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def vpc_security_group_id(self) -> typing.Optional[builtins.str]:
            '''The identifier of the VPC security group.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshift-endpointaccess-vpcsecuritygroup.html#cfn-redshift-endpointaccess-vpcsecuritygroup-vpcsecuritygroupid
            '''
            result = self._values.get("vpc_security_group_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcSecurityGroupProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_redshift.CfnEndpointAccessProps",
    jsii_struct_bases=[],
    name_mapping={
        "cluster_identifier": "clusterIdentifier",
        "endpoint_name": "endpointName",
        "subnet_group_name": "subnetGroupName",
        "vpc_security_group_ids": "vpcSecurityGroupIds",
        "resource_owner": "resourceOwner",
    },
)
class CfnEndpointAccessProps:
    def __init__(
        self,
        *,
        cluster_identifier: builtins.str,
        endpoint_name: builtins.str,
        subnet_group_name: builtins.str,
        vpc_security_group_ids: typing.Sequence[builtins.str],
        resource_owner: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnEndpointAccess``.

        :param cluster_identifier: The cluster identifier of the cluster associated with the endpoint.
        :param endpoint_name: The name of the endpoint.
        :param subnet_group_name: The subnet group name where Amazon Redshift chooses to deploy the endpoint.
        :param vpc_security_group_ids: The security group that defines the ports, protocols, and sources for inbound traffic that you are authorizing into your endpoint.
        :param resource_owner: The AWS account ID of the owner of the cluster.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-endpointaccess.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_redshift as redshift
            
            cfn_endpoint_access_props = redshift.CfnEndpointAccessProps(
                cluster_identifier="clusterIdentifier",
                endpoint_name="endpointName",
                subnet_group_name="subnetGroupName",
                vpc_security_group_ids=["vpcSecurityGroupIds"],
            
                # the properties below are optional
                resource_owner="resourceOwner"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnEndpointAccessProps.__init__)
            check_type(argname="argument cluster_identifier", value=cluster_identifier, expected_type=type_hints["cluster_identifier"])
            check_type(argname="argument endpoint_name", value=endpoint_name, expected_type=type_hints["endpoint_name"])
            check_type(argname="argument subnet_group_name", value=subnet_group_name, expected_type=type_hints["subnet_group_name"])
            check_type(argname="argument vpc_security_group_ids", value=vpc_security_group_ids, expected_type=type_hints["vpc_security_group_ids"])
            check_type(argname="argument resource_owner", value=resource_owner, expected_type=type_hints["resource_owner"])
        self._values: typing.Dict[str, typing.Any] = {
            "cluster_identifier": cluster_identifier,
            "endpoint_name": endpoint_name,
            "subnet_group_name": subnet_group_name,
            "vpc_security_group_ids": vpc_security_group_ids,
        }
        if resource_owner is not None:
            self._values["resource_owner"] = resource_owner

    @builtins.property
    def cluster_identifier(self) -> builtins.str:
        '''The cluster identifier of the cluster associated with the endpoint.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-endpointaccess.html#cfn-redshift-endpointaccess-clusteridentifier
        '''
        result = self._values.get("cluster_identifier")
        assert result is not None, "Required property 'cluster_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def endpoint_name(self) -> builtins.str:
        '''The name of the endpoint.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-endpointaccess.html#cfn-redshift-endpointaccess-endpointname
        '''
        result = self._values.get("endpoint_name")
        assert result is not None, "Required property 'endpoint_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subnet_group_name(self) -> builtins.str:
        '''The subnet group name where Amazon Redshift chooses to deploy the endpoint.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-endpointaccess.html#cfn-redshift-endpointaccess-subnetgroupname
        '''
        result = self._values.get("subnet_group_name")
        assert result is not None, "Required property 'subnet_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vpc_security_group_ids(self) -> typing.List[builtins.str]:
        '''The security group that defines the ports, protocols, and sources for inbound traffic that you are authorizing into your endpoint.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-endpointaccess.html#cfn-redshift-endpointaccess-vpcsecuritygroupids
        '''
        result = self._values.get("vpc_security_group_ids")
        assert result is not None, "Required property 'vpc_security_group_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def resource_owner(self) -> typing.Optional[builtins.str]:
        '''The AWS account ID of the owner of the cluster.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-endpointaccess.html#cfn-redshift-endpointaccess-resourceowner
        '''
        result = self._values.get("resource_owner")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEndpointAccessProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnEndpointAuthorization(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_redshift.CfnEndpointAuthorization",
):
    '''A CloudFormation ``AWS::Redshift::EndpointAuthorization``.

    Describes an endpoint authorization for authorizing Redshift-managed VPC endpoint access to a cluster across AWS accounts .

    :cloudformationResource: AWS::Redshift::EndpointAuthorization
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-endpointauthorization.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_redshift as redshift
        
        cfn_endpoint_authorization = redshift.CfnEndpointAuthorization(self, "MyCfnEndpointAuthorization",
            account="account",
            cluster_identifier="clusterIdentifier",
        
            # the properties below are optional
            force=False,
            vpc_ids=["vpcIds"]
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        account: builtins.str,
        cluster_identifier: builtins.str,
        force: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        vpc_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::Redshift::EndpointAuthorization``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param account: The A AWS account ID of either the cluster owner (grantor) or grantee. If ``Grantee`` parameter is true, then the ``Account`` value is of the grantor.
        :param cluster_identifier: The cluster identifier.
        :param force: Indicates whether to force the revoke action. If true, the Redshift-managed VPC endpoints associated with the endpoint authorization are also deleted.
        :param vpc_ids: The virtual private cloud (VPC) identifiers to grant access to.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnEndpointAuthorization.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEndpointAuthorizationProps(
            account=account,
            cluster_identifier=cluster_identifier,
            force=force,
            vpc_ids=vpc_ids,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnEndpointAuthorization.inspect)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnEndpointAuthorization._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAllowedAllVpCs")
    def attr_allowed_all_vp_cs(self) -> _IResolvable_da3f097b:
        '''Indicates whether all VPCs in the grantee account are allowed access to the cluster.

        :cloudformationAttribute: AllowedAllVPCs
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrAllowedAllVpCs"))

    @builtins.property
    @jsii.member(jsii_name="attrAllowedVpCs")
    def attr_allowed_vp_cs(self) -> typing.List[builtins.str]:
        '''The VPCs allowed access to the cluster.

        :cloudformationAttribute: AllowedVPCs
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrAllowedVpCs"))

    @builtins.property
    @jsii.member(jsii_name="attrAuthorizeTime")
    def attr_authorize_time(self) -> builtins.str:
        '''The time (UTC) when the authorization was created.

        :cloudformationAttribute: AuthorizeTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAuthorizeTime"))

    @builtins.property
    @jsii.member(jsii_name="attrClusterStatus")
    def attr_cluster_status(self) -> builtins.str:
        '''The status of the cluster.

        :cloudformationAttribute: ClusterStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrClusterStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrEndpointCount")
    def attr_endpoint_count(self) -> jsii.Number:
        '''The number of Redshift-managed VPC endpoints created for the authorization.

        :cloudformationAttribute: EndpointCount
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrEndpointCount"))

    @builtins.property
    @jsii.member(jsii_name="attrGrantee")
    def attr_grantee(self) -> builtins.str:
        '''The AWS account ID of the grantee of the cluster.

        :cloudformationAttribute: Grantee
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrGrantee"))

    @builtins.property
    @jsii.member(jsii_name="attrGrantor")
    def attr_grantor(self) -> builtins.str:
        '''The AWS account ID of the cluster owner.

        :cloudformationAttribute: Grantor
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrGrantor"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status of the authorization action.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="account")
    def account(self) -> builtins.str:
        '''The A AWS account ID of either the cluster owner (grantor) or grantee.

        If ``Grantee`` parameter is true, then the ``Account`` value is of the grantor.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-endpointauthorization.html#cfn-redshift-endpointauthorization-account
        '''
        return typing.cast(builtins.str, jsii.get(self, "account"))

    @account.setter
    def account(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnEndpointAuthorization, "account").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "account", value)

    @builtins.property
    @jsii.member(jsii_name="clusterIdentifier")
    def cluster_identifier(self) -> builtins.str:
        '''The cluster identifier.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-endpointauthorization.html#cfn-redshift-endpointauthorization-clusteridentifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "clusterIdentifier"))

    @cluster_identifier.setter
    def cluster_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnEndpointAuthorization, "cluster_identifier").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="force")
    def force(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates whether to force the revoke action.

        If true, the Redshift-managed VPC endpoints associated with the endpoint authorization are also deleted.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-endpointauthorization.html#cfn-redshift-endpointauthorization-force
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "force"))

    @force.setter
    def force(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnEndpointAuthorization, "force").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "force", value)

    @builtins.property
    @jsii.member(jsii_name="vpcIds")
    def vpc_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The virtual private cloud (VPC) identifiers to grant access to.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-endpointauthorization.html#cfn-redshift-endpointauthorization-vpcids
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "vpcIds"))

    @vpc_ids.setter
    def vpc_ids(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnEndpointAuthorization, "vpc_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcIds", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_redshift.CfnEndpointAuthorizationProps",
    jsii_struct_bases=[],
    name_mapping={
        "account": "account",
        "cluster_identifier": "clusterIdentifier",
        "force": "force",
        "vpc_ids": "vpcIds",
    },
)
class CfnEndpointAuthorizationProps:
    def __init__(
        self,
        *,
        account: builtins.str,
        cluster_identifier: builtins.str,
        force: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        vpc_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnEndpointAuthorization``.

        :param account: The A AWS account ID of either the cluster owner (grantor) or grantee. If ``Grantee`` parameter is true, then the ``Account`` value is of the grantor.
        :param cluster_identifier: The cluster identifier.
        :param force: Indicates whether to force the revoke action. If true, the Redshift-managed VPC endpoints associated with the endpoint authorization are also deleted.
        :param vpc_ids: The virtual private cloud (VPC) identifiers to grant access to.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-endpointauthorization.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_redshift as redshift
            
            cfn_endpoint_authorization_props = redshift.CfnEndpointAuthorizationProps(
                account="account",
                cluster_identifier="clusterIdentifier",
            
                # the properties below are optional
                force=False,
                vpc_ids=["vpcIds"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnEndpointAuthorizationProps.__init__)
            check_type(argname="argument account", value=account, expected_type=type_hints["account"])
            check_type(argname="argument cluster_identifier", value=cluster_identifier, expected_type=type_hints["cluster_identifier"])
            check_type(argname="argument force", value=force, expected_type=type_hints["force"])
            check_type(argname="argument vpc_ids", value=vpc_ids, expected_type=type_hints["vpc_ids"])
        self._values: typing.Dict[str, typing.Any] = {
            "account": account,
            "cluster_identifier": cluster_identifier,
        }
        if force is not None:
            self._values["force"] = force
        if vpc_ids is not None:
            self._values["vpc_ids"] = vpc_ids

    @builtins.property
    def account(self) -> builtins.str:
        '''The A AWS account ID of either the cluster owner (grantor) or grantee.

        If ``Grantee`` parameter is true, then the ``Account`` value is of the grantor.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-endpointauthorization.html#cfn-redshift-endpointauthorization-account
        '''
        result = self._values.get("account")
        assert result is not None, "Required property 'account' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cluster_identifier(self) -> builtins.str:
        '''The cluster identifier.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-endpointauthorization.html#cfn-redshift-endpointauthorization-clusteridentifier
        '''
        result = self._values.get("cluster_identifier")
        assert result is not None, "Required property 'cluster_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def force(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates whether to force the revoke action.

        If true, the Redshift-managed VPC endpoints associated with the endpoint authorization are also deleted.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-endpointauthorization.html#cfn-redshift-endpointauthorization-force
        '''
        result = self._values.get("force")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def vpc_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The virtual private cloud (VPC) identifiers to grant access to.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-endpointauthorization.html#cfn-redshift-endpointauthorization-vpcids
        '''
        result = self._values.get("vpc_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEndpointAuthorizationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnEventSubscription(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_redshift.CfnEventSubscription",
):
    '''A CloudFormation ``AWS::Redshift::EventSubscription``.

    :cloudformationResource: AWS::Redshift::EventSubscription
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-eventsubscription.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_redshift as redshift
        
        cfn_event_subscription = redshift.CfnEventSubscription(self, "MyCfnEventSubscription",
            subscription_name="subscriptionName",
        
            # the properties below are optional
            enabled=False,
            event_categories=["eventCategories"],
            severity="severity",
            sns_topic_arn="snsTopicArn",
            source_ids=["sourceIds"],
            source_type="sourceType",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        subscription_name: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        event_categories: typing.Optional[typing.Sequence[builtins.str]] = None,
        severity: typing.Optional[builtins.str] = None,
        sns_topic_arn: typing.Optional[builtins.str] = None,
        source_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        source_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::Redshift::EventSubscription``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param subscription_name: The name of the event subscription to be created. Constraints: - Cannot be null, empty, or blank. - Must contain from 1 to 255 alphanumeric characters or hyphens. - First character must be a letter. - Cannot end with a hyphen or contain two consecutive hyphens.
        :param enabled: A boolean value; set to ``true`` to activate the subscription, and set to ``false`` to create the subscription but not activate it.
        :param event_categories: Specifies the Amazon Redshift event categories to be published by the event notification subscription. Values: configuration, management, monitoring, security, pending
        :param severity: Specifies the Amazon Redshift event severity to be published by the event notification subscription. Values: ERROR, INFO
        :param sns_topic_arn: The Amazon Resource Name (ARN) of the Amazon SNS topic used to transmit the event notifications. The ARN is created by Amazon SNS when you create a topic and subscribe to it.
        :param source_ids: A list of one or more identifiers of Amazon Redshift source objects. All of the objects must be of the same type as was specified in the source type parameter. The event subscription will return only events generated by the specified objects. If not specified, then events are returned for all objects within the source type specified. Example: my-cluster-1, my-cluster-2 Example: my-snapshot-20131010
        :param source_type: The type of source that will be generating the events. For example, if you want to be notified of events generated by a cluster, you would set this parameter to cluster. If this value is not specified, events are returned for all Amazon Redshift objects in your AWS account . You must specify a source type in order to specify source IDs. Valid values: cluster, cluster-parameter-group, cluster-security-group, cluster-snapshot, and scheduled-action.
        :param tags: A list of tag instances.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnEventSubscription.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEventSubscriptionProps(
            subscription_name=subscription_name,
            enabled=enabled,
            event_categories=event_categories,
            severity=severity,
            sns_topic_arn=sns_topic_arn,
            source_ids=source_ids,
            source_type=source_type,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnEventSubscription.inspect)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnEventSubscription._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCustomerAwsId")
    def attr_customer_aws_id(self) -> builtins.str:
        '''The AWS account associated with the Amazon Redshift event notification subscription.

        :cloudformationAttribute: CustomerAwsId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCustomerAwsId"))

    @builtins.property
    @jsii.member(jsii_name="attrCustSubscriptionId")
    def attr_cust_subscription_id(self) -> builtins.str:
        '''The name of the Amazon Redshift event notification subscription.

        :cloudformationAttribute: CustSubscriptionId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCustSubscriptionId"))

    @builtins.property
    @jsii.member(jsii_name="attrEventCategoriesList")
    def attr_event_categories_list(self) -> typing.List[builtins.str]:
        '''The list of Amazon Redshift event categories specified in the event notification subscription.

        Values: Configuration, Management, Monitoring, Security, Pending

        :cloudformationAttribute: EventCategoriesList
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrEventCategoriesList"))

    @builtins.property
    @jsii.member(jsii_name="attrSourceIdsList")
    def attr_source_ids_list(self) -> typing.List[builtins.str]:
        '''A list of the sources that publish events to the Amazon Redshift event notification subscription.

        :cloudformationAttribute: SourceIdsList
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrSourceIdsList"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status of the Amazon Redshift event notification subscription.

        Constraints:

        - Can be one of the following: active | no-permission | topic-not-exist
        - The status "no-permission" indicates that Amazon Redshift no longer has permission to post to the Amazon SNS topic. The status "topic-not-exist" indicates that the topic was deleted after the subscription was created.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrSubscriptionCreationTime")
    def attr_subscription_creation_time(self) -> builtins.str:
        '''The date and time the Amazon Redshift event notification subscription was created.

        :cloudformationAttribute: SubscriptionCreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSubscriptionCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''A list of tag instances.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-eventsubscription.html#cfn-redshift-eventsubscription-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="subscriptionName")
    def subscription_name(self) -> builtins.str:
        '''The name of the event subscription to be created.

        Constraints:

        - Cannot be null, empty, or blank.
        - Must contain from 1 to 255 alphanumeric characters or hyphens.
        - First character must be a letter.
        - Cannot end with a hyphen or contain two consecutive hyphens.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-eventsubscription.html#cfn-redshift-eventsubscription-subscriptionname
        '''
        return typing.cast(builtins.str, jsii.get(self, "subscriptionName"))

    @subscription_name.setter
    def subscription_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnEventSubscription, "subscription_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subscriptionName", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A boolean value;

        set to ``true`` to activate the subscription, and set to ``false`` to create the subscription but not activate it.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-eventsubscription.html#cfn-redshift-eventsubscription-enabled
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnEventSubscription, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="eventCategories")
    def event_categories(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies the Amazon Redshift event categories to be published by the event notification subscription.

        Values: configuration, management, monitoring, security, pending

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-eventsubscription.html#cfn-redshift-eventsubscription-eventcategories
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "eventCategories"))

    @event_categories.setter
    def event_categories(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnEventSubscription, "event_categories").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventCategories", value)

    @builtins.property
    @jsii.member(jsii_name="severity")
    def severity(self) -> typing.Optional[builtins.str]:
        '''Specifies the Amazon Redshift event severity to be published by the event notification subscription.

        Values: ERROR, INFO

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-eventsubscription.html#cfn-redshift-eventsubscription-severity
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "severity"))

    @severity.setter
    def severity(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnEventSubscription, "severity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "severity", value)

    @builtins.property
    @jsii.member(jsii_name="snsTopicArn")
    def sns_topic_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the Amazon SNS topic used to transmit the event notifications.

        The ARN is created by Amazon SNS when you create a topic and subscribe to it.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-eventsubscription.html#cfn-redshift-eventsubscription-snstopicarn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snsTopicArn"))

    @sns_topic_arn.setter
    def sns_topic_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnEventSubscription, "sns_topic_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snsTopicArn", value)

    @builtins.property
    @jsii.member(jsii_name="sourceIds")
    def source_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of one or more identifiers of Amazon Redshift source objects.

        All of the objects must be of the same type as was specified in the source type parameter. The event subscription will return only events generated by the specified objects. If not specified, then events are returned for all objects within the source type specified.

        Example: my-cluster-1, my-cluster-2

        Example: my-snapshot-20131010

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-eventsubscription.html#cfn-redshift-eventsubscription-sourceids
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sourceIds"))

    @source_ids.setter
    def source_ids(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnEventSubscription, "source_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceIds", value)

    @builtins.property
    @jsii.member(jsii_name="sourceType")
    def source_type(self) -> typing.Optional[builtins.str]:
        '''The type of source that will be generating the events.

        For example, if you want to be notified of events generated by a cluster, you would set this parameter to cluster. If this value is not specified, events are returned for all Amazon Redshift objects in your AWS account . You must specify a source type in order to specify source IDs.

        Valid values: cluster, cluster-parameter-group, cluster-security-group, cluster-snapshot, and scheduled-action.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-eventsubscription.html#cfn-redshift-eventsubscription-sourcetype
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceType"))

    @source_type.setter
    def source_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnEventSubscription, "source_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceType", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_redshift.CfnEventSubscriptionProps",
    jsii_struct_bases=[],
    name_mapping={
        "subscription_name": "subscriptionName",
        "enabled": "enabled",
        "event_categories": "eventCategories",
        "severity": "severity",
        "sns_topic_arn": "snsTopicArn",
        "source_ids": "sourceIds",
        "source_type": "sourceType",
        "tags": "tags",
    },
)
class CfnEventSubscriptionProps:
    def __init__(
        self,
        *,
        subscription_name: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        event_categories: typing.Optional[typing.Sequence[builtins.str]] = None,
        severity: typing.Optional[builtins.str] = None,
        sns_topic_arn: typing.Optional[builtins.str] = None,
        source_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        source_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnEventSubscription``.

        :param subscription_name: The name of the event subscription to be created. Constraints: - Cannot be null, empty, or blank. - Must contain from 1 to 255 alphanumeric characters or hyphens. - First character must be a letter. - Cannot end with a hyphen or contain two consecutive hyphens.
        :param enabled: A boolean value; set to ``true`` to activate the subscription, and set to ``false`` to create the subscription but not activate it.
        :param event_categories: Specifies the Amazon Redshift event categories to be published by the event notification subscription. Values: configuration, management, monitoring, security, pending
        :param severity: Specifies the Amazon Redshift event severity to be published by the event notification subscription. Values: ERROR, INFO
        :param sns_topic_arn: The Amazon Resource Name (ARN) of the Amazon SNS topic used to transmit the event notifications. The ARN is created by Amazon SNS when you create a topic and subscribe to it.
        :param source_ids: A list of one or more identifiers of Amazon Redshift source objects. All of the objects must be of the same type as was specified in the source type parameter. The event subscription will return only events generated by the specified objects. If not specified, then events are returned for all objects within the source type specified. Example: my-cluster-1, my-cluster-2 Example: my-snapshot-20131010
        :param source_type: The type of source that will be generating the events. For example, if you want to be notified of events generated by a cluster, you would set this parameter to cluster. If this value is not specified, events are returned for all Amazon Redshift objects in your AWS account . You must specify a source type in order to specify source IDs. Valid values: cluster, cluster-parameter-group, cluster-security-group, cluster-snapshot, and scheduled-action.
        :param tags: A list of tag instances.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-eventsubscription.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_redshift as redshift
            
            cfn_event_subscription_props = redshift.CfnEventSubscriptionProps(
                subscription_name="subscriptionName",
            
                # the properties below are optional
                enabled=False,
                event_categories=["eventCategories"],
                severity="severity",
                sns_topic_arn="snsTopicArn",
                source_ids=["sourceIds"],
                source_type="sourceType",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnEventSubscriptionProps.__init__)
            check_type(argname="argument subscription_name", value=subscription_name, expected_type=type_hints["subscription_name"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument event_categories", value=event_categories, expected_type=type_hints["event_categories"])
            check_type(argname="argument severity", value=severity, expected_type=type_hints["severity"])
            check_type(argname="argument sns_topic_arn", value=sns_topic_arn, expected_type=type_hints["sns_topic_arn"])
            check_type(argname="argument source_ids", value=source_ids, expected_type=type_hints["source_ids"])
            check_type(argname="argument source_type", value=source_type, expected_type=type_hints["source_type"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "subscription_name": subscription_name,
        }
        if enabled is not None:
            self._values["enabled"] = enabled
        if event_categories is not None:
            self._values["event_categories"] = event_categories
        if severity is not None:
            self._values["severity"] = severity
        if sns_topic_arn is not None:
            self._values["sns_topic_arn"] = sns_topic_arn
        if source_ids is not None:
            self._values["source_ids"] = source_ids
        if source_type is not None:
            self._values["source_type"] = source_type
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def subscription_name(self) -> builtins.str:
        '''The name of the event subscription to be created.

        Constraints:

        - Cannot be null, empty, or blank.
        - Must contain from 1 to 255 alphanumeric characters or hyphens.
        - First character must be a letter.
        - Cannot end with a hyphen or contain two consecutive hyphens.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-eventsubscription.html#cfn-redshift-eventsubscription-subscriptionname
        '''
        result = self._values.get("subscription_name")
        assert result is not None, "Required property 'subscription_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A boolean value;

        set to ``true`` to activate the subscription, and set to ``false`` to create the subscription but not activate it.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-eventsubscription.html#cfn-redshift-eventsubscription-enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def event_categories(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies the Amazon Redshift event categories to be published by the event notification subscription.

        Values: configuration, management, monitoring, security, pending

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-eventsubscription.html#cfn-redshift-eventsubscription-eventcategories
        '''
        result = self._values.get("event_categories")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def severity(self) -> typing.Optional[builtins.str]:
        '''Specifies the Amazon Redshift event severity to be published by the event notification subscription.

        Values: ERROR, INFO

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-eventsubscription.html#cfn-redshift-eventsubscription-severity
        '''
        result = self._values.get("severity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sns_topic_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the Amazon SNS topic used to transmit the event notifications.

        The ARN is created by Amazon SNS when you create a topic and subscribe to it.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-eventsubscription.html#cfn-redshift-eventsubscription-snstopicarn
        '''
        result = self._values.get("sns_topic_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of one or more identifiers of Amazon Redshift source objects.

        All of the objects must be of the same type as was specified in the source type parameter. The event subscription will return only events generated by the specified objects. If not specified, then events are returned for all objects within the source type specified.

        Example: my-cluster-1, my-cluster-2

        Example: my-snapshot-20131010

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-eventsubscription.html#cfn-redshift-eventsubscription-sourceids
        '''
        result = self._values.get("source_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def source_type(self) -> typing.Optional[builtins.str]:
        '''The type of source that will be generating the events.

        For example, if you want to be notified of events generated by a cluster, you would set this parameter to cluster. If this value is not specified, events are returned for all Amazon Redshift objects in your AWS account . You must specify a source type in order to specify source IDs.

        Valid values: cluster, cluster-parameter-group, cluster-security-group, cluster-snapshot, and scheduled-action.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-eventsubscription.html#cfn-redshift-eventsubscription-sourcetype
        '''
        result = self._values.get("source_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of tag instances.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-eventsubscription.html#cfn-redshift-eventsubscription-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEventSubscriptionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnScheduledAction(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_redshift.CfnScheduledAction",
):
    '''A CloudFormation ``AWS::Redshift::ScheduledAction``.

    Creates a scheduled action. A scheduled action contains a schedule and an Amazon Redshift API action. For example, you can create a schedule of when to run the ``ResizeCluster`` API operation.

    :cloudformationResource: AWS::Redshift::ScheduledAction
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-scheduledaction.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_redshift as redshift
        
        # target_action: Any
        
        cfn_scheduled_action = redshift.CfnScheduledAction(self, "MyCfnScheduledAction",
            scheduled_action_name="scheduledActionName",
        
            # the properties below are optional
            enable=False,
            end_time="endTime",
            iam_role="iamRole",
            schedule="schedule",
            scheduled_action_description="scheduledActionDescription",
            start_time="startTime",
            target_action=target_action
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        scheduled_action_name: builtins.str,
        enable: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        end_time: typing.Optional[builtins.str] = None,
        iam_role: typing.Optional[builtins.str] = None,
        schedule: typing.Optional[builtins.str] = None,
        scheduled_action_description: typing.Optional[builtins.str] = None,
        start_time: typing.Optional[builtins.str] = None,
        target_action: typing.Any = None,
    ) -> None:
        '''Create a new ``AWS::Redshift::ScheduledAction``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param scheduled_action_name: The name of the scheduled action.
        :param enable: If true, the schedule is enabled. If false, the scheduled action does not trigger. For more information about ``state`` of the scheduled action, see ``ScheduledAction`` .
        :param end_time: The end time in UTC when the schedule is no longer active. After this time, the scheduled action does not trigger.
        :param iam_role: The IAM role to assume to run the scheduled action. This IAM role must have permission to run the Amazon Redshift API operation in the scheduled action. This IAM role must allow the Amazon Redshift scheduler (Principal scheduler.redshift.amazonaws.com) to assume permissions on your behalf. For more information about the IAM role to use with the Amazon Redshift scheduler, see `Using Identity-Based Policies for Amazon Redshift <https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-identity-based.html>`_ in the *Amazon Redshift Cluster Management Guide* .
        :param schedule: The schedule for a one-time (at format) or recurring (cron format) scheduled action. Schedule invocations must be separated by at least one hour. Format of at expressions is " ``at(yyyy-mm-ddThh:mm:ss)`` ". For example, " ``at(2016-03-04T17:27:00)`` ". Format of cron expressions is " ``cron(Minutes Hours Day-of-month Month Day-of-week Year)`` ". For example, " ``cron(0 10 ? * MON *)`` ". For more information, see `Cron Expressions <https://docs.aws.amazon.com//AmazonCloudWatch/latest/events/ScheduledEvents.html#CronExpressions>`_ in the *Amazon CloudWatch Events User Guide* .
        :param scheduled_action_description: The description of the scheduled action.
        :param start_time: The start time in UTC when the schedule is active. Before this time, the scheduled action does not trigger.
        :param target_action: A JSON format string of the Amazon Redshift API operation with input parameters. " ``{\\"ResizeCluster\\":{\\"NodeType\\":\\"ds2.8xlarge\\",\\"ClusterIdentifier\\":\\"my-test-cluster\\",\\"NumberOfNodes\\":3}}`` ".
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnScheduledAction.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnScheduledActionProps(
            scheduled_action_name=scheduled_action_name,
            enable=enable,
            end_time=end_time,
            iam_role=iam_role,
            schedule=schedule,
            scheduled_action_description=scheduled_action_description,
            start_time=start_time,
            target_action=target_action,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnScheduledAction.inspect)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnScheduledAction._render_properties)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrNextInvocations")
    def attr_next_invocations(self) -> typing.List[builtins.str]:
        '''List of times when the scheduled action will run.

        :cloudformationAttribute: NextInvocations
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrNextInvocations"))

    @builtins.property
    @jsii.member(jsii_name="attrState")
    def attr_state(self) -> builtins.str:
        '''The state of the scheduled action.

        For example, ``DISABLED`` .

        :cloudformationAttribute: State
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrState"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="scheduledActionName")
    def scheduled_action_name(self) -> builtins.str:
        '''The name of the scheduled action.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-scheduledaction.html#cfn-redshift-scheduledaction-scheduledactionname
        '''
        return typing.cast(builtins.str, jsii.get(self, "scheduledActionName"))

    @scheduled_action_name.setter
    def scheduled_action_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnScheduledAction, "scheduled_action_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scheduledActionName", value)

    @builtins.property
    @jsii.member(jsii_name="targetAction")
    def target_action(self) -> typing.Any:
        '''A JSON format string of the Amazon Redshift API operation with input parameters.

        " ``{\\"ResizeCluster\\":{\\"NodeType\\":\\"ds2.8xlarge\\",\\"ClusterIdentifier\\":\\"my-test-cluster\\",\\"NumberOfNodes\\":3}}`` ".

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-scheduledaction.html#cfn-redshift-scheduledaction-targetaction
        '''
        return typing.cast(typing.Any, jsii.get(self, "targetAction"))

    @target_action.setter
    def target_action(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnScheduledAction, "target_action").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetAction", value)

    @builtins.property
    @jsii.member(jsii_name="enable")
    def enable(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''If true, the schedule is enabled.

        If false, the scheduled action does not trigger. For more information about ``state`` of the scheduled action, see ``ScheduledAction`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-scheduledaction.html#cfn-redshift-scheduledaction-enable
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "enable"))

    @enable.setter
    def enable(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnScheduledAction, "enable").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enable", value)

    @builtins.property
    @jsii.member(jsii_name="endTime")
    def end_time(self) -> typing.Optional[builtins.str]:
        '''The end time in UTC when the schedule is no longer active.

        After this time, the scheduled action does not trigger.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-scheduledaction.html#cfn-redshift-scheduledaction-endtime
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endTime"))

    @end_time.setter
    def end_time(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnScheduledAction, "end_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endTime", value)

    @builtins.property
    @jsii.member(jsii_name="iamRole")
    def iam_role(self) -> typing.Optional[builtins.str]:
        '''The IAM role to assume to run the scheduled action.

        This IAM role must have permission to run the Amazon Redshift API operation in the scheduled action. This IAM role must allow the Amazon Redshift scheduler (Principal scheduler.redshift.amazonaws.com) to assume permissions on your behalf. For more information about the IAM role to use with the Amazon Redshift scheduler, see `Using Identity-Based Policies for Amazon Redshift <https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-identity-based.html>`_ in the *Amazon Redshift Cluster Management Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-scheduledaction.html#cfn-redshift-scheduledaction-iamrole
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "iamRole"))

    @iam_role.setter
    def iam_role(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnScheduledAction, "iam_role").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iamRole", value)

    @builtins.property
    @jsii.member(jsii_name="schedule")
    def schedule(self) -> typing.Optional[builtins.str]:
        '''The schedule for a one-time (at format) or recurring (cron format) scheduled action.

        Schedule invocations must be separated by at least one hour.

        Format of at expressions is " ``at(yyyy-mm-ddThh:mm:ss)`` ". For example, " ``at(2016-03-04T17:27:00)`` ".

        Format of cron expressions is " ``cron(Minutes Hours Day-of-month Month Day-of-week Year)`` ". For example, " ``cron(0 10 ? * MON *)`` ". For more information, see `Cron Expressions <https://docs.aws.amazon.com//AmazonCloudWatch/latest/events/ScheduledEvents.html#CronExpressions>`_ in the *Amazon CloudWatch Events User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-scheduledaction.html#cfn-redshift-scheduledaction-schedule
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schedule"))

    @schedule.setter
    def schedule(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnScheduledAction, "schedule").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schedule", value)

    @builtins.property
    @jsii.member(jsii_name="scheduledActionDescription")
    def scheduled_action_description(self) -> typing.Optional[builtins.str]:
        '''The description of the scheduled action.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-scheduledaction.html#cfn-redshift-scheduledaction-scheduledactiondescription
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scheduledActionDescription"))

    @scheduled_action_description.setter
    def scheduled_action_description(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnScheduledAction, "scheduled_action_description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scheduledActionDescription", value)

    @builtins.property
    @jsii.member(jsii_name="startTime")
    def start_time(self) -> typing.Optional[builtins.str]:
        '''The start time in UTC when the schedule is active.

        Before this time, the scheduled action does not trigger.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-scheduledaction.html#cfn-redshift-scheduledaction-starttime
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startTime"))

    @start_time.setter
    def start_time(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CfnScheduledAction, "start_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startTime", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_redshift.CfnScheduledActionProps",
    jsii_struct_bases=[],
    name_mapping={
        "scheduled_action_name": "scheduledActionName",
        "enable": "enable",
        "end_time": "endTime",
        "iam_role": "iamRole",
        "schedule": "schedule",
        "scheduled_action_description": "scheduledActionDescription",
        "start_time": "startTime",
        "target_action": "targetAction",
    },
)
class CfnScheduledActionProps:
    def __init__(
        self,
        *,
        scheduled_action_name: builtins.str,
        enable: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        end_time: typing.Optional[builtins.str] = None,
        iam_role: typing.Optional[builtins.str] = None,
        schedule: typing.Optional[builtins.str] = None,
        scheduled_action_description: typing.Optional[builtins.str] = None,
        start_time: typing.Optional[builtins.str] = None,
        target_action: typing.Any = None,
    ) -> None:
        '''Properties for defining a ``CfnScheduledAction``.

        :param scheduled_action_name: The name of the scheduled action.
        :param enable: If true, the schedule is enabled. If false, the scheduled action does not trigger. For more information about ``state`` of the scheduled action, see ``ScheduledAction`` .
        :param end_time: The end time in UTC when the schedule is no longer active. After this time, the scheduled action does not trigger.
        :param iam_role: The IAM role to assume to run the scheduled action. This IAM role must have permission to run the Amazon Redshift API operation in the scheduled action. This IAM role must allow the Amazon Redshift scheduler (Principal scheduler.redshift.amazonaws.com) to assume permissions on your behalf. For more information about the IAM role to use with the Amazon Redshift scheduler, see `Using Identity-Based Policies for Amazon Redshift <https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-identity-based.html>`_ in the *Amazon Redshift Cluster Management Guide* .
        :param schedule: The schedule for a one-time (at format) or recurring (cron format) scheduled action. Schedule invocations must be separated by at least one hour. Format of at expressions is " ``at(yyyy-mm-ddThh:mm:ss)`` ". For example, " ``at(2016-03-04T17:27:00)`` ". Format of cron expressions is " ``cron(Minutes Hours Day-of-month Month Day-of-week Year)`` ". For example, " ``cron(0 10 ? * MON *)`` ". For more information, see `Cron Expressions <https://docs.aws.amazon.com//AmazonCloudWatch/latest/events/ScheduledEvents.html#CronExpressions>`_ in the *Amazon CloudWatch Events User Guide* .
        :param scheduled_action_description: The description of the scheduled action.
        :param start_time: The start time in UTC when the schedule is active. Before this time, the scheduled action does not trigger.
        :param target_action: A JSON format string of the Amazon Redshift API operation with input parameters. " ``{\\"ResizeCluster\\":{\\"NodeType\\":\\"ds2.8xlarge\\",\\"ClusterIdentifier\\":\\"my-test-cluster\\",\\"NumberOfNodes\\":3}}`` ".

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-scheduledaction.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_redshift as redshift
            
            # target_action: Any
            
            cfn_scheduled_action_props = redshift.CfnScheduledActionProps(
                scheduled_action_name="scheduledActionName",
            
                # the properties below are optional
                enable=False,
                end_time="endTime",
                iam_role="iamRole",
                schedule="schedule",
                scheduled_action_description="scheduledActionDescription",
                start_time="startTime",
                target_action=target_action
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CfnScheduledActionProps.__init__)
            check_type(argname="argument scheduled_action_name", value=scheduled_action_name, expected_type=type_hints["scheduled_action_name"])
            check_type(argname="argument enable", value=enable, expected_type=type_hints["enable"])
            check_type(argname="argument end_time", value=end_time, expected_type=type_hints["end_time"])
            check_type(argname="argument iam_role", value=iam_role, expected_type=type_hints["iam_role"])
            check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
            check_type(argname="argument scheduled_action_description", value=scheduled_action_description, expected_type=type_hints["scheduled_action_description"])
            check_type(argname="argument start_time", value=start_time, expected_type=type_hints["start_time"])
            check_type(argname="argument target_action", value=target_action, expected_type=type_hints["target_action"])
        self._values: typing.Dict[str, typing.Any] = {
            "scheduled_action_name": scheduled_action_name,
        }
        if enable is not None:
            self._values["enable"] = enable
        if end_time is not None:
            self._values["end_time"] = end_time
        if iam_role is not None:
            self._values["iam_role"] = iam_role
        if schedule is not None:
            self._values["schedule"] = schedule
        if scheduled_action_description is not None:
            self._values["scheduled_action_description"] = scheduled_action_description
        if start_time is not None:
            self._values["start_time"] = start_time
        if target_action is not None:
            self._values["target_action"] = target_action

    @builtins.property
    def scheduled_action_name(self) -> builtins.str:
        '''The name of the scheduled action.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-scheduledaction.html#cfn-redshift-scheduledaction-scheduledactionname
        '''
        result = self._values.get("scheduled_action_name")
        assert result is not None, "Required property 'scheduled_action_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enable(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''If true, the schedule is enabled.

        If false, the scheduled action does not trigger. For more information about ``state`` of the scheduled action, see ``ScheduledAction`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-scheduledaction.html#cfn-redshift-scheduledaction-enable
        '''
        result = self._values.get("enable")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def end_time(self) -> typing.Optional[builtins.str]:
        '''The end time in UTC when the schedule is no longer active.

        After this time, the scheduled action does not trigger.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-scheduledaction.html#cfn-redshift-scheduledaction-endtime
        '''
        result = self._values.get("end_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iam_role(self) -> typing.Optional[builtins.str]:
        '''The IAM role to assume to run the scheduled action.

        This IAM role must have permission to run the Amazon Redshift API operation in the scheduled action. This IAM role must allow the Amazon Redshift scheduler (Principal scheduler.redshift.amazonaws.com) to assume permissions on your behalf. For more information about the IAM role to use with the Amazon Redshift scheduler, see `Using Identity-Based Policies for Amazon Redshift <https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-identity-based.html>`_ in the *Amazon Redshift Cluster Management Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-scheduledaction.html#cfn-redshift-scheduledaction-iamrole
        '''
        result = self._values.get("iam_role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schedule(self) -> typing.Optional[builtins.str]:
        '''The schedule for a one-time (at format) or recurring (cron format) scheduled action.

        Schedule invocations must be separated by at least one hour.

        Format of at expressions is " ``at(yyyy-mm-ddThh:mm:ss)`` ". For example, " ``at(2016-03-04T17:27:00)`` ".

        Format of cron expressions is " ``cron(Minutes Hours Day-of-month Month Day-of-week Year)`` ". For example, " ``cron(0 10 ? * MON *)`` ". For more information, see `Cron Expressions <https://docs.aws.amazon.com//AmazonCloudWatch/latest/events/ScheduledEvents.html#CronExpressions>`_ in the *Amazon CloudWatch Events User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-scheduledaction.html#cfn-redshift-scheduledaction-schedule
        '''
        result = self._values.get("schedule")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scheduled_action_description(self) -> typing.Optional[builtins.str]:
        '''The description of the scheduled action.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-scheduledaction.html#cfn-redshift-scheduledaction-scheduledactiondescription
        '''
        result = self._values.get("scheduled_action_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def start_time(self) -> typing.Optional[builtins.str]:
        '''The start time in UTC when the schedule is active.

        Before this time, the scheduled action does not trigger.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-scheduledaction.html#cfn-redshift-scheduledaction-starttime
        '''
        result = self._values.get("start_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_action(self) -> typing.Any:
        '''A JSON format string of the Amazon Redshift API operation with input parameters.

        " ``{\\"ResizeCluster\\":{\\"NodeType\\":\\"ds2.8xlarge\\",\\"ClusterIdentifier\\":\\"my-test-cluster\\",\\"NumberOfNodes\\":3}}`` ".

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-scheduledaction.html#cfn-redshift-scheduledaction-targetaction
        '''
        result = self._values.get("target_action")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnScheduledActionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnCluster",
    "CfnClusterParameterGroup",
    "CfnClusterParameterGroupProps",
    "CfnClusterProps",
    "CfnClusterSecurityGroup",
    "CfnClusterSecurityGroupIngress",
    "CfnClusterSecurityGroupIngressProps",
    "CfnClusterSecurityGroupProps",
    "CfnClusterSubnetGroup",
    "CfnClusterSubnetGroupProps",
    "CfnEndpointAccess",
    "CfnEndpointAccessProps",
    "CfnEndpointAuthorization",
    "CfnEndpointAuthorizationProps",
    "CfnEventSubscription",
    "CfnEventSubscriptionProps",
    "CfnScheduledAction",
    "CfnScheduledActionProps",
]

publication.publish()
