const int ledPins[] = {5, 4, 3};
const int buttonPins[] = {8, 9, 10};
const int numButtons = 3;

void setup() {
  Serial.begin(9600);
  for (int i = 0; i < numButtons; i++) {
    pinMode(ledPins[i], OUTPUT);
    pinMode(buttonPins[i], INPUT_PULLUP); // <-- internal pull-up for real Nano
  }
}

void loop() {
  for (int i = 0; i < numButtons; i++) {
    int buttonState = digitalRead(buttonPins[i]);

    if (buttonState == LOW) { // pressed
      digitalWrite(ledPins[i], HIGH);
      
      Serial.print("{\"button\":");
      Serial.print(i + 1);
      Serial.println(",\"state\":\"pressed\"}");
    } else {
      digitalWrite(ledPins[i], LOW);
    }
  }

  delay(400);
}
