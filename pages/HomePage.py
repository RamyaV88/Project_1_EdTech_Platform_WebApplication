from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.BasePage import BasePage
from pages.LoginPage import LoginPage
from pages.RegisterPage import RegisterPage


class HomePage(BasePage):
    """HomePage - Child class of BasePage
            Contains locators and WebDriver operations performed on HomePage."""

    def __init__(self, driver):
        super().__init__(driver)

    """Locators"""

    logo_xpath = "//img[@class='⭐️rwl3jt-0 cursor-pointer guvi_logo']"
    drp_courses_css = ".⭐️rwl3jt-0.my-2.cursor-pointer.ml-2.mr-6.text-base.font-normal.text-gray-500.text-nowrap"
    drp_LIVE_classes_id = 'liveclasseslink'
    drp_Practice_id = 'practiceslink'
    drp_Resources_id = 'resourceslink'
    drp_Products_id = 'solutionslink'
    login_button_xpath = "//a[@id='login-btn']"
    sign_up_button_xpath = "//a[contains (text(),'Sign up')]"
    live_class_placement_xpath = "//span[normalize-space()='Live Classes + Placement Guidance']"
    live_classes_dropdown_link_xpath = "//p[normalize-space()='IIT-M Pravartak Certified Data Science Program']"
    paid_courses_textbox_xpath = "//div[contains (text(),'Paid Courses')]"
    practice_codekata_xpath = "//p[contains (text(),'CodeKata')]"
    resources_success_stories_xpath = "//a[contains (text(),'Success Stories')]"
    products_hackerkid_xpath = "//p[contains (text(),'HackerKID')]"

    """Methods on HomePage"""

    def click_on_login_button(self):
        """Method to click on login button element on HomePage"""
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()
        assert self.driver.title == "GUVI | Login", "Not directed to Login Page"
        return LoginPage(self.driver)

    def click_on_sign_up_button(self):
        """Method to click on sign up button element on HomePage"""
        self.driver.find_element(By.XPATH, self.sign_up_button_xpath).click()
        expected_url = "https://www.guvi.in/register/"
        assert expected_url == self.get_current_url(), "URL does not match"
        assert self.driver.title == "GUVI | Sign Up", "Not directed to Register Page"
        return RegisterPage(self.driver)

    def is_login_displayed(self):
        """Method to check if login button is displayed"""
        return self.check_display_status_of_element("login_button_xpath", self.login_button_xpath)

    def is_login_enabled(self):
        """Method to check if login button is enabled"""
        return self.check_enabled_status_of_element("login_button_xpath", self.login_button_xpath)

    def is_sign_up_displayed(self):
        """Method to check if sign up button is displayed"""
        return self.check_display_status_of_element("sign_up_button_xpath", self.sign_up_button_xpath)

    def is_sign_up_enabled(self):
        """Method to check if sign up button is enabled"""
        return self.check_enabled_status_of_element("sign_up_button_xpath", self.sign_up_button_xpath)

    def click_on_courses(self):
        """Method to click if courses menu and validate the dropdown"""
        self.element_click("drp_courses_css", self.drp_courses_css)
        self.logger.info("****** Clicked on Courses Menu *****")
        assert self.driver.title == "GUVI | courses", "Not navigated to Courses"
        self.check_display_status_of_element("paid_courses_textbox_xpath", self.paid_courses_textbox_xpath)
        self.logger.info("****** Paid Courses Visible on Page *****")
        return True

    def click_on_live_classes(self):
        """Method to click if live classes menu and validate the dropdown"""
        self.element_click("drp_LIVE_classes_id", self.drp_LIVE_classes_id)
        self.logger.info("****** Clicked on Live Classes Menu *****")
        self.check_display_status_of_element("live_classes_dropdown_link_xpath", self.live_classes_dropdown_link_xpath)
        self.logger.info("****** Live Classes - IIT-M Pravartak Certified Data Science Program Displayed *****")
        return True

    def click_on_practice(self):
        """Method to click if practice menu and validate the dropdown"""
        self.element_click("drp_Practice_id", self.drp_Practice_id)
        self.logger.info("****** Clicked on Practice Menu *****")
        self.check_display_status_of_element("practice_codekata_xpath", self.practice_codekata_xpath)
        self.logger.info("****** Practice - Codekata Displayed *****")
        return True

    def click_on_resources(self):
        """Method to click if resources menu and validate the dropdown"""
        self.element_click("drp_Resources_id", self.drp_Resources_id)
        self.logger.info("****** Clicked on Resources Menu *****")
        self.check_display_status_of_element("resources_success_stories_xpath", self.resources_success_stories_xpath)
        self.logger.info("****** Resources - Success Stories Displayed *****")
        return True

    def click_on_products(self):
        """Method to click if products menu and validate the dropdown"""
        self.element_click("drp_Products_id", self.drp_Products_id)
        self.logger.info("****** Clicked on Products Menu *****")
        self.check_display_status_of_element("products_hackerkid_xpath", self.products_hackerkid_xpath)
        self.logger.info("****** Products - HackerKID Displayed *****")
        return True

    def verify_successful_page_loading(self):
        """Method to validate the successful display of the login page by verifying the logo element and text on the DOM"""
        if self.is_logo_displayed():
            self.logger.info("****** Verifying the validity of URL by checking the presence of Guvi Logo element *****")
            if self.driver.find_element(By.XPATH, self.live_class_placement_xpath).is_displayed():
                self.logger.info(
                    "****** Verifying the validity of URL by checking the presence of Live Class & Placement message *****")
                print("Page Loaded Successfully")
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_valid_page_loading.png")
            print("Page Loading Failed")

    def is_logo_displayed(self):
        """Method to check if logo is displayed"""
        return self.check_display_status_of_element("logo_xpath", self.logo_xpath)

    def is_displayed_dobby_asst(self):
        """Method to check if Guvi dobby assistant element is displayed using fluent wait"""
        wait = WebDriverWait(self.driver, timeout=15, poll_frequency=0.5,
                             ignored_exceptions=[NoSuchElementException])
        dobby_asst = wait.until(EC.visibility_of_element_located((By.ID, 'ym-auto-pop-up-content')))
        return dobby_asst.is_displayed()

    def is_displayed_dobby_asst_msg(self):
        """Method to check if message is displayed on Guvi dobby assistant element using fluent wait"""
        wait = WebDriverWait(self.driver, timeout=15, poll_frequency=0.5,
                             ignored_exceptions=[NoSuchElementException])
        dobby_asst_msg = wait.until(EC.visibility_of_element_located((By.ID, 'ym-auto-pop-up-description')))
        return dobby_asst_msg.is_displayed()
