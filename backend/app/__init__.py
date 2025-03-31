from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_restful import Api
from app.routes import initialize_routes
import logging
import requests
from logging.handlers import RotatingFileHandler
import threading
import time

jwt = JWTManager()

# Custom logging handler to synchronize logs to the backup server.
class BackupLogHandler(logging.Handler):
    def emit(self, record):
        log_entry = self.format(record)
        try:
            # Adjust the URL if your backup server is hosted elsewhere.
            requests.post("http://localhost:5001/sync-log", json={"log": log_entry}, timeout=2)
        except Exception:
            # If the backup server is unreachable, simply continue.
            pass

def setup_logging(app):
    """Sets up local file logging and synchronizes logs to the backup server."""
    # Local rotating file handler.
    file_handler = RotatingFileHandler("primary_operations.txt", maxBytes=1_000_000, backupCount=3)
    file_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
    file_handler.setFormatter(formatter)
    app.logger.addHandler(file_handler)

    # Backup log handler for synchronizing logs.
    backup_handler = BackupLogHandler()
    backup_handler.setLevel(logging.INFO)
    backup_handler.setFormatter(formatter)
    app.logger.addHandler(backup_handler)

def start_heartbeat(app):
    """Starts a background thread to ping the backup server's heartbeat endpoint."""
    def heartbeat_monitor():
        while True:
            try:
                response = requests.get("http://localhost:5001/heartbeat", timeout=5)
                if response.status_code == 200:
                    app.logger.info("Backup server heartbeat OK")
                else:
                    app.logger.warning("Backup server heartbeat returned status code: %s", response.status_code)
            except Exception as e:
                app.logger.error("Backup server heartbeat error: %s", e)
            time.sleep(10)  # Interval between heartbeat checks.
    threading.Thread(target=heartbeat_monitor, daemon=True).start()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = "secret_key"
    app.config["JWT_SECRET_KEY"] = "jwt_secret"
    
    jwt.init_app(app)

    # Initialize API routes.
    api = Api(app)
    initialize_routes(api)

    # Setup logging (local file + backup synchronization).
    setup_logging(app)
    
    # Start the heartbeat service.
    start_heartbeat(app)

    return app
