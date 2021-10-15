from pageobjects.base_page import BasePage
from utils.general import get_setting
from time import sleep


class FaqPage(BasePage):
    """
    This class will work for all the faq function
    """
    versi_bahasa_xpath = "//a[@href='/my/learn/landlord-faq']"

    def open_faq(self):
        url = get_setting("URL", 'url') + "/learn/landlord-faq"
        self.browser.get(url)

    def verify_language_changing_work(self):
        prev_url = self.browser.current_url
        prev_title = self.browser.title
        sleep(5)
        self.browser.find_element_by_xpath(self.versi_bahasa_xpath).click()
        sleep(4)
        current_url = self.browser.current_url
        current_title = self.browser.title
        assert prev_url != current_url
        assert prev_title == current_title
