from concurrent import futures
import grpc
from protos import prototres_pb2_grpc


class GreeterServicer(prototres_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return super().SayHello(request,  context)

    def ParrotSaysHello(self, request, context):
        return super().ParrotSayHello(request, context)

    def ChattyClientSaysHello(self, request_iterator, context):
        return super().ChattyClientSaysHello(request_iterator, context)

    def InteractingHello(self, request_iterator, context):
        return super().InteractingHello(request_iterator,context)

def serve():
    server= grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    prototres_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()

