from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import threading


def test_main(caps):
    user_and_pass = ""
    driver = webdriver.Remote(
        command_executor=f'https://{user_and_pass}@hub-cloud.browserstack.com/wd/hub',
        desired_capabilities=caps)

    try:
        driver.get("https://demoqa.com/alerts")
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='promtButton']"))).click()

        alert = driver.switch_to.alert
        alert.send_keys("Bastian")
        alert.accept()
        text = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//span[@id='promptResult']"))).text
        if "Bastian" in text:
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": '
                '"text is in page"}}')

    except NoSuchElementException:
        driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", '
                              '"reason": "Some elements failed to load"}}')
    driver.quit()


capabilities_list = [
    {
        'browserName': 'iPhone',
        'device': 'iPhone 11',
        'realMobile': 'true',
        'os_version': '15',
        'name': 'DemoQa test Iphone 11',
        'build': 'BStack Build Number 1'
    },
    {
        "os": "Windows",
        "os_version": "10",
        "browser": "Chrome",
        "browser_version": "latest",
        "build": "Windows",
        "name": "DemoQa test windows 10",
        "browserstack.selenium_version": "3.14.0"
    },
    {
        "os": "OS X",
        "os_version": "Monterey",
        "browser": "Safari",
        "browser_version": "15.0",
        "build": "MAC",
        "name": "DemoQa test macOS monterrey",
        "browserstack.selenium_version": "3.14.0"
    }
]

threads = list()

for i in range(3):
    t = threading.Thread(target=test_main, args=(capabilities_list[i],))
    t.start()
    threads.append(t)

for thread in threads:
    # Wait for thread to complete
    thread.join()
