import grpc
import time
import threading
from concurrent import futures
import service_pb2
import service_pb2_grpc

# Connect to Heartbeat Server
heartbeat_channel = grpc.insecure_channel('localhost:50001')
heartbeat_stub = service_pb2_grpc.HeartbeatServiceStub(heartbeat_channel)

class LoggingService(service_pb2_grpc.LoggingServiceServicer):
    def SendLog(self, request, context):
        print(f"Backup received log: {request.message}")
        with open("backup_logs.txt", "a") as log_file:
            log_file.write(request.message + "\n")
        return service_pb2.LogResponse(success=True)

def send_heartbeat():
    """ Periodically send heartbeats to the Heartbeat Server """
    while True:
        request = service_pb2.HeartbeatRequest(server_name="Backup Server")
        try:
            response = heartbeat_stub.CheckStatus(request)
            print(f"Backup Server Heartbeat Sent. Alive: {response.is_alive}")
        except grpc.RpcError:
            print("⚠️ Backup Server failed to contact Heartbeat Server!")
        time.sleep(5)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    service_pb2_grpc.add_LoggingServiceServicer_to_server(LoggingService(), server)
    server.add_insecure_port('[::]:5001')
    print("Backup server running on port 5001...")

    # Start heartbeat in a separate thread
    heartbeat_thread = threading.Thread(target=send_heartbeat, daemon=True)
    heartbeat_thread.start()

    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
