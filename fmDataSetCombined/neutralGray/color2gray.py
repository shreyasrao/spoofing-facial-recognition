import cv2
import os, sys, re

for root, dirs, files in os.walk("."):
    for file in files:
        if "jpg" not in file:
            continue
        image = cv2.imread(file)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(file,gray_image)