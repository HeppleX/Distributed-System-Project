import grpc
import time
import threading
from concurrent import futures
import service_pb2
import service_pb2_grpc

# Store the last heartbeat time for each server
server_status = {
    "Main Server": time.time(),
    "Backup Server": time.time()
}
CHECK_INTERVAL = 5  # How often to check for failures
TIMEOUT = 10        # Time in seconds before marking a server as down

class HeartbeatService(service_pb2_grpc.HeartbeatServiceServicer):
    def CheckStatus(self, request, context):
        """ Update the last seen time when a server sends a heartbeat """
        server_status[request.server_name] = time.time()
        return service_pb2.HeartbeatResponse(is_alive=True)

def monitor_servers():
    """ Periodically checks if servers are alive and prints alerts """
    while True:
        time.sleep(CHECK_INTERVAL)
        current_time = time.time()
        
        for server, last_seen in server_status.items():
            if current_time - last_seen > TIMEOUT:
                print(f"⚠️ WARNING: {server} is DOWN!")

def serve():
    """ Start the heartbeat gRPC server """
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    service_pb2_grpc.add_HeartbeatServiceServicer_to_server(HeartbeatService(), server)
    server.add_insecure_port('[::]:50001')
    print("Heartbeat server running on port 50001...")

    # Start monitoring thread
    monitoring_thread = threading.Thread(target=monitor_servers, daemon=True)
    monitoring_thread.start()

    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
