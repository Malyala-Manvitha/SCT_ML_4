import cv2
import joblib

model=joblib.load("model/gesture_model.pkl")

cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(5,5),0)
    _,th=cv2.threshold(blur,60,255,cv2.THRESH_BINARY_INV)

    contours,_=cv2.findContours(th,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        c=max(contours,key=cv2.contourArea)
        area=cv2.contourArea(c)
        data=[[area,len(contours)]]

        pred=model.predict(data)[0]

        cv2.putText(frame,pred,(50,50),
        cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

        cv2.drawContours(frame,[c],-1,(0,255,0),2)

    cv2.imshow("Gesture",frame)

    if cv2.waitKey(1)==27:
        break

cap.release()
cv2.destroyAllWindows()
