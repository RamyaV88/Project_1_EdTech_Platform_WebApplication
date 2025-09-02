from pages.HomePage import HomePage
from testcases.basetest import BaseTest


class TestValidLogin(BaseTest):

    # Test Case 6 - To verify login functionality with valid credentials.

    def test_valid_login(self):
        self.logger.info("****** Test case - 6 : Login Functionality test Started *****")
        self.logger.info("****** Verifying Login with Valid credentials *****")
        home_page = HomePage(self.driver)
        login_page = home_page.click_on_login_button()
        login_page.login_to_application(self.email, self.password)
        login_page.verify_successful_login()
        self.logger.info("****** Test case - 6 : Login Functionality test Completed *****")
