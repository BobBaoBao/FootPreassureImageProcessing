import numpy as np
import cv2


def filt(img):
	img_h = np.zeros(img.shape,np.uint8)
	
	img_l = np.zeros(img.shape,np.uint8)
	for i in range(img.shape[0]) :
		for j in range(img.shape[1]):
			if(img[i,j][0]>100 or img[i,j][1]>100 or img[i,j][2]>100):
				if((img[i,j][2] > img[i,j][0] and img[i,j][2] > img[i,j][1] and i > 10 and i < (img.shape[0]-10) and j > 10 and j < (img.shape[1]-10)) or (img[i,j][1] > img[i,j][0] and img[i,j][1] > img[i,j][2] and i > 10 and i < (img.shape[0]-10) and j > 10 and j < (img.shape[1]-10)) or (img[i,j][0]>60 and img[i,j][1]>100 and img[i,j][2]>0 and img[i,j][0]<255 and img[i,j][1]<255 and img[i,j][2]<25 and i > 10 and i < (img.shape[0]-10) and j > 10 and j < (img.shape[1]-10))):
					img_h[i,j] = [255,255,255]

				# elif(img[i,j][0]>60 and img[i,j][1]>100 and img[i,j][2]>0 and img[i,j][0]<255 and img[i,j][1]<255 and img[i,j][2]<25 and i > 10 and i < (img.shape[0]-10) and j > 10 and j < (img.shape[1]-10)):
				# 	img_h[i,j] = [255,255,255]

				elif(img[i,j][0] > img[i,j][1] and img[i,j][0] > img[i,j][2] and i > 10 and i < (img.shape[0]-10) and j > 10 and j < (img.shape[1]-10)): 
					img_l[i,j] = [255,255,255]

			else :
				img_l[i,j] = [0,0,0]
				img_h[i,j] = [0,0,0]

	return img_l,img_h



def cvtgray(img_l,img_h):
	img_l_g = cv2.cvtColor(img_l,cv2.COLOR_BGR2GRAY)
	
	img_h_g = cv2.cvtColor(img_h,cv2.COLOR_BGR2GRAY)

	return img_l_g,img_h_g




