import pynput
from threading import Thread
import casinoheist
import cayoperico

pressed = []
def on_press(key):
	"""Function used by pynput for it listener"""
	if key in pressed:
		return True
	pressed.append(key)

	try:
		k = key.char
	except:
		k = key.name

	if k == "f8":
		return False

	elif k == "f5":
		thread = Thread(target = casinoheist.digit_hack)
		thread.start() # run an async task so it can killed by pressing F8

	elif k == "f6":
		thread = Thread(target = cayoperico.digit_hack)
		thread.start()

	elif k == "f7":
		thread = Thread(target = casinoheist.hacking_machine)
		thread.start()


def on_release(key):
	"""Function used by pynput for it listener"""
	if key in pressed:
		pressed.remove(key)


listener = pynput.keyboard.Listener(on_press = on_press, on_release = on_release)
listener.start()
listener.join()