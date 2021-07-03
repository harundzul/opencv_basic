#!/usr/bin/env python3
## This is tutorial how to resize an image, crop and rotate.
## The image should be in same directory else need to include specify directory.

import cv2 as cv
import sys

img = cv.imread('myvi-category-image.png')

if img is None:
    sys.exit("Could not read image")

## Resize to 640x480
resize_img = cv.resize(img,(640,480))
## Crop at pixel row:200 to 400 and col:100 to 300
cropped_img = resize_img[200:400,100:300]
## Rotate the resized image
rotate_img = cv.rotate(resize_img,cv.ROTATE_90_CLOCKWISE)
## Save edited image
filename = 'save-image.jpg'
cv.imwrite(filename,cropped_img)

cv.imshow('Resize to specific resolution',resize_img)
cv.imshow('Cropped image',cropped_img)
cv.imshow('Rotate to 180 degree',rotate_img)

quit = cv.waitKey(0)

if quit == ord("q"):
    print("exit")
    cv.destroyAllWindows()
