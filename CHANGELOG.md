# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- **Follow-up player system**
  - Players attending training no longer instantly join the squad
  - Players now go to a 'Follow-up' list where position and skill are revealed
  - Support for Calling (inviting/declining) and Ignoring players
  - Walk-in players from training now go directly to Follow-up list
  - Player source badges (e.g., 'TV Ad', 'Open Training') persist through to Follow-up
- Marketing page UI update:
  - Right-side column now shows 'Contacts' on top and 'Follow-up' on bottom
  - Both sections have fixed 50% height with scrollbars
- Radio Advertisement marketing option ($250, attracts 2-8 players)
- TV Commercial marketing option ($750, attracts 5-15 players)
- Light/Dark mode toggle with theme switcher button in footer
  - Theme preference persists using browser localStorage
  - CSS custom properties (variables) for consistent theming
  - Smooth transitions between light and dark modes
  - Optimized contrast and colors for accessibility in both modes
- **Interactive phone call system for player recruitment (⚠️ Under Construction)**
  - Call button on marketing page to contact interested players
  - Phone call modal with speech bubble interface showing contact responses
  - Two-stage conversation flow with response options
  - Option 1: "Sorry, I think I have the wrong number..." (polite exit)
  - Option 2: Invite contact to open training sessions
  - Training session selection interface when inviting players
  - Fallback message when no training sessions are scheduled
  - Automatic squad recruitment when contact accepts and attends training
  - **Realistic call outcomes with probability-based responses**:
    - 5% chance of disconnected number (wrong number)
    - 10% chance contact declines training invitation
    - 85% chance of successful invitation flow
  - **Dynamic contact removal system**:
    - Contacts removed when disconnected number is encountered
    - Contacts removed when they decline training invitation
    - Different flash messages based on removal reason
  - **Improved call modal UI**:
    - Hang up button always visible below conversation area
    - No longer hides during response options
    - Consistent button placement throughout call flow
- **Training session invitation system**
  - Contacts can be invited to specific scheduled training events
  - Each training event now tracks invited contacts
  - Invited contacts automatically join squad when training session occurs
  - Training page displays count of invited contacts per session
  - View button to see list of invited contacts for each session
- **Separated training scheduling from advertising system**
  - New dedicated `/schedule_training` route for training-specific scheduling
  - Training events now use `training:` prefix instead of `advertising:` prefix
  - Clean separation of concerns between marketing/advertising and training activities
  - Easier to extend with new training types in the future
- Training page two-column layout with upcoming events view
  - Left column: Schedule training events
  - Right column: View upcoming training events with invitation counts
  - Event list view for scheduled training sessions
- **Backend API endpoint for contact removal** (`/remove_contact/<player_index>`)
  - Accepts reason parameter (disconnected or not_interested)
  - Returns appropriate flash messages based on removal reason
  - Integrated with call modal for automatic cleanup
- **Added `gm_logo.png` to the main menu page.**
- **Dark Mode Only**: The game now uses a dark theme exclusively for better visual comfort and reduced eye strain.
- **ARIA Accessibility**: Enhanced UI with ARIA attributes for improved accessibility, including screen reader support and keyboard navigation.

### Changed
- Improved marketing page layout with vertical card stacking
- Updated flyers effect to 0-3 players (was 1-3)
- Changed Social Media Post emoji to megaphone (📣)
- Enhanced CSS architecture with theme variables for better maintainability
- **Marketing contact information now shows only name, age, and source** (removed position and skill level for realism)
- **Recruitment workflow completely redesigned**:
  - Removed instant recruitment button
  - Changed to phone call invitation workflow
  - Contacts must be invited to training sessions
  - Players join squad when they attend scheduled training
- **Open Training Night moved from Marketing page to Training page**
  - Scheduling now uses dedicated training route
  - Confirmation message stays on Training page (not Marketing page)
- Training page restructured to mirror marketing page layout
- Contact badges now have dynamic width based on content
- Aligned "Attract Players" and "Contacts" headings on marketing page
- **Training event execution now includes invited contacts**
  - Invited players automatically join squad when event occurs
  - Random walk-ins still added to contacts list
  - Week results message shows both invited players and walk-ins separately
- **CalendarEvent class extended with `invited_contacts` list attribute**
- **"View Invited Players" modal UI has been updated to match the design of the week results modal**
- **Calendar icon has been restored to the upcoming training list**
- **Cosmetic UI Updates:**
    - Restored the soccer ball (⚽) emoji to the "Open Training Night" title.
    - Restored the calendar (📅) emoji to the player count indicators for upcoming and recent training events.
    - Updated the "Open Training Night" cost display from "$0" to "Free" for consistency.
    - Added the potential player effect (0-5 players) to the "Open Training Night" description.
- **Redesigned the calendar page to a 4-column grid layout.**

### Fixed
- Player source badge width inconsistency across contacts
- Heading alignment issues between left and right columns on marketing page
- Hang up button color now displays correctly in red
- **Routing issue where training confirmations appeared on wrong page**
  - Training events now correctly redirect to Training page
  - Marketing events redirect to Marketing page
- **New Game Bug:** Corrected an issue where the `available_players` list was not cleared when starting a new game, causing contacts from a previous session to persist.
- **"View" Button Functionality:** Resolved an issue with the "View" buttons for recent and upcoming training events, which were not working due to a JavaScript parsing error.
- **Confirmation Banner Styling:** Fixed inconsistent styling for flash messages on the `training.html` page to match the styling on the `marketing.html` page.


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

## [01.1.0] - 2025-01-21

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
