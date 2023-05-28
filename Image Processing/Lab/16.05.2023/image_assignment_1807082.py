import cv2
import matplotlib.pyplot as plt
import numpy as np
import math
 
def gaussian(sigma, mean):
    temp=np.zeros(256,dtype=np.float32)
    for i in range(256):
        r=i-mean
        r=(r**2)/(sigma**2)
        r=math.exp(-r)/(sigma*math.sqrt(2*math.pi))
        temp[i]=r
    return temp
    
img=cv2.imread("lena.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Main Image",img)

L=256
height, width = img.shape

input_histogram = cv2.calcHist([img],[0],None, [256], [0,256])
pdf = input_histogram/(height*width)
cdf = np.zeros(256, dtype=np.float32)
cdf[0]=pdf[0]
s=pdf

for i in range(1, 256):
    cdf[i] = cdf[i-1] + pdf[i]
    s[i]=round((L-1)*cdf[i]) 
        
equalized_img=np.zeros_like(img)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        x=img[i][j]
        equalized_img[i][j]=s[x]

plt.subplot(2,2,1)
plt.title("Input Image")
plt.hist(img.ravel(),256,[0,256])

plt.subplot(2,2,2)
plt.title("Equalized Image")
plt.hist(equalized_img.ravel(),256,[0,256])

sigma_a=20
mean_a=100
g1=gaussian(sigma_a, mean_a)

sigma_b=28
mean_b=150
g2=gaussian(sigma_b,mean_b)

gauss=g1+g2
target_pdf=np.zeros(256)
target_pdf=gauss/gauss.sum()
print(target_pdf.sum())

plt.subplot(2,2,3)
plt.title("Target Histogram")
plt.plot(g1)
plt.plot(g2)
plt.plot(gauss)
plt.show()

G=np.zeros(256)
target_cdf=np.zeros(256)

target_cdf[0]=target_pdf[0]

for i in range(1,256):
    target_cdf[i]=target_cdf[i-1]+target_pdf[i]
    G[i]=round((L-1)*target_cdf[i])

map=np.zeros(256,dtype=np.int64)

for i in range(256):
    x=np.searchsorted(G, s[i])
    if x>0 and abs(s[i]-G[x-1])<abs(G[x]-s[i]):
        x=x-1
    map[int(s[i])]=x

matched_image=np.zeros_like(img)
for i in range(equalized_img.shape[0]):
    for j in range(equalized_img.shape[1]):
        x=equalized_img[i][j]
        matched_image[i][j]=map[x]
        
cv2.imshow("output",matched_image)

plt.subplot(2,2,4)
plt.title("Final Histogram")      
plt.hist(matched_image.ravel(),256,[0,256])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()