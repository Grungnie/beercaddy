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
  // Set start bit
  String send_message = ":";

  // Set the message size
  int send_length = message.length();
  send_message.concat(char(send_length));

  // Set the message command
  send_message.concat(char(1));

  // Add the message
  send_message.concat(message);

  // Add and calculate checksum
  send_message.concat(char(0x01));

  char charBuf[send_length];
  send_message.toCharArray(charBuf, send_length+5);
  Serial.write(charBuf);
}


// the loop routine runs over and over again forever:
void loop() {
  send_log("Hello Matthew");
  delay(1000);
}

