import requests
from bs4 import BeautifulSoup

class WebScraperUtilities:
    # === Requêtes HTTP avec requests ===

    def get_html(self, url):
        """
        Effectue une requête GET pour récupérer le HTML d'une page.
        Retourne le contenu HTML si la requête réussit, sinon None.
        """
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None

    def post_data(self, url, data):
        """
        Envoie des données à un serveur avec une requête POST.
        Retourne la réponse du serveur.
        """
        response = requests.post(url, data=data)
        return response

    def get_with_headers(self, url, headers):
        """
        Effectue une requête GET avec des en-têtes personnalisés.
        Retourne le contenu HTML de la réponse.
        """
        response = requests.get(url, headers=headers)
        return response.text

    def download_file(self, url, file_path):
        """
        Télécharge un fichier à partir d'une URL et le sauvegarde localement.
        """
        response = requests.get(url, stream=True)
        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

    def get_json_from_url(self, url):
        """
        Récupère et retourne le contenu JSON d'une API.
        Si la requête échoue, retourne None.
        """
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        return None

    def handle_cookies(self, url):
        """
        Effectue une requête GET en gérant les cookies via une session.
        Retourne les cookies de la session.
        """
        session = requests.Session()
        response = session.get(url)
        return session.cookies

    def get_status_code(self, url):
        """
        Retourne le code d'état HTTP d'une URL.
        """
        response = requests.get(url)
        return response.status_code

    def check_url_exists(self, url):
        """
        Vérifie si une URL existe en renvoyant True si le code d'état est 200, False sinon.
        """
        response = requests.head(url)
        return response.status_code == 200

    # === Extraction de données avec BeautifulSoup ===

    def parse_html(self, html_content):
        """
        Analyse le contenu HTML d'une page avec BeautifulSoup.
        Retourne l'objet BeautifulSoup correspondant.
        """
        soup = BeautifulSoup(html_content, 'html.parser')
        return soup

    def get_all_links(self, soup):
        """
        Récupère tous les liens (balises <a>) d'une page web.
        """
        return [a['href'] for a in soup.find_all('a', href=True)]

    def get_all_images(self, soup):
        """
        Récupère toutes les balises <img> d'une page web.
        """
        return [img['src'] for img in soup.find_all('img', src=True)]

    def get_text_from_html(self, soup):
        """
        Extrait et retourne tout le texte brut d'une page HTML.
        """
        return soup.get_text()

    def get_element_by_id(self, soup, element_id):
        """
        Trouve et retourne un élément HTML par son identifiant (id).
        """
        return soup.find(id=element_id)

    def get_elements_by_class(self, soup, class_name):
        """
        Récupère tous les éléments avec une classe CSS donnée.
        """
        return soup.find_all(class_=class_name)

    def get_table_data(self, soup):
        """
        Extrait les données d'un tableau HTML (balises <table>).
        Retourne une liste de listes représentant les lignes et colonnes du tableau.
        """
        table = soup.find('table')
        if not table:
            return None
        rows = table.find_all('tr')
        table_data = []
        for row in rows:
            cols = row.find_all(['td', 'th'])
            table_data.append([col.get_text().strip() for col in cols])
        return table_data

    def get_meta_description(self, soup):
        """
        Récupère la meta description (balise <meta name="description">) d'une page web.
        """
        meta = soup.find('meta', attrs={'name': 'description'})
        return meta['content'] if meta else None

    def get_meta_keywords(self, soup):
        """
        Récupère la meta keywords (balise <meta name="keywords">) d'une page web.
        """
        meta = soup.find('meta', attrs={'name': 'keywords'})
        return meta['content'] if meta else None

    def get_title(self, soup):
        """
        Récupère le titre de la page (balise <title>).
        """
        title_tag = soup.find('title')
        return title_tag.get_text() if title_tag else None

    def get_headers(self, soup):
        """
        Récupère tous les titres de la page (balises <h1> à <h6>).
        """
        headers = []
        for i in range(1, 7):
            headers.extend([header.get_text() for header in soup.find_all(f'h{i}')])
        return headers

    def find_elements_by_tag(self, soup, tag_name):
        """
        Récupère tous les éléments d'une page web avec un nom de balise spécifique.
        """
        return soup.find_all(tag_name)

