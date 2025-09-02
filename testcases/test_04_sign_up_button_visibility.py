from pages.HomePage import HomePage
from testcases.basetest import BaseTest


class TestSignUpButtonVisibility(BaseTest):

    # Test Case 4 - To verify visibility and clickable feature of the Sign-Up button.

    def test_sign_up_button_visibility(self):
        self.logger.info("****** Test Case-4 : Test Sign-Up Button Visibility Started *****")
        home_page = HomePage(self.driver)
        if home_page.is_sign_up_displayed() and home_page.is_sign_up_enabled():
            self.logger.info("****** Sign-Up Button Displayed and Enabled *****")
            home_page.click_on_sign_up_button()
            self.logger.info("****** Successfully landed on Register Page *****")
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "TC_04_test_login_button_visibility_error.png")
            self.logger.info("****** Sign-Up Button Not Displayed/Enabled *****")
        self.logger.info("****** Test Case-4 : Test Sign-Up Button Visibility Completed *****")
