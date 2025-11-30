# utils/yt_scraper.py
import os
import requests

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

def youtube_scrape(topic):
    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&q={topic}&key={YOUTUBE_API_KEY}&maxResults=5"
    response = requests.get(url).json()

    videos = []
    for item in response.get("items", []):
        video_id = item["id"]["videoId"]
        title = item["snippet"]["title"]

        stats_url = f"https://www.googleapis.com/youtube/v3/videos?part=statistics&id={video_id}&key={YOUTUBE_API_KEY}"
        stats = requests.get(stats_url).json()
        views = stats["items"][0]["statistics"].get("viewCount", 0)

        videos.append({
            "title": title,
            "views": int(views),
            "video_id": video_id
        })

    return videos
