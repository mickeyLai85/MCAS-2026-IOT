import RPi.GPIO as GPIO
import time

# BCM GPIO 編號
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# HC-SR04
TRIG = 23
ECHO = 24

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, GPIO.LOW)
time.sleep(2)


def measure_distance():

    # 發送 10 us Trigger
    GPIO.output(TRIG, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIG, GPIO.LOW)

    # 等待 ECHO 變 HIGH
    timeout = time.monotonic() + 0.05

    while GPIO.input(ECHO) == GPIO.LOW:
        if time.monotonic() > timeout:
            return None

    pulse_start = time.monotonic()

    # 等待 ECHO 回到 LOW
    timeout = time.monotonic() + 0.05

    while GPIO.input(ECHO) == GPIO.HIGH:
        if time.monotonic() > timeout:
            return None

    pulse_end = time.monotonic()

    # Echo 高電位時間
    pulse_duration = pulse_end - pulse_start

    # 距離 = 時間 × 聲速 / 2
    distance = pulse_duration * 17150

    return round(distance, 2)


try:

    print("HC-SR04 倒車雷達啟動")
    print("按 Ctrl+C 結束程式")
    print("----------------------------")

    while True:

        distance = measure_distance()

        if distance is None:
            print("感測器讀取失敗")

        else:

            if distance < 20:
                status = "注意！！！"
            else:
                status = "沒事"

            print(
                "Distance: {:.2f} cm    Status: {}".format(
                    distance,
                    status
                )
            )

        time.sleep(0.5)


except KeyboardInterrupt:

    print("\n停止測量")


finally:

    GPIO.cleanup()
    print("GPIO 已清理")