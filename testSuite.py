import time
import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

# Set up GPIO and MCP3008
GPIO.setmode(GPIO.BOARD)
led_pin = 11
GPIO.setup(led_pin, GPIO.OUT)

SPI_PORT = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

# Function to blink LED
def blink_led(times, interval):
    for _ in range(times):
        GPIO.output(led_pin, GPIO.HIGH)
        time.sleep(interval)
        GPIO.output(led_pin, GPIO.LOW)
        time.sleep(interval)

# Function to read light sensor and determine brightness
def read_light_sensor():
    threshold = 300
    duration = 5  # 5 seconds
    start_time = time.time()
    while time.time() - start_time < duration:
        light_value = mcp.read_adc(0)  # Assuming light sensor is connected to channel 0
        if light_value > threshold:
            print(f"Light Value: {light_value} - Bright")
        else:
            print(f"Light Value: {light_value} - Dark")
        time.sleep(0.1)

# Function to read sound sensor and detect taps
def read_sound_sensor():
    threshold = 200  # Adjust this threshold based on experimentation
    duration = 5  # 5 seconds
    start_time = time.time()
    while time.time() - start_time < duration:
        sound_value = mcp.read_adc(1)  # Assuming sound sensor is connected to channel 1
        print(f"Sound Value: {sound_value}")
        if sound_value > threshold:
            GPIO.output(led_pin, GPIO.HIGH)  # Turn on LED for 100ms if sound is above threshold
            time.sleep(0.1)
            GPIO.output(led_pin, GPIO.LOW)
        time.sleep(0.1)

# Main testing routine
try:
    while True:
        # Blink the LED 5 times with on/off intervals of 500ms
        blink_led(5, 0.5)
        
        # Read light sensor for 5 seconds with intervals of 100ms
        read_light_sensor()
        
        # Blink the LED 4 times with on/off intervals of 200ms
        blink_led(4, 0.2)
        
        # Read sound sensor for 5 seconds with intervals of 100ms
        read_sound_sensor()

except KeyboardInterrupt:
    print("Testing routine interrupted by user.")
finally:
    GPIO.cleanup()  # Clean up GPIO settings when the script exits

