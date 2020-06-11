import JETDUINO_USB as JDU
import time

u = JDU.USBSerial()    # 通道, 鮑率 
u.setSerial('COM20', 9600)    # "/dev/ttyUSB0"

while True:
    u.sendCmd("RESPOND", 0)    # "START", "STOP", "RESPOND"
    time.sleep(5)
    u.sendCmd("BLINK", 2)    # "START", "STOP", "RESPOND"
    time.sleep(5)




