# ENGI301
Repository for ENGI301 coursework

This repository now includes a simple calculator code and a way to turn on the USR3 LED on the pocketbeagle.
This repository has code to make an LED blink.

This repository also includes the code to run a device that can alert a user that the have been sitting for too long (Project_01).

This repository includes a possible PCB design for the device designed in Project_01 (Project_02) further description is at the bottom of this Readme.    
      
      Below is the Story for this device.
During this pandemic, we have all been sitting at home and not getting the exercise that we need. Doctors recommend that we stand for at least 4 hours a day. This device was created to be able to detect your body position to alert you when you need to stand. This device could be useful when working from home or in the office to act as a friendly reminder and combat a sedentary lifestyle.

Using an accelerometer/gyroscope (MPU-6050) and python, the body position was determined. Since the device is attached to the leg using velcro straps, the acceleration due to gravity can be used to differentiate between sitting and standing. When gravity is in the z-direction, the user is sitting and when gravity is in the y-direction, the user is standing.  To determine when the user is walking, the magnitude of the acceleration in the x, y, and z-directions had to be above 6 m/s^2. This calculation was based on the project by Ashish Choudhary where they create a Portable Step Counter using ATtiny85 and MPU6050. When The position was shown on an LCD screen (Adafruit RGB backlight positive LCD 16x2). If the user has been sitting for longer than an hour, the LCD screen will display the message, "You need to stand!!!" In addition to the message, a mini vibration motor will vibrate repeatedly until the user stands. As soon as the user stands, the motor stops and the message changes to, "Standing". The clock will begin again to count down the hour once the user sits again. The device is powered using a mini portable phone charger, and the microcontroller that regulates this system is a PocketBeagle. 

Overall, this device is functional in alerting the user that they have been sitting for an extended period of time. However, there is still room for improvements. The detection of body position is not effective in distinguishing between standing and walking. This problem can be addressed through an adjustment of the cutoff values after gaining a better understanding of the data outputted by the accelerometer/gyroscope. Additionally, the device is very bulky for a wearable so next steps would include making a printed circuit board to miniaturize the device.


Implementation instructions:

Initialize the PocketBeagle by doing the following:
1.  Connect the PocketBeagle to the internet
2. sudo apt-get update
3. sudo apt-get install build-essential python-dev python-setuptools python-smbus -y
4. git clone https://github.com/adafruit/adafruit-beaglebone-io-python
5. sudo pip3 install --upgrade Adafruit_BBIO

Setting up the hardware:
1. Download Adafruit library for the LCD screen
2. Connect LCD screen following these instructions 
   Note: Although, the LCD screen in the instructions only has 16 pins, the pins all match up to the 18 pin one used in this project. The only difference is that pin 16, 17, and 18 can be grounded in any combination, with at least one of them grounded, to produce a variety colors for the backlight.
3. Test the LCD screen using the rgb_lcd_test.py file
4. Download Adafruit library for MPU6050 
5. Connect Vcc to 3.3V
6. Connect GND to ground
7. Connect SCL to Pin 2_9 on PocketBeagle (the corresponding I2C bus) and a pull up resistor (1 kOhm) to 3.3V
8. Connect SDA to Pin 2_11 on Pocketbeagle (the corresponding I2C bus) and a pull up resistor (1 kOhm) to 3.3V
9. Test the accelerometer/gyroscope using the IMU_test.py file
10. Connect one side wire of the the mini vibrating motor to Pin P2_1 and the other wire to ground. (May need to solder wires on to the mini vibrating motor to make the wires long enough to make the connections.)
11. Connect one button pin to Pin P2_1 with a pull up resistor from this node to 5V.
12. Connect the other pin of the button to ground.

After the hardware is set up, then the BodyPosition.py file can be run and the device can be used. On Cloud 9, the device was made to run when it is connected to power using the cron functionality. 


      PCB Design
This PCB was designed to mimic the breadboard of the initial construction. Amendments were made to have more than one mini vibration motor so that the vibration could be more intense when alerting the user when to stand. The mini motors are also at the back of the PCB board so it is against the leg of the user when it is strapped on. Additionally, the IMU is put in the middle of the board so that it can better detect the changes in body position. Other minor connection changes were also made so that there was easier formation of traces on the PCB, but none require pin recofigurations.
