import cv2
import numpy as np

img1=cv2.imread("lena.jpg")
img=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY) 

cv2.imshow("Main Image",img)

fac=1
row=img.shape[0]
col=img.shape[1]

for x in range(row):
    for y in range(col):
        img[x][y] = np.exp((img[x][y])**fac)-1

cv2.imshow("Final Image(Inverse Log)",img)
cv2.waitKey()
cv2.destroyAllWindows()