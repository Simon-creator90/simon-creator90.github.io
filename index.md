# ESP32 Connect
## Dein ESP32. Dein Smartphone. Kabellose Kontrolle.

**ESP32 Connect** verbindet deinen ESP32 mit deinem Android-Smartphone und macht die Steuerung direkt über eine mobile App möglich. Statt für jede Interaktion einen Computer oder eine kabelgebundene Verbindung zu benötigen, kannst du deinen Mikrocontroller bequem per Bluetooth Low Energy (BLE) bedienen.

Die Lösung besteht aus zwei Komponenten: einer Android-App für die Bedienung und einem MicroPython-Programm für den ESP32.

---

## Was macht ESP32 Connect besonders?

- **Kabellose Steuerung:** Kommuniziere mit deinem ESP32 über Bluetooth Low Energy.
- **Bedienung per Smartphone:** Steuere Funktionen direkt über die Android-App.
- **Schnelle Interaktion:** Sende Befehle an den Mikrocontroller und frage Informationen ab.
- **LED-Steuerung:** Schalte die angeschlossene LED ein und aus.
- **Einfach erweiterbar:** Nutze die Verbindung als Grundlage für weitere ESP32-Projekte und eigene Funktionen.
- **Zwei aufeinander abgestimmte Komponenten:** Die Android-App und das MicroPython-Programm arbeiten zusammen.

## Die wichtigsten Funktionen

### LED-Steuerung

Schalte eine angeschlossene LED direkt über dein Smartphone ein oder aus. So kannst du die kabellose Steuerung unmittelbar ausprobieren.

### Kommunikation mit dem ESP32

Sende Befehle von der App an den Mikrocontroller und fordere Informationen an. Damit entsteht eine direkte Schnittstelle zwischen der mobilen Bedienung und der Hardware.

### Bluetooth Low Energy

Die Verbindung erfolgt über BLE. Dadurch ist keine klassische USB-Verbindung zwischen Smartphone und ESP32 für die Bedienung erforderlich.

### Grundlage für eigene Projekte

ESP32 Connect lässt sich als Ausgangspunkt für weitere Anwendungen nutzen – beispielsweise für eigene Steuerungsfunktionen, Sensorprojekte oder interaktive Hardware.

---

## Die beiden Bestandteile

### 1. ESP32 Connect für Android

Die Android-App ist die Bedienoberfläche des Projekts. Über sie kannst du eine Verbindung zum ESP32 herstellen und die unterstützten Funktionen nutzen.

**[Android-App herunterladen – esp32_connect.apk](./esp32_connect.apk)**

> Lade die APK herunter und installiere sie auf deinem Android-Gerät. Android kann vor der Installation aus einer außerhalb des Play Stores bezogenen Quelle eine zusätzliche Bestätigung verlangen.

### 2. ESP32 Connect für MicroPython

Das Python-Programm wird auf dem ESP32 ausgeführt. Es übernimmt die Mikrocontroller-Seite der Kommunikation und verarbeitet die Befehle der Android-App.

**[MicroPython-Datei herunterladen – esp32_connect.py](./esp32_connect.py)**

Übertrage die Datei mit einem geeigneten MicroPython-Werkzeug auf deinen ESP32 und richte das Gerät entsprechend deinem bestehenden Projekt ein.

---

## So funktioniert es

1. **Vorbereiten:** Richte den ESP32 mit MicroPython und der bereitgestellten Python-Datei ein.
2. **Installieren:** Installiere die Android-App auf deinem Smartphone.
3. **Verbinden:** Stelle über Bluetooth Low Energy die Verbindung zum ESP32 her.
4. **Steuern:** Nutze die App, um unterstützte Befehle zu senden und die verfügbaren Funktionen auszuführen.

---

## Für wen ist ESP32 Connect gedacht?

ESP32 Connect richtet sich an Maker, Entwickler und Technikinteressierte, die Mikrocontroller nicht nur am Computer, sondern auch bequem über ein Smartphone bedienen möchten.

Ob als Demonstration einer BLE-Verbindung, als Einstieg in mobile Hardwaresteuerung oder als Basis für eigene Ideen: Das Projekt verbindet mobile Software mit physischer Hardware.

---

## Projekt herunterladen

Alle benötigten Dateien findest du direkt hier:

- **[Android-App herunterladen](./esp32_connect.apk)**
- **[MicroPython-Programm herunterladen](./esp32_connect.py)**

**ESP32 Connect – kabellose Kontrolle, direkt in deiner Hand.**
