# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import server_pb2 as server__pb2


class ServerServiceStub(object):
    """ServerService is a service that provides information about a Gitaly server.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ServerInfo = channel.unary_unary(
                '/gitaly.ServerService/ServerInfo',
                request_serializer=server__pb2.ServerInfoRequest.SerializeToString,
                response_deserializer=server__pb2.ServerInfoResponse.FromString,
                )
        self.DiskStatistics = channel.unary_unary(
                '/gitaly.ServerService/DiskStatistics',
                request_serializer=server__pb2.DiskStatisticsRequest.SerializeToString,
                response_deserializer=server__pb2.DiskStatisticsResponse.FromString,
                )
        self.ClockSynced = channel.unary_unary(
                '/gitaly.ServerService/ClockSynced',
                request_serializer=server__pb2.ClockSyncedRequest.SerializeToString,
                response_deserializer=server__pb2.ClockSyncedResponse.FromString,
                )


class ServerServiceServicer(object):
    """ServerService is a service that provides information about a Gitaly server.
    """

    def ServerInfo(self, request, context):
        """This comment is left unintentionally blank.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DiskStatistics(self, request, context):
        """This comment is left unintentionally blank.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClockSynced(self, request, context):
        """ClockSynced checks if machine clock is synced
        (the offset is less that the one passed in the request).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ServerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ServerInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.ServerInfo,
                    request_deserializer=server__pb2.ServerInfoRequest.FromString,
                    response_serializer=server__pb2.ServerInfoResponse.SerializeToString,
            ),
            'DiskStatistics': grpc.unary_unary_rpc_method_handler(
                    servicer.DiskStatistics,
                    request_deserializer=server__pb2.DiskStatisticsRequest.FromString,
                    response_serializer=server__pb2.DiskStatisticsResponse.SerializeToString,
            ),
            'ClockSynced': grpc.unary_unary_rpc_method_handler(
                    servicer.ClockSynced,
                    request_deserializer=server__pb2.ClockSyncedRequest.FromString,
                    response_serializer=server__pb2.ClockSyncedResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'gitaly.ServerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ServerService(object):
    """ServerService is a service that provides information about a Gitaly server.
    """

    @staticmethod
    def ServerInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gitaly.ServerService/ServerInfo',
            server__pb2.ServerInfoRequest.SerializeToString,
            server__pb2.ServerInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DiskStatistics(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gitaly.ServerService/DiskStatistics',
            server__pb2.DiskStatisticsRequest.SerializeToString,
            server__pb2.DiskStatisticsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ClockSynced(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gitaly.ServerService/ClockSynced',
            server__pb2.ClockSyncedRequest.SerializeToString,
            server__pb2.ClockSyncedResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
