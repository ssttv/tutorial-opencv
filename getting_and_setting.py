from __future__ import print_function
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="Path to the image")

image = cv2.imread(vars(ap.parse_args())["image"])
cv2.imshow("Original", image)

(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r,
                                                              g, b))

image[0, 0] = (0, 0, 255)
(b, g, r) = image[0, 0]
print("New values of the pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r,
                                                              g, b))
