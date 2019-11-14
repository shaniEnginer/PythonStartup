import cv2

import glob
images= glob.glob("*.jpg")
for i in images:
    cv2.imread(i)
    img=cv2.imread(i)
    re=cv2.resize(img,(100,100))
    cv2.imwrite("resized"+i,re)