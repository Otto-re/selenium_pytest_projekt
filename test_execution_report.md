# ✅ Testausführung: GroceryMate

## 🔍 Funktion: Produktsuche

### Testfall 1 – Produktsuche mit gültigem Schlüsselwort

- **Testziel:** Produktsuche mit „Milch“ testen
- **Eingabe:** Milch
- **Erwartetes Ergebnis:** Liste mit passenden Produkten wird angezeigt
- **Tatsächliches Ergebnis:** Liste wurde korrekt angezeigt
- **Testergebnis:** ✅ Bestanden
- **Datum:** 06.06.2025
- **Tester:** Otto Reifschneider

### Testfall 2 – Produktsuche mit ungültigem Schlüsselwort

- **Testziel:** Überprüfung der Suchfunktion mit einem ungültigen Begriff („xyz123“)
- **Eingabe:** xyz123
- **Erwartetes Ergebnis:** Die Meldung „Keine Produkte gefunden“ wird angezeigt
- **Tatsächliches Ergebnis:** Es wird **keine Meldung** angezeigt. Seite bleibt unverändert.
- **Testergebnis:** ❌ Nicht bestanden
- **Datum:** 06.06.2025
- **Tester:** Otto Reifschneider

### Testfall 3 – Produktsuche mit Sonderzeichen

- **Testziel:** Eingabe ungültiger Sonderzeichen in der Produktsuche testen
- **Eingabe:** !@#$%
- **Erwartetes Ergebnis:** Meldung „Keine Produkte gefunden“ **oder** automatische Bereinigung der Eingabe
- **Tatsächliches Ergebnis:** Keine Meldung, keine Reaktion. Seite bleibt unverändert.
- **Testergebnis:** ❌ Nicht bestanden
- **Datum:** 06.06.2025
- **Tester:** Otto Reifschneider

## 🛒 Funktion: Warenkorb

### Testfall 4 – Einzelnes Produkt zum Warenkorb hinzufügen

- **Testziel:** Überprüfen, ob ein Produkt in den Einkaufswagen gelegt werden kann
- **Eingabe:** Klick auf „In den Warenkorb“ bei einem verfügbaren Produkt
- **Erwartetes Ergebnis:** Produkt wird hinzugefügt, Zähler erhöht sich um 1
- **Tatsächliches Ergebnis:** Verhalten wie erwartet
- **Testergebnis:** ✅ Bestanden
- **Datum:** 06.06.2025
- **Tester:** Otto Reifschneider

---

### Testfall 5 – Mehrere verschiedene Produkte zum Warenkorb hinzufügen

- **Testziel:** Gleichzeitiges Hinzufügen mehrerer Produkte überprüfen
- **Eingabe:** Drei verschiedene Produkte in den Warenkorb legen
- **Erwartetes Ergebnis:** Alle 3 Produkte sind im Warenkorb gelistet
- **Tatsächliches Ergebnis:** Verhalten wie erwartet
- **Testergebnis:** ✅ Bestanden
- **Datum:** 06.06.2025
- **Tester:** Otto Reifschneider

### Testfall 6 – Versuch, ein nicht vorrätiges Produkt in den Warenkorb zu legen

- **Testziel:** Überprüfen, ob beim Hinzufügen eines Produkts mit Lagerbestand = 0 eine Fehlermeldung erscheint
- **Eingabe:** Klick auf „In den Warenkorb“ bei einem Produkt mit Bestand 0
- **Erwartetes Ergebnis:** Fehlermeldung wie „Dieses Produkt ist derzeit nicht verfügbar“
- **Tatsächliches Ergebnis:** Test konnte nicht durchgeführt werden, da kein Produkt mit Lagerbestand = 0 existiert. Es scheint kein Limit beim Hinzufügen zu geben.
- **Testergebnis:** 🚫 Nicht testbar
- **Datum:** 06.06.2025
- **Tester:** Otto Reifschneider

## 🛒 Funktion: Checkout-Prozess

### Testfall 7 – Erfolgreicher Checkout mit gültigen Daten

- **Testziel:** Überprüfen eines vollständigen und gültigen Bestellvorgangs
- **Eingabe:** Gültige Adress- und Zahlungsdaten eingegeben und bestätigt
- **Erwartetes Ergebnis:** Bestellung wird aufgegeben, Bestätigungsnachricht wird angezeigt
- **Tatsächliches Ergebnis:** Bestellung wird aufgegeben, aber **keine Bestätigungsnachricht** erscheint
- **Testergebnis:** ⚠️ Teilweise bestanden
- **Datum:** 06.06.2025
- **Tester:** Otto Reifschneider

---

### Testfall 8 – Bestellung mit Mindestbestellwert (1 €)

- **Testziel:** Überprüfung des Grenzwertes beim Mindestbestellwert
- **Eingabe:** Bestellung mit genau 1 € Warenkorbwert
- **Erwartetes Ergebnis:** Bestellung wird angenommen
- **Tatsächliches Ergebnis:** Bestellung wird angenommen
- **Testergebnis:** ✅ Bestanden
- **Datum:** 06.06.2025
- **Tester:** Otto Reifschneider

---

### Testfall 9 – Bestellung mit ungültigen Zahlungsdaten

- **Testziel:** Fehlermeldung bei ungültiger Kreditkarte simulieren
- **Eingabe:** Abgelaufene oder ungültige Kreditkartendaten
- **Erwartetes Ergebnis:** Fehlermeldung „Zahlung fehlgeschlagen. Bitte überprüfen Sie Ihre Angaben.“
- **Tatsächliches Ergebnis:** Bestellung wird angenommen – **keine Prüfung auf Gültigkeit der Zahlungsdaten**
- **Testergebnis:** ❌ Nicht bestanden
- **Datum:** 06.06.2025
- **Tester:** Otto Reifschneider
