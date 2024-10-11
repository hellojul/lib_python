from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Function to initialize the Chrome WebDriver
def init_chrome_driver(executable_path):
    """
    Initializes the Chrome WebDriver and returns the driver instance.
    Requires the path to the ChromeDriver executable.
    """
    service = ChromeService(executable_path=executable_path)
    driver = webdriver.Chrome(service=service)
    return driver

# Function to navigate to a URL
def navigate_to_url(driver, url):
    """
    Navigates the browser to the specified URL.
    """
    driver.get(url)

# Function to find an element by CSS selector and click on it
def click_element(driver, css_selector):
    """
    Finds an element by its CSS selector and clicks on it.
    """
    element = driver.find_element(By.CSS_SELECTOR, css_selector)
    element.click()

# Function to find an element by its CSS selector and type text into it
def input_text(driver, css_selector, text):
    """
    Finds an input element by its CSS selector and types the specified text into it.
    """
    element = driver.find_element(By.CSS_SELECTOR, css_selector)
    element.send_keys(text)

# Function to clear and then type text into an input element
def clear_and_input_text(driver, css_selector, text):
    """
    Clears the existing content of an input field and types new text.
    """
    element = driver.find_element(By.CSS_SELECTOR, css_selector)
    element.clear()
    element.send_keys(text)

# Function to get the text of a specific element
def get_element_text(driver, css_selector):
    """
    Retrieves the text content of a specific element using its CSS selector.
    """
    element = driver.find_element(By.CSS_SELECTOR, css_selector)
    return element.text

# Function to take a screenshot of a webpage
def take_screenshot(driver, file_name):
    """
    Takes a screenshot of the current page and saves it to the specified file.
    """
    driver.save_screenshot(file_name)

# Function to check if an element exists
def element_exists(driver, css_selector):
    """
    Checks if an element exists on the page by its CSS selector.
    Returns True if the element is found, otherwise False.
    """
    try:
        driver.find_element(By.CSS_SELECTOR, css_selector)
        return True
    except:
        return False

# Function to scroll to the bottom of the page
def scroll_to_bottom(driver):
    """
    Scrolls to the bottom of the webpage.
    """
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

# Function to scroll to a specific element
def scroll_to_element(driver, css_selector):
    """
    Scrolls to a specific element on the page.
    """
    element = driver.find_element(By.CSS_SELECTOR, css_selector)
    driver.execute_script("arguments[0].scrollIntoView();", element)

# Function to simulate pressing the ENTER key
def press_enter(driver, css_selector):
    """
    Simulates pressing the ENTER key on a specific input field.
    """
    element = driver.find_element(By.CSS_SELECTOR, css_selector)
    element.send_keys(Keys.ENTER)

# Function to close the browser session
def close_browser(driver):
    """
    Closes the current browser session.
    """
    driver.quit()

# Function to wait for a specific element to be clickable
def wait_for_element(driver, css_selector, timeout=10):
    """
    Waits for a specific element to be clickable before interacting with it.
    Uses WebDriverWait for better stability in dynamic web pages.
    """
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    
    WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))

# Function to capture full page screenshot
def capture_full_page_screenshot(driver, file_name):
    """
    Captures a screenshot of the full webpage (including scrollable content).
    """
    total_height = driver.execute_script("return document.body.scrollHeight")
    driver.set_window_size(1920, total_height)
    driver.save_screenshot(file_name)

# Function to get the page title
def get_page_title(driver):
    """
    Retrieves the title of the current webpage.
    """
    return driver.title

# Function to refresh the current webpage
def refresh_page(driver):
    """
    Refreshes the current webpage.
    """
    driver.refresh()

