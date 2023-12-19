from pytube import YouTube
from pydub import AudioSegment
import os
import re

def converttomp3():
    print()
    print("***Downloading, please be patient.***")
    url = YouTube(link, use_oauth=True, allow_oauth_cache=True)
    url = url.streams.get_audio_only()
    title = url.title
    filteredtitle = re.sub("[^A-Za-z0-9 ]", "", title)
    url.download(filename= filteredtitle + ".mp4")
    print()
    print("***Download completed successfully.***")
    print()
    bitrateinput = input("What bitrate would you like? (128, 256, 320):")
    print()
    print("***Converting to .mp3, please be patient.***")
    print()
    AudioSegment.from_file(filteredtitle + ".mp4").export(filteredtitle + ".mp3", format="mp3", bitrate=bitrateinput)
    os.remove(filteredtitle + ".mp4")
    print("***File successfully converted. Quiting.***")
    print()
    quit()

def audio():
    print()
    mp3 = input("Would you like to convert to .mp3? (yes or no): ")
    if (mp3) == "yes":
        converttomp3()
    else:
        print()
        print("***Downloading, please be patient.***")
        url = YouTube(link, use_oauth=True, allow_oauth_cache=True)
        url = url.streams.get_audio_only()
        title = url.title
        filteredtitle = re.sub("[^A-Za-z0-9 ]", "", title)
        url.download(filename=filteredtitle + ".mp4")
        print()
        print("***Download completed successfully.***")
        print()
        print("***File will not be converted. Quiting.***")
        print()
        quit()

def both():
    print()
    print("***Downloading, please be patient.***")
    url = YouTube(link, use_oauth=True, allow_oauth_cache=True)
    url = url.streams.get_highest_resolution()
    title = url.title
    filteredtitle = re.sub("[^A-Za-z0-9 ]", "", title)
    url.download(filename=filteredtitle + ".mp4")
    print()
    print("***Download completed successfully. Quiting.***")
    quit()

link = input("YouTube URL: ")
print()
choice = input("""Please select an option: 
               1: Download audio only.
               2: Download video and audio.
            """)
if choice == "1":
    audio()
if choice == "2":
    both()
