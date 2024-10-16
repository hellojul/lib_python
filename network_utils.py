# network_utils.py

import os
import socket
import smtplib
import requests
from http.server import SimpleHTTPRequestHandler, HTTPServer
from email.mime.text import MIMEText


# 1. Fonction pour envoyer une requête GET à une URL
def get_request(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None


# 2. Fonction pour envoyer une requête POST avec des données à une URL
def post_request(url, data):
    response = requests.post(url, json=data)
    if response.status_code == 200:
        return response.text
    else:
        return None


# 3. Fonction pour obtenir l'adresse IP de la machine locale
def get_local_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address


# 4. Fonction pour pinguer une adresse (vérifier la connectivité)
def ping(address):
    response = os.system(f"ping -c 1 {address}")
    if response == 0:
        return True
    else:
        return False


# 5. Fonction pour télécharger un fichier depuis une URL et l'enregistrer localement
def download_file(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)
        return True
    return False


# 6. Fonction pour démarrer un serveur HTTP simple
def start_http_server(port=8080):
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print(f"Serveur en cours d'exécution sur le port {port}...")
    httpd.serve_forever()


# 7. Fonction pour résoudre un nom d'hôte en une adresse IP (recherche DNS)
def resolve_hostname(hostname):
    try:
        return socket.gethostbyname(hostname)
    except socket.error:
        return None


# 8. Fonction pour envoyer un e-mail via SMTP
def send_email(smtp_server, port, sender_email, receiver_email, subject, body, login, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()  # Sécuriser la connexion
            server.login(login, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        return True
    except Exception as e:
        print(f"Échec de l'envoi de l'e-mail : {e}")
        return False


# 9. Fonction pour scanner si un port est ouvert sur une adresse IP donnée
def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((ip, port))
    sock.close()
    if result == 0:
        return True
    else:
        return False


# 10. Fonction pour créer un client TCP et envoyer un message
def tcp_client(server_ip, server_port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((server_ip, server_port))
        sock.sendall(message.encode())
        response = sock.recv(1024)
        return response.decode()
    finally:
        sock.close()


# 11. Fonction pour démarrer un serveur TCP simple
def tcp_server(host='localhost', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"À l'écoute sur {host}:{port}")
        conn, addr = s.accept()
        with conn:
            print(f"Connecté par {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)

