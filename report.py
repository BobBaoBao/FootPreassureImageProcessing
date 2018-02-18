import numpy as np
import cv2
import filter as fill
import find_contours as fc

def rept(path):

	img  = cv2.imread(path)
	
	max_area = img.shape[0]*img.shape[1]

	a = fill.filt(img)
	gray = fill.cvtgray(a[0],a[1])

	contu = fc.contubabu(gray[0],gray[1])
	cv2.drawContours(img, contu, -1, (0,255,0), 3)
	print len(contu),contu
	# while (max_area > 100):

		
	# 	m_cont,max_area,contu = fc.findareababu(contu)

	# 	cent_contu = fc.findcentbabu(m_cont)

	# 	app_centroid = fc.appcentroid(cent_contu[0],cent_contu[1])

	# 	center,rad = fc.findenccircle(m_cont)

	# 	cv2.circle(img,center,rad,(255,255,255),2)

	# 	cv2.circle(img,app_centroid,10,(0,255,255),2)

	# 	pass

	# cv2.imshow("low pressure",gray[0])

	# cv2.imshow("high pressure",gray[1])

	cv2.imshow("final",img)
	cv2.waitKey(0)
	# cv2.destroyAllWindows()

