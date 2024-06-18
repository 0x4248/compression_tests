# Compression test
# Some compression tests done using FFmpeg
# Github https://www.github.com/0x4248/compression_tests
# Licence: GNU General Public License v3.0
# By: 0x4248

import subprocess
import os

def compress_video(input_file, output_file, compression_factor):
    ffmpeg_command = [
        'ffmpeg', '-i', input_file, '-vcodec', 'libx264', '-crf', str(compression_factor), output_file
    ]
    subprocess.run(ffmpeg_command)

def repeated_compression(input_file, iterations, compression_factor):
    base_filename, ext = os.path.splitext(input_file)
    current_input = input_file

    for i in range(1, iterations + 1):
        output_file = f"{base_filename}_compressed_{i}{ext}"
        compress_video(current_input, output_file, compression_factor)
        current_input = output_file
        print(f"Iteration {i}: Compressed video saved as {output_file}")

input_video_path = 'input.mp4' 
iterations = 200
compression_factor = 28
repeated_compression(input_video_path, iterations, compression_factor)