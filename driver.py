import subprocess
import cv2
import numpy as np
import RPi.GPIO as GPIO
import time

def run_motor1():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.OUT)
    GPIO.output(17, GPIO.HIGH) # Motor 1 ON
    print("Motor 1 is ON")
    time.sleep(1)
    GPIO.output(17, GPIO.LOW)
    GPIO.cleanup()

def run_motor2():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    GPIO.output(18, GPIO.HIGH) # Motor 2 ON
    print("Motor 2 is ON")
    time.sleep(1)
    GPIO.output(18, GPIO.LOW)
    GPIO.cleanup()

# Specify the output file name
output_file = "test.jpg"

# Run the libcamera-still command
capture_command = ["libcamera-still", "-o", output_file]
subprocess.run(capture_command)
print(f"Image captured and saved as {output_file}")

# Read the captured image using OpenCV
image = cv2.imread(output_file)

# Check if the image is successfully loaded
if image is None:
    print(f"Error: Could not read the image at {output_file}")
else:
    # Calculate the average color values
    average_color = np.mean(image, axis=(0, 1))
    
    # Store red, green, and blue values in variables
    green_value, blue_value, red_value = average_color
    
    # Convert BGR to RGB for a more human-friendly representation
    average_color_rgb = average_color[::-1]
    print("Average Color (RGB):", average_color_rgb)
    
    # Display the separate values
    print("Red Value:", red_value)
    print("Green Value:", green_value)
    print("Blue Value:", blue_value)
    
    # Add if cases based on the ranges of the variables
    if red_value < 40:
        # Green
        print("Condition 1 satisfied.")
    if red_value > 40 and red_value < 74:
        # Brown
        print("Condition 2 satisfied.")
        run_motor1()
    if red_value > 76 and red_value < 90:
        # Burnt Brown
        print("Condition 3 satisfied.")
        run_motor1()
        run_motor2()
    if red_value > 90:
        # Yellow
        print("Condition 4 satisfied.")
        run_motor2()
