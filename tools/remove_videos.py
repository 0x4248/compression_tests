# Compression test
# Some compression tests done using FFmpeg
# Github https://www.github.com/0x4248/compression_tests
# Licence: GNU General Public License v3.0
# By: 0x4248
#
# Remove videos
# Remove videos that are not the 10nth iteration

import os

def remove_videos(dir):
    files = os.listdir(dir)
    for file in files:
        if file.endswith('.mp4'):
            try:
                if int(file.split('_')[-1].split('.')[0]) % 10 != 0:
                    os.remove(file)
                    print(f"Removed {file}")
            except ValueError:
                print(f"Skipping {file}: does not match expected pattern")

path = input("Enter the path to the directory: ")
remove_videos(path)