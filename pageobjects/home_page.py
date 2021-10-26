from time import sleep

from selenium.webdriver.common.keys import Keys

from pageobjects.base_page import BasePage
from utils.general import get_setting


class HomePage(BasePage):
    search_btn_xpath = "//div[@id='search-form']//input"
    navigation_bar_xpath ="//a[contains(@class,'Navbar_sm-mobile__boCrg')]"
    login_btn_xpath = "//a[@id='LoginButton']"

    def go_to_home_page(self):
        url = get_setting("URL", 'url')
        self.browser.get(url)

    def search(self, keyword):
        sleep(5)
        print("I am searching for ",keyword)
        self.send_text(self.search_btn_xpath, keyword)
        self.send_text(self.search_btn_xpath, Keys.ENTER)

    def click_navigation_bar(self):
        sleep(5)
        print('CLicking on the navigation bar')
        self.click(self.navigation_bar_xpath)

    def click_login(self):
        sleep(2)
        self.click(self.login_btn_xpath)


