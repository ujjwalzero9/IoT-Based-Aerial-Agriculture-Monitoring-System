1) Code to turn on the buzzer with PWM signal on Raspberry Pi Pico:

python
from machine import Pin, PWM

buzzer_pin = Pin(16, Pin.OUT)
button_pin = Pin(21, Pin.IN, Pin.PULL_UP)
pwm_buzzer = PWM(buzzer_pin, freq=200, duty=20)

while True:
    if not button_pin.value():
        pwm_buzzer.duty(20)  # Adjust duty cycle as needed
    else:
        pwm_buzzer.duty(0)


2) To set a PWM frequency of 4kHz:

python
pwm_freq_value = int(1e6 / 4000)  # Calculating the value to pass to freq()


3) To set a PWM duty cycle of 75%:

python
pwm_duty_value = int(75 * 65535 / 100)  # Calculating the value to pass to duty()


4) Code to change the frequency of an existing PWM signal to 2kHz:

python
existing_pwm_channel.freq(2000)  # Replace existing_pwm_channel with your PWM channel


Adjust pin numbers and channel accordingly in the provided code snippets.
