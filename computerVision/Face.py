import cv2

face_cascade= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img=cv2.imread("test.jpg")
#  Converting the img to gray image


gray_img= cv2.cvtColor(img ,cv2.COLOR_BGR2GRAY )
cv2.imshow("face",gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()