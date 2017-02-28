#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np

img = cv2.imread('/Users/amourlee/Desktop/coins.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)


cv2.imshow('im', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
