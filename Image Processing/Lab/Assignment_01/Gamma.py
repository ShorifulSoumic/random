import cv2
import numpy as np

img1=cv2.imread("Lena.jpg")
img=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY) 

cv2.imshow("Main Image",img)

row=img.shape[0]
col=img.shape[1]

up=255
gamma=.2

for x in range(row):
    for y in range(col):
        img[x][y] = up * ((img[x][y]/255)**gamma)

img = np.array(img,dtype=np.uint8)
cv2.imshow("Final Image(Gamma)",img)
cv2.waitKey()
cv2.destroyAllWindows()