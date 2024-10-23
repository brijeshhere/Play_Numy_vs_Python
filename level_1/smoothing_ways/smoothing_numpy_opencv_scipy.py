import numpy as np
import cv2
from scipy.signal import fftconvolve


def kernel(size,sigma=1):
    x=y=np.linspace(-3,3,size)
    xx,yy=np.meshgrid(x,y)
    g=np.exp(-(xx**2+yy**2)/(2*sigma**2))
    return g/np.sum(g)



def main():
    file='Play_Numy_vs_Python/level_1/image.jpg'

    image=cv2.imread(file)

    ker=kernel(11)
    # numpy
    blur=np.convolve(image,ker)

    cv2.imshow('Image',blur)
    cv2.waitKey(0)
    cv2.destoryAllWindows()

if __name__=="__main__":
    main()