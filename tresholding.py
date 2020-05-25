import cv2
img = cv2.imread('image path',0)

ret,thres = cv2.threshold(img, 7, 255, cv2.THRESH_BINARY)
cv2.imshow("table name",thres)
cv2.waitKey(0)
cv2.destroyAllWindows()

ret, thres2 = cv2.threshold(img, 125, cv2.THRESH_BINARY)

cv2.imshow("resim19999",thres)
cv2.waitKey(0)
cv2.destroyAllWindows()
