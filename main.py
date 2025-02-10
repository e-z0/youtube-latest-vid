from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

channel_url = input("Please paste the link of the youtube channel's homepage: ")

# Set up Selenium with Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Replace with the URL of the YouTube channel's homepage

# Open the channel homepage in the browser
driver.get(channel_url)

# Wait for the page to load completely (adjust the wait time as needed)
time.sleep(5)

# Find the videos tab on the channel's homepage

video_tab = driver.find_element(By.LINK_TEXT, "Videos")
video_tab.click()

time.sleep(3)

first_video = driver.find_element(By.ID, "video-title-link")
link = first_video.get_attribute("href")
print(link)

video_title = driver.find_element(By.ID, "video-title")
print(video_title.text)

time.sleep(3)

# Find the first video on the homepage (it should be within <ytd-video-renderer>)
# try:
#     # Locate the first video element
#     video_tab = driver.find_element(By.LINK_TEXT, "Videos")
#
#     # Get the link to the most recent video
#     video_url = video_tab.get_attribute("href")
#     print(f"Most recent video URL: {video_url}")
# except Exception as e:
#     print(f"Error: {e}")

# Close the driver
driver.quit()

