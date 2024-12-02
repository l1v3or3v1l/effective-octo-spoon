import os
import sys
import time
import urllib.request

URL = "https://releases.ubuntu.com/24.04/ubuntu-24.04.1-desktop-amd64.iso"

def progress(count, block_size, total_size):
    global start_time
    if count == 0:
        start_time = time.time()
        return
    duration = time.time() - start_time
    progress_size = int(count * block_size)
    speed = int(progress_size / (1024 * duration))
    percent = int(count * block_size * 100 / total_size)
    sys.stdout.write("\r %d MB, %d KB/s, %d seconds passed" %
                    (progress_size / (1024 * 1024), speed, duration))
    sys.stdout.flush()

def save():
	while True:
		urllib.request.urlretrieve(URL, os.devnull, progress)

if __name__ == '__main__':
	save()