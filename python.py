from asyncio.windows_events import NULL
from turtle import color
from pytube import YouTube
import PySimpleGUI as sg
from sys import argv
from PySimpleGUI import popup

def download(link):
    a = [link]

    my_link = a[0]
    yt = YouTube(my_link)

    yd = yt.streams.get_highest_resolution()
# r'C:\Users\migue\Desktop\test'
    yd.download(r'C:\Users\migue\Desktop\test')
sg.theme('DarkAmber')
layout = [[sg.Text("Enter your Url"), sg.ProgressBar(5, size=(23, 20), bar_color="Blue")],
          [sg.InputText(), sg.Button("Download")]]

win = sg.Window("MyCat Downloader", layout)

while True:
    event, values = win.read()
    if event == 'Download':
        if values[0] != NULL:
            lik = values[0]
            file = sg.popup_get_file("Save", save_as=True, no_window=True)
            sg.popup_menu
            download(lik)
    elif event == sg.WIN_CLOSED:
        break

win.close()

