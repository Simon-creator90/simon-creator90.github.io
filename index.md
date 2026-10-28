# ESP32 ↔ Android App – BLE-Projekt

Eine drahtlose Kommunikation zwischen einem **ESP32** und einer Android-App, die mit **MIT App Inventor** erstellt wurde. Der ESP32 verwendet MicroPython und kommuniziert mit der App über Bluetooth Low Energy (BLE).

---

## Projektübersicht

Ziel des Projekts ist es, den ESP32 über eine Android-App zu steuern und Informationen zwischen beiden Geräten auszutauschen.

**Funktionen:**
- Verbindung zwischen Android-App und ESP32 über BLE
- LED ein- und ausschalten
- Daten und Statusinformationen abfragen
- Verbindung kontrolliert trennen

## Hardware

| Komponente | Beschreibung |
|---|---|
| ESP32 | Mikrocontroller für die BLE-Kommunikation |
| NeoPixel-LED | Über GPIO 8 angesteuerte LED |
| UART-Verbindung | TX an GPIO 10, RX an GPIO 15 |
| Android-Smartphone | Steuert den ESP32 über die App |

## Software

- **MicroPython** – Programm auf dem ESP32
- **MIT App Inventor** – Entwicklung der Android-App
- **Bluetooth Low Energy (BLE)** – Drahtlose Kommunikation
- **GitHub Pages** – Dokumentation des Projekts

## Ablauf der BLE-Kommunikation

1. Der ESP32 startet und initialisiert den BLE-Dienst.
2. Die Android-App sucht nach dem ESP32.
3. Die App verbindet sich mit dem Gerät.
4. Die App sendet Befehle an den ESP32.
5. Der ESP32 verarbeitet die Befehle und führt die entsprechenden Aktionen aus.
6. Antworten oder Statusinformationen werden an die App zurückgegeben.
7. Die Verbindung kann bei Bedarf getrennt werden.

## BLE-Befehle

| Befehl | Funktion |
|---|---|
| `LED_ON` | Schaltet die LED ein |
| `LED_OFF` | Schaltet die LED aus |
| `GET` | Fragt Informationen oder Statusdaten ab |
| `DISCONNECT` | Fordert das Trennen der Verbindung an |

## BLE-UUIDs

Der BLE-Dienst und seine Eigenschaften werden über UUIDs identifiziert.

| Element | UUID |
|---|---|
| Service UUID | `HIER_SERVICE_UUID_EINTRAGEN` |
| TX UUID | `HIER_TX_UUID_EINTRAGEN` |
| RX UUID | `HIER_RX_UUID_EINTRAGEN` |

> **Hinweis:** Ersetze die Platzhalter durch die UUIDs aus deinem bestehenden MicroPython-Code. Ich habe die konkreten UUID-Werte hier nicht vorliegen.

## MicroPython auf dem ESP32

Der ESP32 verwendet MicroPython, um BLE zu initialisieren, Befehle zu empfangen und die angeschlossene Hardware zu steuern.

Vereinfachter Ablauf:

```python
# Vereinfachtes Ablaufbeispiel – kein vollständiger Programmcode

# 1. BLE initialisieren
# 2. BLE-Dienst und Eigenschaften einrichten
# 3. Auf Verbindung mit der App warten
# 4. Empfangene Befehle verarbeiten
# 5. LED oder andere Funktionen steuern
# 6. Statusinformationen zurücksenden
```

Der bestehende Programmcode muss dafür nicht geändert werden. Dieser Abschnitt beschreibt lediglich die Funktionsweise.

## Projektstatus

- [x] ESP32 und Android-App als Projektkomponenten eingerichtet
- [x] BLE-Kommunikation als Verbindung zwischen den Geräten vorgesehen
- [x] Befehle für die LED-Steuerung definiert
- [ ] Dokumentation um die tatsächlichen UUIDs ergänzen
- [ ] Screenshots der Android-App und des Hardware-Aufbaus hinzufügen

## Zusammenfassung

Das Projekt verbindet einen ESP32 mit einer Android-App über Bluetooth Low Energy. Die App ermöglicht es, Befehle an den Mikrocontroller zu senden, die LED zu steuern und Informationen abzufragen. Diese Seite dokumentiert den Aufbau und die grundlegende Kommunikation des Systems.
****
