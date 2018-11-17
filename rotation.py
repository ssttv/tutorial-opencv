import numpy as np
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

rotated = imutils.rotate(image, 45, scale=1.0)
cv2.imshow("Rotated by 45 degrees", rotated)
cv2.waitKey(0)
