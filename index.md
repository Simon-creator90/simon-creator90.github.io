---
---

<link rel="stylesheet" href="{{ '/style.css' | relative_url }}">

<div class="site-layout">

<aside class="sidebar" markdown="1">

### ESP32 Connect

- [Startseite](#startseite)
- [Funktionen](#funktionen)
- [App-Verbindung](#verbindung)
- [Datenvisualisierung](#visualisierung)
- [Komponenten](#komponenten)
- [So funktioniert es](#ablauf)
- [Downloads](#downloads)

</aside>

<main class="content" markdown="1">

<a id="startseite"></a>

# ESP32 Connect

## Dein ESP32. Dein Smartphone. Deine Verbindung.

**ESP32 Connect** verbindet deinen ESP32 mit deinem Android-Smartphone. Über Bluetooth Low Energy (BLE) kannst du deinen Mikrocontroller kabellos steuern, Befehle senden und Daten empfangen.

<div class="product-image">
  <img src="ressourcen/Esp32.jpg" alt="ESP32 Mikrocontroller">
</div>

---

<a id="funktionen"></a>

## Was ESP32 Connect kann

- **Kabellos verbinden:** Kommunikation zwischen Smartphone und ESP32 über Bluetooth Low Energy.
- **Direkt steuern:** Befehle bequem über die Android-App senden.
- **Hardware bedienen:** Angeschlossene Komponenten wie LEDs ein- und ausschalten.
- **Daten empfangen:** Informationen vom ESP32 direkt auf dem Smartphone anzeigen.
- **Daten visualisieren:** Empfangene Werte in einem Diagramm darstellen.
- **Flexibel erweitern:** Eine Grundlage für eigene ESP32-Projekte und Anwendungen.

---

<a id="verbindung"></a>

## Die App in Aktion

<div class="feature-grid">

<div class="feature-card">
  <div class="feature-image">
    <img src="ressourcen/Nicht_verbunden.jpg" alt="ESP32 Connect ohne Verbindung">
  </div>
  <div class="feature-text">
    <h3>Verbindung herstellen</h3>
    <p>Die App ermöglicht es, nach einem ESP32 zu suchen und eine Verbindung herzustellen. Der Verbindungsstatus ist jederzeit sichtbar. So erkennst du direkt, ob dein Smartphone mit dem Mikrocontroller kommuniziert.</p>
  </div>
</div>

<div class="feature-card">
  <div class="feature-image">
    <img src="ressourcen/Verbunden.jpg" alt="ESP32 Connect mit verbundenem ESP32">
  </div>
  <div class="feature-text">
    <h3>Verbunden und einsatzbereit</h3>
    <p>Nach erfolgreicher Verbindung steht die Kommunikation mit dem ESP32 zur Verfügung. Über die App kannst du die unterstützten Funktionen nutzen und Befehle an den Mikrocontroller senden.</p>
  </div>
</div>

</div>

---

<a id="visualisierung"></a>

## Daten empfangen und visualisieren

<div class="feature-row">
  <div class="feature-image">
    <img src="ressourcen/Diagramm.jpg" alt="Diagramm mit empfangenen ESP32-Daten">
  </div>
  <div class="feature-text">
    <h3>Messwerte direkt auf dem Smartphone</h3>
    <p>ESP32 Connect kann Daten vom Mikrocontroller empfangen und grafisch darstellen.</p>
    <p>Die übertragenen Werte werden in einem Diagramm sichtbar. Dadurch lassen sich Datenverläufe direkt am Smartphone verfolgen, ohne dass dafür ein zusätzlicher Computer benötigt wird.</p>
  </div>
</div>

---

<a id="komponenten"></a>

## Zwei Komponenten. Ein System.

### Android-App

Die Android-App bildet die Benutzeroberfläche für die Bedienung und Kommunikation mit dem ESP32.

### MicroPython-Programm

Das Python-Programm wird direkt auf dem ESP32 ausgeführt. Es übernimmt die Kommunikation mit der App und verarbeitet die eingehenden Befehle.

---

<a id="ablauf"></a>

## So funktioniert es

1. Das MicroPython-Programm wird auf dem ESP32 eingerichtet.
2. Die Android-App wird auf dem Smartphone installiert.
3. Smartphone und ESP32 verbinden sich über Bluetooth Low Energy.
4. Über die App können Befehle gesendet und Daten empfangen werden.
5. Empfangene Daten lassen sich in der App visualisieren.

---

<a id="downloads"></a>

## ESP32 Connect ausprobieren

Die beiden benötigten Dateien stehen hier zum Download bereit:

<div class="download-area">

<h3>Alle Dateien</h3>

<p><a href="ressourcen/esp32_connect.apk" download>Android-App herunterladen – esp32_connect.apk</a></p>

<p><a href="ressourcen/esp32_connect.py" download>MicroPython-Programm herunterladen – esp32_connect.py</a></p>

</div>

**ESP32 Connect – mobile Kontrolle und Datenvisualisierung für deinen ESP32.**

</main>
</div>

<script>
document.addEventListener("DOMContentLoaded", function () {
  const links = document.querySelectorAll(".sidebar a[href^='#']");
  const sections = Array.from(links)
    .map(link => ({
      link: link,
      section: document.getElementById(link.getAttribute("href").substring(1))
    }))
    .filter(item => item.section);

  function updateActiveLink() {
    let current = sections[0];

    for (const item of sections) {
      if (item.section.getBoundingClientRect().top <= 160) {
        current = item;
      }
    }

    links.forEach(link => link.classList.remove("active"));

    if (current) {
      current.link.classList.add("active");
    }
  }

  window.addEventListener("scroll", updateActiveLink, { passive: true });
  window.addEventListener("resize", updateActiveLink);
  updateActiveLink();
});
</script>
