/*
  Blink
  Turns on an LED on for one second, then off for one second, repeatedly.
 
  This example code is in the public domain.
 */

int counter;

// the setup routine runs once when you press reset:
void setup() {                
  // initialize the digital pin as an output.
  Serial.begin(9600);
}


// the loop routine runs over and over again forever:
void loop() {
  // String message = "Hellow Matthew x" + String(counter);
  // py_log(message);
  // delay(1000);
  // counter += 1;

  recieve_data();
}


void py_log(String data) {
  return send_data(data, 1);
}


void send_data(String data, int command) {
  // Set start bit
  String send_message = ":";

  // Set the message size
  int send_length = data.length();
  send_message.concat(char(send_length));

  // Set the message command
  send_message.concat(char(command));

  // Add the message
  send_message.concat(data);

  // Add and calculate checksum
  byte byteBuf[send_length+4];
  send_message.getBytes(byteBuf, send_length+4);
  byte checksum = CRC8(byteBuf, send_length+3);
  send_message.concat(char(checksum));

  char charBuf[send_length+5];
  send_message.toCharArray(charBuf, send_length+5);
  Serial.write(charBuf);
}

void recieve_data() {
  int incomingByte = Serial.read();
  py_log(String(incomingByte));
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
