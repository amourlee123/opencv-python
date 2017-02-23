#!/usr/bin/env python
# -*- coding:utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('/Users/amourlee/Desktop/equalization.png', 0)


hist, bins = np.histogram(img.flatten(), 256, [0, 256])

cdf = hist.cumsum()
cdf_m = np.ma.masked_equal(cdf, 0)
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
cdf = np.ma.filled(cdf_m, 0).astype('uint8')
img2 = cdf[img]

# flatten()将数组变成一维
hist, bins = np.histogram(img2.flatten(), 256, [0, 256])

# 计算累积分布图
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max() / cdf.max()

plt.plot(cdf_normalized, color = 'b')
plt.hist(img2.flatten(), 256, [0, 256], color = 'r')
plt.xlim([0, 256])
plt.legend(('cdf', 'histogram'), loc = 'upper left')

plt.subplot(121),plt.imshow(img, 'gray')
plt.title('img'),plt.xticks([]),plt.yticks([])

plt.subplot(122),plt.imshow(img2, 'gray')
plt.title('img2'),plt.xticks([]),plt.yticks([])
plt.show()
