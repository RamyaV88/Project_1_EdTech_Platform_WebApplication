from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utilities.customLogger import LogGen


class BasePage:
    """Base class for all page objects containing common WebDriver operations.

    This class provides standardized methods for interacting with web elements
    using explicit waits to ensure reliable test execution."""
    EXPLICIT_WAIT = 10

    def __init__(self, driver):
        """Initialize the base page with WebDriver instance."""
        self.driver = driver
        self.wait = WebDriverWait(driver, self.EXPLICIT_WAIT)  # Default wait instance

    def enter_text(self, text, locator_name, locator_value):
        """Enter text in element"""
        element = self.get_element(locator_name, locator_value)
        element.click()
        element.clear()
        element.send_keys(text)

    def element_click(self, locator_name, locator_value):
        """Perform click action on an element"""
        element = self.get_element(locator_name, locator_value)
        element.click()

    def check_display_status_of_element(self, locator_name, locator_value):
        """Check the display of an element"""
        element = self.get_element(locator_name, locator_value)
        return element.is_displayed()

    def check_enabled_status_of_element(self, locator_name, locator_value):
        """Check the display of an element"""
        element = self.get_element(locator_name, locator_value)
        return element.is_enabled()

    def retrieve_element_text(self, locator_name, locator_value):
        """Retrieve text of an element"""
        element = self.get_element(locator_name, locator_value)
        return element.text

    def get_element(self, locator_name, locator_value):
        """Find element with locator names"""
        element = None
        if locator_name.endswith("_id"):
            element = self.driver.find_element(By.ID, locator_value)
        elif locator_name.endswith("_name"):
            element = self.driver.find_element(By.NAME, locator_value)
        elif locator_name.endswith("_class_name"):
            element = self.driver.find_element(By.CLASS_NAME, locator_value)
        elif locator_name.endswith("_link_text"):
            element = self.driver.find_element(By.LINK_TEXT, locator_value)
        elif locator_name.endswith("_xpath"):
            element = self.driver.find_element(By.XPATH, locator_value)
        elif locator_name.endswith("_css"):
            element = self.driver.find_element(By.CSS_SELECTOR, locator_value)
        return element

    def get_current_url(self):
        """Get current URL"""
        return self.driver.current_url

    def wait_for_elements(self, locator):
        """Wait for elements to load on the DOM"""
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, locator)))
        self.logger.info("****** Page completely loaded ******")

    """Creating a method for logger object"""
    logger = LogGen.loggen()
