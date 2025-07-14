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
		atexit.register(exit_cleanup)


	func()



















'''
import traceback

def exit_cleanup():
	try:
		sys.stdout.write('\033[0m') # reset styling to default
		sys.stdout.write('\033[?25h') # show cursor
		sys.stdout.write("\033[?1049l") # return to saved console state
		sys.stdout.flush()
	except Exception:
		print("Exception during cleanup:")
		traceback.print_exc()

def handle_exception(exc_type, exc_value, exc_traceback):
	# Show the original crash traceback
	print("Unhandled exception:")
	traceback.print_exception(exc_type, exc_value, exc_traceback)


def main_wrapper(func):
	sys.stdout.write("\033[?1049h") # save console state
	sys.stdout.write('\033[?25l') # hide cursor
	sys.stdout.flush()
	os.system('cls') # clear console

	atexit.register(exit_cleanup)

	sys.excepthook = handle_exception

	try:
		func()
	except:
		sys.excepthook(*sys.exc_info())
'''