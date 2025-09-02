from pages.BasePage import BasePage
from pages.LoginPage import LoginPage


class RegisterPage(BasePage):
    """RegisterPage - Child class of BasePage
                Contains locators and WebDriver operations performed on RegisterPage."""

    def __init__(self, driver):
        super().__init__(driver)

    """Locators"""

    Sign_up_header_xpath = "//h2[normalize-space()='Sign Up']"
    login_button_register_page_xpath = "//a[normalize-space()='Login']"
    fullname_id = "name"
    email_address_id = "email"
    password_id = "password"
    mobile_number_id = "mobileNumber"
    sign_up_button_id = "signup-btn"

    """Methods on RegisterPage"""

    def sign_in_from_sign_up(self):
        self.element_click("login_button_register_page_xpath", self.login_button_register_page_xpath)
        expected_url = "https://www.guvi.in/sign-in/"
        actual_url = self.get_current_url()
        if expected_url == actual_url:
            self.logger.info("****** Successfully landed on Login page upon clicking Login from Register page *****")
        else:
            self.logger.error("****** URL does not match *****")
        return LoginPage(self.driver)
