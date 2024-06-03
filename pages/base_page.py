import time

from selenium.webdriver.common.by import By

from driver import Driver


class BasePage(Driver):
    # declaram constantele ce contin selectorii:(tuple)
    URL = 'https://the-internet.herokuapp.com/login'
    USER_LOC = (By.XPATH, '//input[@name= "username"]')
    PASS_LOC = (By.ID, 'password')
    BUTTON_LOC = (By.XPATH, '//button')
    SECURE_LOC = (By.XPATH, '//h2')

    # definim metodele de interactionare cu elemetele html
    def navigate_to_login(self):
        self.driver.get(self.URL)
        # time.sleep(2)

    # definim metodele de validate
    def enter_username(self):
        self.driver.find_element(*self.USER_LOC).send_keys('tomsmith')
        # time.sleep(3)

    def enter_password(self):
        self.driver.find_element(*self.PASS_LOC).send_keys('SuperSecretPassword!')
        # time.sleep(3)

    def click_on_login(self):
        self.driver.find_element(*self.BUTTON_LOC).click()
        time.sleep(2)

    def validate_secure(self):
        msg = self.driver.find_element(*self.SECURE_LOC).text
        print(msg)
        expected_msg = 'Secure Area'
        assert expected_msg in msg, 'we ar not in secure area'

    def validate_url(self):
        curent_URL = self.driver.current_url
        inspected_url = 'https://the-internet.herokuapp.com/secure'
        assert inspected_url == curent_URL, 'We ar not and the inspected page'

    def enter_invalid(self, username, password):
        self.driver.find_element(*self.USER_LOC).send_keys(username)
        self.driver.find_element(*self.PASS_LOC).send_keys(password)
    def validate_same_URL(self):
        curent_URL = self.driver.current_url
        inspected_url = 'https://the-internet.herokuapp.com/login'
        assert inspected_url == curent_URL, 'We ar not and the inspected page'

