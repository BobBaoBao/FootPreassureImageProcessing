import numpy as np
import cv2
import filter as fill
import find_contours as fc


img  = cv2.imread("img2.jpg")

a = fill.filt(img)
gray = fill.cvtgray(a[0],a[1])

contu = fc.contubabu(gray[0],gray[1])

m_cont = fc.findareababu(contu)

cent_contu = fc.findcentbabu(m_cont)

app_centroid = fc.appcentroid(cent_contu[0],cent_contu[1])

center,rad = fc.findenccircle(m_cont)

cv2.circle(img,center,rad,(255,255,255),2)

cv2.circle(img,app_centroid,10,(0,255,255),2)

# cv2.imshow("low pressure",gray[0])

# cv2.imshow("high pressure",gray[1])
cv2.imshow("final",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
