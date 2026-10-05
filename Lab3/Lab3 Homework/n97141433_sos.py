import RPi.GPIO as GPIO
import time

LED_PIN = 11
BUZZER_PIN = 12

GPIO.setmode(GPIO.BOARD)

GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# 蜂鳴器頻率 523Hz
buzzer = GPIO.PWM(BUZZER_PIN, 523)

SHORT = 0.2
LONG = 0.6
GAP = 0.2


def signal(duration):
    # LED 亮，同時蜂鳴器響
    GPIO.output(LED_PIN, GPIO.HIGH)
    buzzer.start(50)

    time.sleep(duration)

    # LED 滅，同時蜂鳴器停止
    GPIO.output(LED_PIN, GPIO.LOW)
    buzzer.stop()

    time.sleep(GAP)


try:
    while True:

        print("S")

        # S = ...
        signal(SHORT)
        signal(SHORT)
        signal(SHORT)

        time.sleep(0.4)

        print("O")

        # O = ---
        signal(LONG)
        signal(LONG)
        signal(LONG)

        time.sleep(0.4)

        print("S")

        # S = ...
        signal(SHORT)
        signal(SHORT)
        signal(SHORT)

        print("SOS finished")

        # 完整 SOS 播完後停 2 秒
        time.sleep(2)

except KeyboardInterrupt:
    pass

finally:
    buzzer.stop()
    GPIO.cleanup()