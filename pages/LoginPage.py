from pages.BasePage import BasePage


class LoginPage(BasePage):
    """LoginPage - Child class of BasePage
            Contains locators and WebDriver operations performed on LoginPage."""

    """Locators"""

    textbox_email_id = "email"
    textbox_password_id = "password"
    login_button_xpath = "//a[@id='login-btn']"
    login_button_id = "login-btn"
    btn_dropdown_xpath = "//div[@id='dropdown_title']"
    btn_sign_out_xpath = "//*[contains(text(), 'Sign Out')]"
    btn_signup_xpath = "//a[contains (text(), 'Sign up')]"
    btn_login_signup_xpath = "//a[contains (text(), 'Login')]"
    courses_container_xpath = "//div[@ id = 'courses-container']"
    err_msg_box_xpath = "//div[@class='invalid-feedback']"
    error_msg_xpath = "//div[@class='invalid-feedback is-invalid']"
    exp_error_msg = "Incorrect Email or Password"

    def __init__(self, driver):
        super().__init__(driver)

    """Methods on LoginPage"""

    def set_email(self, email):
        """Method to enter text on email element on LoginPage"""
        self.enter_text(email, "textbox_email_id", self.textbox_email_id)

    def set_password(self, password):
        """Method to enter password on the element on LoginPage"""
        self.enter_text(password, "textbox_password_id", self.textbox_password_id)

    def click_login(self):
        """Method to click on login button on the LoginPage"""
        self.element_click("login_button_id", self.login_button_id)

    def login_to_application(self, email, password):
        """Method to click on login on entering email, password and clicking login button on the LoginPage"""
        self.set_email(email)
        self.set_password(password)
        self.click_login()

    def verify_successful_login(self):
        """Method to verify successful login on entering email, password and clicking login button on the LoginPage,
        asserting the expected title with actual title displayed"""
        self.wait_for_elements(self.courses_container_xpath)
        expected_title = 'GUVI | courses'
        actual_title = self.driver.title
        print(f"Actual title of webpage: {actual_title}")
        if expected_title == actual_title:
            self.logger.info("****** Login Successful, landed on Dashboard page *****")
        else:
            self.logger.error("****** Login Failed *****")

    def retrieve_error_message(self):
        """Method to retrieve error message text on the LoginPage for Invalid login credentials"""
        return self.retrieve_element_text("error_msg_xpath", self.error_msg_xpath)
