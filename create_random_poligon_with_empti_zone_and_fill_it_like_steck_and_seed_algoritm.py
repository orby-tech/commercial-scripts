import time
import math
import random
from tkinter import *
import copy
import numpy as np
import math
from PIL import Image, ImageTk



def white_picture_by_gabarits(max_x, max_y):
	gabarits = [max_x, max_y, 3]
	white_picture = np.zeros((gabarits[0], gabarits[1], gabarits[2]), np.uint8)
	color = tuple(reversed((255, 255, 255)))
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
			x_j = x_j // 1
			white_picture[int(x_j)][j] = tuple(reversed((0, 0, 0)))

			x_j = x_j // 1 + 1			
			white_picture[int(x_j)][j] = tuple(reversed((0, 0, 0)))

	for z in range(1, len(array_of_angels), 2):
		i = z
		if z > len(array_of_angels) - 2:
			i -= len(array_of_angels)
		for j in range(min(array_of_angels[i - 1], array_of_angels[i + 1]), max(array_of_angels[i - 1], array_of_angels[i + 1])):
			y1 = array_of_angels[i]
			y2 = array_of_angels[i + 2]
			x1 = array_of_angels[i - 1]
			x2 = array_of_angels[i + 1]

			y_j = y1 + (y2 - y1) * (j - x1) / (x2 - x1)
			y_j = y_j // 1
			white_picture[j][int(y_j)] = tuple(reversed((0, 0, 0)))

			y_j = y_j // 1 + 1			
			white_picture[j][int(y_j)] = tuple(reversed((0, 0, 0)))

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
			
			x_j = x_j // 1
			white_picture[int(x_j)][j] = tuple(reversed((0, 0, 0)))

			x_j = x_j // 1 + 1			
			white_picture[int(x_j)][j] = tuple(reversed((0, 0, 0)))
	for z in range(1, len(array_of_angels), 2):
		i = z
		if z < len(array_of_angels) + 3 or z > len(array_of_angels) - 2:
			i -= len(array_of_angels)
		for j in range(min(array_of_angels[i - 1], array_of_angels[i + 1]), max(array_of_angels[i - 1], array_of_angels[i + 1])):
			y1 = array_of_angels[i]
			y2 = array_of_angels[i + 2]
			x1 = array_of_angels[i - 1]
			x2 = array_of_angels[i + 1]

			y_j = y1 + (y2 - y1) * (j - x1) / (x2 - x1)
			y_j = y_j // 1
			white_picture[j][int(y_j)] = tuple(reversed((0, 0, 0)))

			y_j = y_j // 1 + 1			
			white_picture[j][int(y_j)] = tuple(reversed((0, 0, 0)))

	return white_picture

def clean(white_picture_with_poligons_pics,steck):
	if white_picture_with_poligons_pics[i[0]+1][i[1]][0] != 0:
		if [i[0]+1, i[1]] not in steck:	
			steck.append([i[0]+1, i[1]])
	
	if white_picture_with_poligons_pics[i[0]-1][i[1]][0] != 0:	
		if [i[0]-1, i[1]] not in steck:	
			steck.append([i[0]-1, i[1]])
	
	if white_picture_with_poligons_pics[i[0]][i[1]+1][0] != 0:
		if [i[0], i[1]+1] not in steck:	

			steck.append([i[0], i[1]+1])
	
	if white_picture_with_poligons_pics[i[0]][i[1]-1][0] != 0:	
		if [i[0], i[1]-1] not in steck:	
		
			steck.append([i[0], i[1]-1])		


	if white_picture_with_poligons_pics[i[0]][i[1]][0] != 0:
		white_picture_with_poligons_pics[i[0],i[1]] = tuple(reversed((0, 0, 0)))
	return white_picture_with_poligons_pics, steck


cols_of_angels_poligons = 4
cols_of_angels_empty_zones = 3
max_x = 200
max_y = 200

array_of_angels_of_poligon = create_random_angels_of_poligon(cols_of_angels_poligons)
array_of_angels_of_empty_zone = create_random_angels_of_empty_zone(cols_of_angels_empty_zones)
white_picture = white_picture_by_gabarits(max_x, max_y)
white_picture_with_poligons_pics = append_to_poligon_all_pics(array_of_angels_of_poligon, white_picture)
white_picture_with_poligons_pics = append_to_empty_zone_all_pics(array_of_angels_of_empty_zone, white_picture)

root = Tk()
root.title("")
c = Canvas(root, width=max_x, height=max_y, bg='white')
img =  ImageTk.PhotoImage(image=Image.fromarray(white_picture_with_poligons_pics))
c.create_image(0,0, anchor="nw", image=img)
c.update()

print("as")
steck = []
steck.append([110, 110])

for j in range(100000):
	if len(steck) == 0:
		break
	i = steck[0]
	
	white_picture_with_poligons_pics, steck = clean(white_picture_with_poligons_pics, steck)
	steck.remove(i)



img =  ImageTk.PhotoImage(image=Image.fromarray(white_picture_with_poligons_pics))
c.create_image(0,0, anchor="nw", image=img)
c.update()

c.pack(fill=BOTH, expand=1)
root.mainloop()