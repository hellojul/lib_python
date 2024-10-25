import socket

# Création d'un socket TCP
def create_tcp_socket():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("TCP socket created successfully")
        return s
    except socket.error as e:
        print(f"Error creating socket: {e}")
        return None

# Création d'un socket UDP
def create_udp_socket():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print("UDP socket created successfully")
        return s
    except socket.error as e:
        print(f"Error creating socket: {e}")
        return None

# Connexion d'un socket client à un serveur
def connect_socket(sock, host, port):
    try:
        sock.connect((host, port))
        print(f"Connected to {host} on port {port}")
    except socket.error as e:
        print(f"Connection error: {e}")

# Attacher un socket serveur à un port
def bind_socket(sock, host, port):
    try:
        sock.bind((host, port))
        print(f"Socket bound to {host} on port {port}")
    except socket.error as e:
        print(f"Binding error: {e}")

# Écouter les connexions entrantes (serveur)
def listen_socket(sock, backlog=5):
    try:
        sock.listen(backlog)
        print("Socket is now listening for connections")
    except socket.error as e:
        print(f"Error listening on socket: {e}")

# Accepter une connexion entrante (serveur)
def accept_connection(sock):
    try:
        client_sock, client_address = sock.accept()
        print(f"Accepted connection from {client_address}")
        return client_sock, client_address
    except socket.error as e:
        print(f"Error accepting connection: {e}")
        return None, None

# Envoyer des données sur un socket
def send_data(sock, data):
    try:
        sock.sendall(data.encode())
        print("Data sent successfully")
    except socket.error as e:
        print(f"Error sending data: {e}")

# Recevoir des données depuis un socket
def receive_data(sock, buffer_size=1024):
    try:
        data = sock.recv(buffer_size).decode()
        print("Data received successfully")
        return data
    except socket.error as e:
        print(f"Error receiving data: {e}")
        return None

# Fermer un socket
def close_socket(sock):
    try:
        sock.close()
        print("Socket closed successfully")
    except socket.error as e:
        print(f"Error closing socket: {e}")

# Utiliser un contexte sécurisé pour un socket (SSL/TLS)
def secure_socket(sock, certfile=None, keyfile=None):
    try:
        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        if certfile and keyfile:
            context.load_cert_chain(certfile=certfile, keyfile=keyfile)
        secure_sock = context.wrap_socket(sock, server_side=True)
        print("Socket secured with SSL/TLS")
        return secure_sock
    except Exception as e:
        print(f"Error securing socket: {e}")
        return None

# Utilisation de timeout pour le socket
def set_timeout(sock, timeout=5.0):
    try:
        sock.settimeout(timeout)
        print(f"Socket timeout set to {timeout} seconds")
    except socket.error as e:
        print(f"Error setting timeout: {e}")

