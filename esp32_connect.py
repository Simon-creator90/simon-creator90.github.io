# WICHTIG:
# -> Vor dem Starten des Programms Pin 10 mit Pin 15 mit einem Kabel verbinden!


from micropython import const
import bluetooth, time, random
from machine import Pin, UART
import neopixel

# ---------------- BLE SETUP ----------------
ble = bluetooth.BLE()
ble.active(True)

_IRQ_CENTRAL_CONNECT = const(1)
_IRQ_CENTRAL_DISCONNECT = const(2)
_IRQ_GATTS_WRITE = const(3)

UART_UUID = bluetooth.UUID("6E400001-B5A3-F393-E0A9-E50E24DCCA9E")
TX_UUID   = bluetooth.UUID("6E400003-B5A3-F393-E0A9-E50E24DCCA9E")
RX_UUID   = bluetooth.UUID("6E400002-B5A3-F393-E0A9-E50E24DCCA9E")

service = (
    UART_UUID,
    (
        (TX_UUID, bluetooth.FLAG_READ | bluetooth.FLAG_NOTIFY),
        (RX_UUID, bluetooth.FLAG_WRITE),
    ),
)

((tx, rx),) = ble.gatts_register_services((service,))

conn = None

# ---------------- ZUSTAND ----------------
led_state = False
value = "Bereit"
anz_werte = 0
intervall = 0.5
index = 0
get = False

# ---------------- Signal ----------------
empfanger_pin = Pin(15, Pin.IN)
sender_pin = Pin(10, Pin.OUT)
uart = UART(1, 9600, tx=Pin(10), rx=Pin(15)) #10 sendet, 15 empfängt

# ---------------- NEOPIXEL ----------------
# 1 LED an GPIO 8
np = neopixel.NeoPixel(Pin(8), 1)
np[0] = (0, 0, 0)
np.write()

def led_on():
    np[0] = (255, 0, 0)   # rot an
    np.write()

def led_off():
    np[0] = (0, 0, 0)     # aus
    np.write()

# ---------------- ADVERTISING ----------------
def advertise():
    name = "ESP32"

    adv = bytearray(b'\x02\x01\x06')
    adv += bytearray((len(name) + 1, 0x09))
    adv += name.encode()

    ble.gap_advertise(100000, adv)

# ---------------- IRQ HANDLER ----------------
def irq(event, data):
    global conn, tx, rx, value, led_state, get, anz_werte, intervall, index

    if event == _IRQ_CENTRAL_CONNECT:
        conn, _, _ = data
        get = False
        index = 0
        print("Verbunden")

    elif event == _IRQ_CENTRAL_DISCONNECT:
        print("Getrennt")

        conn = None
        get = False
        index = 0

        advertise()

    elif event == _IRQ_GATTS_WRITE:

        raw_msg = ble.gatts_read(rx)

        if not raw_msg:
            return

        msg = raw_msg.decode().replace("\x00", "").strip()

        print("Handy:", msg)
        
        # ---------------- BEFEHLE ----------------

        if "LED_ON" in msg:
            led_state = True
            led_on()
            value = "LED IST AN"

        elif "LED_OFF" in msg:
            led_state = False
            led_off()
            value = "LED IST AUS"

        elif msg == "DISCONNECT":
            get = False
            index = 0
            
            connection = conn
            print("Connection:", connection)
            
            if connection is not None:
                print("Trenne BLE...")
                ble.gap_disconnect(connection)

            return

        elif msg.startswith("GET,"):
            try:
                parts = msg.split(",")
                anz_werte = int(parts[1].strip())
                intervall = float(parts[2].replace("\x00", "").strip())
                index = 0
                get = True
                value = "GET_OK"
            except Exception as e:
                get = False
                value = "GET_ERR"
                print("GET Parse Fehler:", e)

        else:
            value = "UNBEKANNTER BEFEHL"

        print("Sende an App:", value)

        ble.gatts_write(tx, value.encode())

        if conn is not None:
            ble.gatts_notify(conn, tx, value.encode())

# ---------------- START ----------------
ble.irq(irq)
advertise()

print("ESP32 bereit (BLE UART aktiv)")

while True:
    if get == True:
        try:
            if index < anz_werte:
                value = random.randint(0, 100)
                # ------------ fuer nur 0/1
                # sender_pin.value(value)
                # messwert = empfanger_pin.value()
                # print("Sende an App:", messwert)
                
                uart.write(str(value) + "\n")
                empfangen = uart.readline()
                
                if empfangen:
                    messwert = int(empfangen)
                    print("Sende an App:", messwert)
                
                ble.gatts_write(tx, str(messwert).encode())
                if conn is not None:
                    ble.gatts_notify(conn, tx, str(messwert).encode())

                index += 1
                time.sleep(intervall)

            else:
                get = False
                index = 0
                print("Messung fertig")

        except Exception as e:
            print("Fehler:", e)