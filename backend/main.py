import logging
import grpc
import time
import threading
from flask import request, jsonify
from app import create_app
import service_pb2
import service_pb2_grpc

app = create_app()

# Configure Logging
logging.basicConfig(filename="primary_logs.txt", level=logging.INFO, format="%(asctime)s - %(message)s")

# gRPC connections
heartbeat_channel = grpc.insecure_channel("localhost:50001")
heartbeat_stub = service_pb2_grpc.HeartbeatServiceStub(heartbeat_channel)

backup_channel = grpc.insecure_channel("localhost:5001")
backup_stub = service_pb2_grpc.LoggingServiceStub(backup_channel)

def send_heartbeat():
    """ Periodically sends heartbeats to the Heartbeat Server """
    while True:
        request = service_pb2.HeartbeatRequest(server_name="Main Server")
        try:
            response = heartbeat_stub.CheckStatus(request)
            print(f"Primary Server Heartbeat Sent. Alive: {response.is_alive}")
        except grpc.RpcError:
            print("⚠️ Main Server could not contact Heartbeat Server!")
        time.sleep(5)

if __name__ == "__main__":
    print("Main server started on port 5000...")
    send_heartbeat_thread = threading.Thread(target=send_heartbeat, daemon=True)
    send_heartbeat_thread.start()
    app.run(host="127.0.0.1", port=5000, debug=True)