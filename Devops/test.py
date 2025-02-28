from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get(r"D:\FrontEnd Dev\DevOps_SMAD\Devops\main.html")  # Corrected for Windows


def safe_print(msg):
    try:
        print(msg)
    except UnicodeEncodeError:
        print(msg.encode("utf-8", "ignore").decode())  # Skip unsupported characters

### Test 1: Navigation ###
def test_navigation():
    pages = {
        "Home": "Welcome to Game Jam Tracker",
        "Game Jam": "Upcoming Game Jams",
        "About Us": "About Us",
        "Gallery": "Gallery"
    }

    for page, expected_text in pages.items():
        button = driver.find_element(By.LINK_TEXT, page)
        button.click()
        time.sleep(1)
        assert expected_text in driver.page_source, f"Failed to load {page} page"
        safe_print(f"{page} page loaded successfully") 

### Run Tests ###
safe_print("\nRunning tests...\n")
test_navigation()
safe_print("\n All tests passed successfully! ")

driver.quit()
