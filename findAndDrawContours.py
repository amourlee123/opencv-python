#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np

im = cv2.imread('/Users/amourlee/Desktop/rectangle.png')
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(imgray, 127, 255, 0)
image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]
M = cv2.moments(cnt)

area = cv2.contourArea(cnt)
perimeter = cv2.arcLength(cnt, True)
epsilon = 0.1 * perimeter

approx = cv2.approxPolyDP(cnt, epsilon, True)
#pts = np.array(approx, uint8)
print(approx[1])
print(cnt)
print(perimeter)
print(area)
print(M)
print(M['m00'])



cv2.namedWindow('image')
# cv2.namedWindow('approx')
while(1):
    cv2.imshow('image', image)
  #  cv2.imshow('approx', pts)
    k = cv2.waitKey(1)
    if k == 27:
        break

cv2.destroyAllWindows()

