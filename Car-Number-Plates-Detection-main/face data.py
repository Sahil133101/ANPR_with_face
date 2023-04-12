import cv2
import os
import time



# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier('C:/python37/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')

# Start the video capture
cap = cv2.VideoCapture(0)

# Create a directory to save the detected faces
if not os.path.exists('detected_faces'):
    os.makedirs('detected_faces')

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)

    # Draw rectangles around the detected faces and save them to a folder
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Extract the face from the image
        face_img = gray[y:y+h, x:x+w]

        # Save the extracted face to a file in the detected_faces folder
        filename = os.path.join('detected_faces', f'face_{x}_{y}_{w}_{h}.jpg')
        cv2.imwrite(filename, face_img)

    # Display the resulting frame
    cv2.imshow('Face Recognition', frame)

    # Wait for 'q' key to exit
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()
