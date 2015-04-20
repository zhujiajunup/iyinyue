__author__ = 'Administrator'
from mutagen.mp3 import MP3
import mutagen.id3
from mutagen.easyid3 import EasyID3


def get_mp3_info(path):
    id3info = MP3(path, ID3=EasyID3)
    return id3info

if __name__ == '__main__':
    info = (get_mp3_info(str('G:\music\摇滚\Abominable Putridity - A Massacre In The North.mp3').replace('\\', '/')))
    for k, v in info.items():
        print(k, v)


