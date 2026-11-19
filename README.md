# GroceryMate – End-to-End-Tests mit Selenium und pytest

Dieses Portfolio-Projekt automatisiert typische Abläufe eines **Demo-Webshops**. Die Tests sind nach dem **Page Object Model** aufgebaut, damit Selektoren und Browser-Interaktionen von den Testfällen getrennt bleiben.

## Testumfang

- Anmeldung und Produktsuche
- Warenkorb und Versandkosten
- Checkout mit ungültigen Zahlungsdaten als Negativtest

**Technologien:** Python 3.11, Selenium WebDriver, pytest und Chrome.

## Lokal ausführen

Voraussetzung ist eine installierte Chrome-Version. Für die Browser-Tests wird ein eigenes Konto beim Demo-Webshop benötigt.

```bash
python -m venv .venv
# macOS/Linux: source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Kopiere die [Konfigurationsvorlage](.env.example) nach `.env` und trage dort `USERNAME` und `PASSWORD` für dein **Demo-Konto** ein. Die `.env` bleibt lokal und wird von Git ignoriert.

```bash
python -m pytest --collect-only -q  # Prüft, ob pytest die Tests findet
python -m pytest -v                 # Führt die Browser-Tests aus
```

## GitHub Actions

Bei Pushes und Pull Requests prüft [QA checks](https://github.com/Otto-re/selenium_pytest_projekt/actions), ob sich die Tests ohne Zugangsdaten sammeln lassen. Das ist **kein** End-to-End-Testlauf. Die Browser-Tests können manuell über den Workflow gestartet werden, wenn `GROCERYMATE_USERNAME` und `GROCERYMATE_PASSWORD` als GitHub-Actions-Secrets hinterlegt sind.

## Testdokumentation

- [Testplan](testplan.md)
- [Testfälle](testcases.md)
- [Bericht zur ursprünglichen Testdurchführung](test_execution_report.md)
