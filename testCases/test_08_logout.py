from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TestLogout:
    email = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

# Test Case 10 : To verify Logout button functionality.

    def test_logout(self,driver):
        self.logger.info("****** Test Case - 10 : Logout Functionality Test Started *****")
        self.lp = LoginPage(driver)
        self.lp.click_login_btn()
        self.lp.set_email(self.email)
        self.lp.set_password(self.password)
        self.lp.click_login()
        # After clicking on Login button, explicit wait of 10 seconds is used to load the elements on the DOM
        wait = WebDriverWait(driver, 10)
        elements = wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@id='courses-container']")))
        current_url = driver.current_url
        print(f"Current URL upon Successful login is : {current_url}")
        exp_url = "https://www.guvi.in/courses/?current_tab=myCourses"
    # Checking Current URL with the Expected URL for a successful login using conditional statement
        if current_url == exp_url:
            self.logger.info("****** Login Successful *****")
            self.lp.click_sign_out()
            self.logger.info("****** Logout Successful *****")
        else:
            driver.save_screenshot(".\\screenshots\\" + "test_logout.png")
            self.logger.info("****** Login Failed *****")
        self.logger.info("****** Test Case - 10 : Logout Functionality Test Completed *****")