import cv2 as cv
import numpy as np

img=cv.imread("Lena.jpg",cv.IMREAD_GRAYSCALE)
cv.imshow("Main Image",img)

min=img.min()
max=img.max()
imgg=img

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if img[i][j]>=0 and img[i][j]<=min:
            imgg[i][j]=0
        elif(img[i][j]>min and img[i][j]<=max):
            imgg[i][j]=((img[i][j] - min)/(max-min))*255
        else:
            imgg[i][j]=255

cv.imshow("Final Image(Contrast Streching)",imgg)
cv.waitKey()
cv.destroyAllWindows()