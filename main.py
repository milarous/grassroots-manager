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
        self.facilities = "None"
        self.competition = "None"

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


# -----------------------------
# Flask Web Application
# -----------------------------
app = Flask(__name__)

# Initialize a default club
club = None

# Available players for recruitment
available_players = []

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
                    if saved_club:
                        try:
                            club_info = {
                                'name': saved_club.name,
                                'city': saved_club.city,
                                'country': saved_club.country,
                                'finances': saved_club.finances,
                                'reputation': saved_club.reputation
                            }
                        except:
                            # If there's an error accessing club attributes, set to None
                            club_info = None
                    
                    slots[str(i)] = {
                        'exists': True,
                        'label': label,
                        'timestamp': formatted_time,
                        'club_info': club_info
                    }
            except Exception as e:
                # If there's an error reading the file, treat as legacy save
                slots[str(i)] = {
                    'exists': True,
                    'label': f'Slot {i} (Legacy Save)',
                    'timestamp': 'Unknown',
                    'club_info': None
                }
        else:
            slots[str(i)] = {'exists': False, 'label': '', 'timestamp': '', 'club_info': None}
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
    return render_template('facilities.html', club=club, save_slots=save_slots)

@app.route('/competitions')
def competitions_view():
    if club is None:
        return redirect(url_for('main_menu'))
    save_slots = get_save_slots()
    return render_template('competitions.html', club=club, save_slots=save_slots)

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
