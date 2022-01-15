import time
from unittest import TestCase


class TestForm(TestCase):
    """
    It is require to have a path to chromedriver configured in PATH
    echo 'export PATH=$PATH:<path-to-your-chromedriver>' >> ~/.bashrc
    or
    echo 'export PATH=$PATH:<path-to-your-chromedriver>' >> ~/.zshrc
    """
    def setUp(self) -> None:
        from selenium import webdriver
        self.driver = webdriver.Chrome("/Users/vadymkhodak/chromedriver")

    def tearDown(self) -> None:
        self.driver.close()

    def test_generate_email(self):
        # GIVEN Selenium Chrome web driver of index page
        self.driver.get("http://127.0.0.1:5000")
        # WHEN set value "Vadym Khodak" for element with id "name"
        time.sleep(1)
        elem = self.driver.find_element("id", "name")
        elem.send_keys("Vadym Khodak")
        # WHEN click on button "generate"
        time.sleep(1)
        generate = self.driver.find_element("id", "generate")
        generate.click()
        # THEN value of element with id "email" equals "vadym.khodak@datarobot.com"
        email = self.driver.find_element("id", "email")
        assert email.get_attribute("value") == "vadym.khodak@datarobot.com"
        time.sleep(1)


if __name__ == "__main__":
    pass
