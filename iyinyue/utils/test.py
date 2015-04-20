__author__ = 'Administrator'
from iyinyue.utils import filedir, mp3reader
import mutagen.mp3


def test():
    path = 'G:/music'
    all_files = filedir.print_path(path)
    total = {}
    for file in all_files:
        if '.mp3' not in file:
            continue
        try:
            print(file)
            info = mp3reader.get_mp3_info(file)
        except mutagen.mp3.HeaderNotFoundError:
            continue
        print(info)
        for k, v in info.items():
            print(k+"  "+v[0])
            if k not in total:
                total[k] = 0
            else:
                total[k] += 1
    print('!!!', total)
if __name__ == '__main__':
    test()