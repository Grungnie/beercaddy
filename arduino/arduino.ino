/*
  Blink
  Turns on an LED on for one second, then off for one second, repeatedly.
 
  This example code is in the public domain.
 */

// the setup routine runs once when you press reset:
void setup() {                
  // initialize the digital pin as an output.
  Serial.begin(9600);
}

// the loop routine runs over and over again forever:
void loop() {
  char command = char(0);
  char end_stop = char(255);
  String message = "Hello Matthew";
  String send_message = String(command + message + end_stop);

  int send_length = send_message.length()+1;

  char charBuf[send_length];
  send_message.toCharArray(charBuf, send_length);
  
  Serial.write(charBuf);
  delay(1000);
}

