#/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('/Users/amourlee/Desktop/test.jpg')

# plt.hist(img.ravel(), 256, [0, 256])
# plt.show()



# BGR

color = ('b', 'g', 'r')

for i, col in enumerate(color):
    histr = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot( histr, col)
    plt.xlim([0, 256])

plt.show()
