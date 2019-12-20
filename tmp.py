import cv2
m_pic = cv2.imread("./facades/train/1.jpg")
HSV = cv2.cvtColor(m_pic,cv2.COLOR_BGR2HSV)
#HSV[...,0] =0
#HSV[...,1] =0
HSV[...,2] //=2
cv2.imshow("test",HSV)
cv2.waitKey(0)
#cv2.imshow("test",m_pic)
#cv2.waitKey(0)
