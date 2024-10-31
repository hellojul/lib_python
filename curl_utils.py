import subprocess

def curl_get(url, headers=None):
    """Effectue une requête GET à l'URL spécifiée."""
    command = ["curl", "-X", "GET", url]
    if headers:
        for key, value in headers.items():
            command.extend(["-H", f"{key}: {value}"])
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

def curl_post(url, data=None, headers=None):
    """Effectue une requête POST à l'URL spécifiée avec des données."""
    command = ["curl", "-X", "POST", url]
    if headers:
        for key, value in headers.items():
            command.extend(["-H", f"{key}: {value}"])
    if data:
        for key, value in data.items():
            command.extend(["-d", f"{key}={value}"])
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

def curl_download_file(url, output_path):
    """Télécharge un fichier depuis une URL et le sauvegarde dans le chemin spécifié."""
    command = ["curl", "-o", output_path, url]
    subprocess.run(command)

def curl_check_site_status(url):
    """Vérifie le statut d'un site via une requête HEAD."""
    command = ["curl", "-I", url]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

def curl_upload_file(url, file_path, headers=None):
    """Upload un fichier à une URL en utilisant une requête POST multipart."""
    command = ["curl", "-X", "POST", "-F", f"file=@{file_path}", url]
    if headers:
        for key, value in headers.items():
            command.extend(["-H", f"{key}: {value}"])
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

def curl_get_with_auth(url, username, password):
    """Effectue une requête GET avec authentification de base."""
    command = ["curl", "-u", f"{username}:{password}", url]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

def curl_get_json(url):
    """Récupère et renvoie le contenu JSON d'une URL."""
    command = ["curl", "-H", "Accept: application/json", url]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

def curl_with_cookies(url, cookie_file):
    """Envoie une requête GET avec un fichier de cookies spécifié."""
    command = ["curl", "-b", cookie_file, url]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

def curl_save_cookies(url, cookie_file):
    """Sauvegarde les cookies d'une session dans un fichier spécifié."""
    command = ["curl", "-c", cookie_file, url]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

def curl_speed_test(url):
    """Teste la vitesse de téléchargement depuis une URL."""
    command = ["curl", "-w", "%{speed_download}", "-o", "/dev/null", "-s", url]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

def curl_follow_redirects(url):
    """Suit les redirections jusqu'à la destination finale."""
    command = ["curl", "-L", url]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

def curl_custom_timeout(url, timeout):
    """Effectue une requête GET avec un délai d'attente personnalisé."""
    command = ["curl", "--max-time", str(timeout), url]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

def curl_verbose_output(url):
    """Effectue une requête GET et affiche un retour détaillé pour débogage."""
    command = ["curl", "-v", url]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

def curl_custom_user_agent(url, user_agent):
    """Envoie une requête GET avec un User-Agent personnalisé."""
    command = ["curl", "-A", user_agent, url]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

def curl_restrict_rate(url, rate_limit):
    """Limite la vitesse de téléchargement de la requête."""
    command = ["curl", "--limit-rate", rate_limit, url]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

def curl_head_request(url):
    """Effectue une requête HEAD pour récupérer uniquement les en-têtes."""
    command = ["curl", "-I", url]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

def curl_get_ip_info():
    """Utilise un service d'IP pour obtenir les informations de l'adresse IP actuelle."""
    command = ["curl", "https://ipinfo.io"]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

