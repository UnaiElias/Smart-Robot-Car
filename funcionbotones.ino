String command;
const int enAPin = 6; // Left motor PWM speed control
const int in1Pin = 7; // Left motor Direction ATZEA
const int in2Pin = 5; // Left motor Direction AURREA
const int in3Pin = 4; // Right motor Direction 1
const int in4Pin = 2; // Right motor Direction 2
const int enBPin = 3; // Right motor PWM speed control

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(in1Pin, OUTPUT);
  pinMode(in2Pin, OUTPUT);
  pinMode(enAPin, OUTPUT);
  pinMode(in3Pin, OUTPUT);
  pinMode(in4Pin, OUTPUT);
  pinMode(enBPin, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  
  
  if (Serial.available()){
    command = Serial.readStringUntil('\n'); //read until ‘\n’  
    command.trim(); 

    if(command.equals("Forward")){
      digitalWrite(enAPin, HIGH);
      digitalWrite(in1Pin, LOW);
      digitalWrite(in2Pin, HIGH);
      digitalWrite(enBPin, HIGH);
      digitalWrite(in3Pin, LOW);
      digitalWrite(in4Pin, HIGH);
      Serial.print("Going forward...");
    }
    else if(command.equals("Backward")){
      digitalWrite(enAPin, HIGH);
      digitalWrite(in1Pin, HIGH);
      digitalWrite(in2Pin, LOW);
      digitalWrite(enBPin, HIGH);
      digitalWrite(in3Pin, HIGH);
      digitalWrite(in4Pin, LOW);
      Serial.print("Going backward...");
    }
    else if(command.equals("Right")){
      digitalWrite(enAPin, HIGH);
      digitalWrite(in1Pin, LOW);
      digitalWrite(in2Pin, HIGH);
      digitalWrite(enBPin, HIGH);
      digitalWrite(in3Pin, HIGH);
      digitalWrite(in4Pin, LOW);
      Serial.print("Going right...");
    }
    else if(command.equals("Left")){
      digitalWrite(enAPin, HIGH);
      digitalWrite(in1Pin, HIGH);
      digitalWrite(in2Pin, LOW);
      digitalWrite(enBPin, HIGH);
      digitalWrite(in3Pin, LOW);
      digitalWrite(in4Pin, HIGH);
      Serial.print("Going left...");
    }
    else if(command.equals("Stop")){
     digitalWrite(enAPin, LOW);
     digitalWrite(enBPin, LOW);
     Serial.print("Stop!");
  }
  delay(100);
}





}
