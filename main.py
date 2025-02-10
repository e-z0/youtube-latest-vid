from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


# Get homepage channel URL from user
channel_url = input("Please paste the link of the youtube channel's homepage: ")

# Set up Selenium with Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the channel homepage in the browser
driver.get(channel_url)

# Wait for the page to load completely (adjust the wait time as needed)
time.sleep(5)

# Find the videos tab on the channel's homepage
video_tab = driver.find_element(By.LINK_TEXT, "Videos")
video_tab.click()

# Wait for page to load
time.sleep(3)

# Find the first video and grab link
first_video = driver.find_element(By.ID, "video-title-link")
link = first_video.get_attribute("href")

# Get video title
video_title = driver.find_element(By.ID, "video-title")
print(video_title.text)

time.sleep(3)

# Close the driver
driver.quit()

