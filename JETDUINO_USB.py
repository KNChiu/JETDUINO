#!/usr/bin/python3

""" NKUST AICT <KaiNengChiu>
2020-05-29 v0.1    UART-ttyTHS1 TX,RX
2020-05-30 v0.5    加入指令
2020-06-02 v0.7    封裝為類別
2020-06-03 v0.75   包成套件
2020-06-04 v0.75   修改cmd輸入方式(字串, 整數)
2020-06-08 v0.8    解析兩筆資料方式修改
License: GPLv2
"""

import time
import serial
import io

class USBSerial():

    def __init__(self):
        self.CMDARRARY = ["NULL", b"START\n", b"STOP\n", b"RESPOND\n", b"SPEEDUP\n"]  # 預設指令
        #self.setSerial()
        #self.getSerial()

    def setSerial(self, serialPort, baudrate):    # 設定連線通道
        self.serial_port = serial.Serial(
            #port="/dev/ttyTHS1",  # Jetson nano TX,RX
            #port="/dev/ttyUSB0",  # Jetson nano USB
            #'COM20',              # 電腦
            serialPort,            
            baudrate=baudrate,
            bytesize=serial.EIGHTBITS,    # 8bit
            parity=serial.PARITY_NONE,    # 檢查
            stopbits=serial.STOPBITS_ONE, # 停止位元
            timeout=10.0                  # 連線超時設定
        )
        time.sleep(0.1)
    
    def getSerial(self, serialGet):                  # 監視序列

        data = ""
        sendFinish = False
        print("----------------------")
        print('serial send:', serialGet)
        # time.sleep(0.5)
        
        while (sendFinish == False):
            # time.sleep(0.5)
            if (self.serial_port.inWaiting() != 0):
                data_raw = self.serial_port.readline()
                data = data_raw.decode()
                data = data.strip()
                #print('redata :', data_raw)
                #print("----------------------")
                print('serial get:', data)
                

            if (data == 'UART_Finish'):
                print("----------------------")
                sendFinish = True


    def sendCmd(self, cmdSend, cmdData):
            cmdData_str = str(cmdData)
            self.serial_port.write((cmdSend+"\n").encode())
            self.getSerial((cmdSend+"\n").encode())
            
            self.serial_port.write((cmdData_str+"\n").encode())
            self.getSerial((cmdData_str+"\n").encode())
            

        
        

                
            
       




