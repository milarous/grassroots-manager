from flask import Flask, render_template, request, redirect, url_for

import os
import pickle

# -----------------------------
# Core Data Classes
# -----------------------------
class Club:
    def __init__(self, name, city=None, country=None):
        self.name = name
        self.city = city
        self.country = country
        self.finances = 1000       # starting money
        self.reputation = 1        # starts as unknown
        self.squad = []            # will add later
        self.facility = None       # Current rented facility
        self.competition = None    # Current entered competition
        self.week = 1              # Current game week
        self.year = 2026           # Current game year

    def get_summary(self):
        return (
            f"Club: {self.name}\n"
            f"City: {self.city}\n"
            f"Country: {self.country}\n"
            f"Finances: ${self.finances}\n"
            f"Reputation: {self.reputation}\n"
            f"Facilities: {self.facilities}\n"
            f"Competition: {self.competition}"
        )


class Player:
    def __init__(self, name, age, position, skill_level=1):
        self.name = name
        self.age = age
        self.position = position  # e.g., "Forward", "Midfielder", "Defender", "Goalkeeper"
        self.skill_level = skill_level  # 1-10 scale
        self.player_type = "Senior"  # For now, only Senior players

    def __str__(self):
        return f"{self.name} ({self.age}, {self.position}, Skill: {self.skill_level})"


class Facility:
    def __init__(self, name, city, monthly_cost):
        self.name = name
        self.city = city
        self.monthly_cost = monthly_cost

    def __str__(self):
        return f"{self.name} ({self.city}) - ${self.monthly_cost}/month"


class Competition:
    def __init__(self, name, yearly_fee):
        self.name = name
        self.yearly_fee = yearly_fee

    def __str__(self):
        return f"{self.name} - ${self.yearly_fee}/year"


# -----------------------------
# Flask Web Application
# -----------------------------
app = Flask(__name__)

# Initialize a default club
club = None

# Available players for recruitment
available_players = []

# Adelaide facilities available for rent
adelaide_facilities = [
    Facility("Hackham Soccer Complex", "Hackham", 800),
    Facility("Findon Sports Park", "Findon", 1200),
    Facility("Salisbury Sports Ground", "Salisbury", 950),
    Facility("Campbelltown Football Ground", "Campbelltown", 1100)
]

# South Australian grassroots competitions
competitions = [
    Competition("Southern Districts Soccer Association", 650),
    Competition("Elizabeth & Districts Soccer Association", 600),
    Competition("Adelaide Hills Football Association", 550),
    Competition("Western Football League", 500)
]

# Create saves directory if it doesn't exist
if not os.path.exists('saves'):
    os.makedirs('saves')

def save_game(slot, label=""):
    """Save the current game state to a slot"""
    global club, available_players
    from datetime import datetime
    save_data = {
        'club': club,
        'available_players': available_players,
        'label': label,
        'timestamp': datetime.now().isoformat()
    }
    with open(f'saves/slot_{slot}.pkl', 'wb') as f:
        pickle.dump(save_data, f)

def load_game(slot):
    """Load game state from a slot"""
    global club, available_players
    try:
        with open(f'saves/slot_{slot}.pkl', 'rb') as f:
            save_data = pickle.load(f)
            club = save_data['club']
            available_players = save_data['available_players']
            # Ensure legacy saves without Competition objects reset to None
            if club and not isinstance(getattr(club, 'competition', None), Competition):
                club.competition = None
            # Ensure legacy saves have week and year attributes
            if club and not hasattr(club, 'week'):
                club.week = 1
            if club and not hasattr(club, 'year'):
                club.year = 2026
        return True
    except FileNotFoundError:
        return False

def get_save_slots():
    """Get status of all save slots"""
    from datetime import datetime
    slots = {}
    for i in range(1, 4):
        file_path = f'saves/slot_{i}.pkl'
        if os.path.exists(file_path):
            try:
                with open(file_path, 'rb') as f:
                    save_data = pickle.load(f)
                    label = save_data.get('label', f'Slot {i}')
                    timestamp_str = save_data.get('timestamp', '')
                    if timestamp_str:
                        timestamp = datetime.fromisoformat(timestamp_str)
                        formatted_time = timestamp.strftime('%Y-%m-%d %H:%M:%S')
                    else:
                        formatted_time = 'Unknown'
                    
                    # Get club info for display
                    saved_club = save_data.get('club')
                    club_info = None
                    game_date = 'Unknown'
                    if saved_club:
                        try:
                            # Get game date
                            week = getattr(saved_club, 'week', 1)
                            year = getattr(saved_club, 'year', 2026)
                            game_date = f"Week {week}, {year}"
                            
                            facility_info = None
                            if saved_club.facility:
                                facility_info = {
                                    'name': saved_club.facility.name,
                                    'city': saved_club.facility.city,
                                    'monthly_cost': saved_club.facility.monthly_cost
                                }
                            club_info = {
                                'name': saved_club.name,
                                'city': saved_club.city,
                                'country': saved_club.country,
                                'finances': saved_club.finances,
                                'reputation': saved_club.reputation,
                                'facility': facility_info
                            }
                        except:
                            # If there's an error accessing club attributes, set to None
                            club_info = None
                    
                    slots[str(i)] = {
                        'exists': True,
                        'label': label,
                        'timestamp': formatted_time,
                        'game_date': game_date,
                        'club_info': club_info
                    }
            except Exception as e:
                # If there's an error reading the file, treat as legacy save
                slots[str(i)] = {
                    'exists': True,
                    'label': f'Slot {i} (Legacy Save)',
                    'timestamp': 'Unknown',
                    'game_date': 'Unknown',
                    'club_info': None
                }
        else:
            slots[str(i)] = {'exists': False, 'label': '', 'timestamp': '', 'game_date': '', 'club_info': None}
    return slots

def generate_random_player():
    """Generate a random player for recruitment"""
    import random
    
    first_names = ["John", "Mike", "David", "James", "Robert", "William", "Thomas", "Daniel", "Matthew", "Joseph"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]
    
    name = f"{random.choice(first_names)} {random.choice(last_names)}"
    age = random.randint(18, 35)
    positions = ["Forward", "Midfielder", "Defender", "Goalkeeper"]
    position = random.choice(positions)
    skill_level = random.randint(1, 5)  # Start with lower skilled players for grassroots
    
    return Player(name, age, position, skill_level)

def scout_players():
    """Add some random players to the available pool"""
    global available_players
    num_players = 3  # Scout 3 players at a time
    for _ in range(num_players):
        available_players.append(generate_random_player())

@app.route('/')
def main_menu():
    save_slots = get_save_slots()
    return render_template('index.html', save_slots=save_slots)

@app.route('/create_club', methods=['POST'])
def create_club():
    global club
    club_name = request.form.get('club_name')
    country = request.form.get('country')
    city = request.form.get('city')
    
    club = Club(club_name, city, country)
    return redirect(url_for('club_overview'))

@app.route('/club')
def club_overview():
    if club is None:
        return redirect(url_for('main_menu'))
    save_slots = get_save_slots()
    return render_template('club.html', club=club, save_slots=save_slots)

@app.route('/squad')
def squad_view():
    if club is None:
        return redirect(url_for('main_menu'))
    save_slots = get_save_slots()
    return render_template('squad.html', club=club, available_players=available_players, save_slots=save_slots)

@app.route('/scout_players')
def scout_players_route():
    scout_players()
    return redirect(url_for('squad_view'))

@app.route('/recruit_player/<int:player_index>')
def recruit_player(player_index):
    if club is None:
        return redirect(url_for('main_menu'))
    global available_players
    if 0 <= player_index < len(available_players):
        player = available_players.pop(player_index)
        club.squad.append(player)
    return redirect(url_for('squad_view'))

@app.route('/facilities')
def facilities_view():
    if club is None:
        return redirect(url_for('main_menu'))
    save_slots = get_save_slots()
    return render_template('facilities.html', club=club, save_slots=save_slots, facilities=adelaide_facilities)

@app.route('/rent_facility/<int:facility_index>')
def rent_facility(facility_index):
    if club is None:
        return redirect(url_for('main_menu'))
    if 0 <= facility_index < len(adelaide_facilities):
        club.facility = adelaide_facilities[facility_index]
    return redirect(url_for('facilities_view'))


@app.route('/leave_facility')
def leave_facility():
    if club is None:
        return redirect(url_for('main_menu'))
    club.facility = None
    return redirect(url_for('facilities_view'))

@app.route('/competitions')
def competitions_view():
    if club is None:
        return redirect(url_for('main_menu'))
    current_comp = club.competition if isinstance(club.competition, Competition) else None
    if club.competition is not current_comp:
        club.competition = current_comp
    save_slots = get_save_slots()
    return render_template('competitions.html', club=club, save_slots=save_slots, competitions=competitions, current_competition=current_comp)


@app.route('/enter_competition/<int:competition_index>')
def enter_competition(competition_index):
    if club is None:
        return redirect(url_for('main_menu'))
    if 0 <= competition_index < len(competitions):
        club.competition = competitions[competition_index]
    return redirect(url_for('competitions_view'))


@app.route('/leave_competition')
def leave_competition():
    if club is None:
        return redirect(url_for('main_menu'))
    club.competition = None
    return redirect(url_for('competitions_view'))

@app.route('/next_week')
def next_week():
    if club is None:
        return redirect(url_for('main_menu'))
    club.week += 1
    if club.week > 52:
        club.week = 1
        club.year += 1
    referrer = request.referrer if request.referrer else url_for('club_overview', _external=True)
    return redirect(referrer)

@app.route('/save_game/<int:slot>', methods=['POST'])
def save_game_route(slot):
    if 1 <= slot <= 3:
        label = request.form.get('label', f'Slot {slot}')
        save_game(slot, label)
    return redirect(request.referrer or url_for('main_menu'))

@app.route('/load_game/<int:slot>')
def load_game_route(slot):
    if 1 <= slot <= 3 and load_game(slot):
        return redirect(url_for('club_overview'))
    return redirect(url_for('main_menu'))

@app.route('/delete_game/<int:slot>')
def delete_game_route(slot):
    if 1 <= slot <= 3:
        file_path = f'saves/slot_{slot}.pkl'
        if os.path.exists(file_path):
            os.remove(file_path)
    return redirect(request.referrer or url_for('main_menu'))

@app.route('/exit')
def exit_game():
    return render_template('exit.html')


# -----------------------------
# Run Application
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
