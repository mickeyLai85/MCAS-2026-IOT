#!/usr/bin/env python3

from datetime import datetime
from time import sleep
import tm1637

# TM1637 接線 GPIO 編號（BCM）
CLK = 23
DIO = 24

# 建立 TM1637 物件
tm = tm1637.TM1637(clk=CLK, dio=DIO)

# 設定亮度 0~7
tm.brightness(3)

try:
    while True:
        # 取得目前時間
        now = datetime.now()

        hour = now.hour
        minute = now.minute
        second = now.second

        # 偶數秒顯示冒號，奇數秒關閉冒號
        if second % 2 == 0:
            colon = True
        else:
            colon = False

        # 顯示 HH:MM
        tm.numbers(hour, minute, colon)

        # 每 0.1 秒檢查一次時間
        sleep(0.1)

except KeyboardInterrupt:
    # Ctrl+C 時清除顯示器
    tm.show('    ')
    print("\nClock stopped")