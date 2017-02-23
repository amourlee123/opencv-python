#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt

img_rgb = cv2.imread('/Users/amourlee/Desktop/mario.png')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('/Users/amourlee/Desktop/coin.png', 0)

w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
thresh = 0.8

loc = np.where( res >= thresh)
for pt in zip(*loc[::-1]):
    print pt
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 1)

cv2.imshow('RES', img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
