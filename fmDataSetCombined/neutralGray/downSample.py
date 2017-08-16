import cv2
import os, sys, re

for root, dirs, files in os.walk("."):
    for file in files:
        if "jpg" not in file:
            continue
        image = cv2.imread(file)
        
        # we need to keep in mind aspect ratio so the image does
        # not look skewed or distorted -- therefore, we calculate
        # the ratio of the new image to the old image
        r = 92.0 / image.shape[1]
        dim = (92, int(image.shape[0] * r))

        # perform the actual resizing of the image and show it
        resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
        cv2.imwrite(file,resized)