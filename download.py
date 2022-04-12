from pytube import YouTube
import os

def extract (url, path):
    # url input from user
    print(url)

    # extract only audio
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    
    # check for destination to save file
    destination = path or '.'
    
    # download the file
    out_file = video.download(output_path=destination)
    
    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)