# Testausführungsbericht – GroceryMate

## Produktsuche

### Testfall 1 – Produktsuche mit gültigem Schlüsselwort
- **Ziel:** Überprüfung der Suchfunktion mit einem gültigen Begriff
- **Eingabe:** „Milch“
- **Erwartetes Ergebnis:** Es wird eine Trefferliste mit passenden Produkten angezeigt.
- **Tatsächliches Ergebnis:** Trefferliste wird korrekt angezeigt.
- **Status:** Bestanden
- **Datum:** 06.06.2025
- **Tester:** Otto Reifschneider

### Testfall 2 – Produktsuche mit ungültigem Schlüsselwort
- **Ziel:** Überprüfung der Reaktion auf einen Suchbegriff ohne Treffer
- **Eingabe:** „xyz123“
- **Erwartetes Ergebnis:** Eine Meldung wie „Keine Produkte gefunden“ wird angezeigt.
- **Tatsächliches Ergebnis:** Keine Meldung. Seite bleibt unverändert.
- **Status:** Nicht bestanden
- **Datum:** 06.06.2025
- **Tester:** Otto Reifschneider

### Testfall 3 – Produktsuche mit Sonderzeichen
- **Ziel:** Überprüfung der Eingabebehandlung bei ungültigen Sonderzeichen
- **Eingabe:** „!@#$%“
- **Erwartetes Ergebnis:** Fehlermeldung oder Eingabesäuberung.
- **Tatsächliches Ergebnis:** Keine Meldung. Seite bleibt unverändert.
- **Status:** Nicht bestanden
- **Datum:** 06.06.2025
- **Tester:** Otto Reifschneider

---

## Warenkorb

### Testfall 4 – Einzelnes Produkt hinzufügen
- **Ziel:** Sicherstellen, dass ein Produkt erfolgreich hinzugefügt werden kann.
- **Erwartetes Ergebnis:** Produkt wird im Warenkorb angezeigt, Zähler erhöht sich.
- **Tatsächliches Ergebnis:** Erwartetes Verhalten.
- **Status:** Bestanden

### Testfall 5 – Mehrere unterschiedliche Produkte hinzufügen
- **Ziel:** Überprüfung, ob mehrere Produkte korrekt übernommen werden.
- **Erwartetes Ergebnis:** Alle hinzugefügten Produkte erscheinen im Warenkorb.
- **Tatsächliches Ergebnis:** Erwartetes Verhalten.
- **Status:** Bestanden

### Testfall 6 – Produkt mit Lagerbestand = 0
- **Ziel:** Prüfung der Fehlermeldung bei nicht verfügbarem Produkt.
- **Erwartetes Ergebnis:** Meldung wie „Dieses Produkt ist nicht verfügbar“.
- **Tatsächliches Ergebnis:** Kein Produkt mit Lagerbestand 0 verfügbar → nicht testbar.
- **Status:** Nicht durchführbar

---

## Checkout

### Testfall 7 – Gültiger Checkout
- **Ziel:** Ordnungsgemäßer Bestellabschluss
- **Erwartetes Ergebnis:** Bestellbestätigung wird angezeigt.
- **Tatsächliches Ergebnis:** Bestellung wird ausgeführt, jedoch ohne sichtbare Bestätigungsnachricht.
- **Status:** Teilweise bestanden

### Testfall 8 – Mindestbestellwert (Grenzwerttest)
- **Eingabe:** Warenkorbwert = 1 €
- **Erwartetes Ergebnis:** Bestellung wird akzeptiert.
- **Tatsächliches Ergebnis:** Erwartetes Verhalten.
- **Status:** Bestanden

### Testfall 9 – Ungültige Zahlungsdaten
- **Ziel:** Validierung der Zahlungsprüfung
- **Eingabe:** Abgelaufene/ungültige Kreditkarte
- **Erwartetes Ergebnis:** Fehlermeldung zur Zahlung.
- **Tatsächliches Ergebnis:** Bestellung wird trotzdem akzeptiert. Keine Validierung.
- **Status:** Nicht bestanden

