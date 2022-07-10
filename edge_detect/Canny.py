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
img = cv2.imread("/home/tdd/python_practice/edge_detect/frogg.jpg", 0)
img = cv2.GaussianBlur(img, (5,5), sigmaX= 2, sigmaY=2)
canny = cv2.Canny(img, 50, 100)
cv2.imshow("canny", canny)
cv2.imwrite("./canny.png", canny)
cv2.waitKey(0)
cv2.destroyAllWindows()
