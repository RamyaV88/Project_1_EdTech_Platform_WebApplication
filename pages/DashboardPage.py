from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.BasePage import BasePage


class DashboardPage(BasePage):
    """DashboardPage - Child class of BasePage
        Contains locators and WebDriver operations performed on Dashboard Page."""

    def __init__(self, driver):
        super().__init__(driver)

    """Locators"""

    dialog_box_id = "weekly-rewards-popup"
    dialog_box_later_button_xpath = "//button[normalize-space()='Later']"
    dropdown_button_xpath = "//div[@id='dropdown_title']"
    sign_out_button_xpath = "//*[contains(text(), 'Sign Out')]"

    def click_sign_out(self):
        """Method to click on sign out button on Dashboard Page"""
        # Before performing logout functionality explicit wait of 10 seconds is used to load the dropdown elements on the DOM
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.dropdown_button_xpath))).click()
        self.logger.info("****** Clicking on Logout button *****")
        self.driver.find_element(By.XPATH, self.sign_out_button_xpath).click()
