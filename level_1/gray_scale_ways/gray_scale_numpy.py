import numpy as np
import cv2
import os

# get file
file='image.jpg'
file_path=os.path.join('Play_Numy_vs_Python/Begineers',file)

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


# print(image[0][0])
# print(gray_mat)
# print(np.dot(np.matmul(image[0][0],gray_mat),gray_mat[0]))
# print(np.dot(image[0][0],gray_mat[0]))
# print(C)
## here
for i in range(height):
    for j in range(width):
        C[i][j]=np.dot(np.matmul(image[i][j],gray_mat),gray_mat[0])
        

# Show image
cv2.imshow('image',C)
cv2.waitKey(0)