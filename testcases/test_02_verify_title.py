from testcases.basetest import BaseTest


class TestVerifyTitle(BaseTest):

    def test_verify_title(self):
        self.logger.info("****** Test Case-2 : TestVerifyTitle Started *****")
        expected_title = "GUVI | Learn to code in your native language"
        actual_title = self.driver.title
        print(f"Actual title : {actual_title}")
        assert expected_title == actual_title, "Title does not match"
        self.logger.info("****** Test Case-2 : TestVerifyTitle Completed *****")
