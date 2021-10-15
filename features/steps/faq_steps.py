from behave import *

from pageobjects.faq_page import FaqPage


@given("I am on Landlord FAQ page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    FaqPage(context).open_faq()



@then("I verify changing language works")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    FaqPage(context).verify_language_changing_work()