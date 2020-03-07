from sense_emu import SenseHat
import time
wait_for = 1


def send_to_aws(data):
    print("send data to aws")
    print(data)


def sensor_hat():
    sense = SenseHat()

    green = (0, 255, 0)
    white = (255, 255, 255)
    last_humidity = 0
    while True:
        time.sleep(wait_for)
        humidity = int(sense.humidity)
        # humidity_value = int64 * humidity / 100
        # pixels = [green if i < humidity_value else white for i in range(64)]
        # sense.set_pixels(pixels)
        if humidity > last_humidity + 1 or humidity < last_humidity - 1:

            send_to_aws(humidity)
            last_humidity = humidity


def main():
    print("Developed by Adilson Perinei - adilson@perinei.com")
    print("SenseHat Project: Send data to AWS IoT")
    sensor_hat()


main()
