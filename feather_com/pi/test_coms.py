import RPi.GPIO as GPIO
import time

# ------------------------ #
# --- HELPER FUNCTIONS --- #
# ------------------------ #

def set_active_cmd_num(out_1, out_2, out_3):

	GPIO.output(16, out_1)
	GPIO.output(20, out_2)
	GPIO.output(19, out_3)


def reset_feather():

	GPIO.output(21, 0)
	time.sleep(0.1)
	GPIO.output(21, 1)


def set_active_cmd_str(cmd):

	if cmd == "IDLE":
		set_active_cmd_num(0, 0, 0)
	elif cmd == "LOWER_MANUAL":
		set_active_cmd_num(0, 0, 1)
	elif cmd == "RAISE_MANUAL":
		set_active_cmd_num(0, 1, 0)
	elif cmd == "LOWER_AUTO":
		set_active_cmd_num(0, 1, 1)
	elif cmd == "RAISE_AUTO":
		set_active_cmd_num(1, 0, 0)
	elif cmd == "SCOOP":
		set_active_cmd_num(1, 0, 1)
	elif cmd == "DEPOSIT":
		set_active_cmd_num(1, 1, 0)


# ----------------- #
# --- MAIN CODE --- #
# ----------------- #

### INITIAL PIN SETUP ### 

# Configure pin numbering scheme to BCM
GPIO.setmode(GPIO.BCM)

# Set pin as an output
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.IN)
GPIO.setup(21, GPIO.OUT)

# Set pin to high/low
GPIO.output(16, GPIO.LOW)
GPIO.output(20, GPIO.LOW)
GPIO.output(19, GPIO.LOW)
GPIO.output(21, GPIO.HIGH) 
#reset_feather()

### CONTROL CODE ###

while True:

	set_active_cmd_num(0, 0, 1)
	time.sleep(2)
	set_active_cmd_num(0, 1, 0)
	time.sleep(2)
	set_active_cmd_num(1, 0, 0)
	time.sleep(2)
	set_active_cmd_num(0, 0, 0)
	time.sleep(4)

#set_active_cmd_str("RAISE_MANUAL")
#time.sleep(20)


### SHUTDOWN OPS ###

# Reset all pins to default states
GPIO.output(16, GPIO.LOW)
GPIO.output(20, GPIO.LOW)
GPIO.output(19, GPIO.LOW)
GPIO.cleanup()
