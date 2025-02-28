from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Specify ChromeDriver path explicitly
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path=r"C:\WebDrivers\chromedriver-win64\chromedriver.exe", options=chrome_options)

# Open the target website (Replace with actual URL)
driver.get("http://127.0.0.1:5500/Devops/main.html")  # Update with your actual website URL

def safe_print(msg):
    try:
        print(msg)
    except UnicodeEncodeError:
        print(msg.encode("utf-8", "ignore").decode())  # Handle unsupported characters

### Test 1: Navigation ###
def test_navigation():
    pages = {
        "Home": "Welcome to Game Jam Tracker",
        "Game Jam": "Upcoming Game Jams",
        "About Us": "About Us",
        "Gallery": "Gallery"
    }

    for page, expected_text in pages.items():
        try:
            button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, page)))
            button.click()
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{expected_text}')]")))
            safe_print(f"[✓] {page} page loaded successfully")
        except Exception as e:
            safe_print(f"❌ Failed to load {page} page: {e}")

### Run Tests ###
safe_print("\nRunning tests...\n")
test_navigation()
safe_print("\n🎉 All tests passed successfully! 🎉")

driver.quit()
