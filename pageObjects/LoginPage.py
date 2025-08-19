from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Login page menu elements are located and functions are defined
class LoginPage:
    btn_login_id = "login-btn"
    textbox_email_id = "email"
    textbox_password_id = "password"
    btn_login_xpath = "//a[@id='login-btn']"
    btn_dropdown_xpath = "//div[@id='dropdown_title']"
    btn_sign_out_xpath = "//*[contains(text(), 'Sign Out')]"
    btn_signup_xpath = "//a[contains (text(), 'Sign up')]"
    btn_login_signup_xpath = "//a[contains (text(), 'Login')]"

    def __init__(self,driver):
        self.driver = driver

    def click_login_btn(self):
        self.driver.find_element(By.ID, self.btn_login_id).click()

    def set_email(self,email):
        self.driver.find_element(By.ID, self.textbox_email_id).clear()
        self.driver.find_element(By.ID, self.textbox_email_id).send_keys(email)

    def set_password(self,password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def set_invalid_email(self,invalid_email):
        self.driver.find_element(By.ID, self.textbox_email_id).clear()
        self.driver.find_element(By.ID, self.textbox_email_id).send_keys(invalid_email)

    def set_invalid_password(self,invalid_password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(invalid_password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()

    def click_sign_out(self):
        # Before performing logout functionality explicit wait of 10 seconds is used to load the dropdown elements on the DOM
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.btn_dropdown_xpath))).click()
        self.driver.find_element(By.XPATH, self.btn_sign_out_xpath).click()

