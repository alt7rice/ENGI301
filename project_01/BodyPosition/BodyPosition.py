"""
--------------------------------------------------------------------------
Body Position Sensor
--------------------------------------------------------------------------
License:   
Copyright 2021 Angelica Torres

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this 
list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

This code uses components that were worked on in conjuction with the ENGI 301 
Professor Erik Welsh. Some parts of the code stem directly from the code 
developed in the class.

This code is calculating "walking" using the method developed by Ashish 
Choudhary in when they  delveloped a way to "Build a Portable Step Counter 
using ATtiny85 and MPU6050". 
https://circuitdigest.com/microcontroller-proejcts/build-a-portable-step-counter-using-attiny85-and-mpu6050

--------------------------------------------------------------------------


Use the following hardware components to make a body position sensor:  
  - Adafruit RGB backlight positive LCD 16x2 Display
  - Button
  - Potentiometer
  - MPU-6050 MPU6050 3 Axis Accelerometer Gyroscope 
  - Mini Vibration Motor

Requirements:
  - Hardware:
    - When sitting:   Display shows "Sitting"
        -If sitting for over an hour the Display will show "You need to stand!!"
        and the mini vibration motor will turn on 
    - When standing:  Display will show "Standing"
    - When standing:  Display will show "Walking"
    - Button: Starts and Stops the collection of body position data
    - User interaction:
        - Needs to change display in a way that aligns with user's position and 
        notify the user to stand.
        - Needs to start and stop when the user presses on and off button


Uses:
  - buzzer_music  library developed in class
  - adafruit_mpu6050 developed for accelerometer
  - adafruit_character_lcd for LCD screen
  - Adafruit_BBIO for PWM
  - time
  - cmath

"""

#General Imports
import time
import board

#Import for IMU
import adafruit_mpu6050

#Import fro LCD
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd

#To calculate acceleration for walking
import cmath


#Import for Haptic
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import buzzer_music


i2c = board.I2C()  # uses board.SCL and board.SDA
mpu = adafruit_mpu6050.MPU6050(i2c)

walking      = 0
prev_walking = 0

# Modify this if you have a different sized character LCD
lcd_columns = 16
lcd_rows = 2

# PocketBeagle Pin Config:
lcd_rs = digitalio.DigitalInOut(board.P1_2)
lcd_en = digitalio.DigitalInOut(board.P1_4)
lcd_d7 = digitalio.DigitalInOut(board.P2_24)
lcd_d6 = digitalio.DigitalInOut(board.P2_22)
lcd_d5 = digitalio.DigitalInOut(board.P2_20)
lcd_d4 = digitalio.DigitalInOut(board.P2_18)
#lcd_backlight = digitalio.DigitalInOut(board.P2_3)

# Initialise the lcd class
lcd = characterlcd.Character_LCD_Mono(
    lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows
)

seconds = 0   
buzzer = "P2_1"
button_pin = "P2_2"

# Initialize Button
GPIO.setup (button_pin, GPIO.IN)

try:
    sensor_on = False
    music = buzzer_music.BuzzerMusic(buzzer)
    walking = 0
    lcd.message = "    Sleeping     \n                   "
    while True:
        # Wait for button press
        while(GPIO.input(button_pin) == 1):
            if sensor_on:
                #print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2"%(mpu.acceleration))
                #print("Gyro X:%.2f, Y: %.2f, Z: %.2f degrees/s"%(mpu.gyro))
                #print("Temperature: %.2f C"%mpu.temperature)
                #print("")
                acc_x, acc_y, acc_z = mpu.acceleration
                gyro_x, gyro_y, gyro_z = mpu.gyro
                temperature = mpu.temperature
                #lcd.clear()
                prev_walking = walking
                #This calculation for walking is from Ashish Choudhary
                walking = cmath.sqrt((acc_x*acc_x)+(acc_y*acc_y)+(acc_z*acc_z))
                walking = abs(walking)
                
                #print("Walking = {0}    Prev = {1}   Diff = {2}".format(walking, prev_walking, abs(walking - prev_walking)))
                #print("Accel Y = {0}    Accel Z = {1}".format(acc_y, acc_z))
                
                
                if (acc_z < (-9.8)):
                    lcd.message = "                \n     Sitting       "
                    #lcd.clear()
                    seconds = seconds + 1
                    if seconds >= 3600: 
                      #Tells person to stand on LCD screen and starts buzzing after one hour of sitting
                        lcd.message = "   You need   \n   to stand!!!   "
                        music.zelda_secret()
                    time.sleep(0.9)
            
                elif (acc_y > (8.5)):
                    lcd.message = "                \n    Standing       "
                    seconds = 0
                    #lcd.clear()
                
                elif (abs(walking - prev_walking) > 6):
                    lcd.message = "                \n     Walking       "
                    seconds = 0
                    #lcd.clear()
            
                else:
                    lcd.clear()
                
                time.sleep(0.1)
            else:
                # Sleep for a short period of time to reduce CPU load
                time.sleep(0.1)

        # Turn on sensor or off based on current
        if sensor_on:
            sensor_on = False
            lcd.message = "    Sleeping     \n                   "
        else:
            sensor_on = True

        # Wait for button release to make sure state only switches once
        while(GPIO.input(button_pin) == 0):
            # Sleep for a short period of time to reduce CPU load
            time.sleep(0.1)

except KeyboardInterrupt:
    music.stop()
    lcd.clear()
    
