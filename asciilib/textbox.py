import string

typeable = list(string.ascii_lowercase) + list('0123456789')

class Textbox:
	def __init__(self, pos:list[int]|tuple[int], dim:list[int]|tuple[int]):
		self.pos = pos
		self.dim = dim
		self.data = ''

	def update(self, keys):
		tapped = keys.get_tapped()
		pressed = keys.get_pressed()

		caps = False
		if 'left shift' in pressed or 'right shift' in pressed or 'shift' in pressed:
			caps = True

		for key in tapped:
			match key:
				case 'space':
					self.data += ' '
				case 'backspace':
					if not len(self.data) > 0:
						continue
							
					self.data = ''.join(list(self.data)[:-1])
				case _:
					if key in typeable:
						self.data += key if not caps else key.upper()

	def clear(self):
		self.data = ''


	def draw_on_window(self, window, attribute=None):
		if attribute is None:
			window.wrap_around((0,0), self.data, x_restraint=window.dim[0])
			return

		window.wrap_around((0,0), self.data, attribute=attribute, x_restraint=window.dim[0])

	def render_wrap_around(self, screen, pos, attribute=None, x_restraint:int=10, get_lines=False):
		if attribute is None:
			return screen.wrap_around(pos, self.data, x_restraint=x_restraint, get_lines=get_lines)

		return screen.wrap_around(pos, self.data, attribute=attribute, x_restraint=x_restraint, get_lines=get_lines)