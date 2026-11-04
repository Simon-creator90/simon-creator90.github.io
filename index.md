# ESP32 Connect

## Dein ESP32. Dein Smartphone. Deine Verbindung.

**ESP32 Connect** macht deinen ESP32 direkt über dein Android-Smartphone steuerbar. Die Verbindung erfolgt kabellos über Bluetooth Low Energy (BLE). So kannst du Geräte verbinden, Befehle senden und Daten empfangen – ganz ohne Computer als Bedienoberfläche.

![ESP32 Connect – ESP32 Mikrocontroller](Esp32.jpg)

[**Android-App herunterladen**](esp32_connect.apk) · [**MicroPython-Programm herunterladen**](esp32_connect.py)

---

## Was ESP32 Connect kann

- **Kabellos verbinden:** Stelle eine Bluetooth-LE-Verbindung zwischen Smartphone und ESP32 her.
- **Direkt steuern:** Sende Befehle über die Android-App an deinen Mikrocontroller.
- **Hardware bedienen:** Schalte beispielsweise eine angeschlossene LED ein und aus.
- **Daten empfangen:** Übertrage Informationen vom ESP32 auf dein Smartphone.
- **Daten visualisieren:** Stelle empfangene Messwerte in einem Diagramm dar.
- **Flexibel erweitern:** Nutze das Projekt als Grundlage für eigene ESP32-Anwendungen.

---

## Die App in Aktion

### 1. Geräteverbindung

Die App zeigt übersichtlich, ob eine Verbindung zum ESP32 besteht. Du kannst nach einem Gerät suchen und die Verbindung herstellen.

![ESP32 Connect – kein Gerät verbunden](Nicht_verbunden.jpg)

*Die App im Zustand ohne aktive Verbindung.*

![ESP32 Connect – ESP32 verbunden](Verbunden.jpg)

*Nach erfolgreicher Verbindung steht die Kommunikation mit dem ESP32 zur Verfügung.*

### 2. Daten empfangen und visualisieren

ESP32 Connect kann nicht nur Befehle senden, sondern auch Daten vom Mikrocontroller empfangen. Die empfangenen Werte lassen sich direkt in einem Diagramm darstellen.

![ESP32 Connect – Diagramm mit empfangenen Daten](Diagramm.jpg)

*Messwerte vom ESP32 werden in der App grafisch dargestellt.*

---

## Zwei Komponenten. Ein System.

### Android-App

Die Android-App bildet die Benutzeroberfläche. Sie ermöglicht die Verbindung mit dem ESP32 und die Bedienung der unterstützten Funktionen.

[**esp32_connect.apk – Android-App herunterladen**](esp32_connect.apk)

### MicroPython-Programm

Das Python-Programm läuft direkt auf dem ESP32. Es stellt die BLE-Kommunikation bereit, verarbeitet die Befehle der App und überträgt Daten an das Smartphone.

[**esp32_connect.py – MicroPython-Datei herunterladen**](esp32_connect.py)

---

## So funktioniert es

1. Das MicroPython-Programm wird auf dem ESP32 eingerichtet.
2. Die Android-App wird auf dem Smartphone installiert.
3. Smartphone und ESP32 verbinden sich über Bluetooth Low Energy.
4. Über die App können Befehle gesendet und Daten empfangen werden.
5. Empfangene Daten können in der App visualisiert werden.

---

## Jetzt ausprobieren

Alle benötigten Dateien stehen hier zum Download bereit:

- [**Android-App herunterladen – esp32_connect.apk**](esp32_connect.apk)
- [**MicroPython-Programm herunterladen – esp32_connect.py**](esp32_connect.py)

**ESP32 Connect – mobile Kontrolle und Datenvisualisierung für deinen ESP32.**
