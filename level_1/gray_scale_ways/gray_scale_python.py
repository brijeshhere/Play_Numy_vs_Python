import numpy as np
import cv2
import os

# get file
file='image.jpg'
file_path=os.path.join('Begineers',file)

# Read file
image=cv2.imread(file_path)

## Get image dims
height=image.shape[0]
width=image.shape[1]
channels=image.shape[2]

# Gray scale

## 1/3 mat
gray_mat=np.full((3,3),1/3)
cols_of_gray_mat=gray_mat.shape[0]

## Store matrix
C=np.zeros((height,width),dtype=np.uint8)

## here
for i in range(height):
    for j in range(width):
        gray_value=0
        for a in range(channels):
            for b in range(cols_of_gray_mat):
                gray_value+=image[i][j][b]*gray_mat[b][a]
        C[i][j]=gray_value/3


# Show image
cv2.imshow('image',C)
cv2.waitKey(0)