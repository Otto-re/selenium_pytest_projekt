# Testplan – GroceryMate Webshop (Selenium + PyTest)

## Ziel
Dieser Testplan beschreibt die Überprüfung der zentralen Funktionen des GroceryMate Webshops.
Getestet werden Produktsuche, Warenkorb und Checkout-Prozess, um sicherzustellen, dass Nutzer Produkte zuverlässig finden, auswählen und bestellen können.

## Umfang (Scope)

### Im Testumfang
- Produktsuche (Suchfeld & Ergebnisverhalten)
- Hinzufügen von Produkten in den Warenkorb
- Checkout-Prozess (Bestellabschluss und Validierung)

### Nicht im Testumfang
- Backend-Datenbanklogik
- Admin- / Content-Management Bereiche
- Performance- oder Lasttests

---

## Testansatz
Die Tests wurden **manuell und automatisiert** durchgeführt.

- **Manuell:** Grenzfälle, UI-Reaktionen, Verhalten bei fehlerhaften oder ungewöhnlichen Eingaben.
- **Automatisiert:** Funktionale Kernabläufe mithilfe von Selenium WebDriver und PyTest im Page Object Model (POM).

---

## Testumgebung

| Komponente | Version / Information |
|-----------|-----------------------|
| Betriebssystem | Windows / macOS |
| Browser | Chrome (aktuelle Version) |
| Sprache / Framework | Python + PyTest |
| Automatisierung | Selenium WebDriver |
| Testmuster | Page Object Model (POM) |

---

## Testdaten
- Produktsuche mit gültigen, ungültigen und Sonderzeichen-Eingaben
- Warenkorb mit einem oder mehreren Artikeln
- Checkout mit gültigen und ungültigen Zahlungsinformationen

---

## Erfolgs- / Abnahmekriterien
- Funktionen verhalten sich gemäß Erwartung.
- Kritische Fehler dürfen nicht offen sein.
- Testergebnisse sind dokumentiert (siehe `test_execution_report.md`).

---

## Lieferobjekte
| Datei | Inhalt |
|------|--------|
| testplan.md | Dieser Testplan |
| testcases.md | Strukturierte Testfälle |
| test_execution_report.md | Testergebnisse |
| README.md | Projektübersicht & Setup |

