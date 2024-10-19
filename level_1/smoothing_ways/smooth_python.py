import numpy as np
import plotly.express as px
import cv2
import os

def xy(left_right_value,odd_size):
    if left_right_value>0:
        x=y=np.linspace(-left_right_value,left_right_value,odd_size)
        return x,y
    else:
        print("left_right_value has to be greater than zero")
        exit(0)

def gaussian(x,y,sigma=1):
    xx,yy=np.meshgrid(x,y)
    g=np.exp(-(xx**2+yy**2)/(2*sigma**2))
    return g/np.sum(g)

def padded(image,pad_size):
    return np.pad(image,((pad_size,pad_size),(pad_size,pad_size),(0,0)),mode='constant')
def smooth(image,kernel):
    height,width,channels=image.shape

    pad_size=kernel.shape[0]//2
    kernel_size=kernel.shape[0]
    ## padded image
    padded_image=padded(image,pad_size=pad_size)

    ## output image
    output=np.zeros((image.shape),dtype=np.uint8)

    for h in range(height):
        for w in range(width):
            # region=padded_image[h:h+kernel_size,w:w+kernel_size,:]
            rgb_vec=np.zeros((1,3))
            for c in range(channels):
                rgb_vec[:,c]+=np.sum(kernel*padded_image[h:h+kernel_size,w:w+kernel_size,c])
            output[h,w]=rgb_vec
    return output


def main():
    image='Play_Numy_vs_Python/Begineers/smoothing_ways/image.jpg'

    # read image
    img=cv2.imread(image)
    # img=img[:,:,::-1]

    x,y=xy(3,5)
    kernel=gaussian(x,y)

    out=smooth(img,kernel)

    cv2.imshow('out',out)
    cv2.waitKey(0)
    # cv2.destoryAllWindows()

if __name__=="__main__":
    main()