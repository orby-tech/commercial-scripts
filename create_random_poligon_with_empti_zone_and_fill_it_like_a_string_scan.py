import time
import math
import random
from tkinter import *
import copy
import numpy as np
import math


def white_picture_by_gabarits(max_x, max_y):
	gabarits = [max_x, max_y, 3]
	white_picture = np.zeros((gabarits[0], gabarits[1], gabarits[2]), np.uint8)
	color = tuple(reversed((255, 255, 255)))
	# Fill image with color
	white_picture[:] = color
	return white_picture


def create_random_angels_of_poligon(cols_of_angels):
	array_of_angels = []
	circle = math.pi * 2
	R = min(max_x, max_y)//2
	r = int(max_x / 8 * 2 * pow(2, 0.5))

	max_step = circle / cols_of_angels
	min_step = max_step / 4 * 3

	angel_now = random.random()

	for i in range(cols_of_angels):
		step = random.randint(int(min_step*1000), int(max_step*1000))/1000
		distanse = random.randint(r, R)
		
		angel_now += step
		
		x_temp = max_x//2 + int(math.cos(angel_now)*distanse)-1
		y_temp = max_y//2 + int(math.sin(angel_now)*distanse)-1
		print(x_temp, y_temp)

		array_of_angels.append(x_temp)
		array_of_angels.append(y_temp)
	return array_of_angels


def create_random_angels_of_empty_zone(cols_of_angels):
	array_of_angels = []
	circle = math.pi * 2
	R = min(max_x, max_y)//8
	r = int(max_x / 16)

	max_step = circle / cols_of_angels
	min_step = max_step / 4 * 3

	angel_now = random.random()

	for i in range(cols_of_angels):
		step = random.randint(int(min_step*1000), int(max_step*1000))/1000
		distanse = random.randint(r, R)
		
		angel_now += step
		
		x_temp = max_x//2 + int(math.cos(angel_now)*distanse)-1
		y_temp = max_y//2 + int(math.sin(angel_now)*distanse)-1
		print(x_temp, y_temp)

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


def append_to_empty_zone_all_pics(array_of_angels, white_picture):
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

cols_of_angels_poligons = 4
cols_of_angels_empty_zones = 3
max_x = 500
max_y = 500

array_of_angels_of_poligon = create_random_angels_of_poligon(cols_of_angels_poligons)
array_of_angels_of_empty_zone = create_random_angels_of_empty_zone(cols_of_angels_empty_zones)
white_picture = white_picture_by_gabarits(max_x, max_y)
white_picture_with_poligons_pics = append_to_poligon_all_pics(array_of_angels_of_poligon, white_picture)
white_picture_with_poligons_pics = append_to_empty_zone_all_pics(array_of_angels_of_empty_zone, white_picture)

root = Tk()
root.title("")
c = Canvas(root, width=max_x, height=max_y, bg='white')

for j in range(max_y):
	index = 0
	last_pic = []
	count_pic = 0
	for i in range(max_x):
		if white_picture_with_poligons_pics[i][j][0] == 255 and white_picture_with_poligons_pics[i][j][1] == 0:	
			count_pic += 1
	if count_pic % 2 == 0:
		for i in range(max_x):
			if white_picture_with_poligons_pics[i][j][0] == 255 and white_picture_with_poligons_pics[i][j][1] == 0:	
					index += 1
					if index % 2 == 1:
						last_pic = [i, j]
					elif index % 2 == 0 and index != 0:
						xy_coords = [last_pic[0], last_pic[1], i, j]
						c.create_line(xy_coords, width=1)
						last_pic = []
	elif count_pic %3 ==0: 
		for i in range(max_x):
			if white_picture_with_poligons_pics[i][j][0] == 255 and white_picture_with_poligons_pics[i][j][1] == 0:	
					index += 1
					if index == 1:
						first_pic = [i, j]

					else: 
						last_pic = [i, j]
		xy_coords = [first_pic[0], first_pic[1], last_pic[0], last_pic[1]]
		c.create_line(xy_coords, width=1)
		last_pic = []

c.pack(fill=BOTH, expand=1)
root.mainloop()
