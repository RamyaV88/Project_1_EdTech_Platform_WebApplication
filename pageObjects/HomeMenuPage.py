from selenium.webdriver.common.by import By

# Home page menu elements are located and functions are defined
class HomeMenuPage:
    drp_courses_css = ".⭐️rwl3jt-0.my-2.cursor-pointer.ml-2.mr-6.text-base.font-normal.text-gray-500.text-nowrap"
    drp_LIVE_classes_id = 'liveclasseslink'
    drp_Practice_id = 'practiceslink'
    drp_Resources_id = 'resourceslink'
    drp_Products_id = 'solutionslink'
    exp_course_url = "https://www.guvi.in/courses/?current_tab=paidcourse"

    def __init__(self,driver):
        self.driver = driver

    def click_courses(self):
        self.driver.find_element(By.CSS_SELECTOR, self.drp_courses_css).click()

    def click_live_classes(self):
        self.driver.find_element(By.ID, self.drp_LIVE_classes_id).click()

    def click_practice(self):
        self.driver.find_element(By.ID, self.drp_Practice_id).click()

    def click_resources(self):
        self.driver.find_element(By.ID, self.drp_Resources_id).click()

    def click_products(self):
        self.driver.find_element(By.ID, self.drp_Products_id).click()
