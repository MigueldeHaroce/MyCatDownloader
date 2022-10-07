from asyncio.windows_events import NULL
from pytube import YouTube
import PySimpleGUI as sg
from sys import argv
from PySimpleGUI import popup

def download(link, site):
    a = [link]

    my_link = a[0]
    yt = YouTube(link)

    yd = yt.streams.get_highest_resolution()
# r'C:\Users\migue\Desktop\test'
    yd.download(f"r{site}")
sg.theme('DarkAmber')
layout = [[sg.Text("Enter your Url")],
          [sg.InputText(), sg.Button("Download")]]

win = sg.Window("MyCat Downloader", layout)

while True:
    event, values = win.read()
    if event == 'Download':
        if values[0] != NULL:
            
            lik = values[0]
            file = sg.popup_get_folder
            download(lik, file)
    elif event == sg.WIN_CLOSED: # if user closes window or clicks cancel
        break

win.close()

