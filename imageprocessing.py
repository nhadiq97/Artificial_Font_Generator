import numpy as np
 import cv2
 img=cv2.imread('C:/Users/ips/AppData/Local/Programs/Python/Python36-32/name123.jpg',0)
 #otzu binarization
 ret,thr =cv2.threshold(img,0,255,cv2.THRESH_OTSU)
 image, contours, hierarchy = cv2.findContours(thr,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
  for c in contours:
    # bounding rectangle
    x, y, w, h = cv2.boundingRect(c)
    # draw a rectangle
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 0), 2)
    print(len(contours))
cv2.drawContours(img, contours, -1, (255, 255, 0), 1)
idx = 0
#crop induvidual contours
for c in contours:
	x,y,w,h = cv2.boundingRect(c)
	if w>50 and h>50:
		idx+=1
		newimage=image[y:y+h,x:x+w]
    #save induvidual contours
		cv2.imwrite(str(idx) + '.png', newimage)
cv2.namedWindow('contours',cv2.WINDOW_NORMAL)
 cv2.imshow("contours", img)
cv2.resizeWindow('image',600,600)