from flask import Flask, request
import subprocess
import os
import socket
app = Flask(__name__)

seed = 0

@app.get("/")
def get_seed():
    return socket.gethostname(), 200


@app.post("/")
def update_seed():
    subprocess.Popen('./stress_cpu.py')
    return '', 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
