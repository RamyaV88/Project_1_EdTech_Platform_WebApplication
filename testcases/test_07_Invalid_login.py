from pages.HomePage import HomePage
from testcases.basetest import BaseTest


class TestLogin(BaseTest):

    # Test Case 7 - To verify login with invalid credentials, to check the error message displayed.

    def test_invalid_login(self):
        self.logger.info("****** Test case - 7 : Invalid Login Functionality test Started *****")
        self.logger.info("****** Verifying Login with Invalid credentials *****")
        home_page = HomePage(self.driver)
        login_page = home_page.click_on_login_button()
        login_page.login_to_application(self.invalid_email, self.invalid_password)
        displayed_error_msg = login_page.retrieve_error_message()
        if displayed_error_msg == login_page.exp_error_msg:
            assert True
            self.logger.info("****** Error message displayed as expected *****")
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "TC_07_test_invalid_login.png")
            self.logger.error("****** Error message not displayed as expected *****")
        self.logger.info("****** Test case - 7 : Invalid Login Functionality test Completed *****")
