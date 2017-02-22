#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sun Feb 19 2017

@author: amourleey
"""

import numpy as np
import cv2

# load a color image in grayscale
img = cv2.imread('/Users/amourlee/Desktop/main_building.png', 0)
cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
cv2.imshow('image', img)
k = cv2.waitKey(0)

# wait for ECS key to exit
if k == 27:
    cv2.destroyWindow('image')

# wait for 's' key to save and exit
elif k == ord('s'):
    cv2.imwrite('/Users/amourlee/Desktop/gray.png', img)
    cv2.destroyAllWindows()
