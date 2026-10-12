import socket
import threading
import time
import tm1637

# -----------------------------
# TM1637 設定
# -----------------------------
CLK = 23
DIO = 24

tm = tm1637.TM1637(clk=CLK, dio=DIO)
tm.brightness(3)

# -----------------------------
# 本機傳輸設定
# -----------------------------
HOST = "127.0.0.1"
PORT = 5000

received_data = ""


def receiver():
    global received_data

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_REUSEADDR,
        1
    )

    server.bind((HOST, PORT))
    server.listen(1)

    conn, addr = server.accept()

    while True:
        data = conn.recv(1024)

        if not data:
            break

        received_data = data.decode().strip()

        print("接收：", received_data)

        # 如果收到的是數字
        if received_data.isdigit():

            number = int(received_data)

            if 0 <= number <= 9999:
                tm.number(number)
                print("LED 顯示：", received_data)

    conn.close()
    server.close()


# 啟動接收端執行緒
thread = threading.Thread(
    target=receiver,
    daemon=True
)

thread.start()

time.sleep(1)

# 建立傳送端
client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

client.connect((HOST, PORT))

print("Lab4-3 數字傳輸測試")
print("輸入 0~9999")
print("輸入 q 離開")
print("----------------------------")

try:
    while True:

        data = input("請輸入要傳送的數字：")

        if data.lower() == "q":
            break

        # 檢查是不是數字
        if not data.isdigit():
            print("請輸入數字")
            continue

        number = int(data)

        # TM1637 最多顯示四位數
        if number > 9999:
            print("最大只能輸入 9999")
            continue

        print("傳送：", data)

        # 傳給自己
        client.send(data.encode())

        time.sleep(0.5)

        print("----------------------------")


except KeyboardInterrupt:
    print("\n程式停止")


finally:
    client.close()

    tm.show("    ")

    print("程式結束")