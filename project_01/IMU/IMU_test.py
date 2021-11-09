"""
--------------------------------------------------------------------------
IMU Test
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


This code was downloaded from the adafruit library
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

import time
import board
import adafruit_mpu6050

i2c = board.I2C()  # uses board.SCL and board.SDA
mpu = adafruit_mpu6050.MPU6050(i2c)

while True:
    print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2"%(mpu.acceleration))
    print("Gyro X:%.2f, Y: %.2f, Z: %.2f degrees/s"%(mpu.gyro))
    print("Temperature: %.2f C"%mpu.temperature)
    print("")
    time.sleep(10)
