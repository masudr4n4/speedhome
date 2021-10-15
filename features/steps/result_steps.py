from behave import *

from pageobjects.search_result_page import ResultPage


@then("I verify result page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    ResultPage(context).verify_result_page()