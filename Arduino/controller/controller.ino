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
const int ledPin =  7;      // the number of the LED pin



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
  readBtn();
  readSerial();
}

void readBtn(){
  // read the state of the pushbutton value:
  btnGreenState = digitalRead(buttonGreen);
  btnBlueState = digitalRead(buttonBlue);
  btnWhiteState = digitalRead(buttonWhite);
  btnRedState = digitalRead(buttonRed);
  

  // check if the pushbutton is pressed. If it is, the buttonState is HIGH:
  if (btnGreenState == HIGH) {
    Serial.println('g');
 
  } else if (btnBlueState == HIGH) {
    // turn LED on:
    Serial.println('b');

  } 
  else if (btnWhiteState == HIGH) {
    // turn LED on:
    Serial.println('w');
  } else if (btnRedState == HIGH) {
    // turn LED on:
    Serial.println('r');
  } 
  delay(500);
  
}

void readSerial(){
  if (Serial.available() > 0) {
    // read the incoming string:
    String incomingString = Serial.readString();

    // prints the received data
    //Serial.print("I received: ");
    //Serial.println(incomingString);
    compareIncoming(incomingString);
    //return incomingString;
  }
}


void compareIncoming(String message){
  if(message=="hola"){
    digitalWrite(ledPin, HIGH);
    delay(1000); // Wait for 1000 millisecond(s)
    digitalWrite(ledPin, LOW);
    delay(1000); // Wait for 1000 millisecond(s)
  }
}
