from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLogin:
    email = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

# Test Case 6 - To verify login functionality with valid credentials.

    def test_valid_login(self,driver):
        self.logger.info("****** Test case - 6 : Login Functionality test Started *****")
        self.logger.info("****** Verifying Login with Valid credentials *****")
        self.lp = LoginPage(driver)
        self.lp.click_login_btn()
        self.lp.set_email(self.email)
        self.lp.set_password(self.password)
        self.lp.click_login()
        # After clicking on Login button, explicit wait of 10 seconds is used to load the elements on the DOM
        wait = WebDriverWait(driver, 10)
        elements = wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@id='courses-container']")))
        actual_title = driver.title
        print(f"Title is : {actual_title}")
        if actual_title=="GUVI | courses":
            assert True
            self.logger.info("****** Login Successful *****")
        else:
            driver.save_screenshot(".\\screenshots\\" + "test_valid_login.png")
            self.logger.error("****** Login Failed *****")
        self.logger.info("****** Test case - 6 : Login Functionality test Completed *****")

