from pages.HomePage import HomePage
from testcases.basetest import BaseTest


class TestMenuItems(BaseTest):

    # Test Case 8 - To Validate Display and Navigation of Courses Menu on Home Page

    def test_courses(self):
        self.logger.info("****** Test Case-8 - Validation of Menu Items Started *****")
        self.logger.info("****** Validation of Courses Menu *****")
        home_page = HomePage(self.driver)
        home_page.click_on_courses()

    # Test Case to Validate Display of LIVE Classes Menu on Home Page

    def test_live_classes(self):
        self.logger.info("****** Validation of Courses Menu *****")
        home_page = HomePage(self.driver)
        home_page.click_on_live_classes()

    # Test Case to Validate Practice Menu on Home Page

    def test_practice(self):
        self.logger.info("****** Validation of Practice Menu *****")
        home_page = HomePage(self.driver)
        home_page.click_on_practice()

    # Test Case to Validate Resources Menu on Home Page

    def test_resources(self):
        self.logger.info("****** Validation of Resources Menu  *****")
        home_page = HomePage(self.driver)
        home_page.click_on_resources()

    # Test Case to Validate Products Menu on Home Page

    def test_products(self):
        self.logger.info("****** Validation of Products Menu  *****")
        home_page = HomePage(self.driver)
        home_page.click_on_products()
        self.logger.info("****** Test Case-8 - Validation of Menu Items Completed *****")
