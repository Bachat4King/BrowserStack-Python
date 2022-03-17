from behave import step
from selenium.webdriver.common.by import By


@step('go to {url}')
def go_to_website(context, url):
    context.browser.get(url)


@step('demoqa-textbox: fill the form with valid data')
def fill_form(context):
    context.browser.find_element(By.XPATH, "//input[@id='userName']").send_keys("abc")
    context.browser.find_element(By.XPATH, "//input[@id='userEmail']").send_keys("abc@gmail.com")
    context.browser.find_element(By.XPATH, "//textarea[@id='currentAddress']").send_keys("my address")
    context.browser.find_element(By.XPATH, "//textarea[@id='permanentAddress']").send_keys("my permanent address")


@step('demoqa-textbox: click submit button')
def click_submit(context):
    context.browser.find_element(By.XPATH, "//button[@id='submit']").click()


@step('the data is displayed on the page')
def get_data(context):
    assert context.browser.find_element(By.XPATH, "//p[@id='name']").text
    assert context.browser.find_element(By.XPATH, "//p[@id='email']").text
    assert context.browser.find_element(By.XPATH, "//p[@id='currentAddress']").text
    assert context.browser.find_element(By.XPATH, "//p[@id='permanentAddress']").text
