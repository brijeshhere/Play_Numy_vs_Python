import numpy as np
import cv2

def apply_edge_kernel(image,kernel):
    height,width,channel=image.shape
    kernel_height,kernel_width=kernel.shape
    pad_h,pad_w=kernel_height//2,kernel_width//2
    padded=np.pad(image,((pad_h,pad_h),(pad_w,pad_w),(0,0)),mode='constant',constant_values=0)
    output=np.zeros((image.shape),dtype=np.uint8)
    for h in range(height):
        for w in range(width):
            region=padded[h:h+kernel_height,w:w+kernel_width,:]
            rgb_vec=np.zeros((1,3))
            for c in range(channel):
                rgb_vec[:,c]=np.sum(kernel*region[:,:,c])
            output[h,w]=rgb_vec
    return output
kernel = np.array([
    [1, 2, 1],
    [2, 4, 2],
    [1, 2, 1]
]) / 16
image=cv2.imread('C:/Users/Windows/Desktop/hello/Play_Numy_vs_Python/level_1/image.jpg')
output=apply_edge_kernel(image,kernel)
output=cv2.resize(output,(150,300))

cv2.imshow("image",output)
cv2.waitKey(0)
