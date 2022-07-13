import cv2
from cv2 import CV_16S
from cv2 import imshow
import numpy as np
src_img = cv2.imread("filter_pra/lena_gaussian-noise.png", cv2.IMREAD_COLOR)

"""src_img = cv2.cvtColor(src_img, cv2.COLOR_BGR2RGB)
X = cv2.getGaussianKernel(ksize=5, sigma=0.7)
gaussian = X * X.T  # gaussian kernel
dst = cv2.filter2D(src_img, CV_16S, gaussian, dst=-1)
dst = dst.astype("uint8")
dst = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)
gaussian_dst = cv2.Canny(dst, 100, 200, apertureSize=3)"""

src_img = cv2.cvtColor(src_img, cv2.COLOR_BGR2RGB)
mean = np.ones((5, 5), np.float32) / (
    pow(5, 2)
)  # mean kernel
dst = cv2.filter2D(src_img, CV_16S, mean, dst=-1)
dst = dst.astype("uint8")
dst = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)
mean_dst = cv2.Canny(dst, 50, 80, apertureSize=3)
cv2.imshow("hi", dst)
cv2.waitKey(0)
cv2.imshow("hi", mean_dst)
cv2.waitKey(0)
