FG_ANSI = {
	'black' : 30,
	'red' : 31,
	'green' : 32,
	'yellow' : 33,
	'blue' : 34,
	'magenta' : 35,
	'cyan' : 36,
	'white' : 37,
	'gray' : 90,
	'bright red' : 91,
	'bright green' : 92,
	'bright yellow' : 93,
	'bright blue' : 94,
	'bright magenta' : 95,
	'bright cyan' : 96,
	'bright white' : 97,
}

BG_ANSI = {
	'black' : 40,
	'red' : 41,
	'green' : 42,
	'yellow' : 43,
	'blue' : 44,
	'magenta' : 45,
	'cyan' : 46,
	'white' : 47,
	'gray' : 100,
	'bright red' : 101,
	'bright green' : 102,
	'bright yellow' : 103,
	'bright blue' : 104,
	'bright magenta' : 105,
	'bright cyan' : 106,
	'bright white' : 107  
}

STYLE_ANSI = {
	'reset' : 0,
	'bold' : 1,
	'dim' : 2,
	'italic' : 3,
	'underlined' : 4,
	'invert' : 7
}




def _style_formatted(styles) -> str:
	final = ''
	for style in styles:
		char = str(STYLE_ANSI.get(style, None))
		if char is None:
			raise Exception(f'INVALID STYLE: {style}')

		final += char + ';'
	return final



ESC = '\033'

class Attribute:
	def __init__(self, full_fidelity: bool, styles: list[str], *args):

		'''
		full fidelity (RGB):
			args -> (r, g, b), (br, bg, bb)
		not full (16 col):
			args -> color: int
		'''

		self.styles = styles
		self.full_fidelity = full_fidelity
		self.fg_rgb = None
		self.bg_rgb = None
		self.fg_color = None
		self.bg_color = None

		if full_fidelity:
			if len(args) != 2:
				raise Exception(f'INVALID ARGUMENTS: {args}')

			self.fg_rgb = args[0]
			self.bg_rgb = args[1]

		else:
			if len(args) != 2:
				raise Exception(f'INVALID ARGUMENTS: {args}')

			self.fg_color = args[0]
			self.bg_color = args[1]







	def _get_color_code(self, is_foreground: bool) -> str:
		rgb = self.fg_rgb if is_foreground else self.bg_rgb
		color = self.fg_color if is_foreground else self.bg_color
		ansi_map = FG_ANSI if is_foreground else BG_ANSI
		default_code = '39;' if is_foreground else '49;'
		rgb_prefix = '38;2;' if is_foreground else '48;2;'

		# checking for null values (returns respective default value if so)
		if self.full_fidelity:
			if rgb is None:
				return default_code
		else:
			if color is None:
				return default_code

		# format and return if no null
		if self.full_fidelity:
			return f'{rgb_prefix}{round(rgb[0])};{round(rgb[1])};{round(rgb[2])};'

		return str(ansi_map[color]) + ';'



	def _get_format(self) -> str:
		styles = _style_formatted(self.styles)

		foreground = self._get_color_code(is_foreground=True)
		background = self._get_color_code(is_foreground=False)

		return f'{ESC}[{styles}{foreground}{background}m'


	def format_str(self, s) -> str:
		return self._get_format() + s + ESC + '[0m'




