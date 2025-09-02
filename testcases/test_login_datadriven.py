import time

from pages.DashboardPage import DashboardPage
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from testcases.basetest import BaseTest
from utilities import excel_utils


class TestLoginDataDriven(BaseTest):
    path = ".//testdata/login_testdata.xlsx"

    # Test case to Verify Data Driven Login Functionality test with Valid and Invalid credentials from an Excel file.

    def test_login_data_driven(self):
        self.logger.info("****** Verifying Login - Data Driven Login Started *****")
        home_page = HomePage(self.driver)
        home_page.click_on_login_button()
        self.rows = excel_utils.get_row_count(self.path, 'Sheet1')
        print("Number of rows", self.rows)
        status_list = []

        for r in range(2, self.rows + 1):
            self.email = excel_utils.read_data(self.path, 'Sheet1', r, 1)
            self.password = excel_utils.read_data(self.path, 'Sheet1', r, 2)
            self.exp_login = excel_utils.read_data(self.path, 'Sheet1', r, 3)

            login_page = LoginPage(self.driver)
            login_page.login_to_application(self.email, self.password)
            time.sleep(2)
            actual_title = self.driver.title
            expected_title = "GUVI | courses"
            dashboard_page = DashboardPage(self.driver)
            if actual_title == expected_title:
                if self.exp_login == "Yes":
                    self.logger.info("Test data is Passed")
                    dashboard_page.click_sign_out()
                    status_list.append("Pass")
                elif self.exp_login == "No":
                    self.logger.info("Test data is Failed")
                    dashboard_page.click_sign_out()
                    status_list.append("Fail")

            elif actual_title != expected_title:
                if self.exp_login == "Yes":
                    self.logger.info("Test data is Failed")
                    status_list.append("Fail")
                elif self.exp_login == "No":
                    self.logger.info("Test data is Passed")
                    status_list.append("Pass")
            print("Status list is ", status_list)

        if "Fail" not in status_list:
            self.logger.info("Login check with Data Driven Passed")
            assert True
        else:
            self.logger.error("Login check with Data Driven Failed")
            assert False

        self.logger.info("****** Data Driven Login Completed *****")
