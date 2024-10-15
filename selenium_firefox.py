# python3 -m venv .my_env
# pip install selenium
# pip install webdriver-manager
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

# Créer le WebDriver pour Firefox
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

# Ouvrir une page
driver.get("https://www.***.com")


# Fermer le navigateur
driver.quit()

