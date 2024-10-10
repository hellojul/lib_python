import requests
from bs4 import BeautifulSoup

# === Requêtes HTTP avec requests ===

# Effectue une requête GET pour récupérer le HTML d'une page
def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

# Envoie des données à un serveur avec une requête POST
def post_data(url, data):
    response = requests.post(url, data=data)
    return response

# Effectue une requête GET avec des en-têtes personnalisés
def get_with_headers(url, headers):
    response = requests.get(url, headers=headers)
    return response.text

# Télécharge un fichier à partir d'une URL
def download_file(url, file_path):
    response = requests.get(url, stream=True)
    with open(file_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)

# Récupère et retourne le JSON d'une API
def get_json_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

# Effectue une requête tout en gérant les cookies
def handle_cookies(url):
    session = requests.Session()
    response = session.get(url)
    return session.cookies

# === Extraction de données avec BeautifulSoup ===

# Analyse le HTML d'une page avec BeautifulSoup
def parse_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup

# Récupère tous les liens d'une page web
def get_all_links(soup):
    return [a['href'] for a in soup.find_all('a', href=True)]

# Récupère toutes les balises images d'une page web
def get_all_images(soup):
    return [img['src'] for img in soup.find_all('img', src=True)]

# Extrait tout le texte d'une page HTML
def get_text_from_html(soup):
    return soup.get_text()

# Trouve un élément HTML par son identifiant
def get_element_by_id(soup, element_id):
    return soup.find(id=element_id)

# Récupère tous les éléments avec une classe CSS donnée
def get_elements_by_class(soup, class_name):
    return soup.find_all(class_=class_name)

# Extrait les données d'un tableau HTML
def get_table_data(soup):
    table = soup.find('table')
    rows = table.find_all('tr')
    table_data = []
    for row in rows:
        cols = row.find_all(['td', 'th'])
        table_data.append([col.get_text() for col in cols])
    return table_data

# Récupère la meta description d'une page web
def get_meta_description(soup):
    meta = soup.find('meta', attrs={'name': 'description'})
    return meta['content'] if meta else None

