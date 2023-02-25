from pytube import YouTube

link ="https://youtu.be/EAYlckSaviI"
youtube_1 = YouTube(link)
print(youtube_1.title)
print(youtube_1.thumbnail_url)
videos = youtube_1.streams.all() #all format
videos = youtube_1.streams.filter(only_audio=True) #only audio

vid = list(enumerate(videos))
for i in vid:
    print(i)
strm = int(input("Enter: "))
videos[strm].download()
print('successfully')

# complete playlist
from pytube import Playlist

py = Playlist('https://www.youtube.com/playlist?list=PLjVLYmrlmjGfa9HAI6K_wIYPHQRARrl6E')
print(f'Downloading : {py.title}')

for video in py.videos:
    video.streams.first().download()