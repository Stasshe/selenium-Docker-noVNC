from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define WebDriver options
options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--remote-debugging-port=9222")

# Instantiate the WebDriver
driver = webdriver.Remote(
    command_executor="http://localhost:4444/wd/hub",
    options=options
)

# Open the desired webpage
driver.get("https://www.google.com")

try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    # Execute JavaScript to set navigator.webdriver to false
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => false})")
    print(driver.title)
finally:
    pass  # Replace pass with driver.quit() when you want to close the browser
