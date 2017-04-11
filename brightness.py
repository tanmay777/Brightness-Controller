import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
red=11
GPIO.setup(red,GPIO.OUT)
my_pwm=GPIO.PWM(red,100)
my_pwm.start(0)
x=0
while(1):
	bright=input("How bright do you want the led?(0-100) ")
	my_pwm.ChangeDutyCycle(bright)
	x=input("Do you want to enter more? ")
my_pwm.stop()
GPIO.cleanup()
