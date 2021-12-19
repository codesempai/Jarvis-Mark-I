import os
import random
from random import randint

def play_songs():
    n = random.randint(0,10)
    print(n)
    music_dir = 'D:/Japanese Songs/audio'
    songs = os.listdir(music_dir)
    print(songs)
    os.startfile(os.path.join(music_dir,songs[n]))

