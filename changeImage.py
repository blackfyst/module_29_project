#!/usr/bin/env python3

from PIL import Image
import os
import filetype
from pathlib import Path

def modify_images():
    """Resize and save as jpg on directory of images"""
    read_directory = "/home/donsacafq/Module_29_project/supplier-data/images"
    write_directory = "/home/donsacafq/Module_29_project/supplier-data/images"
    for filename in os.listdir(read_directory):
        path_and_filename = read_directory + "/" + filename
        if filetype.is_image(path_and_filename):
            im = Image.open(path_and_filename)
            rgb_im = im.convert('RGB')
            root, ext = os.path.splitext(filename)
            filename = root
            rgb_im.resize((600,400)).save(write_directory + "/" + filename + ".jpeg")

def main():
    modify_images()

if __name__ == "__main__":
    main()