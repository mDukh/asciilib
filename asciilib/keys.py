import keyboard
import string
import copy


letter_keys = list(string.ascii_lowercase)
number_keys = list(string.digits)
function_keys = [f'f{i}' for i in range(1, 13)]
nav_keys = [
    'up', 'down', 'left', 'right',
    'home', 'end', 'page up', 'page down',
    'insert', 'delete'
]
control_keys = [
    'enter', 'space', 'tab', 'backspace', 'esc',
    'print screen', 'pause', 'menu', 'caps lock',
    'num lock', 'scroll lock'
]
modifier_keys = list(keyboard.all_modifiers)
symbol_keys = ['-', '=', '[', ']', '\\', ';', "'", ',', '.', '/', '`']

all_keys = sorted(set(letter_keys + number_keys + function_keys + nav_keys + control_keys + modifier_keys + symbol_keys))

class Keys:
	def __init__(self):
		self.key_states = {key: False for key in all_keys}
		self.past_key_states = {key: False for key in all_keys}
		self.keys_tapped = {key: False for key in all_keys}

	def update(self) -> None:
		self.past_key_states = copy.deepcopy(self.key_states)
		for key in all_keys:
			try:
				self.key_states[key] = keyboard.is_pressed(key)
			except:	
				self.key_states[key] = False

		for key in all_keys:
			try:
				self.keys_tapped[key] = self.key_states[key] and not self.past_key_states[key]
			except:
				self.keys_tapped[key] = False

				
	def is_pressed(self, key:str) -> bool:
		return self.key_states[key]

	def is_tapped(self, key:str) -> bool:
		return self.keys_tapped[key]

	def get_pressed(self) -> list[str]:
		return [k for k, v in self.key_states.items() if v]

	def get_tapped(self) -> list[str]:
		return [k for k, v in self.keys_tapped.items() if v]