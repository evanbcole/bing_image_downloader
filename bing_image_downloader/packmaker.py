from bing_image_downloader.downloader import download
import downloader
import string
import random
import os

def string_generator(size, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

# get file name for every png in the directory
def get_file_names(directory) -> list:
    file_names = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".png"):
                file_names.append(file)
    return file_names

def download_block_images(number_of_blocks, output_dir):
    for i in range(number_of_blocks):
        successful = False
        while not successful:
            random_int = random.randint(2, 10)
            search_string = string_generator(random_int)
            print(i)
            res = downloader.download(search_string, limit=1, output_dir=output_dir)
            if res:
                successful = True

# rename each file in a directory to the next string in a list
def rename_files(directory, list_of_strings):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".png"):
                os.rename(os.path.join(root, file), os.path.join(root, list_of_strings[0] + ".png"))
                list_of_strings.pop(0)

def main():
    # downloader.download("dsd", limit=1, output_dir="./images/blocks")
    list_of_files = get_file_names("V:/YouTube Video Files/Texture Pack Files/VanillaDefault+1.19/assets/minecraft/textures/block")
    download_block_images(len(list_of_files), "./images/blocks")
    rename_files("./images/blocks", list_of_files)

main()