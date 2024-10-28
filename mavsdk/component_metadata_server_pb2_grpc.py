# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import component_metadata_server_pb2 as component__metadata__server_dot_component__metadata__server__pb2


class ComponentMetadataServerServiceStub(object):
    """Provide component metadata json definitions, such as parameters.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SetMetadata = channel.unary_unary(
                '/mavsdk.rpc.component_metadata_server.ComponentMetadataServerService/SetMetadata',
                request_serializer=component__metadata__server_dot_component__metadata__server__pb2.SetMetadataRequest.SerializeToString,
                response_deserializer=component__metadata__server_dot_component__metadata__server__pb2.SetMetadataResponse.FromString,
                )


class ComponentMetadataServerServiceServicer(object):
    """Provide component metadata json definitions, such as parameters.
    """

    def SetMetadata(self, request, context):
        """
        Provide metadata (can only be called once)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ComponentMetadataServerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SetMetadata': grpc.unary_unary_rpc_method_handler(
                    servicer.SetMetadata,
                    request_deserializer=component__metadata__server_dot_component__metadata__server__pb2.SetMetadataRequest.FromString,
                    response_serializer=component__metadata__server_dot_component__metadata__server__pb2.SetMetadataResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'mavsdk.rpc.component_metadata_server.ComponentMetadataServerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ComponentMetadataServerService(object):
    """Provide component metadata json definitions, such as parameters.
    """

    @staticmethod
    def SetMetadata(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mavsdk.rpc.component_metadata_server.ComponentMetadataServerService/SetMetadata',
            component__metadata__server_dot_component__metadata__server__pb2.SetMetadataRequest.SerializeToString,
            component__metadata__server_dot_component__metadata__server__pb2.SetMetadataResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)