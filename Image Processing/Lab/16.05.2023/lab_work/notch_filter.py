import numpy as np
import matplotlib.pyplot as plt
import math 
import cv2 as cv
import matplotlib

def min_max_normalize(img_inp):
    inp_min = np.min(img_inp)
    inp_max = np.max(img_inp)

    for i in range (img_inp.shape[0]):
        for j in range(img_inp.shape[1]):
            img_inp[i][j] = (((img_inp[i][j]-inp_min)/(inp_max-inp_min))*255)
    return np.array(img_inp, dtype='uint8')

img = cv.imread('input.jpg',cv.IMREAD_GRAYSCALE)

f1 = plt.figure(1)
plt.title("Input Image")
plt.imshow(img,'gray')

D0 = float(input("Enter a radious: \n"))

M = img.shape[0]
N = img.shape[1]

f = np.fft.fft2(img)
shift = np.fft.fftshift(f)
mag = np.abs(shift)

matplotlib.use('TkAgg')

point_list=[]

img = np.zeros((10,12), np.uint8)
img=mag
img[4:6, 5:7] = 1
# click and seed point set up
x = None
y = None

# The mouse coordinate system and the Matplotlib coordinate system are different, handle that
def onclick(event):
    global x, y
    ax = event.inaxes
    if ax is not None:
        x, y = ax.transData.inverted().transform([event.x, event.y])
        x = int(round(x))
        y = int(round(y))
        print('button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
              (event.button, event.x, event.y, x, y))
        point_list.append((x,y))


X = np.zeros_like(img)
plt.title("Please select seed pixel from the input")
im = plt.imshow(img, cmap='gray')
im.figure.canvas.mpl_connect('button_press_event', onclick)
plt.show(block=True)

print(point_list)

angle = np.angle(shift)

f1 = plt.figure(3)
plt.title("input image spectrum")
plt.imshow(np.log(mag),'gray')
pp = np.log(mag)

filter = np.zeros((M,N),np.float32)

for i in range(M):
    for j in range(N):
        filter1 = np.zeros((M,N),np.float32)
        for (x, y) in point_list:
            a = M - x
            b = N - y
            
            if i>=M//2 and j>=M//2:
                D = math.sqrt((i-x)**2 + (j-y)**2)
            if i<M//2 and j<M//2:
                D = math.sqrt((i-a)**2 + (j-b)**2) 

            if D: 
                h=(1/(1+(D0/D)))
            else:
                h=0

            if D<=D0:    
                filter1[i][j] = h
            else:
                filter1[i][j] = 0
    filter = filter1 * filter


f1 = plt.figure(2)
plt.title("Filter Image")
filter=min_max_normalize(filter)
plt.imshow(filter,'gray')
mag = mag * filter


inv = np.multiply(mag,np.exp(1j * angle))

inv_shift = np.fft.ifftshift(inv)

out = np.real(np.fft.ifft2(inv_shift))

f1 = plt.figure(4)
plt.title("input image spectrum")
plt.imshow(pp * filter,'gray')

f1 = plt.figure(5)

plt.title("Ouput Image")
plt.imshow(out,'gray')
plt.show()        
        
        
plt.subplots_adjust(left=0.1,
                    bottom=0.1,
                    right=0.9,
                    top=0.9,
                    wspace=0.4,
                    hspace=0.4)


cv.waitKey()
cv.destroyAllWindows()