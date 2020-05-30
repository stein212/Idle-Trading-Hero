import grpc

import route_pb2
import route_pb2_grpc


channel = grpc.insecure_channel('localhost:50051')
stub = route_pb2_grpc.RouteStub(channel)

from google.protobuf.struct_pb2 import Struct
params = Struct()
params.update({
    'ema26': 26,
    'ema12': 12,
    'ema9': 9,
})

Selection = route_pb2.Selection(Strategy='MACD',
                                 Parameters=params,
                                 Capital=1000)

feature = stub.InitialiseAlgorithm(Selection)
print(feature)