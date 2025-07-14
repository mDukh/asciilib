import string

typeable = list(string.ascii_lowercase) + list('0123456789')

class Textbox:
	def __init__(self, pos:list[int]|tuple[int], dim:list[int]|tuple[int]):
		self.pos = pos
		self.dim = dim
		self.data = ''

	def update(self, keys) -> None:
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