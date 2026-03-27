# Grassroots Football Manager

A web-based football management simulation game built with Flask. Manage your grassroots football club from the ground up — recruit players through advertising and open training events, build your squad through a realistic follow-up process, manage your finances and facilities, and track your season on a 52-week calendar.

---

## Features

### Core Gameplay

* **Club Creation** — Create and name your football club with city and country selection
* **Club Management** — View club overview including finances, reputation, facility, and competition status
* **Squad Management** — Build your squad through a realistic player recruitment pipeline
* **Time Progression** — Advance the season week by week using the "Next Week" button; all scheduled events execute automatically with results shown in a popup modal
* **Save System** — 3 save slots with custom labels, timestamps, and full game state persistence

---

### Player Recruitment Pipeline

Players don't just appear in your squad — they go through a realistic multi-step process:

1. **Advertise** — Run marketing campaigns to attract interested players to your Contacts list
2. **Call & Invite** — Use the phone call system to invite contacts to an Open Training Night
3. **Train** — When the training session runs, invited contacts and random walk-ins attend
4. **Follow-up** — Attendees appear in your Follow-up list where you can see their position and skill level
5. **Recruit or Ignore** — Decide whether to bring each player into the squad

#### Advertising Methods

| Method | Cost | Effect |
|---|---|---|
| 📣 Social Media Post | Free | Based on club reputation |
| 📋 Flyers | $50 | 0–3 interested players |
| 📻 Radio Advertisement | $250 | 2–8 interested players |
| 📺 TV Commercial | $750 | 5–15 interested players |
| 💬 Word of Mouth | Automatic | Passive weekly attraction based on reputation |

* Events can be scheduled up to 3 weeks in advance
* Player source is tracked and displayed throughout the pipeline (e.g. "Radio Ad", "Open Training")

#### Phone Call System

* Call button on the Marketing page initiates a phone conversation with a contact
* Speech bubble modal with realistic dialogue and branching choices
* Outcome probabilities: 5% wrong number, 10% contact declines, 85% successful invitation
* Contacts removed from list if they decline or number is disconnected
* When a contact accepts, you select which scheduled training session to invite them to

---

### Training

* **Training Page** — Dedicated page for scheduling and managing Open Training Nights
* **Open Training Night** — Free community sessions that attract walk-in players and process invited contacts
  + 0–5 random walk-ins attend, plus all invited contacts
  + All attendees move to the Follow-up list after the session
* **Two-column layout** — Schedule on the left, upcoming events with invited contact counts on the right
* **View Button** — See the full list of contacts invited to any upcoming session
* Events scheduled independently from the advertising/marketing system

---

### Calendar

* **52-Week Calendar** — Full-year interactive calendar in a 4-column grid layout
* **Colour-coded event types**: Match, Training, Meeting, Maintenance, Marketing
* **Week navigation** — Browse all 52 weeks with year transitions
* **Event details** — Click weeks to view scheduled event information
* **Automatic execution** — Events fire when "Next Week" is clicked from any page

---

### Facilities

* Start with no facility; choose from 4 Adelaide locations to rent:

| Facility | Location | Monthly Cost |
|---|---|---|
| Hackham Soccer Complex | Hackham | $800 |
| Findon Sports Park | Findon | $1,200 |
| Salisbury Sports Ground | Salisbury | $950 |
| Campbelltown Football Ground | Campbelltown | $1,100 |

* View your current facility details at any time
* Switch or leave a facility using the search and "Leave Facility" buttons

---

### Competitions

* Start with no competition; enter one of 4 South Australian associations:

| Association | Annual Fee |
|---|---|
| Southern Districts Soccer Association | $650 |
| Elizabeth & Districts Soccer Association | $600 |
| Adelaide Hills Football Association | $550 |
| Western Football League | $500 |

* Enter, change, or leave competitions at any time

---

### Save System

* **3 Save Slots** — Save and load game progress across multiple slots
* **Custom Labels** — Name your saves for easy identification
* **Save Info Display** — Shows Week/Year, timestamp, club name, and facility
* **Backward Compatibility** — Legacy saves load correctly with automatic attribute migration
* **Modal Interface** — Save/load modals available from any game page via the burger menu

---

### User Interface

* **Dark Mode** — Exclusive dark theme for visual comfort
* **Navigation Menu** — Left-side sidebar on all game pages:
  + Club Overview
  + Calendar
  + Squad
  + Training
  + Marketing
  + Facilities
  + Competitions
* **Top-Right Controls** — "Next Week" button (red) and burger menu for Save/Return to Menu
* **ARIA Accessibility** — Screen reader support and keyboard navigation across the UI
* **Flash Messages** — Feedback for all player actions (recruiting, scheduling, saving)
* **Weekly Results Modal** — Popup summarising all events that fired when advancing the week
* **Footer** — Consistent branding with version info

---

## Installation

1. Clone the repository:

```
git clone https://github.com/milarous/grassroots-manager.git
cd grassroots-manager
```

2. Install dependencies:

```
pip install -r requirements.txt
```

---

## Usage

### Starting the Game

```
python main.py
```

Open your browser and go to `http://127.0.0.1:5000/`

### Playing the Game

1. **Main Menu** — Create a new club or load a saved game
2. **Club Creation** — Enter club name, country, and city
3. **Marketing** — Run advertising campaigns to populate your Contacts list
4. **Training** — Schedule Open Training Nights; invite contacts via the call system
5. **Follow-up** — After training runs, review attendees and recruit those you want
6. **Calendar** — Track and manage all scheduled events across the 52-week season
7. **Facilities** — Rent a training ground to establish your club
8. **Competitions** — Join a local association to compete
9. **Next Week** — Advance time; all events for that week fire automatically
10. **Save** — Use the burger menu on any page to save your progress

---

## Project Structure

```
grassroots-manager/
├── main.py                     # Flask app, game logic, all routes and classes
├── requirements.txt            # Python dependencies
├── venv-setup.md               # Virtual environment setup notes
├── CHANGELOG.md                # Version history
│
├── templates/
│   ├── index.html              # Main menu
│   ├── club.html               # Club overview
│   ├── squad.html              # Squad list
│   ├── marketing.html          # Player recruitment (contacts + follow-up)
│   ├── training.html           # Training scheduling and upcoming events
│   ├── calendar.html           # 52-week calendar
│   ├── facilities.html         # Facility management
│   ├── competitions.html       # Competition management
│   ├── exit.html               # Exit screen
│   ├── _game_menu.html         # Reusable navigation sidebar
│   ├── _save_modal.html        # Reusable save modal
│   ├── _load_modal.html        # Reusable load modal
│   ├── _call_modal.html        # Phone call modal with training invitation
│   └── _week_results_modal.html # Weekly event results popup
│
├── static/
│   ├── styles.css              # Main stylesheet with CSS custom properties
│   ├── burger_menu.js          # Burger menu toggle
│   ├── save_modal.js           # Save modal logic
│   ├── load_modal.js           # Load modal logic
│   ├── call_modal.js           # Phone call flow and training invitation
│   ├── theme_toggle.js         # (Legacy — dark mode is now exclusive)
│   └── Images/
│       └── gm_logo.png         # Game logo
│
└── saves/
    └── slot_*.pkl              # Pickled save files (auto-created)
```

### Key Classes (`main.py`)

| Class | Purpose |
|---|---|
| `Club` | Club state — finances, reputation, week/year, squad, facility, competition, calendar |
| `Player` | Player attributes — name, age, position, skill level, source |
| `CalendarEvent` | Scheduled events — type, week/year, notes, invited contacts, attendees |
| `Facility` | Rentable training ground with monthly cost |
| `Competition` | League association with annual fee |

---

## Requirements

* Python 3.x
* Flask
* See `requirements.txt` for full dependency list

---

## About

**Grassroots Manager** is a grassroots-to-pro football club management sim. Starting with nothing — no players, no facility, no competition — your goal is to build a club from the ground up.

The game is in active pre-release development. Version 1.0.0 will mark the first full season loop with match simulation, league tables, and season progression.