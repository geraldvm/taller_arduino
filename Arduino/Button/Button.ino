/*
  Button


  The circuit:
  - LED attached from pin 13 to ground through 220 ohm resistor
  - pushbutton attached to pin 2 from +5V
  - 10K resistor attached to pin 2 from ground

  - Note: on most Arduinos there is already an LED on the board
    attached to pin 13.


*/

// constants won't change. They're used here to set pin numbers:
const int buttonRed = 8;     // the number of the pushbutton pin
const int buttonGreen = 9;
const int buttonWhite = 10;
const int buttonBlue = 11;
const int ledPin =  13;      // the number of the LED pin



// variables will change:
int btnGreenState = 0;         // variable for reading the pushbutton status
int btnRedState = 0;
int btnBlueState = 0;
int btnWhiteState = 0;

void setup() {
  // initialize the LED pin as an output:
  pinMode(ledPin, OUTPUT);
  // initialize the pushbutton pin as an input:
  pinMode(buttonGreen, INPUT);
  pinMode(buttonBlue, INPUT);
  pinMode(buttonWhite, INPUT);
  pinMode(buttonRed, INPUT);
  Serial.begin(9600);
  Serial.println("Start");
}

void loop() {
  // read the state of the pushbutton value:
  btnGreenState = digitalRead(buttonGreen);
  btnBlueState = digitalRead(buttonBlue);
  btnWhiteState = digitalRead(buttonWhite);
  btnRedState = digitalRead(buttonRed);
  

  // check if the pushbutton is pressed. If it is, the buttonState is HIGH:
  if (btnGreenState == HIGH) {
    // turn LED on:
    Serial.println('g');
    digitalWrite(ledPin, HIGH);
  } else if (btnBlueState == HIGH) {
    // turn LED on:
    Serial.println('b');
    digitalWrite(ledPin, HIGH);
  } 
  else if (btnWhiteState == HIGH) {
    // turn LED on:
    Serial.println('w');
    digitalWrite(ledPin, HIGH);
  } else if (btnRedState == HIGH) {
    // turn LED on:
    Serial.println('r');
    digitalWrite(ledPin, HIGH);
  } 
  else {
    // turn LED off:
    digitalWrite(ledPin, LOW);
  }
  delay(500);
}
