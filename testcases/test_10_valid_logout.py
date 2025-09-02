from pages.DashboardPage import DashboardPage
from pages.HomePage import HomePage
from testcases.basetest import BaseTest


class TestValidLogout(BaseTest):

    # Test Case 10 - To verify logout functionality with valid credentials.

    def test_valid_logout(self):
        self.logger.info("****** Test case - 10 : Logout Functionality test Started *****")
        self.logger.info("****** Verifying Login with Valid credentials *****")
        home_page = HomePage(self.driver)
        login_page = home_page.click_on_login_button()
        login_page.login_to_application(self.email, self.password)
        login_page.verify_successful_login()
        dashboard_page = DashboardPage(self.driver)
        dashboard_page.click_sign_out()
        self.logger.info("****** Test case - 10 : Logout Functionality test Completed *****")
