#python-2.7
# proto compile
cd test_case/protos/order/
python -m grpc.tools.protoc -I=. --python_out=../../pb2/test --grpc_python_out=../../pb2/test common.proto  orderQueryService.proto
python -m grpc.tools.protoc -I=. --python_out=../../pb2/sms --grpc_python_out=../../pb2/sms commons.proto  messagesendservice.proto
教程地址：
https://note.youdao.com/ynoteshare1/index.html?id=269939c6cb5417d43ee0f6abb6626226&type=note
