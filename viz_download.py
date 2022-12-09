import urllib.request
import re
from pytube import YouTube, Search

# keyword
key_word = "kill+me"

# getting the video id/url
html = urllib.request.urlopen('https://www.youtube.com/results?search_query=' + key_word)
video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
for i in range(2):
    print(video_ids[i])

# getting the video from pytube
yt_search = Search("satan")
print(len(yt_search.results))
print((yt_search.results[0]).watch_url)

# downloading the video
yt_video = YouTube((yt_search.results[0]).watch_url)
print(yt_video.title)
print(yt_video.views)
yt_video = yt_video.streams.get_lowest_resolution()
yt_video.download()