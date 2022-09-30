from pytube import YouTube
from sys import argv

a = ["https://www.youtube.com/watch?v=yvvBJn0XxKI&ab_channel=HolyFists"]

link = a[0]
yt = YouTube(link)

yd = yt.streams.get_highest_resolution()

yd.download(r'C:\Users\migue\Desktop\test')