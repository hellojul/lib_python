# network_utils.py

import os
import socket
import smtplib
import requests
from http.server import SimpleHTTPRequestHandler, HTTPServer
from email.mime.text import MIMEText


# 1. Function to send a GET request to a URL
def get_request(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None


# 2. Function to send a POST request with data to a URL
def post_request(url, data):
    response = requests.post(url, json=data)
    if response.status_code == 200:
        return response.text
    else:
        return None


# 3. Function to get the local machine's IP address
def get_local_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address


# 4. Function to ping an address (check connectivity)
def ping(address):
    response = os.system(f"ping -c 1 {address}")
    if response == 0:
        return True
    else:
        return False


# 5. Function to download a file from a URL and save it locally
def download_file(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)
        return True
    return False


# 6. Function to start a simple HTTP server
def start_http_server(port=8080):
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print(f"Serving on port {port}...")
    httpd.serve_forever()


# 7. Function to resolve a hostname to an IP address (DNS lookup)
def resolve_hostname(hostname):
    try:
        return socket.gethostbyname(hostname)
    except socket.error:
        return None


# 8. Function to send an email via SMTP
def send_email(smtp_server, port, sender_email, receiver_email, subject, body, login, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()  # Secure the connection
            server.login(login, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False


# 9. Function to scan if a port is open on a given IP address
def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((ip, port))
    sock.close()
    if result == 0:
        return True
    else:
        return False


# 10. Function to create a TCP client and send a message
def tcp_client(server_ip, server_port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((server_ip, server_port))
        sock.sendall(message.encode())
        response = sock.recv(1024)
        return response.decode()
    finally:
        sock.close()


# 11. Function to start a simple TCP server
def tcp_server(host='localhost', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Listening on {host}:{port}")
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)

