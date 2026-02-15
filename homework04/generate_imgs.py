#!/usr/bin/env python3

import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

# Load our pattern
IMG = 'filter_imgs'
if not os.path.exists(IMG):
    os.makedirs(IMG, exist_ok=True)

gray = cv2.imread("pattern.png",cv2.IMREAD_GRAYSCALE)

for i in range(5, 16):
    for j in range(2, 5):
        for k in range(2, 5):
            ksize = i     # try something between 5 and 15
            sigma = j     # try something between 2.0 and 4.0
            theta = 0.0     # keep it 0.0 if you want to focus on vertically-oriented patterns 
            lbd = k       # try something between 2.0 and 4.0
            gamma = 1.0     # keep it 1.0
            psi = 0.0       # keep it 0.0

            kernel = cv2.getGaborKernel((ksize, ksize), sigma, theta, lbd, gamma, psi, ktype=cv2.CV_32F)
            kernel /= kernel.sum()
            kernel -= kernel.mean()

            res1 = cv2.filter2D(gray, cv2.CV_8UC3, kernel)
            path = os.path.join(IMG, f"fp_ksize_{i}_sigma_{j}_lbd_{k}.png")
            cv2.imwrite(path, res1)