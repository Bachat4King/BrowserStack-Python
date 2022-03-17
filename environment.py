from selenium import webdriver
import os
import json

# set up config file and task id from the environment variables
config_file = os.environ['CONFIG_FILE'] if 'CONFIG_FILE' in os.environ else 'config/single.json'
task_id = int(os.environ['TASK_ID']) if 'TASK_ID' in os.environ else 0

# open the config file
with open(config_file) as data_file:
    config = json.load(data_file)

# set up user and key from config file
username = config['user']
access_key = config['key']


# set up before feature
def before_feature(context, feature):
    desired_capabilities = config['environments'][task_id]

    for key in config["capabilities"]:
        if key not in desired_capabilities:
            desired_capabilities[key] = config["capabilities"][key]

    context.browser = webdriver.Remote(
        desired_capabilities=desired_capabilities,
        command_executor=f"https://{username}:{access_key}@hub.browserstack.com/wd/hub")


# set up after feature
def after_feature(context, feature):
    if context.failed is True:
        context.browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "At least 1 assertion failed"}}')
    if context.failed is not True:
        context.browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "All assertions passed"}}')
    context.browser.quit()
