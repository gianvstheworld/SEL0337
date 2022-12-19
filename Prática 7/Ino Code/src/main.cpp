// Declaração de bibliotecas
#include <Arduino.h>
#include <Wire.h>

// Declaração dos pinos de entrada e saída
const int ledPin = LED_BUILTIN;
const int analog_pin = A0;

// Função de recepção de dados
void receiveEvent(int howMany)
{
    Serial.println(F("---> Dados recebidos"));
    while (0 < Wire.available())
    {                            // enquanto houver dados para ler
        char c = Wire.read();    // recebe um byte do mestre
        digitalWrite(ledPin, c); // escreve o byte no pino de saída
    }
}

// Função de requisição de dados
void requestEvents()
{
    Serial.println(F("---> Pedido requerido"));
    Wire.write(highByte(analogRead(analog_pin))); // escreve o mais significativo
    Wire.write(lowByte(analogRead(analog_pin)));  // escreve o menos significativo
}

void setup()
{
    Serial.begin(9600);
    Serial.println("I2C Scanner");

    Wire.begin(0x8); // inicia a comunicação I2C como escravo
    Wire.onRequest(requestEvents);
    Wire.onReceive(receiveEvent);

    /*
    PARTE SÓ DO LED
    Wire.onReceive(receiveEvent); // registra evento de recepção

    pinMode(ledPin, OUTPUT);
    digitalWrite(ledPin, LOW);
    */
}

void loop()
{
    delay(100);
    Serial.println(analogRead(analog_pin));
}