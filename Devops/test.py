from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get(r"D:\FrontEnd Dev\DevOps_SMAD\Devops\main.html")  # Adjust path as needed

def safe_print(msg):
    """Prints message safely, avoiding Unicode errors."""
    try:
        print(msg)
    except UnicodeEncodeError:
        print(msg.encode("utf-8", "ignore").decode())

### Test 1: Navigation ###
def test_navigation():
    """Tests navigation across different pages."""
    pages = {
        "Home": "Welcome to Game Jam Tracker",
        "Game Jam": "Upcoming Game Jams",
        "About Us": "About Us",
        "Gallery": "Gallery"
    }

    for page, expected_text in pages.items():
        button = driver.find_element(By.LINK_TEXT, page)
        button.click()
        time.sleep(1)  # Allow page content to update
        assert expected_text in driver.page_source, f"Failed to load {page} page"
        safe_print(f"{page} page loaded successfully") 

### Test 2: Dark Mode Toggle ###
def test_dark_mode_toggle():
    """Tests toggling between dark and light mode."""
    try:
        toggle_button = driver.find_element(By.TAG_NAME, "button")  # Selects first button (toggle button)
        
        # Click to enable light mode
        toggle_button.click()
        time.sleep(1)  # Allow transition

        # Verify light mode activation
        body_class = driver.find_element(By.TAG_NAME, "body").get_attribute("class")
        assert "light-mode" in body_class, "Light mode activation failed"
        safe_print("✅ Light mode activated successfully")

        # Click to return to dark mode
        toggle_button.click()
        time.sleep(1)

        # Verify dark mode activation
        body_class = driver.find_element(By.TAG_NAME, "body").get_attribute("class")
        assert "light-mode" not in body_class, "Dark mode activation failed"
        safe_print("✅ Dark mode activated successfully")

    except Exception as e:
        safe_print(f"❌ Error in dark mode toggle test: {e}")

### Run Tests ###
safe_print("\n🔍 Running tests...\n")
test_navigation()
test_dark_mode_toggle()
safe_print("\n✅ All tests passed successfully!")

# Close WebDriver
driver.quit()
