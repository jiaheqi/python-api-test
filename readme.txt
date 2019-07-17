#python-2.7
# proto compile
cd test_case/protos/order/
python -m grpc.tools.protoc -I=. --python_out=../../pb2/test --grpc_python_out=../../pb2/test common.proto  orderQueryService.proto


python -m grpc.tools.protoc -I=. --python_out=../../pb2/sms --grpc_python_out=../../pb2/sms commons.proto  messagesendservice.proto
