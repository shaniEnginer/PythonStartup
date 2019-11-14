import cv2 ,time
while True:
    video = cv2.VideoCapture(0)
    check , frame =video.read()
    print(frame)
    cv2.imshow("Test" ,frame)


    cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # time.sleep(1)

    cv2.waitKey(1)
video.release()
cv2.destroyAllWindows()

