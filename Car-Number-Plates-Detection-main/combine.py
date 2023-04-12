import cv2
import easyocr
import os
import time
import csv
harcascade = "model/haarcascade_russian_plate_number.xml"

cap = cv2.VideoCapture(0)
cap.set(3, 640) # width
cap.set(4, 480) # height

min_area = 600
count = 0

if not os.path.exists('number_plates'):
    os.makedirs('number_plates')

while True:
    success, img = cap.read()

    plate_cascade = cv2.CascadeClassifier(harcascade) # load harcascade model
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # change color bgr to gray

    plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)  # load cascade model, arguments are by default

    for (x,y,w,h) in plates:
        area = w * h

        if area > min_area:
            cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
            cv2.putText(img, "Number Plate", (x,y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)

            img_roi = img[y: y+h, x:x+w]  # crop image
            cv2.imshow("ROI", img_roi)

            # write image to file
            cv2.imwrite('number_plates/plate_{}.png'.format(str(time.time())), img)

            # read image from file
            img1 = cv2.imread('number_plates/plate_{}.png'.format(str(time.time())))

            # perform OCR on image
            reader = easyocr.Reader(['ch_sim', 'en'])  # this needs to run only once to load the model into memory
            npData = reader.readtext(img_roi)

        result = ''

        for item in npData:
            for val in item:
                if isinstance(val, str):
                    result += val

        with open('results.csv', 'a', newline = '') as file:
            writer = csv.writer(file)
            writer.writerow(result) 

    cv2.imshow("Result", img)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()