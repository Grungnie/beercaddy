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


void send_log(String message) {
  //char command = char(0);
  char end_stop = char(255);
  String send_message = String(message + end_stop);
  String send_message_with_command = String(0x00 + send_message);

  int send_length = send_message_with_command.length()+1;

  char charBuf[send_length];
  send_message_with_command.toCharArray(charBuf, send_length);
  Serial.write(charBuf);
}


// the loop routine runs over and over again forever:
void loop() {
  send_log("Hello Matthew");
  delay(1000);
}

