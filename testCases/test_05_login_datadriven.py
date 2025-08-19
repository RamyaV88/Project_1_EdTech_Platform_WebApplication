import time
from pageObjects.LoginPage import LoginPage
from utilities import excel_utils
from utilities.customLogger import LogGen


class TestLoginDataDriven:
    path = ".//testdata/login_testdata.xlsx"
    logger = LogGen.loggen()

# Test case to Verify Data Driven Login Functionality test with Valid and Invalid credentials from an Excel file.

    def test_login_data_driven(self,driver):
        self.logger.info("****** Verifying Login - Data Driven Login Started *****")
        self.lp = LoginPage(driver)
        self.lp.click_login_btn()

        self.rows = excel_utils.getRowCount(self.path, 'Sheet1')
        print("Number of rows", self.rows)
        status_list = []

        for r in range(2, self.rows+1):
            self.email = excel_utils.readData(self.path,'Sheet1',r,1)
            self.password = excel_utils.readData(self.path, 'Sheet1', r, 2)
            self.exp_login = excel_utils.readData(self.path, 'Sheet1', r, 3)

            self.lp.set_email(self.email)
            self.lp.set_password(self.password)
            self.lp.click_login()
            time.sleep(2)

            actual_title = driver.title
            expected_title = "GUVI | courses"

            if actual_title == expected_title:
                if self.exp_login == "Yes":
                    self.logger.info("Test data is Passed")
                    self.lp.click_sign_out()
                    status_list.append("Pass")
                elif self.exp_login == "No":
                    self.logger.info("Test data is Failed")
                    self.lp.click_sign_out()
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

        self.logger.info("****** Verifying Login - Data Driven Login Completed *****")


