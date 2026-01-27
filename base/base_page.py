from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def click(self, locator):
        """Click element with explicit wait"""
        self.wait.until(EC.element_to_be_clickable(locator)).click()
    
    def send_keys(self, locator, text):
        """Send keys to element with explicit wait"""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator):
        """Get text of element with explicit wait"""
        return self.wait.until(EC.visibility_of_element_located(locator)).text
    
    def is_visible(self, locator):
        """Check if element is visible"""
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False
    
    def is_present(self, locator):
        """Check if element is present in DOM"""
        try:
            self.driver.find_element(*locator)
            return True
        except:
            return False
    
    def get_title(self):
        """Get page title"""
        return self.driver.title
    
    def get_current_url(self):
        """Get current URL"""
        return self.driver.current_url
    
    def scroll_to_element(self, locator):
        """Scroll to specific element"""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
    
    def wait_for_page_load(self):
        """Wait for page to completely load"""
        self.wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")
