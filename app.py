from flask import Flask, request, jsonify
import socket
import sqlite3
from database import init_db

app = Flask(__name__)

# Initialize database at startup
init_db()

HOST = '127.0.0.1'
PORT = 65432


def send_to_machine(command):
    """
    Sends a command to the simulated machine
    via TCP socket and waits for acknowledgment.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(command.encode())
        data = s.recv(1024)
        return data.decode()


def log_command(command, status):
    """
    Logs command and machine response into database
    for traceability and debugging.
    """
    conn = sqlite3.connect("lab.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO machine_logs (command, status) VALUES (?, ?)",
        (command, status)
    )

    conn.commit()
    conn.close()


@app.route("/start", methods=["POST"])
def start_machine():
    """
    Starts machine operation.
    """
    response = send_to_machine("START")
    log_command("START", response)
    return jsonify({"message": response})


@app.route("/stop", methods=["POST"])
def stop_machine():
    """
    Stops machine operation.
    """
    response = send_to_machine("STOP")
    log_command("STOP", response)
    return jsonify({"message": response})


@app.route("/status", methods=["GET"])
def status():
    """
    Returns current machine status.
    (In real system, this would query telemetry.)
    """
    return jsonify({"machine_status": "Running"})


if __name__ == "__main__":
    app.run(debug=True)