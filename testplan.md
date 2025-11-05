🎯 Ziel (Objective)
Ziel dieses Testplans ist es, die korrekte Implementierung und Funktionsweise neuer Funktionen des GroceryMate-Webshops sicherzustellen. Dazu gehören die Überprüfung des Warenkorbs, der Produktsuche und des Checkout-Prozesses. Die Funktionen sollen benutzerfreundlich, fehlerfrei und auf allen unterstützten Geräten sowie Browsern zuverlässig funktionieren.

👥 Zielgruppe (User Base)
Das Produkt wird genutzt von:

Privatkunden, die Lebensmittel online bestellen.
Stakeholdern wie: Endnutzer, Kundensupport, Entwickler, Produktmanager.
Typische Benutzer:

Technikaffine Nutzer auf Mobilgeräten
Ältere Nutzer über Desktop oder Laptop
Personen mit Barrierefreiheitsbedürfnissen (z. B. Screenreader)

🖥️ Hardware- und Softwareanforderungen
Hardware-Anforderungen

Geräte: PCs, Laptops, Smartphones, Tablets
Mindestanforderungen:
Mobil: mind. 4 GB RAM, aktuelle Android-/iOS-Version
Desktop: mind. 4 GB RAM, 2 GHz Prozessor
Software-Anforderungen

Betriebssysteme: Windows, macOS, Android, iOS
Browser: Chrome, Firefox, Safari, Edge (jeweils aktuelle 2 Versionen)
Abhängigkeiten: Backend-Dienste, Drittanbieter-APIs (z. B. Zahlungsanbieter, Produktdatenbank)
⚙️ Produktfunktionalität
Bestehende und geplante Funktionen:

Registrierung und Login
Produktsuche und -durchsicht
Hinzufügen und Entfernen von Artikeln im Warenkorb
Checkout mit Zahlungsabwicklung
Bestellhistorie und Benutzerprofilverwaltung
## 2. Teststrategie

### Testumfang (Scope of Testing)

**Im Umfang (In Scope):**
- Neue Features des Webshops:
  - Produktsuche und Filterfunktionen
  - Warenkorb-Funktionalität
  - Checkout-Prozess mit Zahlungsabwicklung

**Außerhalb des Umfangs (Out of Scope):**
- Interne Backend-Logik und Datenbank-Performance
- Content-Management-Features (z. B. Admin-Panel-Inhalte)

---

### Testarten (Type of Testing)

- **Funktionstests** – Sicherstellung, dass neue Features korrekt funktionieren
- **Regressionstests** – Überprüfung, ob bestehende Funktionen weiterhin korrekt arbeiten
- **Usability-Tests** – Bewertung der Benutzerfreundlichkeit der neuen Funktionen
- **Cross-Browser-Tests** – Sicherstellung, dass der Webshop in allen unterstützten Browsern funktioniert

---

### Risiken und Probleme (Risks and Issues)

- **Verzögerungen in der Entwicklung**  
  → Pufferzeiten im Zeitplan berücksichtigen

- **Mangel an Testdaten**  
  → Erstellung von Mock-Daten zur Testnutzung

- **Nicht verfügbare Testressourcen (z. B. Geräte, Teammitglieder)**  
  → Definition von Ersatzressourcen

---

### Testlogistik (Test Logistics)

| Rolle             | Name                | Aufgabe                                   |
|-------------------|---------------------|-------------------------------------------|
| Testmanager       | Jane Smith          | Koordination und Überwachung              |
| QA Engineer       | John Doe            | Funktionale und Regressionstests          |
| QA Engineer       | Alice Johnson       | Performance- und Sicherheitstests         |
| QA Engineer       | Robert Brown        | Usability-Tests                           |
| Endnutzer (UAT)   | Maria Garcia        | Abnahme und Feedback 
## 3. Testziele (Define Test Objectives)

### Ziele (Objectives)

- **Funktionalität:** Sicherstellen, dass neue und bestehende Funktionen wie vorgesehen arbeiten.
- **Benutzeroberfläche (GUI):** Überprüfung der Benutzeroberfläche auf Konsistenz, Lesbarkeit und intuitive Bedienung.
- **Performance:** Sicherstellen, dass das System unter Last stabil und schnell reagiert.
- **Sicherheit:** Aufdecken und Absichern potenzieller Sicherheitslücken.
- **Benutzerfreundlichkeit (Usability):** Bewertung der Nutzererfahrung und allgemeinen Bedienbarkeit.

---

### Erwartete Ergebnisse (Expected Outcomes)

- **Funktionalität:** Alle Funktionen verhalten sich gemäß den Spezifikationen.
- **Benutzeroberfläche:** Das UI ist reaktionsschnell, fehlerfrei und verständlich.
- **Performance:** Die Plattform erfüllt definierte Performance-Grenzwerte (z. B. Ladezeiten).
- **Sicherheit:** Es wurden keine kritischen Sicherheitsmängel festgestellt.
- **Benutzerfreundlichkeit:** Nutzer können das System intuitiv bedienen und ihre Ziele erreichen.
## 4. Testkriterien

### Eintrittskriterien (Entry Criteria)
- Das Entwicklungsteam hat die neuen Features vollständig bereitgestellt.
- Die Testumgebung ist einsatzbereit.
- Alle notwendigen Testdaten liegen vor.
- Der Testplan und die Testfälle wurden genehmigt.

### Abnahmekriterien (Exit Criteria)
- Alle als kritisch eingestuften Testfälle wurden erfolgreich abgeschlossen.
- Es bestehen keine offenen Blocker- oder kritischen Fehler.
- Alle Testergebnisse sind dokumentiert.
- Alle geplanten Regressionstests wurden durchgeführt.

---

## 5. Ressourcenplanung

| Rolle               | Name            | Aufgabe                                  |
|---------------------|------------------|-------------------------------------------|
| Testmanager         | Jane Smith       | Planung, Koordination, Reporting          |
| QA Engineer         | John Doe         | Manuelle Tests, Regressionstests          |
| QA Engineer         | Alice Johnson    | Automatisierte Tests                      |
| Entwickler (Support)| Max Müller       | Unterstützung bei Fehleranalyse           |
| Fachtester (UAT)    | Maria Garcia     | Feedback aus Sicht der Endnutzer          |

---

## 6. Testumgebung

- **Plattformen:**  
  - Windows 10 / 11  
  - macOS Ventura / Sonoma  
  - Android 12+  
  - iOS 15+

- **Browser:**  
  - Chrome (aktuelle 2 Versionen)  
  - Firefox  
  - Safari (nur macOS/iOS)  
  - Microsoft Edge

- **Endgeräte:**  
  - Desktop-PCs  
  - Laptops  
  - Tablets  
  - Smartphones

- **Tools:**  
  - Testautomatisierung: Selenium, Python  
  - Testmanagement: GitHub Issues, TestRail (optional)  
  - Kommunikation: Slack, E-Mail

---

## 7. Zeitplan & Aufwandsschätzung

| Phase                | Startdatum     | Enddatum       | Dauer      |
|----------------------|----------------|----------------|------------|
| Testplanung          | 03.06.2025     | 04.06.2025     | 2 Tage     |
| Testfall-Design      | 05.06.2025     | 06.06.2025     | 2 Tage     |
| Testdurchführung     | 07.06.2025     | 10.06.2025     | 4 Tage     |
| Fehleranalyse        | 08.06.2025     | 11.06.2025     | 4 Tage     |
| Berichtserstellung   | 11.06.2025     | 12.06.2025     | 2 Tage     |
| Gesamtdauer:         |                |                | **10 Tage**|

---

## 8. Test-Lieferobjekte (Deliverables)

- Vollständiger Testplan (`testplan.md`)
- Testfalldokumentation (`testcases.md`)
- Testausführungsbericht (`test-execution-report.md`)
- Fehlerberichte (Bug-Issues in GitHub)
- Abschlussbericht mit Empfehlungen
