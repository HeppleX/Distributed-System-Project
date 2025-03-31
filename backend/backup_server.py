from flask import Flask, request, jsonify
import os
import threading
import time
import requests

app = Flask(__name__)

LOG_FILE = "backup_operations.txt"
PRIMARY_SERVER_URL = "http://localhost:5000"
IS_PRIMARY = False  # Track whether this server is acting as the primary


@app.route('/heartbeat', methods=['GET'])
def heartbeat():
    return jsonify({"status": "alive"}), 200


@app.route('/sync-log', methods=['POST'])
def sync_log():

    data = request.get_json()
    log_entry = data.get("log")
    if log_entry:
        with open(LOG_FILE, "a") as f:
            f.write("SYNC FROM PRIMARY:\n" + log_entry + "\n")
        return jsonify({"message": "Log synchronized"}), 200

    return jsonify({"message": "No log data provided"}), 400


def monitor_primary():
    """Continuously checks if the primary server is alive. If it fails, take over."""
    global IS_PRIMARY

    while True:
        try:
            response = requests.get(f"{PRIMARY_SERVER_URL}/heartbeat", timeout=5)
            if response.status_code == 200:
                print("Primary server is alive.")
                IS_PRIMARY = False  # Reset state if the primary is back
            else:
                print("Primary server not responding properly.")
        except requests.exceptions.RequestException:
            print("Primary server down! Switching to primary mode.")
            # IS_PRIMARY = True  # Promote backup to act as primary
            # os.system("python main.py")  # Start main app 

        time.sleep(10)  # Check every 10 seconds


if __name__ == '__main__':
    # Start primary monitoring in a background thread
    threading.Thread(target=monitor_primary, daemon=True).start()

    # Run the backup server
    app.run(port=5001, debug=True)
