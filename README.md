# Meinungsfreiheit Checker

Eine Flask-Webanwendung, die Benutzer durch einen Entscheidungsbaum führt, um zu prüfen, ob ihre Meinungsfreiheit tatsächlich eingeschränkt wurde.

## Über das Projekt

Diese Anwendung basiert auf einem Flowchart von Rechtsanwalt Gerhard Rahn (Fachanwalt für Strafrecht und Sozialrecht), das humorvoll erklärt, wann Meinungsfreiheit wirklich eingeschränkt wird und wann nicht.

## Features

- Interaktive Schritt-für-Schritt-Führung durch den Entscheidungsbaum
- Verfolgung der bisherigen Antworten
- Klare Ergebnisse mit Erklärungen
- Responsive Design für mobile und Desktop-Geräte
- Deutschsprachige Benutzeroberfläche

## Installation

1. Stelle sicher, dass Python 3.8+ installiert ist

2. Installiere die Abhängigkeiten:
```bash
pip install -r requirements.txt
```

## Verwendung

1. Starte die Anwendung:
```bash
python app.py
```

2. Öffne deinen Browser und navigiere zu:
```
http://localhost:5002
```

3. Folge den Fragen, um herauszufinden, ob deine Meinungsfreiheit eingeschränkt wurde

## Projektstruktur

```
meinung/
├── app.py                          # Flask-Hauptanwendung mit Entscheidungslogik
├── requirements.txt                # Python-Abhängigkeiten
├── static/
│   └── css/
│       └── style.css              # Styling für die Webanwendung
├── templates/
│   ├── base.html                  # Basis-Template
│   ├── index.html                 # Startseite
│   ├── question.html              # Fragenseite
│   └── result.html                # Ergebnisseite
└── photo_2025-10-23 20.25.07.jpeg # Original-Flowchart
```

## Entscheidungslogik

Der Entscheidungsbaum prüft folgende Fragen:

1. Wurdest du ignoriert?
2. Wurdest du kritisiert?
3. Wurdest du juristisch belangt?
4. Verstieb deine Aussage gegen geltende Gesetze?

Basierend auf den Antworten wird das Ergebnis ermittelt.

## Technologie-Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3
- **Session Management**: Flask Sessions
- **Styling**: Custom CSS mit Gradient-Design

## Lizenz

Basiert auf Material von Rechtsanwalt Gerhard Rahn.
