''
#######################################################
# Program : Testing Ground
# Description : This code is contains series of test that the LEGO Turret
#				had to go through before coding the actual code for it.
# History
# ---------------------------------
# Author	Date		Comment
# Kevin		02.14.14	Creation Date with basic test for tilt.
#  ""		02.15.14	Added prompt screen, setup motors + sensors, added complex testing for tilt.
#  ""		02.17.14	Added Shooting Test, Sensor Test, Commenting, Min/Max for tilt test
#  ""		02.22.14	Change motor, sensor ports
#
#######################################################
''

# COMMANDS ARE IN THE PROMPT
# REQUIRES BATTERIES BECAUSE MOTORS WILL ONLY WORK IN LOW IF ITS POWERED BY USB. BATTERIES = HIGH POWER ON MOTOR
# TEST LEGO TURRET v2.2 + v3.3 + v3.4

# import every function from the BrickPi script
from BrickPi import *


BrickPiSetup();										# setup motor input

tiltMotor = PORT_B									# obtain motor ports and initialize them
BrickPi.MotorEnable[tiltMotor] = 1
shootMotor = PORT_A
BrickPi.MotorEnable[shootMotor] = 1

tiltMin = PORT_1									# obtain tilt(touch) sensors and initialize tilt sensors
BrickPi.SensorType[tiltMin] = TYPE_SENSOR_TOUCH
tiltMax = PORT_2
BrickPi.SensorType[tiltMax] = TYPE_SENSOR_TOUCH


BrickPiSetupSensors()								# setup tilt sensors
ans = ""
	
# function which test the tilt motor
def tiltTest():
	tilt = ""
                        	        	        
	while tilt.lower() != "b":
		# set the brick pi to stop at 500ms
		BrickPi.Timeout = 1000
		BrickPiSetTimeout()
			
		print "\nInput U to go up (+y) or D to go down (-y)"
		print "or S to Stop the Motor or B to go back"
		tilt = raw_input("Up or Down : ")
		
		if tilt.lower() == "u":
			BrickPiUpdateValues()
			if BrickPi.Sensor[tiltMax] == 1:			# check if its at max
				BrickPi.MotorSpeed[tiltMotor] = 0
				print "Cannot go up any further!"
			else:
				BrickPi.MotorSpeed[tiltMotor] = -140    # go up	
			BrickPiUpdateValues()
		elif tilt.lower() == "d":
			BrickPiUpdateValues()
			if BrickPi.Sensor[tiltMin] == 1:			# check if its at min
				BrickPi.MotorSpeed[tiltMotor] = 0
				print "Cannot go down any further!"
			else:
				BrickPi.MotorSpeed[tiltMotor] = 25	    # go down
			BrickPiUpdateValues()	
		elif tilt.lower() == "s":
			BrickPiUpdateValues()
			BrickPi.MotorSpeed[tiltMotor] = 0       # stop the motor
			BrickPiUpdateValues()
			
# function which test the shooting motor
def shootTest():
	shoot = ""
	
	while shoot.lower() != "b":	
		# set the brick pi to stop at 250ms
		BrickPi.Timeout = 150
		BrickPiSetTimeout()
		print "\nInput S to shoot or B to go back!"
		shoot = raw_input("Your Input : ")
		if shoot.lower() == "s":
			BrickPi.MotorSpeed[shootMotor] = 255
		BrickPiUpdateValues()
		
# function which test the sensors and the tilt motors
def sensorTest():
	sensor = ""
	
	while sensor.lower() != "b":
		print "\nInput test to test the sensors!"
		sensor = raw_input("Your Input : ")

		if sensor.lower() == "test":
			BrickPiUpdateValues()
			i = 0
			while i < 10:										# go up and down 10 times
				while BrickPi.Sensor[tiltMax] == 0:			
					BrickPi.MotorSpeed[tiltMotor] = -140
					BrickPiUpdateValues()
				BrickPi.MotorSpeed[tiltMotor] = 0
				BrickPiUpdateValues()
				print "Tilt hit the maximum where tiltMax is 1"
				
				while BrickPi.Sensor[tiltMin] == 0:			
					BrickPi.MotorSpeed[tiltMotor] = 50
					BrickPiUpdateValues()
				BrickPi.MotorSpeed[tiltMotor] = 0
				BrickPiUpdateValues()
				print "Tilt hit the minimum where tiltMin is 1"		
				i+=1
		
		
while ans.lower() != "q":
	print "\nLEGO Turret Testing Grounds!\n"
	print "Input T to test the Tilt Motor!"			# basic tilt with no shooter on top
	print "Input S to test the Shooting Motor!"		# shoot balls
	print "Input M to test the Tilt Sensors!"		# loop for 10 seconds going up and down while hitting sensors
	print "Input Q to exit the Testing Ground!\n" 

	ans = raw_input("Your input : ")

	if  ans.lower() == "t":
		tiltTest()
	elif ans.lower() == "s":
		shootTest()
	elif ans.lower() == "m":
		sensorTest()
