# autogenerated
# mypy: ignore-errors
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from rime_sdk.protos.secrets import secrets_pb2 as secrets_dot_secrets__pb2


class SecretManagerStub(object):
    """******************************
    INTERNAL RPCs
    these methods should only be used by internal services and not advertised to
    users.
    ******************************
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateSecret = channel.unary_unary(
                '/rime.SecretManager/CreateSecret',
                request_serializer=secrets_dot_secrets__pb2.CreateSecretRequest.SerializeToString,
                response_deserializer=secrets_dot_secrets__pb2.CreateSecretResponse.FromString,
                )
        self.DeleteSecret = channel.unary_unary(
                '/rime.SecretManager/DeleteSecret',
                request_serializer=secrets_dot_secrets__pb2.DeleteSecretRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.ReadSecret = channel.unary_unary(
                '/rime.SecretManager/ReadSecret',
                request_serializer=secrets_dot_secrets__pb2.ReadSecretRequest.SerializeToString,
                response_deserializer=secrets_dot_secrets__pb2.ReadSecretResponse.FromString,
                )


class SecretManagerServicer(object):
    """******************************
    INTERNAL RPCs
    these methods should only be used by internal services and not advertised to
    users.
    ******************************
    """

    def CreateSecret(self, request, context):
        """CreateSecret

        Creates a new secret in the backend if it does not exist.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteSecret(self, request, context):
        """DeleteSecret

        Hard-delete a secret in the backend.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadSecret(self, request, context):
        """ReadSecret

        Reads the secret with `name` from the Secret Manager.
        This should only be used by services that need to know the secret.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SecretManagerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateSecret': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateSecret,
                    request_deserializer=secrets_dot_secrets__pb2.CreateSecretRequest.FromString,
                    response_serializer=secrets_dot_secrets__pb2.CreateSecretResponse.SerializeToString,
            ),
            'DeleteSecret': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteSecret,
                    request_deserializer=secrets_dot_secrets__pb2.DeleteSecretRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'ReadSecret': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadSecret,
                    request_deserializer=secrets_dot_secrets__pb2.ReadSecretRequest.FromString,
                    response_serializer=secrets_dot_secrets__pb2.ReadSecretResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'rime.SecretManager', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SecretManager(object):
    """******************************
    INTERNAL RPCs
    these methods should only be used by internal services and not advertised to
    users.
    ******************************
    """

    @staticmethod
    def CreateSecret(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rime.SecretManager/CreateSecret',
            secrets_dot_secrets__pb2.CreateSecretRequest.SerializeToString,
            secrets_dot_secrets__pb2.CreateSecretResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteSecret(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rime.SecretManager/DeleteSecret',
            secrets_dot_secrets__pb2.DeleteSecretRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReadSecret(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rime.SecretManager/ReadSecret',
            secrets_dot_secrets__pb2.ReadSecretRequest.SerializeToString,
            secrets_dot_secrets__pb2.ReadSecretResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
