import cv2
import numpy as np
import os

def generateLabel(file_path):
	img = cv2.imread(file_path)
	print(file_path)
	# cv2.imshow("image", img) 
	# cv2.waitKey(0)  

	label = 3

	# get dimensions of image
	dimensions = img.shape
	 
	# height, width, number of channels in image
	height = img.shape[0]
	width = img.shape[1]
	print(str(height) + " " + str(width))

	first = False

	tl = []
	br = []

	for y in range(0,height-13):
		line_cnt = 0
		for x in range(0,width):
			if img[y,x,0] == 0 and img[y,x,1] == 0 and img[y,x,2] == 255:
				line_cnt = line_cnt + 1
		if line_cnt > 200:					#Considera que mais de 100 pixels pretos e uma linha
			if first == False:
				for test in range(0,width):
					if img[y,test,0] == 0 and img[y,test,1] == 0 and img[y,test,2] == 255:
						print("Point in " + str(test) + ", " + str(y))
						tl = test, y
						first = True
						break
			else:
				for test in reversed(range(width)):
					if img[y,test,0] == 0 and img[y,test,1] == 0 and img[y,test,2] == 255:
						print("Point in " + str(test) + ", " + str(y))
						br = test, y
						break
	# if len(br) == 0:
	# 	br = 0,0
	# 	tl = 0,0

	size_x = br[0] - tl[0]
	center_x = (br[0] + tl[0])/2
	size_y = br[1] - tl[1]
	center_y = (br[1] + tl[1])/2


	print(str(label) + " " + str(center_x/width) + " " + str(center_y/height) + " " + str(size_x/width) + " " + str(size_y/height))

	label_path = "labels/" + file_path[0:7] + ".txt"
	o = open(label_path, 'w')
	o.write(str(label) + " " + str(center_x/width) + " " + str(center_y/height) + " " + str(size_x/width) + " " + str(size_y/height))

	o.close()


# img = cv2.imread("5825801.jpg")
# cv2.imshow("image", img) 
# cv2.waitKey(0)  


file_paths = os.listdir()
for file in file_paths:
	if file.find("png") > 0 or file.find("jpg") > 0:
		generateLabel(file)