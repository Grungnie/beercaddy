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
  Serial.write("hello"); //send the string “hello” and return the length of the string.
  delay(500);               // wait for a second
  Serial.write("Matthew"); //send the string “hello” and return the length of the string.
  delay(500);               // wait for a second
}
