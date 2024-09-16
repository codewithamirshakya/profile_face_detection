import cv2
import numpy as np

def detect_faces(image_path):
    # Load the Haar Cascade model
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Read the image
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Could not read image")
        return

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw rectangles around faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Display the output
    cv2.imshow('Detected Faces', img)
    cv2.waitKey()

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if cv2.waitKey(99) & 0xFF == ord('c'):
        image_path = 'face-original.jpg'
        cv2.imwrite(image_path, frame)
        detect_faces(image_path)

cap.release()
cv2.destroyAllWindows()