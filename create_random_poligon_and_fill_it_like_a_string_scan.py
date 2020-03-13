import time
import math
import random
from tkinter import *
import copy
import numpy as np


def white_picture_by_gabarits(max_x, max_y):
	gabarits = [max_x, max_y, 3]
	white_picture = np.zeros((gabarits[0], gabarits[1], gabarits[2]), np.uint8)
	color = tuple(reversed((255, 255, 255)))
	# Fill image with color
	white_picture[:] = color
	return white_picture


def create_random_angels(cols_of_angels):
	array_of_angels = []
	for i in range(cols_of_angels):
		x_temp = random.randint(0, max_x)
		y_temp = random.randint(0, max_y)
		array_of_angels.append(x_temp)
		array_of_angels.append(y_temp)
	return array_of_angels


def append_to_poligon_all_pics(array_of_angels, white_picture):
	for z in range(0, len(array_of_angels), 2):
		i = z
		if z < len(array_of_angels) + 2 or z > len(array_of_angels) - 1:
			i -= len(array_of_angels)
		for j in range(min(array_of_angels[i + 1], array_of_angels[i + 3]), max(array_of_angels[i + 1], array_of_angels[i + 3])):
			x1 = array_of_angels[i]
			x2 = array_of_angels[i + 2]
			y1 = array_of_angels[i + 1]
			y2 = array_of_angels[i + 3]

			x_j = x1 + (x2 - x1) * (j - y1) / (y2 - y1)
			if x_j % 1 < 0.5:
				x_j = x_j // 1
			else:
				x_j = x_j // 1 + 1
			color = tuple(reversed((0, 0, 255)))

			white_picture[int(x_j)][j] = color
	return white_picture


cols_of_angels = 3
max_x = 500
max_y = 500

array_of_angels = create_random_angels(cols_of_angels)
white_picture = white_picture_by_gabarits(max_x, max_y)
white_picture_with_poligons_pics = append_to_poligon_all_pics(array_of_angels, white_picture)

root = Tk()
root.title("")
c = Canvas(root, width=max_x, height=max_y, bg='white')

for j in range(max_y):
	index = 0
	last_pic = []
	for i in range(max_x):
		if white_picture_with_poligons_pics[i][j][0] == 255 and white_picture_with_poligons_pics[i][j][1] == 0:			
			index += 1
			if index % 2 == 1:
				last_pic = [i, j]
			elif index % 2 == 0 and index != 0:
				xy_coords = [last_pic[0], last_pic[1], i, j]
				c.create_line(xy_coords, width=1)
				last_pic = []

c.pack(fill=BOTH, expand=1)
root.mainloop()
