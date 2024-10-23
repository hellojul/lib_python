from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
import time

# Initialiser le WebDriver pour Firefox
def init_driver():
    service = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    return driver

# Aller à une URL spécifiée
def navigate_to_url(driver, url):
    driver.get(url)

# Cliquer sur un élément via son sélecteur CSS
def click_element(driver, css_selector):
    element = driver.find_element(By.CSS_SELECTOR, css_selector)
    element.click()

# Saisir du texte dans un champ input
def input_text(driver, css_selector, text):
    element = driver.find_element(By.CSS_SELECTOR, css_selector)
    element.send_keys(text)

# Effacer et saisir du texte dans un champ input
def clear_and_input_text(driver, css_selector, text):
    element = driver.find_element(By.CSS_SELECTOR, css_selector)
    element.clear()
    element.send_keys(text)

# Obtenir le texte d'un élément
def get_element_text(driver, css_selector):
    element = driver.find_element(By.CSS_SELECTOR, css_selector)
    return element.text

# Vérifier si un élément existe
def element_exists(driver, css_selector):
    try:
        driver.find_element(By.CSS_SELECTOR, css_selector)
        return True
    except:
        return False

# Faire défiler la page jusqu'en bas
def scroll_to_bottom(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

# Faire défiler jusqu'à un élément spécifique
def scroll_to_element(driver, css_selector):
    element = driver.find_element(By.CSS_SELECTOR, css_selector)
    driver.execute_script("arguments[0].scrollIntoView();", element)

# Simuler l'appui sur la touche Entrée
def press_enter(driver, css_selector):
    element = driver.find_element(By.CSS_SELECTOR, css_selector)
    element.send_keys(Keys.ENTER)

# Prendre une capture d'écran de la page actuelle
def take_screenshot(driver, file_name):
    driver.save_screenshot(file_name)

# Obtenir le titre de la page
def get_page_title(driver):
    return driver.title

# Actualiser la page
def refresh_page(driver):
    driver.refresh()

# Fermer le navigateur
def close_browser(driver):
    driver.quit()

# Attendre qu'un élément soit cliquable avant d'interagir
def wait_for_element(driver, css_selector, timeout=10):
    WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))

# Obtenir les cookies de la session actuelle
def get_cookies(driver):
    return driver.get_cookies()

# Ajouter un cookie à la session
def add_cookie(driver, cookie_dict):
    driver.add_cookie(cookie_dict)

# Supprimer tous les cookies
def delete_all_cookies(driver):
    driver.delete_all_cookies()

# Récupérer les handles des fenêtres ouvertes
def get_window_handles(driver):
    return driver.window_handles

# Basculer vers une fenêtre spécifique
def switch_to_window(driver, handle):
    driver.switch_to.window(handle)

# Revenir à la page précédente
def go_back(driver):
    driver.back()

# Aller à la page suivante
def go_forward(driver):
    driver.forward()

# Obtenir plusieurs éléments correspondant à un sélecteur CSS
def get_elements(driver, css_selector):
    return driver.find_elements(By.CSS_SELECTOR, css_selector)

# Exécuter un script Javascript dans le navigateur
def execute_js_script(driver, script):
    return driver.execute_script(script)

# Récupérer un attribut spécifique d'un élément
def get_element_attribute(driver, css_selector, attribute_name):
    element = driver.find_element(By.CSS_SELECTOR, css_selector)
    return element.get_attribute(attribute_name)

# Récupérer tous les liens (href) de la page
def get_all_links(driver):
    links = driver.find_elements(By.TAG_NAME, 'a')
    return [link.get_attribute('href') for link in links]

# Récupérer toutes les images (src) de la page
def get_all_images(driver):
    images = driver.find_elements(By.TAG_NAME, 'img')
    return [img.get_attribute('src') for img in images]

# Récupérer le texte de plusieurs éléments avec le même sélecteur
def get_texts_from_elements(driver, css_selector):
    elements = driver.find_elements(By.CSS_SELECTOR, css_selector)
    return [element.text for element in elements]

# Récupérer le contenu d'un tableau HTML
def get_html_table(driver, table_css_selector):
    table = driver.find_element(By.CSS_SELECTOR, table_css_selector)
    rows = table.find_elements(By.TAG_NAME, "tr")
    table_data = []
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")  # Utiliser <th> pour l'en-tête
        row_data = [cell.text for cell in cells]
        table_data.append(row_data)
    return table_data

# Télécharger un fichier via un lien ou un bouton
def download_file(driver, download_link_css_selector):
    element = driver.find_element(By.CSS_SELECTOR, download_link_css_selector)
    element.click()
    # Attendre le téléchargement ou ajouter une vérification si nécessaire

# Récupérer les métadonnées de la page
def get_page_metadata(driver):
    metadata = {
        'title': driver.title,
        'description': get_element_attribute(driver, 'meta[name="description"]', 'content'),
        'keywords': get_element_attribute(driver, 'meta[name="keywords"]', 'content')
    }
    return metadata

# Compter le nombre d'éléments avec un sélecteur CSS donné
def count_elements(driver, css_selector):
    elements = driver.find_elements(By.CSS_SELECTOR, css_selector)
    return len(elements)

