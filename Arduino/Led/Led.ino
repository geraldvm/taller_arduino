const int ledPin =  13;      // the number of the LED pin
void setup()
{
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
  Serial.println("START");
}

void loop()
{
  
  //Serial.println(read());
  read();
}

void read(){
  if (Serial.available() > 0) {
    // read the incoming string:
    String incomingString = Serial.readString();

    // prints the received data
    Serial.print("I received: ");
    Serial.println(incomingString);
    compareIncoming(incomingString);
    //return incomingString;
  }
}

void compareIncoming(String message){
  if(message=="hola"){
    Serial.println("COMPARE");
    digitalWrite(ledPin, HIGH);
    delay(1000); // Wait for 1000 millisecond(s)
    digitalWrite(ledPin, LOW);
    delay(1000); // Wait for 1000 millisecond(s)
  }
}
