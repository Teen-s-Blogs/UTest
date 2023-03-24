import time
from selenium import webdriver

# initialize the webdriver
driver = webdriver.Chrome()

# navigate to the web page
driver.get("https://teen-s-blogs.github.io/Grey-Blogs/")

# wait for the page to load
time.sleep(2)

# find the Google sign-in button and click it
google_button = driver.find_element_by_css_selector(".g-signin2")
google_button.click()

# wait for the Google sign-in popup to appear
time.sleep(2)

# switch to the Google sign-in popup window
driver.switch_to.window(driver.window_handles[-1])

# enter your Google email address and click Next
email_field = driver.find_element_by_css_selector("input[type='email']")
email_field.send_keys("your-email-address@gmail.com")
next_button = driver.find_element_by_css_selector("#identifierNext")
next_button.click()

# wait for the password field to appear
time.sleep(2)

# enter your Google password and click Next
password_field = driver.find_element_by_css_selector("input[type='password']")
password_field.send_keys("your-password")
next_button = driver.find_element_by_css_selector("#passwordNext")
next_button.click()

# wait for the Google sign-in to complete
time.sleep(5)

# switch back to the main window
driver.switch_to.window(driver.window_handles[0])

# assert that the user is signed in and redirected to the correct page
assert "Welcome" in driver.page_source
assert "Logout" in driver.page_source

# close the browser
driver.quit()
