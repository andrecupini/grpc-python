# grpc-python
- Server/Client gRPC in Python <br />
A simple Hello World project to demonstrate use of gRPC with Python

Run the commands bellow to install **grpc** and **grpc tools**

```
# Update pip
python -m pip install --upgrade pip
```

```
# Install grpc
python -m pip install grpcio
```

```
# Install grpc tools
python -m pip install grpcio_tools
```

Run this command to get the artifact auto generated from the protobuf file
```
 python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. HelloService.proto
```

<sup><sub>André Cupini - 2021-06-16</sub></sup>