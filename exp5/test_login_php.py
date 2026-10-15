from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# ---------- CONFIGURATION ----------
URL = "http://localhost/exp12/login.php"   # change if hosted elsewhere
USERNAME = "admin"
PASSWORD = "12345"

# ---------- SETUP CHROME ----------
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(URL)
time.sleep(2)

# ---------- TEST CASE 1: Page Title and URL ----------
print("TC01 - Checking page title and URL")
assert "Login" in driver.title, "❌ Page title mismatch"
assert "login" in driver.current_url, "❌ URL does not contain 'login'"
print("✅ Page loaded correctly")

# ---------- TEST CASE 2: Successful Login ----------
print("TC02 - Valid login test")
driver.find_element(By.NAME, "username").clear()
driver.find_element(By.NAME, "username").send_keys(USERNAME)
driver.find_element(By.NAME, "password").clear()
driver.find_element(By.NAME, "password").send_keys(PASSWORD)
driver.find_element(By.NAME, "login").click()
time.sleep(1)

page_source = driver.page_source
assert "Login Successful" in page_source, "❌ Valid login failed"
print("✅ Valid login passed")

# ---------- Go back to login page ----------
driver.get(URL)
time.sleep(1)

# ---------- TEST CASE 3: Invalid Username ----------
print("TC03 - Invalid username test")
driver.find_element(By.NAME, "username").send_keys("wronguser")
driver.find_element(By.NAME, "password").send_keys(PASSWORD)
driver.find_element(By.NAME, "login").click()
time.sleep(1)
assert "Invalid" in driver.page_source, "❌ Invalid username not handled"
print("✅ Invalid username handled correctly")

# ---------- Go back to login page ----------
driver.get(URL)
time.sleep(1)

# ---------- TEST CASE 4: Invalid Password ----------
print("TC04 - Invalid password test")
driver.find_element(By.NAME, "username").send_keys(USERNAME)
driver.find_element(By.NAME, "password").send_keys("wrongpass")
driver.find_element(By.NAME, "login").click()
time.sleep(1)
assert "Invalid" in driver.page_source, "❌ Invalid password not handled"
print("✅ Invalid password handled correctly")

# ---------- Go back to login page ----------
driver.get(URL)
time.sleep(1)

# ---------- TEST CASE 5: Empty Fields ----------
print("TC05 - Empty fields test")
driver.find_element(By.NAME, "username").clear()
driver.find_element(By.NAME, "password").clear()
driver.find_element(By.NAME, "login").click()
time.sleep(1)
# Check for 'required' attribute behavior or no action
print("✅ Empty fields test executed (browser shows required warning if HTML5 required attribute is used)")

# ---------- TEST CASE 6: Verify Input Elements Exist ----------
print("TC06 - Checking presence of input fields")
username_field = driver.find_element(By.NAME, "username")
password_field = driver.find_element(By.NAME, "password")
login_button = driver.find_element(By.NAME, "login")

assert username_field.is_displayed(), "❌ Username field missing"
assert password_field.is_displayed(), "❌ Password field missing"
assert login_button.is_displayed(), "❌ Login button missing"
print("✅ All input fields found")

# ---------- CLEANUP ----------
time.sleep(2)
driver.quit()
print("\n🎉 All test cases executed successfully!")
