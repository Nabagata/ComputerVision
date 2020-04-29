import cv2
import numpy as np

img = cv2.imread("j.png",0)
kernel = np.ones((5,5), np.uint8)

erosion = cv2.erode(img, kernel, iterations=1)
dilation = cv2.dilate(img, kernel, iterations=1)

opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

cv2.imshow("erosion", erosion)
cv2.imshow("dilation", dilation)

cv2.imshow("opening", opening)
cv2.imshow("closing", closing)
cv2.waitKey(0)
