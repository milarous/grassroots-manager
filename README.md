# Grassroots Football Manager

A simple web-based football management simulation game built with Flask. Manage your grassroots football club from the ground up, starting with basic finances and reputation, and build your squad and facilities.

## Features

- Create and customize your football club
- View club overview including finances, reputation, and facilities
- Scout and recruit senior players to build your squad
- View club facilities (basic view)
- View competitions (basic view)
- Save and load game progress (3 save slots)
- Simple web interface with HTML templates

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

Run the application:
```
python main.py
```

Open your web browser and navigate to `http://127.0.0.1:5000/` to start the game.

- Start by creating your club on the main menu.
- Navigate through the club overview, squad view (scout and recruit players), facilities view, competitions view, and other sections.
- Save your progress using the "Save Game" button on any page, and load previous games from the main menu.

## Requirements

- Python 3.x
- Flask
- See `requirements.txt` for full list of dependencies.

## Project Structure

- `main.py`: Main Flask application and game logic
- `templates/`: HTML templates for the web interface
  - `index.html`: Main menu and club creation
  - `club.html`: Club overview
  - `squad.html`: Squad management
  - `facilities.html`: Facilities view
  - `competitions.html`: Competitions view
  - `exit.html`: Exit page
- `requirements.txt`: Python dependencies