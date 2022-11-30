from pytube import YouTube
import os

def downloadYtVid(lik, dir):

    a = [lik]

    link = a[0]
    yt = YouTube(link)

    yd = yt.streams.get_highest_resolution()

    yd.download(dir) # type: ignore

def downloadYtAudio(lik, dir):
    a = [lik]

    link = a[0]
    yt = YouTube(link)

    video = yt.streams.filter(only_audio=True).first()

    out_file = video.download(output_path=dir) # type: ignore

    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

