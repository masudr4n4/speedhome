from time import sleep

from pageobjects.base_page import BasePage


class LoginPage(BasePage):
    """
    This class will work for login page.
    """

    def verify_login_page(self):
        sleep(4)
        login_box_title_xpath = '//h2'
        text = self.browser.find_element_by_xpath(login_box_title_xpath).text
        assert "Login to your account" in text
        assert "auth.speedhome.com" in self.browser.current_url
