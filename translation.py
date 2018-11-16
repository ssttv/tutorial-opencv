import numpy as np
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
                help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

shifted = imutils.translate(image, 40, 50)
cv2.imshow("Shifted Down-Right", shifted)

shifted = imutils.translate(image, -50, -25)
cv2.imshow("Shifted Up-Left", shifted)