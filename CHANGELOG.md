# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Radio Advertisement marketing option ($250, attracts 2-8 players)
- TV Commercial marketing option ($750, attracts 5-15 players)

### Changed
- Improved marketing page layout with vertical card stacking
- Updated flyers effect to 0-3 players (was 1-3)
- Changed Social Media Post emoji to megaphone (📣)

## [0.3.0] - 2025-01-25

### Added
- Player recruitment system with multiple advertising methods
- Marketing page with contacts management
- Calendar system with 52-week view and event scheduling
- Training page with open training night scheduling
- Week-by-week time progression with "Next Week" button
- Automated event execution with results popup modal
- Player source tracking (shows where each player was recruited from)
- Ability to schedule events up to 3 weeks in advance

### Changed
- Moved save/load controls to burger menu in top-right corner
- Updated UI controls and navigation across all pages
- Enhanced documentation with detailed feature descriptions

## [0.2.0] - 2025-01-22

### Added
- Facility rental system with 4 Adelaide locations
  - Hackham Soccer Complex ($800/month)
  - Findon Sports Park ($1,200/month)
  - Salisbury Sports Ground ($950/month)
  - Campbelltown Football Ground ($1,100/month)
- Ability to leave current facility
- Competition management system
  - Southern Districts Soccer Association ($650/year)
  - Elizabeth & Districts Soccer Association ($600/year)
  - Adelaide Hills Football Association ($550/year)
  - Western Football League ($500/year)
- Ability to enter, change, and leave competitions
- Yearly competition fees deducted from finances

### Changed
- Updated UI styling for facilities and competitions pages
- Added danger buttons (red) for leave actions
- Improved CSS organization with action row styles

### Fixed
- Legacy save compatibility for facilities and competitions

## [0.1.0] - 2025-01-21

### Added
- 3-slot save/load system with pickle persistence
- Custom save labels for easy identification
- Save metadata display (timestamp, club details, week/year)
- Separate save and load modal dialogs
- Squad management page showing player roster
- Player scouting system (simple player generator)
- Ability to recruit players to squad
- Club Overview page displaying finances and reputation

### Changed
- Externalized CSS to separate stylesheet (styles.css)
- Improved save/load menu styling consistency
- Enhanced modal interfaces for better UX

### Fixed
- Button visibility management in modals
- .gitignore configuration for log files

## [0.0.2] - 2025-01-20

### Added
- Club creation with customizable name
- Location selection (country and city)
- Basic navigation between pages
- Club details display

### Changed
- Improved HTML structure for easier navigation
- Enhanced styling for better visual hierarchy

## [0.0.1] - 2025-01-19

### Added
- Initial project setup
- Flask web framework implementation
- Basic menu system
- Main menu with club creation option
- Exit functionality

### Changed
- Migrated from Tkinter to Flask web framework for better cross-platform support

---

## Version Notes

**Pre-release (0.x.x)**: The game is in active development. Features and gameplay mechanics are subject to change. Version 1.0.0 will mark the first stable release.
