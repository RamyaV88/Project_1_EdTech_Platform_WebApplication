from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class TestLogin:
    invalid_email = ReadConfig.getinvalidUseremail()
    invalid_password = ReadConfig.getinvalidPassword()
    logger = LogGen.loggen()

# Test Case 7 - To verify login with invalid credentials, to check the error message displayed.

    def test_invalid_login(self,driver):
        self.logger.info("****** Test case - 7 : Invalid Login Functionality test Started *****")
        self.logger.info("****** Verifying Login with Invalid credentials *****")
        self.lp = LoginPage(driver)
        self.lp.click_login_btn()
        self.lp.set_invalid_email(self.invalid_email)
        self.lp.set_invalid_password(self.invalid_password)
        self.lp.click_login()
        exp_error_msg = "Incorrect Email or Password"
        err_msg_box = driver.find_element(By.XPATH, "//div[@class='invalid-feedback']")
        displayed_error = str(err_msg_box.text)
        print(f"Error message: {displayed_error}")
        if displayed_error == exp_error_msg:
            assert True
            self.logger.info("****** Error message displayed as expected *****")
        else:
            driver.save_screenshot(".\\screenshots\\" + "test_invalid_login.png")
            self.logger.error("****** Error message not displayed as expected *****")
        self.logger.info("****** Test case - 7 : Invalid Login Functionality test Completed *****")
        self.logger.info("****** TestLogin Completed *****")
