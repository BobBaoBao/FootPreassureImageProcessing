import cv2
import numpy as np


def contubabu(img1,img3):
	ret1, thresh1 = cv2.threshold(img1, 127, 255, 0)
	cnt1, hrc1 = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)



	ret3, thresh3 = cv2.threshold(img3, 127, 255, 0)
	cnt3, hrc3 = cv2.findContours(thresh3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	print len(cnt3)

	return cnt3


def findareababu(cnt): 
	area = []
	print len(cnt)
	for i in range(len(cnt)):

		area.append(cv2.contourArea(cnt[i]))
	
	max_area = max(area)

	main_cnt = 0
	for i in range(len(cnt)):
		if(cv2.contourArea(cnt[i]) == max_area):
			main_cnt = cnt[i]
			#


	return main_cnt,max_area,cnt

def findcentbabu(cnt):
	M = cv2.moments(cnt)
	cx = int(M['m10']/M['m00'])
	cy = int(M['m01']/M['m00'])
	return cx,cy
		

def findenccircle(cnt):
	(x,y),radius = cv2.minEnclosingCircle(cnt)

	center = (int(x),int(y))
	radius = int(radius)

	return center,radius

def appcentroid(cx,cy):
	cx = int(cx)
	cy = int(cy)
	return cx,cy