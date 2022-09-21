# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import diff_pb2 as diff__pb2


class DiffServiceStub(object):
    """DiffService is a service which provides RPCs to inspect differences
    introduced between a set of commits.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CommitDiff = channel.unary_stream(
                '/gitaly.DiffService/CommitDiff',
                request_serializer=diff__pb2.CommitDiffRequest.SerializeToString,
                response_deserializer=diff__pb2.CommitDiffResponse.FromString,
                )
        self.CommitDelta = channel.unary_stream(
                '/gitaly.DiffService/CommitDelta',
                request_serializer=diff__pb2.CommitDeltaRequest.SerializeToString,
                response_deserializer=diff__pb2.CommitDeltaResponse.FromString,
                )
        self.RawDiff = channel.unary_stream(
                '/gitaly.DiffService/RawDiff',
                request_serializer=diff__pb2.RawDiffRequest.SerializeToString,
                response_deserializer=diff__pb2.RawDiffResponse.FromString,
                )
        self.RawPatch = channel.unary_stream(
                '/gitaly.DiffService/RawPatch',
                request_serializer=diff__pb2.RawPatchRequest.SerializeToString,
                response_deserializer=diff__pb2.RawPatchResponse.FromString,
                )
        self.DiffStats = channel.unary_stream(
                '/gitaly.DiffService/DiffStats',
                request_serializer=diff__pb2.DiffStatsRequest.SerializeToString,
                response_deserializer=diff__pb2.DiffStatsResponse.FromString,
                )
        self.FindChangedPaths = channel.unary_stream(
                '/gitaly.DiffService/FindChangedPaths',
                request_serializer=diff__pb2.FindChangedPathsRequest.SerializeToString,
                response_deserializer=diff__pb2.FindChangedPathsResponse.FromString,
                )


class DiffServiceServicer(object):
    """DiffService is a service which provides RPCs to inspect differences
    introduced between a set of commits.
    """

    def CommitDiff(self, request, context):
        """Returns stream of CommitDiffResponse with patches chunked over messages
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CommitDelta(self, request, context):
        """Return a stream so we can divide the response in chunks of deltas
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RawDiff(self, request, context):
        """This comment is left unintentionally blank.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RawPatch(self, request, context):
        """This comment is left unintentionally blank.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DiffStats(self, request, context):
        """This comment is left unintentionally blank.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FindChangedPaths(self, request, context):
        """Return a list of files changed along with the status of each file
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DiffServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CommitDiff': grpc.unary_stream_rpc_method_handler(
                    servicer.CommitDiff,
                    request_deserializer=diff__pb2.CommitDiffRequest.FromString,
                    response_serializer=diff__pb2.CommitDiffResponse.SerializeToString,
            ),
            'CommitDelta': grpc.unary_stream_rpc_method_handler(
                    servicer.CommitDelta,
                    request_deserializer=diff__pb2.CommitDeltaRequest.FromString,
                    response_serializer=diff__pb2.CommitDeltaResponse.SerializeToString,
            ),
            'RawDiff': grpc.unary_stream_rpc_method_handler(
                    servicer.RawDiff,
                    request_deserializer=diff__pb2.RawDiffRequest.FromString,
                    response_serializer=diff__pb2.RawDiffResponse.SerializeToString,
            ),
            'RawPatch': grpc.unary_stream_rpc_method_handler(
                    servicer.RawPatch,
                    request_deserializer=diff__pb2.RawPatchRequest.FromString,
                    response_serializer=diff__pb2.RawPatchResponse.SerializeToString,
            ),
            'DiffStats': grpc.unary_stream_rpc_method_handler(
                    servicer.DiffStats,
                    request_deserializer=diff__pb2.DiffStatsRequest.FromString,
                    response_serializer=diff__pb2.DiffStatsResponse.SerializeToString,
            ),
            'FindChangedPaths': grpc.unary_stream_rpc_method_handler(
                    servicer.FindChangedPaths,
                    request_deserializer=diff__pb2.FindChangedPathsRequest.FromString,
                    response_serializer=diff__pb2.FindChangedPathsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'gitaly.DiffService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DiffService(object):
    """DiffService is a service which provides RPCs to inspect differences
    introduced between a set of commits.
    """

    @staticmethod
    def CommitDiff(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/gitaly.DiffService/CommitDiff',
            diff__pb2.CommitDiffRequest.SerializeToString,
            diff__pb2.CommitDiffResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CommitDelta(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/gitaly.DiffService/CommitDelta',
            diff__pb2.CommitDeltaRequest.SerializeToString,
            diff__pb2.CommitDeltaResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RawDiff(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/gitaly.DiffService/RawDiff',
            diff__pb2.RawDiffRequest.SerializeToString,
            diff__pb2.RawDiffResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RawPatch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/gitaly.DiffService/RawPatch',
            diff__pb2.RawPatchRequest.SerializeToString,
            diff__pb2.RawPatchResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DiffStats(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/gitaly.DiffService/DiffStats',
            diff__pb2.DiffStatsRequest.SerializeToString,
            diff__pb2.DiffStatsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FindChangedPaths(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/gitaly.DiffService/FindChangedPaths',
            diff__pb2.FindChangedPathsRequest.SerializeToString,
            diff__pb2.FindChangedPathsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
