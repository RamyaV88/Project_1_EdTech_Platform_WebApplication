from pages.HomePage import HomePage
from testcases.basetest import BaseTest


class TestLoginButtonVisibility(BaseTest):

    # Test Case 3 - To verify visibility and clickable feature of the Login button.

    def test_login_button_visibility(self):
        self.logger.info("****** Test Case-3 : Test Login Button Visibility Started *****")
        home_page = HomePage(self.driver)
        if home_page.is_login_displayed() and home_page.is_login_enabled():
            self.logger.info("****** Login Button Displayed and Enabled *****")
            home_page.click_on_login_button()
            self.logger.info("****** Successfully landed on Login Page *****")
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "TC_03_test_login_button_visibility_error.png")
            self.logger.info("****** Login Button Not Displayed/Enabled *****")
        self.logger.info("****** Test Case-3 : Test Login Button Visibility Completed *****")
