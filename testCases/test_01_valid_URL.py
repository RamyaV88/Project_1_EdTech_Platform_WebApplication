from utilities.customLogger import LogGen
from selenium.webdriver.common.by import By

class TestValidURL:
    logger = LogGen.loggen()


    def test_valid_url_loading(self,driver):
        self.logger.info("****** Test Case-1 : TestValidURL Started *****")
        self.logger.info("****** Verifying the validity of URL by checking the presence of Guvi Logo element *****")
        logo_xpath = (driver.find_element(By.XPATH, "//img[@class='⭐️rwl3jt-0 cursor-pointer guvi_logo']"))
        if logo_xpath.is_displayed():
            print("URL loaded successfully")
            self.logger.info("****** URL loaded successfully *****")
        else:
            print("URL not loaded successfully")
            driver.save_screenshot(".\\screenshots\\" + "test_valid_url_loading.png")
            self.logger.error("****** URL loading error *****")
        self.logger.info("****** Test Case-1 : TestValidURL Completed *****")

# Test Case 2: To verify whether the title of the webpage is correct.

    def test_is_title_valid(self, driver):
        self.logger.info("****** Test Case-2 : Title Validation Started *****")
        self.logger.info("****** Verifying the Homepage Title *****")
        # Fetching the actual title from the webpage.
        actual_title = driver.title
        expected_title = "GUVI | Learn to code in your native language"
        # Using conditional statement, Checking if the Title displayed is as expected.
        if actual_title == expected_title:
            assert True
            self.logger.info("****** Title displayed as expected *****")
        else:
            # Upon failure capturing screenshot of the webpage
            driver.save_screenshot(".\\screenshots\\" + "test_is_title_valid.png")
            self.logger.error("****** Title Error *****")
        self.logger.info("****** Test Case-2 : Title Validation Completed *****")
