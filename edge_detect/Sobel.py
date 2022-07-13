import cv2
from cv2 import Sobel
from cv2 import imwrite
from cv2 import CV_16S
import numpy as np
img = cv2.imread("filter_pra/lena_gaussian-noise.png",0)
x = cv2.Sobel(img, cv2.CV_16S, 1, 0, ksize = 1)
y = cv2.Sobel(img, cv2.CV_16S, 0, 1, ksize = 1)

absX = cv2.convertScaleAbs(x)
absY = cv2.convertScaleAbs(y)

dst1 = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)
dst1 = dst1.astype(dtype = np.uint8)

dst2 = np.zeros_like(absX, dtype = np.uint16)
dst2 = absX + absY
dst2 = dst2.astype(dtype = np.uint8)
#print(dst2)

dst3 = np.zeros_like(dst2, dtype = np.uint16)
dst3[:, :] = dst2[:, :]
dst3 = dst3.astype(dtype = np.uint8)
#print(dst3)

dst3[np.where(np.logical_and(dst3 >= 30, dst3 <= 60))] = 50
dst3[np.where(dst3 < 30)] = 0
dst3[np.where(dst3 > 60)] = 220


cv2.imshow("1", dst1)
cv2.imshow("2", dst2)
cv2.imshow("3", dst3)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""imwrite("./sobel1.png", dst1)
imwrite("./sobel2.png", dst2)
imwrite("./sobel3.png", dst3)"""
