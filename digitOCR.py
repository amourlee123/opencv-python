#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('/Users/amourlee/Desktop/digits.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Now we splite the image to 5000 cells, each 20x20 size
cells = [np.hsplit(row, 100) for now in np.vsplit(gray, 50)]

# 
