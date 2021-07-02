#!/usr/bin/env python3
import cv2 as cv
import sys

img = cv.imread('myvi-category-image.png')

if img is None:
    sys.exit("Could not read image")

cv.imshow('Myvi 2021',img)
quit = cv.waitKey(0)

if quit == ord("q"):
    print("exit")
    cv.destroyAllWindows()
