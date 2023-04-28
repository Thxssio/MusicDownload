
#!/usr/bin/env python3
#          
#  ______ _    ___   __ _____ _____ _____ ____  
# |__   __| |  | \ \ / // ____/ ____|_   _/ __ \ 
#    | |  | |__| |\ V /| (___| (___   | || |  | |
#    | |  |  __  | > <  \___ \\___ \  | || |  | |
#    | |  | |  | |/ . \ ____) |___) |_| || |__| |
#    |_|  |_|  |_/_/ \_\_____/_____/|_____\____/ Music Download 
#
# Version: 1.2                    Written by Thxssio (DEX)
#
# 
# Github : https://github.com/thxssio

# imports

C = "\033[0m"     # clear (end) | Color 
R = "\033[0;31m"  # red (error) | Color 
G = "\033[0;32m"  # green (process) | Color 
B = "\033[0;36m"  # blue (choice) | Color 
Y = "\033[0;33m"  # yellow (info) | Color 



from pytube import YouTube #import the lib
from pytube import Playlist #import the lib
import moviepy.editor as mp #import the lib
import re #import the lib
import os #import the lib
import sys #import the lib

def banner(): #def banner lib
    print(B)
    print(r"""  
    
 ________ __  ____   __ _____ _____ _____ ____  
 |__   __| |  | \ \ / // ____/ ____|_   _/ __ \ 
    | |  | |__| |\ V /| (___| (___   | || |  | |
    | |  |  __  | > <  \___ \\___ \  | || |  | |
    | |  | |  | |/ . \ ____) |___) |_| || |__| |
    |_|  |_|  |_/_/ \_\_____/_____/|_____\____/
    
    """,end="")
    print(f"{C} Youtube Music Download\n")
    print(f"     Written by {B}Thxssio{C} (DEX)")


def download_music():
    link = input('Digite o Link do Vídeo: ')
    path = input('Caminho de download: ')
    yt = YouTube(link)
    #Fazer o dowload
    ys = yt.streams.filter(only_audio=True).first().download(path)
    #Converter o video(mp4) para mp3
    for file in os.listdir(path):                 
        if re.search('mp4', file):                                     
            mp4_path = os.path.join(path , file)  
            mp3_path = os.path.join(path, os.path.splitext(file)[0]+'.mp3') 
            new_file = mp.AudioFileClip(mp4_path)  
            new_file.write_audiofile(mp3_path)    
            os.remove(mp4_path)                    
    print("Download Completo")

def download_playlist():
    Playlist = int(input('Digite a quantidade de musicas: '))
    musicas = list()
    path = input('Caminho de download: ')
    for cc in range(1, Playlist + 1):
        links = str(input(f'Digite o {cc}ª link: '))
        musicas.append(links)
    for musica in musicas:
        yt = YouTube(musica)
        ys = yt.streams.filter(only_audio=True).first().download(path)
        for file in os.listdir(path):                 
            if re.search('mp4', file):                                     
                mp4_path = os.path.join(path , file)  
                mp3_path = os.path.join(path, os.path.splitext(file)[0]+'.mp3') 
                new_file = mp.AudioFileClip(mp4_path)  
                new_file.write_audiofile(mp3_path)    
                os.remove(mp4_path)  
                print("Download Completo")      


banner()
download_music()

 
