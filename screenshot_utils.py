import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time

# Function to take a screenshot of the entire screen
def take_screenshot(file_name):
    """
    Takes a screenshot of the entire screen and saves it to the specified file.
    """
    screenshot = pyautogui.screenshot()
    screenshot.save(file_name)

# Function to take a screenshot of a specific region of the screen
def take_screenshot_region(file_name, region):
    """
    Takes a screenshot of a specific region of the screen and saves it to the specified file.
    `region` should be a tuple (left, top, width, height).
    """
    screenshot = pyautogui.screenshot(region=region)
    screenshot.save(file_name)

# Function to initialize a Selenium WebDriver for Chrome
def init_chrome_driver(executable_path):
    """
    Initializes a Selenium Chrome WebDriver and returns the driver instance.
    Requires the path to the ChromeDriver executable.
    """
    service = ChromeService(executable_path=executable_path)
    driver = webdriver.Chrome(service=service)
    return driver

# Function to take a screenshot of the visible part of a webpage
def take_webpage_screenshot(driver, url, file_name):
    """
    Navigates to a webpage using the WebDriver and takes a screenshot of the visible part of the page.
    Saves the screenshot to the specified file.
    """
    driver.get(url)
    time.sleep(2)  # Wait for the page to load
    driver.save_screenshot(file_name)

# Function to take a full-page screenshot (entire scrollable area) in a webpage
def take_full_page_screenshot(driver, url, file_name):
    """
    Takes a full-page screenshot of a webpage (including the scrollable area) using the WebDriver.
    """
    driver.get(url)
    time.sleep(2)  # Wait for the page to load

    # Adjust window size to capture the full page
    total_height = driver.execute_script("return document.body.scrollHeight")
    driver.set_window_size(1920, total_height)  # Width is fixed, height is set dynamically

    driver.save_screenshot(file_name)

# Function to close the WebDriver session
def close_driver(driver):
    """
    Closes the WebDriver session.
    """
    driver.quit()

# Function to take a screenshot of a specific element on a webpage
def take_element_screenshot(driver, url, element_selector, file_name):
    """
    Navigates to a webpage, finds an element by its CSS selector, and takes a screenshot of that element.
    """
    driver.get(url)
    time.sleep(2)  # Wait for the page to load
    element = driver.find_element(By.CSS_SELECTOR, element_selector)
    element.screenshot(file_name)

