import time
import grovepi  # Assuming you are using GrovePi library for sensors and LED control

# Set pin numbers for sensors and LED (please adjust these according to your hardware setup)
led_pin = 2
light_sensor_pin = 0
sound_sensor_pin = 1

# Thresholds for light and sound sensors (you may need to adjust these after experimentation)
light_threshold = 300
sound_threshold = 100

# Blink LED function
def blink_led(times, interval):
    for _ in range(times):
        grovepi.digitalWrite(led_pin, 1)  # Turn ON LED
        time.sleep(interval)
        grovepi.digitalWrite(led_pin, 0)  # Turn OFF LED
        time.sleep(interval)

# Main testing routine
try:
    while True:
        # Blink LED 5 times with on/off intervals of 500ms
        blink_led(5, 0.5)

        # Read light sensor for 5 seconds with intervals of 100ms
        start_time = time.time()
        while time.time() - start_time < 5:
            light_value = grovepi.analogRead(light_sensor_pin)
            if light_value > light_threshold:
                print(f"Light Value: {light_value} - Bright")
            else:
                print(f"Light Value: {light_value} - Dark")
            time.sleep(0.1)

        # Blink LED 4 times with on/off intervals of 200ms
        blink_led(4, 0.2)

        # Read sound sensor for 5 seconds with intervals of 100ms
        start_time = time.time()
        while time.time() - start_time < 5:
            sound_value = grovepi.analogRead(sound_sensor_pin)
            print(f"Sound Value: {sound_value}")
            if sound_value > sound_threshold:
                grovepi.digitalWrite(led_pin, 1)  # Turn ON LED for 100ms if sound is above threshold
                time.sleep(0.1)
                grovepi.digitalWrite(led_pin, 0)  # Turn OFF LED
            time.sleep(0.1)

except KeyboardInterrupt:
    print("Testing routine interrupted by user.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    grovepi.digitalWrite(led_pin, 0)  # Ensure the LED is turned off
