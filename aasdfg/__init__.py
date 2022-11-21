#!/usr/bin/env python3

import os
import cv2
import math
import time

import numpy as np
from PIL import Image


def compute_shannon_entropy(data):
    if not data:
        return 0

    entropy = 0
    for x in range(256):
        p_x = float(data.count(chr(x)))/len(data)
        if p_x > 0:
            entropy += - p_x*math.log(p_x, 2)
    return entropy

def take_snap(iter):
    # Start camera
    cam = cv2.VideoCapture(0)
    time.sleep(0.1)

    # Capture image
    ret, frame = cam.read()

    # Save image
    time.sleep(0.1)
    cv2.imwrite("snap" + str(iter) + ".png", frame)

    # Stop camera
    cam.release()
    # cam.destroyAllWindows()

def load_image_into_numpy_array(image):
    (im_width, im_height) = image.size
    return np.array(image.getdata()).reshape(
        (im_height, im_width, 3)).astype(np.uint8)

def GenerateSeed(photo_count=1, folds=1, verbose=False, trigger=True):
    start = photo_count - 1
    end = photo_count - 1
    for i in range(start, end+1):
        take_snap(i)

    pics_data = []
    for i in range(start, end+1):
        pics_data.append(load_image_into_numpy_array(Image.open("snap" + str(i) + ".png")))

    # Get least significant bit of each pixel and each channel
    lsbs = []
    for pic in pics_data:
        for row in pic:
            for pixel in row:
                for channel in pixel:
                    lsbs.append(channel & 1)

    # join all the bits
    bits = ''.join(map(str, lsbs))

    # For each 'fold' xor half of the bits with the other half
    for i in range(folds):
        bits = ''.join(str(int(bits[i]) ^ int(bits[i + len(bits)//2])) for i in range(len(bits)//2))
   
    # delete photos
    for i in range(start, end+1):
        os.remove("snap" + str(i) + ".png")

    # Convert bits value to int
    # save to file as well
    seed = int(bits, 2)
    with open("seed.txt", "wb") as f:
        f.write(seed.to_bytes((seed.bit_length() + 7) // 8, 'big'))

    # get size of file:
    file_size = os.path.getsize("seed.txt")
    shan_scale = compute_shannon_entropy(bits)
    if verbose:
        print(f"Gained {file_size} bits of entropy.")
        print(f"Shannon entropy: {shan_scale}")

    if shan_scale < 0.9999:
        raise Exception("Entropy is too low. Try again.")
    
    return seed.to_bytes((seed.bit_length() + 7) // 8, 'big'), file_size, shan_scale
