import bs4
import selenium
import requests
from bs4 import BeautifulSoup

# youtube_channel = input("Please paste the link of the youtube channel's homepage: ")

def get_video(channel_url):

    # Send GET request to channel URL
    response = requests.get(channel_url)

    # Confirm request was successful
    if response.status_code != 200:
        print("Failed to retreive the page")
        return None

    # Make soup with HTML parser
    soup = BeautifulSoup(response.text, "html.parser")

    # Look for youtube specific layout for videos
    # video = soup.find(id = "contents", class_ = "style-scope ytd-section-list-renderer")
    video = soup.find("body")
    # link = video.get("href")

    print(video)
    # print(link)

    # if video:
    #     # Find video URL
    #     link = video.find("a", {"href": True})
    #     if link:
    #         video_url = "https://www.youtube.com" + link["href"]
    #         return video_url
    # return "No video found"

recent_video = get_video("https://www.youtube.com/@DailyValorantqq")

# if recent_video:
#     print(f"The most recent video from [Channel Name] is: {recent_video}")
# else:
#     print("Could not find the most recent video.")