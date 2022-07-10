import cv2
import numpy as np

img = cv2.imread("python_practice/try/frogg.jpg", cv2.IMREAD_COLOR)
img = cv2.GaussianBlur(img, (7,7), 0)
cv2.imshow("hi", img)
cv2.waitKey(0)
cv2.destroyAllWindows()