import cv2
from PIL import Image
import pytesseract


src_img1 = cv2.imread("./text.jpg", cv2.IMREAD_UNCHANGED)
#src_img1 = cv2.cvtColor(src_img1, cv2.COLOR_BGR2RGB)
#src_img1 = Image.open("text.jpg")
text1 = pytesseract.image_to_string(src_img1, lang = "chi_tra")

"""src_img2 = cv2.imread("./eng_text.jpg", cv2.IMREAD_UNCHANGED)
src_img2 = cv2.cvtColor(src_img2, cv2.COLOR_BGR2RGB)
text2 = pytesseract.image_to_string(src_img2, lang = "eng")

src_img3 = cv2.imread("./color_text.jpg", cv2.IMREAD_UNCHANGED)
src_img3 = cv2.cvtColor(src_img3, cv2.COLOR_BGR2RGB)
text3 = pytesseract.image_to_string(src_img3, lang = "eng")"""

print(text1)
