from behave import *

from pageobjects.login_page import LoginPage


@then("I verify login page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    LoginPage(context).verify_login_page()