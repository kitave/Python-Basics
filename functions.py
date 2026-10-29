# functions methods
print("Hello World")
from custom_functions import greet

with open("temp.txt", "w") as file:
    file.write("99.34\n")
    file.write("100\n")
    file.write("54.34\n")

with open("temp.txt", "r") as file:
    content = file.read()
    print(content)

import yt_dlp

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [
        {
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }
    ],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://youtu.be/iMNukFQKS3c'])

greet()
