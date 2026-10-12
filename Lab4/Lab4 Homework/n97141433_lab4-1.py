import time
import adafruit_dht
import board

# DHT11 接線：
# VCC  -> 實體 PIN 2 (5V)
# GND  -> 實體 PIN 6 (GND)
# DOUT -> 實體 PIN 7 (BCM GPIO4)

dht_device = adafruit_dht.DHT11(board.D4)

try:
    while True:
        try:
            # 讀取攝氏溫度
            temperature_c = dht_device.temperature

            # 攝氏轉華氏
            temperature_f = temperature_c * (9 / 5) + 32

            # 讀取濕度
            humidity = dht_device.humidity

            # 顯示結果
            print(
                "Temp:{:.1f} C / {:.1f} F    Humidity: {}%".format(
                    temperature_c,
                    temperature_f,
                    humidity
                )
            )

        except RuntimeError as err:
            # DHT11 偶爾讀取失敗時，顯示錯誤後繼續
            print(err.args[0])

        time.sleep(2.0)

except KeyboardInterrupt:
    print("\nProgram stopped")

finally:
    dht_device.exit()