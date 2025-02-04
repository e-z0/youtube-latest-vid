import bs4
import selenium
import requests
from bs4 import BeautifulSoup

# youtube_channel = input("Please paste the link of the youtube channel: ")

daily_val_home = requests.get("https://www.youtube.com/@DailyValorantqq")

daily_val_content = daily_val_home.content

soup = BeautifulSoup(daily_val_content, "html.parser")

print(soup.title)

