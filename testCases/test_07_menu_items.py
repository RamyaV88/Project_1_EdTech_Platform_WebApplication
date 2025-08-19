from utilities.customLogger import LogGen
from pageObjects.HomeMenuPage import HomeMenuPage


class TestMenuItems:
    logger = LogGen.loggen()

# Test Case 8 - To Validate Display and Navigation of Courses on Home Page

    def test_courses(self, driver):
        self.logger.info("****** Test Case-8 - Validation of Menu Items Started *****")
        self.logger.info("****** Validation of Courses Menu *****")
        self.hp = HomeMenuPage(driver)
        self.hp.click_courses()
        self.logger.info("****** Courses visible on menu bar *****")
        self.logger.info("****** Clicking on Courses *****")
        assert driver.current_url == self.hp.exp_course_url

# Test Case to Validate Display of LIVE Classes on Home Page

    def test_live_classes(self, driver):
        self.logger.info("****** Validation of LIVE Classes Menu *****")
        self.hp = HomeMenuPage(driver)
        self.hp.click_live_classes()
        self.logger.info("****** LIVE Classes visible on menu bar *****")
        self.logger.info("****** Clicking on LIVE Classes *****")

# Test Case to Validate Practice of Courses on Home Page

    def test_practice(self, driver):
        self.logger.info("****** Validation of Practice Menu *****")
        self.hp = HomeMenuPage(driver)
        self.hp.click_practice()
        self.logger.info("****** Practice visible on menu bar *****")
        self.logger.info("****** Clicking on Practice *****")

# Test Case to Validate Resources of Courses on Home Page

    def test_resources(self, driver):
        self.logger.info("****** Validation of Resources Menu  *****")
        self.hp = HomeMenuPage(driver)
        self.hp.click_resources()
        self.logger.info("****** Resources visible on menu bar *****")
        self.logger.info("****** Clicking on Resources *****")

#Test Case to Validate Products of Courses on Home Page

    def test_products(self, driver):
        self.logger.info("****** Validation of Products Menu  *****")
        self.hp = HomeMenuPage(driver)
        self.hp.click_products()
        self.logger.info("****** Products visible on menu bar *****")
        self.logger.info("****** Clicking on Products *****")
        self.logger.info("****** Test Case-8 - Validation of Menu Items Completed *****")
