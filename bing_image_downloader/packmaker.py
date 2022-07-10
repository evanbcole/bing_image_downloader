import downloader
import string
import random

def string_generator(size, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def main():
    downloader.download("dsd", limit=1, output_dir="./images/blocks")


main()