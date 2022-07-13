import cv2
from cv2 import Sobel
from cv2 import imread
from cv2 import imshow
from cv2 import GaussianBlur
import numpy as np

retval = cv2.useOptimized()
cv2.setUseOptimized(True)
print("Optimized:", retval)
#--------------加速---------------
img = cv2.imread("filter_pra/lena_gaussian-noise.png")
#img = cv2.GaussianBlur(img, (5,5), sigmaX= 2, sigmaY=2)
for i in range(3, 9, 2):
    canny = cv2.Canny(img, 150, 200, apertureSize=i )
    cv2.imshow("canny", canny)
    cv2.waitKey(0)
    
#cv2.imwrite("./canny.png", canny)

