##############################################################
#		Развитие программы подразумевает:
#	Добавление функцианала станка
#	Добавление минимального визуального оформления
#	Апроксимация не только по линиям, но и по окружностям
#	Добавление файлов рисунков через файловый менеджер
#	Добавление документации к созданной программе
#
###############################################################

import numpy as np
import cv2

F = 100
eps = 0.0001
array_of_dialog_lines = []
array_of_CHPU_comands = []


def create_array_of_dialog_lines(eps):
	img = cv2.imread('/home/tim/contur.JPG')

	canvas = np.zeros(img.shape, np.uint8)
	img2gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	# filter out small lines between counties
	kernel = np.ones((5, 5), np.float32) / 25
	img2gray = cv2.filter2D(img2gray, -1, kernel)

	# threshold the image and extract contours
	ret, thresh = cv2.threshold(img2gray, 250, 255, cv2.THRESH_BINARY_INV)
	contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

	# find the main island (biggest area)
	cnt = contours[0]
	max_area = cv2.contourArea(cnt)

	for cont in contours:
	    if cv2.contourArea(cont) > max_area:
	        cnt = cont
	        max_area = cv2.contourArea(cont)

	epsilon = eps * cv2.arcLength(cnt, True)
	array_of_piks = cv2.approxPolyDP(cnt, epsilon, True)

	N = len(array_of_piks)
	for i in range(N - 1):
		x1 = array_of_piks[i][0][0]
		y1 = array_of_piks[i][0][1]
		x2 = array_of_piks[i + 1][0][0]
		y2 = array_of_piks[i + 1][0][1]
		xy_coords = [x1, y1, x2, y2]
		array_of_dialog_lines.append(xy_coords)
		i += 1

	cv2.drawContours(canvas, cnt, -1, (0, 255, 0), 1)
	cv2.drawContours(canvas, [array_of_piks], -1, (0, 0, 255), 1)

	cv2.imshow("Contour", canvas)
	k = cv2.waitKey(0)

	if k == 27:         # wait for ESC key to exit
	    cv2.destroyAllWindows()
	return array_of_dialog_lines


array_of_dialog_lines = create_array_of_dialog_lines(eps)


array_of_CHPU_comands.append("N10" + " G00 " + "X" + str(array_of_dialog_lines[0][0]) + " Y" + str(array_of_dialog_lines[0][1]))
for i in range(len(array_of_dialog_lines)):
	array_of_CHPU_comands.append("N" + str((i + 2) * 10) + " G01 " + "X" + str(array_of_dialog_lines[i][2]) + " Y" + str(array_of_dialog_lines[i][3]) + " F" + str(F))

for i in range(len(array_of_CHPU_comands)):

	print(array_of_CHPU_comands[i])
