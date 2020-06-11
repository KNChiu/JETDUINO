// NKUST AICT <KaiNengChiu>
// 2020-05-29 v0.1   UART-ttyTHS1
// 2020-05-30 v0.5
// 2020-06-02 v0.7   time cmd
// 2020-06-03 v0.75  回應發送結束
// 2020-06-04 v0.75  修改指令判斷方式(使用字串陣列)
// License: GPLv2

#define LED_PIN 13

int MODE = 0;

void setup(){
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(9600);

  Serial.println("Arduino UART on");  // 初始提示訊息
  Serial.println("UART_Finish");      // 結束傳送
// delay(100);
}

void loop(){
    int cont = resolveCmd(getSerial());

    switch (MODE){
      case 0:
        break;
      case 1:
        for (int i = 0; i < cont; i++){
          digitalWrite(LED_PIN, HIGH);
          delay(200);
          digitalWrite(LED_PIN, LOW);
          delay(200);
        }
        break;
      
      default:
        break;
    }

}

String getSerial(){
  String str = "";
  if (Serial.available()) {                // 等待
    str = Serial.readStringUntil('\n');    // 讀到"\n"為止 
  }
  return str;
}

int resolveCmd(String getCmd){              // 解析收到的資料，如果沒有帶數值回傳0，有就回傳數值
  int getData = 0;
  

  if (getCmd != ""){
    if (getCmd == "START"){
      MODE = 0;
      Serial.println("v0.75 start");

    }else if (getCmd == "STOP"){
      MODE = 0;
      Serial.println("arduino stop");

    }else if (getCmd == "RESPOND"){
      MODE = 0;
      Serial.println(bootTime());

    }else if (getCmd == "SPEEDUP"){
      MODE = 0;
      Serial.println("SPEEDUP");

    }else if (getCmd == "BLINK"){
      MODE = 1;
      Serial.println("BLINK");

    }else if (getCmd.toInt() >= 0){      // 判斷是否有帶數值
      getData = getCmd.toInt();
      Serial.println(getData);
      
    }else{
      Serial.println(getCmd + "ISNOTCMD");

    }

    Serial.println("UART_Finish");
  }
  return getData;                         // 回傳數值，否則回傳0
}

String bootTime() {
  long t = millis() / 1000;        // 晶片開機時間(ms)
  word h = t / 3600;
  byte m = (t / 60) % 60;
  byte s = t % 60;
  String theTime = String(h) + ":" + String(m) + ":" + String(s);

  return theTime;
}

