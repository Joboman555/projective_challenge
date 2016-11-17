from scipy import misc
import matplotlib.pyplot as plt
import numpy as np
import cv2

image = cv2.imread('pics/0_1.jpg')
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower = np.array([80, 150, 50])
upper = np.array([180, 255,  70])
shapeMask = cv2.inRange(hsv, lower, upper)
maskedImage = cv2.bitwise_and(image,image, mask= shapeMask)
cv2.imshow('mask', maskedImage)
cv2.waitKey(0)