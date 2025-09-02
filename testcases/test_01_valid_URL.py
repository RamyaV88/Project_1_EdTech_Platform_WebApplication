from pages.HomePage import HomePage
from testcases.basetest import BaseTest


class TestValidURL(BaseTest):

    def test_valid_url_loading(self):
        self.logger.info("****** Test Case-1 : TestValidURL Started *****")
        home_page = HomePage(self.driver)
        home_page.verify_successful_page_loading()
        self.logger.info("****** Test Case-1 : TestValidURL Completed *****")
