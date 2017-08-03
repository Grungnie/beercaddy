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

//CRC-8 - based on the CRC8 formulas by Dallas/Maxim
//code released under the therms of the GNU GPL 3.0 license
byte CRC8(const byte *data, byte len) {
  byte crc = 0x00;
  while (len--) {
    byte extract = *data++;
    for (byte tempI = 8; tempI; tempI--) {
      byte sum = (crc ^ extract) & 0x01;
      crc >>= 1;
      if (sum) {
        crc ^= 0x8C;
      }
      extract >>= 1;
    }
  }
  return crc;
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
  byte byteBuf[send_length+4];
  send_message.getBytes(byteBuf, send_length+4);
  byte checksum = CRC8(byteBuf, send_length+3);
  send_message.concat(char(checksum));

  char charBuf[send_length+5];
  send_message.toCharArray(charBuf, send_length+5);
  Serial.write(charBuf);
}


// the loop routine runs over and over again forever:
void loop() {
  send_log("Hello Matthew");
  delay(1000);
}

