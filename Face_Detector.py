import cv2
from random import randrange

# Load a pre-trained data from face from opencv
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# choose the image to read the face in
# img = cv2.imread('Krishnan_Pic.PNG')
# To capture video from webcam
webcam = cv2.VideoCapture(0)
# iterate over frames
while True:
    # read the current frame
    successful_frame_read, frame = webcam.read()


# convert the image to greyscale
    greyscale_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# # Detect faces
#     face_coordinates = trained_face_data.detectMultiScale(greyscale_img)
#
# # Draw the rectangles around the faces
#     for (x, y, w, h) in face_coordinates:
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (randrange(256), randrange(256), randrange(256)), 10)

# print(face_coordinates)

    cv2.imshow("Clever Python Face Detector App", frame)
    # waitkey function of Python OpenCV allows users to display a window for given milliseconds or until any key is
    # pressed. It takes time in milliseconds as a parameter and waits for the given time to destroy the window,
    # if 0 is passed in the argument it waits till any key is pressed.
    key = cv2.waitKey(1)

    print("Code completed")
