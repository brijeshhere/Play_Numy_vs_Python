import numpy as np
import cv2
import plotly.express as px

def scale_image(image,dims):
    new_height,new_width=dims

    height,width,channel=image.shape

    
    scale_y=new_height/height #0.5
    scale_x=new_width/width

    resized_image=np.zeros((new_height,new_width,channel),dtype=image.dtype)

    for i in range(new_height):
        for j in range(new_width):

            new_y=int(i/scale_y)
            new_x=int(j/scale_x)

            new_y=min(new_y,height-1)
            new_x=min(new_x,width-1)

            resized_image[i,j]=image[new_y,new_x]
    return resized_image

image=cv2.imread('C:/Users/Windows/Desktop/hello/Play_Numy_vs_Python/level_1/image.jpg')
cv2.imshow("image",scale_image(image,(640,480)))
print(scale_image(image,(640,480)).shape)
print(image.shape)

cv2.waitKey(0)
# px.imshow(scale_image(image,(640,480)))

