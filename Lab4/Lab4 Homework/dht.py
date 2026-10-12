import time
import adafruit_dht
import board

# DHT11 的 DOUT 接 Raspberry Pi 實體 PIN 10
# 實體 PIN 10 = BCM GPIO15
dht_device = adafruit_dht.DHT11(board.D15)

print("DHT11 溫濕度感測器開始讀取...")
print("按 Ctrl+C 結束程式")

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
            # DHT11 偶爾讀取失敗是正常現象
            print(err.args[0])

        # 每 2 秒讀取一次
        time.sleep(2.0)

except KeyboardInterrupt:
    print("\n程式結束")

finally:
    dht_device.exit()