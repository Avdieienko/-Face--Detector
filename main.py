import cv2

alg = "haarcascade_frontalface_default.xml"
haar_cascade = cv2.CascadeClassifier(alg)


#Enable webcam
cap = cv2.VideoCapture(0)
while True:
    #Importing pig photo
    pig = cv2.imread("pig.png", 1)

    text = "No hohol"
    #Capturing webcam as an image
    ret, frame = cap.read()
    #Flipping it vertically
    frame = cv2.flip(frame, 1)
    #Creating gray versioon of the frame
    grayImg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #Detecting face coordinates
    face = haar_cascade.detectMultiScale(grayImg,1.3,4)

    text2 = ""
    #drawing the rectangle
    for (x, y, w, h) in face:
        pig = cv2.resize(pig, (w, h))
        text = "Hohol detected"
        frame[y:y+h, x:x+w] = pig
        if w>130 :
            text2 = "Go away hohol"
    #Putting text
    frame = cv2.putText(frame, text2, (x+10, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2, cv2.LINE_AA)
    frame = cv2.putText(frame, text, (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2,(0,0,255),4,cv2.LINE_AA)

    #Press q to quit the window
    cv2.imshow("Window", frame)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
