import atexit
import sys
import os
import time
import traceback

def exit_cleanup():
	sys.stdout.write('\033[0m') # reset styling to default
	sys.stdout.write('\033[?25h') # show cursor
	sys.stdout.write("\033[?1049l") # return to saved console state
	sys.stdout.flush()



def main_wrapper(func, cleanup=True):
	sys.stdout.write("\033[?1049h") # save console state
	sys.stdout.write('\033[?25l') # hide cursor
	sys.stdout.flush()
	os.system('cls') # clear console

	if cleanup:
		atexit.register(exit_cleanup) # calls exit_cleanup() whenever the program ends/crashes


	func()












