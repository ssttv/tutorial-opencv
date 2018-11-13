from __future__ import print_function
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="Path to the image")

image = cv2.imread(vars(ap.parse_args())["image"])
cv2.imshow("Original", image)