#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('/Users/amourlee/Desktop/test.png', 0)

laplacian = cv2.Laplacian(img, cv2.CV_64F)

sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize = 5)

sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize = 5)

images = [ img, laplacian, sobelx, sobely]
titles = [ 'Original', 'Laplacian', 'Sobel X', 'Sobel Y']

for i in range(4):
    plt.subplot(2, 2, i+1), plt.imshow(images[i],'gray')
    plt.title(titles[i]), plt.xticks([]), plt.yticks([])

plt.show()
