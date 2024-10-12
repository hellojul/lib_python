from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class BrowserAutomation:
    """
    A class for automating browser tasks using Selenium WebDriver.
    """

    def __init__(self, executable_path):
        """
        Initializes the Chrome WebDriver.
        Requires the path to the ChromeDriver executable.
        """
        service = ChromeService(executable_path=executable_path)
        self.driver = webdriver.Chrome(service=service)

    def navigate_to_url(self, url):
        """
        Navigates the browser to the specified URL.
        """
        self.driver.get(url)

    def click_element(self, css_selector):
        """
        Finds an element by its CSS selector and clicks on it.
        """
        element = self.driver.find_element(By.CSS_SELECTOR, css_selector)
        element.click()

    def input_text(self, css_selector, text):
        """
        Finds an input element by its CSS selector and types the specified text into it.
        """
        element = self.driver.find_element(By.CSS_SELECTOR, css_selector)
        element.send_keys(text)

    def clear_and_input_text(self, css_selector, text):
        """
        Clears the existing content of an input field and types new text.
        """
        element = self.driver.find_element(By.CSS_SELECTOR, css_selector)
        element.clear()
        element.send_keys(text)

    def get_element_text(self, css_selector):
        """
        Retrieves the text content of a specific element using its CSS selector.
        """
        element = self.driver.find_element(By.CSS_SELECTOR, css_selector)
        return element.text

    def element_exists(self, css_selector):
        """
        Checks if an element exists on the page by its CSS selector.
        Returns True if the element is found, otherwise False.
        """
        try:
            self.driver.find_element(By.CSS_SELECTOR, css_selector)
            return True
        except:
            return False

    def scroll_to_bottom(self):
        """
        Scrolls to the bottom of the webpage.
        """
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    def scroll_to_element(self, css_selector):
        """
        Scrolls to a specific element on the page.
        """
        element = self.driver.find_element(By.CSS_SELECTOR, css_selector)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def press_enter(self, css_selector):
        """
        Simulates pressing the ENTER key on a specific input field.
        """
        element = self.driver.find_element(By.CSS_SELECTOR, css_selector)
        element.send_keys(Keys.ENTER)

    def take_screenshot(self, file_name):
        """
        Takes a screenshot of the current page and saves it to the specified file.
        """
        self.driver.save_screenshot(file_name)

    def capture_full_page_screenshot(self, file_name):
        """
        Captures a screenshot of the full webpage (including scrollable content).
        """
        total_height = self.driver.execute_script("return document.body.scrollHeight")
        self.driver.set_window_size(1920, total_height)
        self.driver.save_screenshot(file_name)

    def get_page_title(self):
        """
        Retrieves the title of the current webpage.
        """
        return self.driver.title

    def refresh_page(self):
        """
        Refreshes the current webpage.
        """
        self.driver.refresh()

    def close_browser(self):
        """
        Closes the current browser session.
        """
        self.driver.quit()

    def wait_for_element(self, css_selector, timeout=10):
        """
        Waits for a specific element to be clickable before interacting with it.
        """
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))

    def get_cookies(self):
        """
        Retrieves all cookies from the current session.
        """
        return self.driver.get_cookies()

    def add_cookie(self, cookie_dict):
        """
        Adds a cookie to the browser session.
        """
        self.driver.add_cookie(cookie_dict)

    def delete_all_cookies(self):
        """
        Deletes all cookies from the current session.
        """
        self.driver.delete_all_cookies()

    def get_window_handles(self):
        """
        Retrieves the window handles for all open tabs.
        """
        return self.driver.window_handles

    def switch_to_window(self, handle):
        """
        Switches to a specific window or tab by its handle.
        """
        self.driver.switch_to.window(handle)

    def go_back(self):
        """
        Navigates back to the previous page in the browser history.
        """
        self.driver.back()

    def go_forward(self):
        """
        Navigates forward to the next page in the browser history.
        """
        self.driver.forward()

    def get_elements(self, css_selector):
        """
        Returns a list of elements that match the given CSS selector.
        """
        return self.driver.find_elements(By.CSS_SELECTOR, css_selector)


