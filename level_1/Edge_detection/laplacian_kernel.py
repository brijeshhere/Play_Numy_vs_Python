import numpy as np
import cv2

def create_laplacian_like_kernel(size):
    mat=np.zeros((size,size))
    h,w=mat.shape
    center=size//2
    for i in range(h):
        for j in range(w):
            # distance=max(abs(i-center),abs(j-center))
            if abs(i-center)+abs(j-center)<=center:
                mat[i,j]=-1
    mat[center,center]=16
    return mat
print(create_laplacian_like_kernel(5))

