____Overview____
The Smart Lab Equipment Automation Simulator is a Python-based backend system designed to simulate automated laboratory machinery used in agricultural and biotech research environments.
The system allows users to send machine control commands via RESTful APIs, receive telemetry responses through TCP socket communication, and log operational data into a relational database.
This project demonstrates practical experience in:
Python automation engineering
JSON API development
SQL relational database design
Socket-based communication
Logging, debugging, and system validation

____System Architecture____
Client (Postman)
⬇
Flask REST API
⬇
Machine Command Processor
⬇
TCP Socket Simulation
⬇
SQLite Database Logging

____Features____
Start and Stop machine operations
Simulated telemetry generation (temperature & humidity)
TCP socket-based machine response handling
SQL-based activity logging
Threshold validation alerts
Structured exception handling

____Tech Stack____
Python 3
Flask
SQLite
TCP Socket Programming
JSON APIs

____Database Schema____
Table: machines
id (Primary Key)
machine_name
status
Table: machine_logs
id (Primary Key)
machine_id
command
temperature
humidity
timestamp

____Setup Instructions____
Clone repository
Install dependencies:
pip install -r requirements.txt
Run application:
python app.py
Use Postman to test endpoints:
POST /start
POST /stop
