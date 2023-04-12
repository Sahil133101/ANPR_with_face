# Python code to read image


import pytesseract
import cv2


path = "C:/Users/hp/Downloads/Compressed/Car-Number-Plates-Detection-main/Car-Number-Plates-Detection-main/plates/14.jpg"
img = cv2.imread(path)

img = cv2.resize(img, (600, 360))
#pytesseract.pytesseract.tesseract_cmd =r"D:/Tesseract-OCR/tesseract.exe"
#print("hwllo")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#noise removal
noise=cv2.medianBlur(gray,3)
# thresholding# converting it to binary image by Thresholding
# this step is require if you have colored image because if you skip this part
# then tesseract won’t able to detect text correctly and this will give incorrect #result
thresh = cv2.threshold(noise, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
#Configuration
config = ("-l eng — oem 3 — psm 3")
# pytessercat
text = pytesseract.image_to_string(thresh,config=config)
print(text)
