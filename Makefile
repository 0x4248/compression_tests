# Compression test
# Some compression tests done using FFmpeg
# Github https://www.github.com/0x4248/compression_tests
# Licence: GNU General Public License v3.0
# By: 0x4248

PYTHON=python3
SRC=src
MAIN=main.py

all: run

run: 
	$(PYTHON) $(SRC)/$(MAIN)