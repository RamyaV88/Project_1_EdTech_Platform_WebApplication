
from selenium.common import TimeoutException

from pages.HomePage import HomePage
from testcases.basetest import BaseTest


class TestDobbyAsst(BaseTest):

    # Test Case 9 - To Validate the Presence of Dobby Guvi Assistant on Home Page

    def test_dobby_asst(self):
        self.logger.info("****** Test Case-9 - Validation of Dobby Guvi Assistant Started *****")
        home_page = HomePage(self.driver)
        try:
            if home_page.is_displayed_dobby_asst():
                self.logger.info("****** Verified the Presence of Dobby Guvi Assistant ******")
                if home_page.is_displayed_dobby_asst_msg():
                    self.logger.info("****** Verified the Presence of Dobby Guvi Assistant Message ******")
            else:
                self.logger.info("****** Dobby Guvi Assistant not found ******")
        except TimeoutException:
            print("Dobby Guvi Assistant not found within the specified time.")
        finally:
            self.logger.info("****** Test Case-9 - Validation of Dobby Guvi Assistant Completed ******")
