import os
import threading
from multiprocessing import Process
from threading import Thread
from time import perf_counter

import requests


# CPU-bound task (heavy computation)
def encrypt_file(path: str):
    print(f"Processing file from {path} in process {os.getpid()}")
    # Simulate heavy computation by sleeping for a while
    _ = [i for i in range(100_000_000)]


# I/O-bound task (downloading image from URL)
def download_image(image_url):
    print(
        f"Downloading image from {image_url} "
        f"in thread {threading.current_thread().name}"
    )
    response = requests.get(image_url)
    with open("image.jpg", "wb") as f:
        f.write(response.content)


def main():
    try:
        process = Process(target=encrypt_file, args=("rockyou.txt",))
        thread = Thread(
            target=download_image, args=("https://picsum.photos/1000/1000",)
        )
        start = perf_counter()
        thread.start()
        process.start()
        thread.join()
        download_counter = perf_counter() - start
        process.join()
        encryption_counter = perf_counter() - start
        total = perf_counter() - start
        print(
            f"Time taken for encryption task: {encryption_counter:00.2f}, "
            f"I/O-bound task: {download_counter:00.2f}, "
            f"Total: {total:00.2f} seconds"
        )
    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    main()
