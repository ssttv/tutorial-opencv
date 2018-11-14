import numpy as np
import cv2

canvas = np.zeros((400,4,3), dtype="unit8")

green = (0, 255, 0)
cv2.line(canvas,(0,0), (300,300), green)
cv2.imshow("Canvas", canvas)
cv2.waitkey(0)

red = (0, 0, 255)
cv2.line(canvas,(300,0), (169,300), red)
cv2.imshow("Canvas", canvas)
cv2.waitkey(0)