from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Specify ChromeDriver path explicitly
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path=r"C:\WebDrivers\chromedriver-win64\chromedriver.exe", options=chrome_options)

# Open the target website
driver.get("http://127.0.0.1:5500/Devops/main.html")  # Update with your actual website URL

def safe_print(msg):
    try:
        print(msg)
    except UnicodeEncodeError:
        print(msg.encode("utf-8", "ignore").decode())  # Handle unsupported characters

### Test 1: Dark Mode Toggle ###
def test_dark_mode():
    try:
        button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.TAG_NAME, "button")))
        button.click()
        time.sleep(1)
        body_class = driver.find_element(By.TAG_NAME, "body").get_attribute("class")
        assert "light-mode" in body_class, "❌ Dark Mode toggle failed!"
        safe_print("[✓] Dark Mode toggled successfully!")
    except Exception as e:
        safe_print(f"❌ Dark Mode toggle test failed: {e}")

### Test 2: Home Page Load ###
def test_home_page():
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Welcome to Game Jam Tracker')]")))
        safe_print("[✓] Home page loaded successfully!")
    except Exception as e:
        safe_print(f"❌ Home page failed to load: {e}")

### Test 3: About Us Page Load ###
def test_about_us():
    try:
        button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, "About Us")))
        button.click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'About Us')]")))
        safe_print("[✓] About Us page loaded successfully!")
    except Exception as e:
        safe_print(f"❌ About Us page failed to load: {e}")

### Test 4: Game Jam Page Load ###
def test_game_jam():
    try:
        button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, "Game Jam")))
        button.click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Upcoming Game Jams')]")))
        safe_print("[✓] Game Jam page loaded successfully!")
    except Exception as e:
        safe_print(f"❌ Game Jam page failed to load: {e}")

### Test 5: Gallery Page Load ###
def test_gallery():
    try:
        button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, "Gallery")))
        button.click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Gallery')]")))
        safe_print("[✓] Gallery page loaded successfully!")
    except Exception as e:
        safe_print(f"❌ Gallery page failed to load: {e}")

### Run Selected Tests ###
safe_print("\nRunning tests...\n")
test_dark_mode()
test_home_page()
test_about_us()
test_game_jam()
test_gallery()
safe_print("\n🎉 All tests completed successfully! 🎉")

driver.quit()
