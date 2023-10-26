import cv2
image=cv2.imread("lena.jpg",1)
cv2.line(image,(0,0),(600,600),(255,0,0),5)
cv2.rectangle(image,(200,200),(400,400),(0,255,0),4)
cv2.circle(image,(50,50),50,(0,0,255),-1)
cv2.circle(image,(50,450),50,(0,0,255),-1)
cv2.circle(image,(450,50),50,(0,0,255),-1)
cv2.circle(image,(450,450),50,(0,0,255),-1)
font=cv2.FONT_HERSHEY_COMPLEX
cv2.putText(image,"CV",(200,300),font,4,(0,255,0))
cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyWindow()