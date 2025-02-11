from selenium import webdriver

options = webdriver.ChromeOptions()
driver = webdriver.Remote(
    command_executor="http://localhost:4444/wd/hub",
    options=options
)

driver.get("https://www.google.com")
