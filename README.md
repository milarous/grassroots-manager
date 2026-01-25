# Grassroots Football Manager

A web-based football management simulation game built with Flask. Manage your grassroots football club from the ground up—recruit players through various marketing methods, schedule events on a 52-week calendar, organize training sessions, and build your squad. Features a modern UI with modal dialogs, interactive save/load system, responsive navigation, and comprehensive calendar integration.

## Features

### Core Gameplay
- **Club Creation**: Create and customize your football club with name, city, and country selection
- **Club Management**: View club overview including finances, reputation, facility, and competition
- **Squad Management**: Recruit players to build your squad with detailed player information (name, age, position, skill level, recruitment source)
- **Facilities**:
   - Start with no facility and rent one of 4 options in Adelaide:
      - Hackham Soccer Complex ($800/month)
      - Findon Sports Park ($1,200/month)
      - Salisbury Sports Ground ($950/month)
      - Campbelltown Football Ground ($1,100/month)
   - View your current facility details; search to change facilities
   - Leave a facility at any time with the red "Leave Facility" button
- **Competitions**:
   - Start with no competition; choose from these associations (annual fee):
      - Southern Districts Soccer Association ($650/year)
      - Elizabeth & Districts Soccer Association ($600/year)
      - Adelaide Hills Football Association ($550/year)
      - Western Football League ($500/year)
   - Enter a competition, view its details, change competitions, or use the red "Leave Competition" button
- **Time Progression**: Advance the season with the top-right "Next Week" button. Week/year are shown under Club Overview and stored in save data. Weekly events are executed automatically with results displayed in a popup modal.

### Player Recruitment & Marketing
- **Marketing Page**: Centralized location for all player recruitment activities with two-column layout
- **Advertising Methods**:
  - **Flyers**: Print and distribute flyers around the local area (Cost: $50 | Effect: 1-3 players)
  - **Social Media Post**: Reach potential players through social media (Cost: Free | Effect: Based on club reputation)
  - **Open Training Nights**: Invite players to training sessions (Cost: Free | Effect: Higher risk, reputation-dependent)
  - **Word of Mouth**: Passive recruitment based on club reputation (Automatic weekly execution)
- **Player Source Tracking**: View where each player was recruited with colored source badges
- **Event Scheduling**: Schedule marketing campaigns up to 3 weeks in advance for automatic execution
- **Contacts Management**: Browse and recruit available players who have responded to marketing efforts

### Calendar System
- **52-Week Calendar**: Full-year interactive calendar view with color-coded event types
- **Event Types**: Match, Training, Meeting, Maintenance, Marketing
- **Week Navigation**: Browse through all 52 weeks with year transitions
- **Event Details**: View scheduled event information and notes
- **Automatic Event Execution**: Scheduled events execute when "Next Week" is clicked with results popup

### Training Management
- **Training Page**: Dedicated page for organizing training activities
- **Open Training Nights**: Schedule community training sessions to attract new players
- **Week Scheduling**: Select which week to hold training up to 3 weeks in advance

### Save System
- **3 Save Slots**: Save your game progress in up to 3 different slots
- **Custom Labels**: Add custom labels to your saves for easy identification
- **Save Information**: View game progress (Week/Year), save timestamp, club details, facility, and scheduled events
- **Load/Delete**: Load previous games or delete old saves
- **Modal Interface**: User-friendly, reusable save and load modals available across pages
- **Data Persistence**: All club data, squad, facilities, competitions, calendar events, and player sources are saved and restored on load
- **Backward Compatibility**: Legacy saves load correctly with automatic attribute initialization

### User Interface
- **Modern Web Interface**: Clean, responsive HTML/CSS design with grid and flexbox layouts
- **Navigation Menu**: Easy-to-use left-side navigation menu on all game pages
  - Club Overview
  - Calendar
  - Squad
  - Training
  - Marketing (Player Recruitment)
  - Facilities
  - Competitions
- **Top-Right Controls**: Red "Next Week" button and blue burger menu for Save Game and Return to Main Menu
- **Interactive Modals**: Modal dialogs for saving, loading, and game results
- **Visual Feedback**: Button states, hover effects, active page indicators, and flash messages
- **Flash Messages**: Informational feedback for actions (recruiting, saving, event results)
- **Footer Branding**: Consistent footer with copyright and version information

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

## Usage

### Starting the Game

Run the application:
```
python main.py
```

Open your web browser and navigate to `http://127.0.0.1:5000/` to start the game.

### Playing the Game

1. **Main Menu**:
   - Click "Create Club" to start a new game
   - Click "Load Game" to continue from a saved slot
   - Click "Exit Game" to close

2. **Club Creation**:
   - Enter your club name
   - Select your country (currently: Australia)
   - Select your city (currently: Adelaide)
   - Click "Confirm" to create your club

3. **Game Navigation**:
   - Use the left sidebar menu to navigate between sections:
     - **Club Overview**: View finances, reputation, facility, competition, and club details
     - **Calendar**: 52-week calendar view with scheduled events
     - **Squad**: View your current squad members
     - **Training**: Schedule and manage training sessions
     - **Marketing**: Recruit players through advertising methods and manage contacts
     - **Facilities**: Rent and manage your club facilities
     - **Competitions**: Enter, view, change, or leave competitions
   - Use the top-right burger menu for Save Game and Return to Main Menu

4. **Player Recruitment (Marketing)**:
   - Access the Marketing page from the left navigation menu
   - **Left Column - Attract Players**:
     - Use "Put Up Flyers" ($50, attracts 1-3 players)
     - Use "Social Media Post" (Free, reputation-dependent)
   - **Right Column - Contacts**:
     - Browse available players showing name, age, position, skill level, and recruitment source
     - Click "Recruit" to add any available player to your squad
   - Schedule advertising campaigns 0-3 weeks in advance for automatic execution

5. **Training Management**:
   - Access the Training page from the left navigation menu
   - Schedule "Open Training Night" events to attract new players
   - Select the week (current or up to 3 weeks in advance)
   - Click "Schedule Training" to add the event to your calendar

6. **Calendar Management**:
   - Access the Calendar page from the left navigation menu
   - View all 52 weeks of the year with color-coded events
   - Click on weeks to see event details
   - Events are automatically executed when you click "Next Week" from any page
   - Calendar events are persistent and save with your game

7. **Facilities Management**:
   - If you don't have a facility yet, browse and select one of the 4 available facilities in Adelaide to rent
   - Once you have a facility, the page shows your current facility details (name, location, monthly cost)
   - Use "Search for New Facility" to view options and switch
   - Use "Leave Facility" (red) to revert back to no facility

8. **Competitions Management**:
   - If you have no current competition, the page shows "No Current Competition" and lists the available associations
   - Click "Enter Competition" to join one; current competition details will display
   - Click "Change Competition" to show all options (current one is marked)
   - Click "Leave Competition" (red) to revert back to no competition

9. **Time Progression**:
   - Click "Next Week" in the top right to advance the season
   - All scheduled events for that week execute automatically
   - A popup modal displays the results of all executed events
   - Week and Year are shown under the Club Overview heading
   - After week 52, the year advances and the week resets to 1

10. **Saving Your Game**:
    - Click the "Save Game" button on any game page (via burger menu)
    - Select one of the 3 available save slots
    - Enter a custom label for your save (e.g., "My First Club")
    - Click "Confirm" to save
    - Existing saves show label, game progress (Week/Year), save time, and club information

11. **Loading a Game**:
    - From the main menu, click "Load Game"
    - Select a save slot to view its details
    - Click "Load" to continue from that save
    - All previous data including squad, calendar events, and marketing progress are restored

## Requirements

- Python 3.x
- Flask
- See `requirements.txt` for full list of dependencies.

## Project Structure

```
grassroots-manager/
├── main.py                 # Main Flask application and game logic
│                           # - Club, Player, CalendarEvent, Facility, Competition classes
│                           # - Flask routes for all game pages and API endpoints
│                           # - Save/load functionality with pickle
│                           # - Event scheduling and execution system
│
├── templates/              # HTML templates for the web interface
│   ├── index.html          # Main menu with club creation and load modals
│   ├── club.html           # Club overview page
│   ├── squad.html          # Squad management and player list
│   ├── marketing.html      # Player recruitment with two-column layout
│   ├── training.html       # Training event management
│   ├── calendar.html       # 52-week calendar view with events
│   ├── facilities.html     # Facilities management and rental
│   ├── competitions.html   # Competition selection and management
│   ├── exit.html           # Exit page
│   ├── _game_menu.html     # Reusable navigation menu component
│   ├── _save_modal.html    # Reusable save modal component
│   ├── _load_modal.html    # Reusable load modal component
│   └── _week_results_modal.html # Weekly event results popup
│
├── static/                 # Static assets (CSS and JavaScript)
│   ├── styles.css          # Main stylesheet with:
│   │                       # - Base styles and layout
│   │                       # - Modal dialog styles
│   │                       # - Button and form styles
│   │                       # - Navigation menu styles
│   │                       # - Two-column marketing layout
│   │                       # - Calendar and event styles
│   │                       # - Player source badge styles
│   ├── burger_menu.js      # Burger menu toggle for Save/Return dropdown
│   ├── save_modal.js       # Save modal functionality
│   └── load_modal.js       # Load modal functionality
│
├── saves/                  # Save game files (created automatically)
│   └── slot_*.pkl          # Pickled save data files containing:
│                           # - Club object with all attributes
│                           # - Squad list with player sources
│                           # - Available players list
│                           # - Calendar events
│                           # - Timestamp and custom labels
│
└── requirements.txt        # Python dependencies
```

### Key Components

- **Flask Application**: Built with Flask web framework for routing and template rendering
- **Game Classes**:
  - `Club`: Manages club state (finances, reputation, week/year, squad, facilities, competitions)
  - `Player`: Represents players with attributes and recruitment source tracking
  - `CalendarEvent`: Manages scheduled events with type and timing information
  - `Facility`: Represents rentable training facilities
  - `Competition`: Represents league associations
- **Persistence**: Save system using Python's pickle module for object serialization
- **Event System**: Automatic event scheduling and execution with weekly progression
- **Frontend**: HTML5, CSS3 with Grid/Flexbox, and vanilla JavaScript for interactive UI
- **Modal System**: Reusable modal components for save/load and event results
