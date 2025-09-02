from pages.HomePage import HomePage
from pages.RegisterPage import RegisterPage
from testcases.basetest import BaseTest


class TestSignInSignUpButton(BaseTest):

    # Test Case 5 - To verify navigation to the Sign-In page via the Sign-Up button.

    def test_sign_up_button_visibility(self):
        self.logger.info("****** Test Case-5 : To Test Sign In Via Sign-Up Button Started *****")
        home_page = HomePage(self.driver)
        if home_page.is_sign_up_displayed() and home_page.is_sign_up_enabled():
            self.logger.info("****** Sign-Up Button Displayed and Enabled *****")
            home_page.click_on_sign_up_button()
            self.logger.info("****** Successfully landed on Register Page *****")
            register_page = RegisterPage(self.driver)
            register_page.sign_in_from_sign_up()

        self.logger.info("****** Test Case-5 : Sign In Via Sign-Up Button Completed *****")
