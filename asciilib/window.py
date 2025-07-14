import sys
import copy
import os
from .cols import Attribute

default_attr = Attribute(False, [], 'white', None)

def get_attr(attribute):
	if type(attribute) is str:
		return Attribute(False, [], attribute, None)

	if type(attribute) is tuple or type(attribute) is list:
		return Attribute(True, [], attribute, None)

	if type(attribute) is Attribute:
		return attribute

	raise Exception(f'INVALID ATTRIBUTE: {attribute}')



class Window:
	def __init__(self, dim, title=None):
		self.dim = dim
		self.grid = [[(None, default_attr) for i in range(dim[0])] for i in range(dim[1])]
		self.base_grid = copy.deepcopy(self.grid)
		self.title = title


	def wipe(self):
		self.grid = copy.deepcopy(self.base_grid)

	def render(self, surface, rel_pos, draw_border=True):
		if draw_border:
			self.draw_box((0,0), self.dim)
			if not self.title is None:
				self.draw_text((1,0), f' {self.title} ')

		for y in range(len(self.grid)):
			for x in range(len(self.grid[y])):
				value = self.grid[y][x][0]
				attr = self.grid[y][x][1]
				pos = (rel_pos[0] + x, rel_pos[1] + y)

				if value is None:
					value = ' '
					continue 

				surface.draw_text(pos, value, attr)
					
				

		self.wipe()

	def clear_console(self):	
		os.system('cls')


	def check_inbounds(self, pos) -> bool:
		return (0 <= pos[0] <= self.dim[0]-1) and (0 <= pos[1] <= self.dim[1]-1)

	def draw_text(self, pos, value:str, attribute=default_attr):
		attr = get_attr(attribute)

		for x, char in enumerate(value):
			p = [pos[0]+x, pos[1]]

			if self.check_inbounds(p):
				self.grid[p[1]][p[0]] = (char, attr)

	def draw_rect(self, pos, dim, value:str, attribute=default_attr,  fill=False):
		attr = get_attr(attribute)

		for y in range(dim[1]):
			for x in range(dim[0]):
				p = [pos[0]+x, pos[1]+y]

				if self.check_inbounds(p):
					if fill or x == 0 or x == dim[0]-1 or y == 0 or y == dim[1]-1:
						self.grid[p[1]][p[0]] = (value[0], attr)

	def wrap_around(self, pos, value:str, attribute=default_attr, x_restraint:int=10, get_lines=False):
		attr = get_attr(attribute)

		lines = []
		line = ''
		char_pos = [0,0]
		line_count = 1


		for word in value.split(' '):

			if char_pos[0] + len(word) + 1 > x_restraint:
				char_pos[0] = 0
				char_pos[1] += 1
				lines.append(line)
				line = ''
				line_count += 1
				
			line += word
			line += ' '
			char_pos[0] += len(word) + 1

		lines.append(line)

		if get_lines:
			return lines

		for y, l in enumerate(lines):
			self.draw_text((pos[0],pos[1]+y), l, attr)

	def draw_box(self, pos, dim, attribute=default_attr, chars=['┌', '┐', '┘', '└', '─', '│', '─', '│']):
		attr = get_attr(attribute)

		self.draw_text((pos[0], pos[1]), chars[0], attr)
		self.draw_text((pos[0]+dim[0]-1, pos[1]), chars[1], attr)
		self.draw_text((pos[0], pos[1]+dim[1]-1), chars[3], attr)
		self.draw_text((pos[0]+dim[0]-1, pos[1]+dim[1]-1), chars[2], attr)

		self.draw_rect((pos[0]+1, pos[1]), (dim[0]-2, 1), chars[4], attr)
		self.draw_rect((pos[0]+dim[0]-1, pos[1]+1), (1, dim[1]-2), chars[5], attr)
		self.draw_rect((pos[0]+1, pos[1]+dim[1]-1), (dim[0]-2, 1), chars[6], attr)
		self.draw_rect((pos[0], pos[1]+1), (1, dim[1]-2), chars[7], attr)