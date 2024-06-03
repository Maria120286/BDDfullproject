from behave import *


@given('I am on the login page')
def step_impl(context):
    context.base_page.navigate_to_login()
    print('Suntem in given')


@when('I enter a valid username')
def step_impl(context):
    context.base_page.enter_username()
    print('Suntem in primul when')


@when('I enter a valid password')
def step_impl(context):
    context.base_page.enter_password()
    print('Suntem in primul And')


@when('I click on login button')
def step_impl(context):
    context.base_page.click_on_login()
    print('Suntem in al doilea And')


@then('I am on the secure area')
def step_impl(context):
    context.base_page.validate_secure()
    print('Suntem in Then')


@then('I am on the new page')
def step_impl(context):
    context.base_page.validate_url()
    print('Suntem in ultimul And')


@when('I use invalid "{username}" or "{password}"')
def step_impl(context, username, password):
    context.base_page.enter_invalid(username, password)


@then('I should remain on the login page')
def step_impl(context):
    context.base_page.validate_same_URL()
