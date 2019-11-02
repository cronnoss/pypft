from selenium.webdriver.firefox.webdriver import WebDriver
import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
# from selenium.webdriver.chrome.webdriver import WebDriver


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class test_add_group(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def test_test_add_group(self):
        success = True
        wd = self.wd
        wd.get("http://localhost/addressbook/")
        wd.set_window_size(1196, 797)
        wd.find_element(By.NAME, "user").click()
        wd.find_element(By.NAME, "user").send_keys("admin")
        wd.find_element(By.NAME, "pass").send_keys("secret")
        wd.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()
        wd.find_element(By.LINK_TEXT, "groups").click()
        wd.find_element(By.NAME, "new").click()
        wd.find_element(By.NAME, "group_name").click()
        wd.find_element(By.NAME, "group_name").send_keys("pytest1")
        wd.find_element(By.NAME, "group_header").click()
        wd.find_element(By.NAME, "group_header").send_keys("pytest2")
        wd.find_element(By.NAME, "group_footer").click()
        wd.find_element(By.NAME, "group_footer").send_keys("pytest3")
        wd.find_element(By.NAME, "submit").click()
        wd.find_element(By.LINK_TEXT, "group page").click()
        wd.find_element(By.LINK_TEXT, "Logout").click()
        self.assertTrue(success)

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()
