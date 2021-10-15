from time import sleep

from pageobjects.base_page import BasePage


class ResultPage(BasePage):
    """
    This class will contain all the functionality in the search result page.
    """
    search_list_status_text  = "//h1"
    def verify_result_page(self):
        sleep(5)
        status = self.browser.find_element_by_xpath(self.search_list_status_text).text
        assert "Property For Rent" in status, f"Can not find expected text in the search result page"
        assert "rent" in self.browser.current_url
