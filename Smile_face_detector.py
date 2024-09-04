from random import randrange

import cv2

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_detector = cv2.CascadeClassifier('haarcascade_smile.xml')

# To capture video from webcam
webcam = cv2.VideoCapture(0)

while True:
    # Reads single frame
    successful_frame_read, frame = webcam.read()

    if not successful_frame_read:
        break

    # convert the image to greyscale
    frame_greyscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces first
    faces = face_detector.detectMultiScale(frame_greyscale)
    # smiles = smile_detector.detectMultiScale(frame_greyscale)

    # Draw the rectangles around the faces
    for (x, y, w, h) in faces:
        # 4 is thickness of rectangle
        cv2.rectangle(frame, (x, y), (x + w, y + h), (100, 200, 50), 4)

        # Get the sub frame using numpy N-dimensional array slicing
        the_face = frame[y:y+h, x:x+w]

        # change to greyscale
        face_greyscale = cv2.cvtColor(the_face, cv2.COLOR_BGR2GRAY)
        smile = smile_detector.detectMultiScale(face_greyscale, scaleFactor=1.7, minNeighbors=20)

        # Run smile detection within each of those faces
        # for (x_, y_, w_, h_) in smile:
        #     cv2.rectangle(the_face, (x_, y_), (x_ + w_, y_ + h_), (100, 200, 50), 4)

        if len(smile) > 0:
            cv2.putText(frame, "smiling", (x, y+h+40), fontScale=3,
                        fontFace=cv2.FONT_HERSHEY_PLAIN, color=(255,255,255))
    cv2.imshow("Smile Detector ", frame)
    cv2.waitKey()

    # Release video capture object
    webcam.release()
    cv2.destroyAllWindows()
    print("Code completed")
