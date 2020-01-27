from __future__ import unicode_literals
import youtube_dl
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '192'
    }],
    'postprocessor_args': [
        '-ar', '48000'
    ],
    'prefer_ffmpeg': True,
}


with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    path=[
    'https://www.youtube.com/watch?v=-4v5dQcqDJA']

    for i in path:
        ydl.download([i])