from __future__ import print_function
import grpc
import logging
import HelloService_pb2
import HelloService_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = HelloService_pb2_grpc.HelloServiceStub(channel)
        response = stub.hello(HelloService_pb2.HelloRequest(firstName='André', lastName='Cupini', location='grpc python client'))
    print("Python client received: " + response.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()
