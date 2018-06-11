#include <Servo.h>

Servo mainhoist;
int staticdir = 97;
int gospeed = 102;
int backspeed = 94;
void setup() {
  Serial.begin(9600); // set the baud rate
  Serial.println("Ready"); // print "Ready" once
  mainhoist.attach(8);
  mainhoist.write(staticdir);
}
void loop() {
  char inByte = ' ';
  if(Serial.available()){ // only send data back if data has been sent
    char inByte = Serial.read(); // read the incoming data
    Serial.println(inByte); // send the data back in a new line so that it is not all one long line
    if(inByte=='1'){
      Serial.println("Aye Aye Cap'n, Full Steam Ahead!");
      mainhoist.write(gospeed);
    }
    else if (inByte=='2'){
      Serial.println("Reverse Thrust Engaged.");
      mainhoist.write(backspeed);
    }
    else{
      mainhoist.write(staticdir);
      Serial.println("All Stopping Power!");
    }
  }
  delay(100); 
  Serial.flush();
}


