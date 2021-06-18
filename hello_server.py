from concurrent import futures

import grpc
import logging
import HelloService_pb2
import HelloService_pb2_grpc


class HelloService(HelloService_pb2_grpc.HelloServiceServicer):

    def hello(self, request, context):
        return HelloService_pb2.HelloResponse(
            message='Hello, %s %s - This message came from: %s!' % (request.firstName, request.lastName, request.location))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    HelloService_pb2_grpc.add_HelloServiceServicer_to_server(HelloService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
