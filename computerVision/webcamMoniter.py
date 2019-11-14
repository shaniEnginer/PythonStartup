import cv2
fist_frame=None
video = cv2.VideoCapture(0)
# a=0


while  True:
    check ,frame=video.read()
    gray= cv2.cvtColor(frame ,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(21,21),0)
    status=0

    if fist_frame is None:
        fist_frame=gray
        continue

    delta_frame=cv2.absdiff(fist_frame,gray)
    threshed_delta=cv2.threshold(delta_frame,30,255, cv2.THRESH_BINARY)[1]
    threshed_delta=cv2.dilate(threshed_delta,None,iterations=2)
    
    cnts, test =cv2.findContours(threshed_delta.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    # cv2.findContours()
    for counters in cnts:
        if cv2.contourArea(counters)<1000:
            continue
        status=1

        (x,y,w,h)=cv2.boundingRect(counters)
        cv2.rectangle(frame,(x,y) ,(x+w,y+h),(0,255,0),3)




    cv2.imshow("image" ,gray)
    cv2.imshow("delta" ,delta_frame)
    cv2.imshow("Threshedframe",threshed_delta)
    cv2.imshow("color area",frame)


    key =cv2.waitKey(0)
    print(gray)

    if key==ord("q"):
        break

    print(status)



video.release()
cv2.destroyAllWindows()