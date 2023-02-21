from ppadb.client import Client
import time
import keyboard

MIN_PIXEL = 1238
MAX_PIXEL = 1578
DEFAULT = 1345
#Y_LOCATION = 318 #3D Volume
Y_LOCATION = 409 #Trainer Difficulty
TAP_DURATION = 200

current_location = 1333



def addPercent(n):
	result = current_location + ((MAX_PIXEL - MIN_PIXEL) * n/100.0)
	if result > MAX_PIXEL:
		result = MAX_PIXEL
	return result

def subPercent(n):
	result =  current_location - ((MAX_PIXEL - MIN_PIXEL) * n/100.0)
	if result < MIN_PIXEL:
		result = MIN_PIXEL
	return result

def chageSetting(device, current_location):
	
	device.shell(f'input touchscreen swipe 960 540 960 540 {int(TAP_DURATION)}') #tap screen for menu

	device.shell(f'input touchscreen swipe 181 1022 181 1022 {int(TAP_DURATION)}') #tap menu

	device.shell(f'input touchscreen swipe 1719 858 1719 858 {int(TAP_DURATION)}') #tap settings

	device.shell(f'input touchscreen swipe {int(current_location)} {int(Y_LOCATION)} {int(current_location)} {int(Y_LOCATION)} {int(TAP_DURATION)}')

	device.shell(f'input touchscreen swipe 960 935 960 935 {int(TAP_DURATION)}') #tap OK

	device.shell(f'input touchscreen swipe 655 1025 655 1025 {int(TAP_DURATION)}') #tap Back
	device.shell(f'input touchscreen swipe 655 1025 655 1025 {int(TAP_DURATION)}') #tap Back


def dummy (direction, current_location):
	if direction == "up":
		x_pos = addPercent()
	else:
		x_pos = subPercent()

	current_location = x_pos

	print(current_location)

	return current_location


adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()
print(devices)

if len(devices) == 0:
	print('no device attached')
	quit()

device = devices[0]


running = True

while running:
	event = keyboard.read_event()
	if event.event_type == keyboard.KEY_DOWN:
		print(event.name)
		if event.name == 'space':
			print('space was pressed')
		
		elif event.name == 'up':
			print('up was pressed')
			current_location = addPercent(10.0)
			chageSetting(device, current_location)

		elif event.name == 'down':
			print('down was pressed')
			current_location = subPercent(10.0)
			chageSetting(device, current_location)

		elif event.name == 'left':
			print('left was pressed')
			current_location = subPercent(20.0)
			chageSetting(device, current_location)

		elif event.name == 'right':
			print('right was pressed')
			current_location = addPercent(20.0)
			chageSetting(device, current_location)

		elif event.name == 'r':
			print('reset was pressed')
			current_location = DEFAULT
			chageSetting(device, current_location)
		
		elif event.name == 'esc':
			print('esc was pressed')
			quit()
		

	'''	
	if keyboard.is_pressed("p"):
		print("You pressed p")
		current_location = chageSetting(device, "up", current_location)
		#current_location = dummy("up", current_location)
		time.sleep(1.5)
		continue
	elif keyboard.is_pressed("d"):
		print("You pressed d")
		current_location = chageSetting(device, "down", current_location)
		#current_location = dummy("down", current_location)
		time.sleep(1.5)
		continue
	elif keyboard.is_pressed("esc"):
		print("quitting")
		time.sleep(1.5)
		quit()
	'''