#!/usr/bin/env python3
## This is tutorial how to open an image
## The image should be in same directory else need to include specify directory.

## Load the module
import cv2 as cv
import sys

## Load the image
img = cv.imread('myvi-category-image.png')

if img is None:
    sys.exit("Could not read image")

## Display the image
cv.imshow('Myvi 2021',img)
quit = cv.waitKey(0)

## Press q to exit
if quit == ord("q"):
    print("exit")
    cv.destroyAllWindows()
