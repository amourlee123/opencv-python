#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on Feb 20 2017
@author: amourleey

"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('/Users/amourlee/Desktop/test.jpg')
b, g, r = cv2.split(img)
img2 = cv2.merge([r, g, b])
plt.subplot(121);plt.imshow(img)
plt.subplot(122);plt.imshow(img2)
plt.show()

cv2.imshow('bgr image', img)
cv2.imshow('rgb image', img2)
cv2.waitKey( 0 )
cv2.destroyAllWindows()
