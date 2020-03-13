import random
from tkinter import *
import copy


def Sorting_array_by_first_element_by_puzirek(array_of_piks)
	N = len(array_of_piks)
	for i in range(N - 1):
	    for j in range(N - i - 1):
	        if array_of_piks[j][1] > array_of_piks[j + 1][1]:
	            array_of_piks[j][1], array_of_piks[j + 1][1] = array_of_piks[j + 1][1], array_of_piks[j][1]
	            array_of_piks[j][0], array_of_piks[j + 1][0] = array_of_piks[j + 1][0], array_of_piks[j][0]
	return array_of_piks

def  Sorting_array_by_second_element_by_puzirek(array_of_piks):
	N = len(array_of_piks)
	for i in range(N - 1):
	    for j in range(N - i - 1):
	        if array_of_piks[j][0] > array_of_piks[j + 1][0] and array_of_piks[j][1] == array_of_piks[j + 1][1]:
	            array_of_piks[j][0], array_of_piks[j + 1][0] = array_of_piks[j + 1][0], array_of_piks[j][0]
	            array_of_piks[j][1], array_of_piks[j + 1][1] = array_of_piks[j + 1][1], array_of_piks[j][1]
	return array_of_piks

def Create_random_angels(cols_of_angels):
	array_of_angels = []
	for i in range(cols_of_angels):
		x_temp = random.randint(0, max_x)
		y_temp = random.randint(0, max_y)
		array_of_angels.append(x_temp)
		array_of_angels.append(y_temp)
	return array_of_angels

def  Coordinats_all_pics_of_sides_by_poligon(array_of_angels):
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

			array_of_piks.append([x_j, j])
	return array_of_piks


cols_of_angels = 10
array_of_piks = []
array_of_angels = []
max_x = 1000
max_y = 1000

array_of_angels = Create_random_angels(cols_of_angels)
array_of_piks = Coordinats_all_pics_of_sides_by_poligon(array_of_angels)
array_of_piks = Sorting_array_by_first_element_by_puzirek(array_of_piks)
array_of_piks = Sorting_array_by_second_element_by_puzirek(array_of_piks)

print(array_of_piks)

root = Tk()
root.title("")
c = Canvas(root, width=max_x, height=max_y, bg='white')

c.create_polygon(array_of_angels, outline='red', fill='white', width=1)

for i in range(N - 1):
	x1 = array_of_piks[i][0]
	y1 = array_of_piks[i][1]
	x2 = array_of_piks[i + 1][0]
	y2 = array_of_piks[i + 1][1]
	xy_coords = [x1, y1, x2, y2]
	c.create_line(xy_coords, width=1)
	c.update()
	i += 1
c.pack(fill=BOTH, expand=1)
root.mainloop()
