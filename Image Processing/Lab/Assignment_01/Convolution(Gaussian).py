import cv2 
import numpy as np
import math

img=cv2.imread("Lena.jpg")
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgg=np.zeros(img_gray.shape)

def padding(karnel,x,y):
    n=karnel.shape[0]
    m=karnel.shape[1]

    pad=[]
    pad.append(n-1-x)
    pad.append(x)
    pad.append(m-1-y)
    pad.append(y)
    return pad

def border(img,l):
    gray=cv2.copyMakeBorder(src=img,top=pad[0],bottom=pad[1],left=pad[2],right=pad[3],borderType=cv2.BORDER_CONSTANT)
    return gray

def gaussian(width,hight,cen_x,cen_y,):
    kernel=np.ones((width,hight),dtype='float32')
    s=sigma**2
    c=2*math.pi*s
    c=1/c
    for i in range(0,width):
        for j in range(0,hight):
            p = ((i-cen_x)**2 + (j-cen_y)**2)/(2*s)
            kernel[i,j]=math.exp(-p)/c
    return kernel


width=5
hight=5
sigma=5
cx=4
cy=4

karnel=gaussian(width,hight,cx,cy)
pad=padding(karnel,cx,cy)
temp=border(img_gray,pad)

    
def cnv(img,karnel,row,col):
    a=img.shape
    b=karnel.shape
    for i in range(pad[0],pad[0]+a[0]):
        for j in range(pad[2],pad[2]+a[1]):
            total=0
            for ii in range(-row,b[0]-row):
                for jj in range(-col,b[1]-col):
                    l=i-ii
                    r=j-jj
                    total+=temp[l][r]*karnel[ii+row][jj+col]
            imgg[i-pad[0]][j-pad[2]]=total
            

cnv(img_gray,karnel,cx,cy)
cv2.normalize(imgg,imgg,0,255,cv2.NORM_MINMAX)
imgg=np.round(imgg).astype(np.uint8)

cv2.imshow("Main Image",img_gray)
cv2.imshow("Final Image(Gaussian)",imgg)

cv2.waitKey(0)
cv2.destroyAllWindows()