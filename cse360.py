import time
import RPi.GPIO as GPIO
from RPLCD import CharLCD

GPIO.setmode(GPIO.BOARD)
#GPIO.setup(10, GPIO.OUT)

###Platform pin no.
GPIO.setup(21, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(10, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(19, GPIO.IN, GPIO.PUD_DOWN)

## Display pin no.
lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[40,38,36,32,33,31,29,23])#
#GPIO.output(10, True)

#key pad pin
MATRIX = [ [1,2,3,'A'],
           [4,5,6,'B'],
           [7,8,9,'C'],
           ['*',0,'#','D'] ]
ROW = [7,11,13,15]
COL = [12,16,18,22]
for j in range(4):
  GPIO.setup(COL[j], GPIO.OUT)
  GPIO.output(COL[j], 1)
  
for i in range(4):
  GPIO.setup(ROW[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)

array = [0,0,0];

clock1 = 0
clock2 = 0
clock3 = 0

clockA = 0
clockB = 0
clockC = 0

A = 0
B = 0
C = 0

def display(x, pin):
	
	if x>50 and pin==1:
		lcd.clear()
		lcd.write_string('[B1,C1]')
		time.sleep(0.9)
	if x>50 and pin==2:
		lcd.clear()
		lcd.write_string('[A1,C1]')
		time.sleep(0.9)
	if x>50 and pin==3:
		lcd.clear()
		lcd.write_string('[A1,B1]')
		time.sleep(0.9)
	
	if x>50 and pin==4:
		lcd.clear()
		lcd.write_string('[No space]')
		time.sleep(0.9)
		
	if x>50 and pin==5:
		lcd.clear()
		lcd.write_string('[C1]')
		time.sleep(0.9)
		
	if x>50 and pin==6:
		lcd.clear()
		lcd.write_string('[B1]')
		time.sleep(0.9)		
	
	if x>50 and pin==7:
		lcd.clear()
		lcd.write_string('[A1]')
		time.sleep(0.9)

while True:
	
    if GPIO.input(21):
        clock1=clock1+1
        if clock1>2:
			clockA = clockA + 1
			print clockA
			A = clockA
			array[0] = A
			display(A, 1)
			
    else:
		#print("A1 low")
		print "A1= "+str(A)
		clock1 = 0
		clockA = 0
		
	
    if GPIO.input(19):
        clock2=clock2+1
        if clock2>2:
			clockB = clockB + 1
			print clockB
			B = clockB
			array[1] = B
			display(B, 2)
			
    else:
		#print("B1 low")
		print "B1= "+str(B)
		clock2 = 0
		clockB = 0
			
		
    if GPIO.input(10):
        clock3=clock3+1
        if clock3>2:
			clockC = clockC + 1
			print clockC
			C = clockC
			array[2] = C
			display(C, 3)
			
    else:
		#print("C1 low")
		print "C1= "+str(C)
		clock3 = 0
		clockC = 0
			
		
    if GPIO.input(21)==0 and GPIO.input(10)==0 and GPIO.input(19)==0:
        lcd.clear()
        lcd.write_string('[A1,B1,C1]')
        time.sleep(0.5)
        
    if GPIO.input(21)==1 and GPIO.input(10)==1 and GPIO.input(19)==1:
		lcd.clear()
		lcd.write_string('No space')
		time.sleep(0.5)
        
    if GPIO.input(21)==1 and GPIO.input(19)==1:
		display(100, 5)
        
    if GPIO.input(21)==1 and GPIO.input(10)==1:
		display(100, 6)
        
    if GPIO.input(19)==1 and GPIO.input(10)==1:
		display(100, 7)
			
    for j in range(4):
		GPIO.output(COL[j],0)
 
		for i in range(4):
			if GPIO.input(ROW[i]) == 0:
				bal1= MATRIX[i][j]
				print bal1
				if bal1=='A':
					lcd.clear()
					lcd.write_string('TK.'+str(array[0]*5))
					print (array)
					time.sleep(0.5)
				if bal1=="B":
					lcd.clear()
					lcd.write_string('TK.'+str(array[1]*5))
					time.sleep(0.5)
				if bal1=='C':
					lcd.clear()
					lcd.write_string('TK.'+str(array[2]*5))
					time.sleep(0.5)	 	
				time.sleep(0.4)
				while(GPIO.input(ROW[i]) == 0):
					pass
														
		GPIO.output(COL[j],1)
