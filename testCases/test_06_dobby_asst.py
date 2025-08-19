from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen


class TestDobbyAsst:
    logger = LogGen.loggen()

# Test Case 9 - To Validate the Presence of Dobby Guvi Assistant on Home Page

    def test_dobby_asst(self,driver):
        self.logger.info("****** Test Case-9 - Validation of Dobby Guvi Assistant Started *****")
        self.logger.info("****** Verifying the Presence of Dobby Guvi Assistant in Login Page *****")
        self.lp = LoginPage(driver)
        wait = WebDriverWait(driver, timeout=15, poll_frequency=0.5,
                             ignored_exceptions=[NoSuchElementException])
        dobby_asst = wait.until(EC.visibility_of_element_located((By.ID, 'ym-auto-pop-up-content')))
        try:
            if dobby_asst.is_displayed():
                print("Dobby Guvi Assistant is displayed on DOM.")
                self.logger.info("****** Verified the Presence of Dobby Guvi Assistant in Login Page *****")
            else:
                self.logger.info("****** Dobby Guvi Assistant not found in Login Page *****")
                print("Dobby Guvi Assistant is not displayed on DOM.")
        except TimeoutException:
            print("Dobby Guvi Assistant Element not found within the specified time.")
        finally:
            self.logger.info("****** Test Case-9 - Validation of Dobby Guvi Assistant Completed *****")
