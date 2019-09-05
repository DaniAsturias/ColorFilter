"""
Company:ArcelorMIttal
Author: Daniel González CAstro

Summary: Program to perform a HSV filter of an image

"""
import numpy as np
import cv2
import sys


class filtroRGB ():
	"""
	Class with four variables and four methods:
	Variables:
		-window_names-> NAme of the windows in where the image is showed

		-image-> Numpy arrary used by opencv for storages images or frames.

		-values-> List with the treshold to be applied.

		.HSVimage-> Image with HSV colorspace.

	Methods:
		- _init_-> Constructor. It receives the path to he image.

		.callback -> It does not do anything. It is a kind of convention to apply asynchronus programming.

		-set_trackbar -> Create the window and the trackbars.

		-process -> Show the image, wait for the trackbar changes and show again the results.
	"""

	def __init__(self,filename):
		self.window_name=filename
		self.image=cv2.imread(filename)
		self.values=[['hue high',0,179],['hue low',0,179],['saturation high',0,255],['saturation low',0,255],['value high',0,255],['value low',0,255]]
		self.HSVimage=cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
		
	def callback(self,value):
		pass
		

	def set_trackbar(self):
		cv2.namedWindow(self.window_name)
		for i in self.values: 
			cv2.createTrackbar(i[0], self.window_name, i[1],i[2], self.callback)

	def proccess(self):
		
		while True:
			hsvl = np.array([cv2.getTrackbarPos(self.values[1][0],self.window_name), cv2.getTrackbarPos(self.values[3][0],self.window_name), cv2.getTrackbarPos(self.values[5][0],self.window_name)])
			hsvh = np.array([cv2.getTrackbarPos(self.values[0][0],self.window_name), cv2.getTrackbarPos(self.values[2][0],self.window_name), cv2.getTrackbarPos(self.values[4][0],self.window_name)])
			mask = cv2.inRange(self.HSVimage, hsvl, hsvh)
			res = cv2.bitwise_and(self.image, self.image, mask=mask)
			cv2.imshow(self.window_name,res)
			ch = cv2.waitKey(5)
			if ch== 27:
				break



def main():
	miFiltro=filtroRGB("imagenes/"+sys.argv[1])
	miFiltro.set_trackbar()
	miFiltro.proccess()

if __name__ == '__main__':
   main()

		