from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Desafio Custom Message - ceps-repo"

@app.route("/teste")
def get_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return f"IP da máquina: {ip_address}"