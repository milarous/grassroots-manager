# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

*Nothing yet — see [0.4.0] for the latest changes.*

---

## [0.4.0] - 2025-03-27

### Added

* **Follow-up player system**
  + Players attending training no longer instantly join the squad
  + Players now appear in a Follow-up list where position and skill are revealed
  + Support for recruiting or ignoring follow-up players
  + Walk-in players from open training nights go directly to the Follow-up list
  + Player source badges (e.g., "TV Ad", "Open Training") persist through to Follow-up
* **Radio Advertisement** marketing option ($250, attracts 2–8 players)
* **TV Commercial** marketing option ($750, attracts 5–15 players)
* **Interactive phone call system for player recruitment**
  + Call button on the marketing page to contact interested players
  + Phone call modal with speech bubble interface showing contact responses
  + Two-stage conversation flow with branching response options
  + Realistic outcome probabilities:
    - 5% chance of disconnected number (contact removed)
    - 10% chance contact declines training invitation (contact removed)
    - 85% chance of successful invitation flow
  + Dynamic contact removal when number is disconnected or contact declines
  + Hang up button always visible below the conversation area
* **Training session invitation system**
  + Contacts can be invited to specific scheduled training events via the call modal
  + Each training event tracks its own invited contacts list
  + Invited contacts automatically move to Follow-up when training session occurs
  + Training page shows invited contact count per session
  + "View" button to see the full invited list for a session
* **Separated training scheduling from advertising system**
  + New dedicated `/schedule_training` route for training-specific scheduling
  + Training events use a `training:` prefix in notes (previously `advertising:`)
  + Clean separation of concerns between marketing and training activities
* **Training page two-column layout**
  + Left column: schedule Open Training Nights
  + Right column: upcoming training events with invited contact counts and view button
* **Backend API endpoint for contact removal** (`/remove_contact/<player_index>`)
  + Accepts a `reason` parameter (`disconnected` or `not_interested`)
  + Returns appropriate flash messages per removal reason
* **Marketing page layout update**
  + Right column now shows Contacts (top) and Follow-up (bottom) with 50/50 split and scrollbars
* **Brand logo** (`gm_logo.png`) added to the main menu page
* **Dark mode only** — light theme removed; game now uses an exclusive dark theme
* **ARIA accessibility** — ARIA attributes added across UI for screen reader and keyboard navigation support

### Changed

* **Recruitment workflow completely redesigned**
  + Removed instant "Recruit" button from contacts list
  + Players must now be invited to a training session via the phone call system
  + Players join the Follow-up list after attending training, not the squad directly
* **Marketing contact cards** now show only name, age, and source (position and skill hidden for realism)
* **Open Training Night** moved from the Marketing page to the Training page
* **Training event execution** now processes both invited contacts and random walk-ins:
  + Invited contacts move to Follow-up list
  + Walk-ins are also added to Follow-up list
  + Weekly results popup reports both groups separately
* **`CalendarEvent` class** extended with `invited_contacts` and `attendees` list attributes
* **Calendar page** redesigned to a 4-column grid layout
* **"View Invited Players" modal** redesigned to match the week results modal style
* Calendar icon restored to upcoming training event list
* Flyers effect adjusted to 0–3 players (was 1–3)
* Social Media Post emoji changed to megaphone (📣)
* Open Training Night cost display changed from "$0" to "Free"
* Open Training Night description now includes the potential walk-in range (0–5 players)
* Soccer ball emoji (⚽) restored to Open Training Night title
* CSS architecture refactored to use custom properties (variables) for theming

### Fixed

* Training confirmation flash messages now correctly redirect to Training page (not Marketing page)
* **New game bug** — `available_players` list now correctly cleared when starting a new game
* "View" button JavaScript parsing error on Training page resolved
* Flash message styling on `training.html` now matches `marketing.html`
* Player source badge width inconsistency across contact cards
* Hang up button colour now correctly displays in red
* Heading alignment between left and right columns on the marketing page

---

## [0.3.0] - 2025-01-25

### Added

* Player recruitment system with multiple advertising methods
* Marketing page with contacts management
* Calendar system with 52-week view and event scheduling
* Training page with open training night scheduling
* Week-by-week time progression with "Next Week" button
* Automated event execution with weekly results popup modal
* Player source tracking (coloured source badges on each player)
* Ability to schedule events up to 3 weeks in advance

### Changed

* Moved save/load controls to burger menu in top-right corner
* Updated UI controls and navigation across all pages
* Enhanced documentation with detailed feature descriptions

---

## [0.2.0] - 2025-01-22

### Added

* Facility rental system with 4 Adelaide locations:
  + Hackham Soccer Complex ($800/month)
  + Findon Sports Park ($1,200/month)
  + Salisbury Sports Ground ($950/month)
  + Campbelltown Football Ground ($1,100/month)
* Ability to leave current facility
* Competition management system with 4 South Australian associations:
  + Southern Districts Soccer Association ($650/year)
  + Elizabeth & Districts Soccer Association ($600/year)
  + Adelaide Hills Football Association ($550/year)
  + Western Football League ($500/year)
* Ability to enter, change, and leave competitions
* Yearly competition fees deducted from finances

### Changed

* Updated UI styling for facilities and competitions pages
* Added danger buttons (red) for leave/exit actions
* Improved CSS organisation with action row styles

### Fixed

* Legacy save compatibility for facilities and competitions

---

## [0.1.0] - 2025-01-21

### Added

* 3-slot save/load system with pickle persistence
* Custom save labels for easy identification
* Save metadata display (timestamp, club details, week/year)
* Separate save and load modal dialogs
* Squad management page showing player roster
* Player scouting system (simple random player generator)
* Ability to recruit players directly to the squad
* Club Overview page displaying finances and reputation

### Changed

* Externalised CSS to a separate stylesheet (`styles.css`)
* Improved save/load menu styling consistency
* Enhanced modal interfaces for better UX

### Fixed

* Button visibility management in modals
* `.gitignore` configuration for log files

---

## [0.0.2] - 2025-01-20

### Added

* Club creation with customisable name
* Location selection (country and city)
* Basic navigation between pages
* Club details display

### Changed

* Improved HTML structure for easier navigation
* Enhanced styling for better visual hierarchy

---

## [0.0.1] - 2025-01-19

### Added

* Initial project setup
* Flask web framework implementation
* Basic menu system
* Main menu with club creation option
* Exit functionality

### Changed

* Migrated from Tkinter to Flask for better cross-platform support

---

## Version Notes

**Pre-release (0.x.x)**: The game is in active development. Features and gameplay mechanics are subject to change. Version 1.0.0 will mark the first stable, feature-complete release with a full season loop.