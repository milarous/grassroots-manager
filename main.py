from flask import Flask, render_template, request, redirect, url_for, flash, session

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
        self.follow_up_players = [] # Players waiting for follow up
        self.facility = None       # Current rented facility
        self.competition = None    # Current entered competition
        self.week = 1              # Current game week
        self.year = 2026           # Current game year
        self.calendar_events = []  # Calendar events

    def get_summary(self):
        return (
            f"Club: {self.name}\n"
            f"City: {self.city}\n"
            f"Country: {self.country}\n"
            f"Finances: ${self.finances}\n"
            f"Reputation: {self.reputation}\n"
            f"Facility: {self.facility}\n"
            f"Competition: {self.competition}"
        )


class Player:
    def __init__(self, name, age, position, skill_level=1, source=None):
        self.name = name
        self.age = age
        self.position = position  # e.g., "Forward", "Midfielder", "Defender", "Goalkeeper"
        self.skill_level = skill_level  # 1-10 scale
        self.player_type = "Senior"  # For now, only Senior players
        self.source = source  # Where the player came from (flyers, social_media, open_training, word_of_mouth)

    def __str__(self):
        source_text = f" ({self.source})" if self.source else ""
        return f"{self.name} ({self.age}, {self.position}, Skill: {self.skill_level}){source_text}"


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


class CalendarEvent:
    def __init__(self, name, event_type, week, year, notes=""):
        self.name = name
        self.event_type = event_type  # "match", "training", "meeting", "maintenance"
        self.week = week
        self.year = year
        self.notes = notes
        self.invited_contacts = []  # List of player dictionaries invited to this event
        self.attendees = [] # List of players who attended the event

    def __str__(self):
        return f"{self.name} (Week {self.week}, {self.year})"


# Event type colors
EVENT_COLORS = {
    "match": "#FF6B6B",        # Red for matches
    "training": "#4ECDC4",     # Teal for training
    "meeting": "#95E1D3",      # Light teal for meetings
    "maintenance": "#F7DC6F",  # Yellow for maintenance
    "marketing": "#9B59B6"     # Purple for marketing/advertising
}


# -----------------------------
# Flask Web Application
# -----------------------------
app = Flask(__name__)
app.secret_key = 'grassroots-manager-secret-key'

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
            migrate_save_data(club) # This will fix the save data
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

def migrate_save_data(club):
    """Corrects data inconsistencies in loaded save files."""
    if not club:
        return

    # Ensure legacy saves have necessary attributes
    if not hasattr(club, 'follow_up_players'):
        club.follow_up_players = []
    if not hasattr(club, 'competition'):
        club.competition = None
    if not hasattr(club, 'week'):
        club.week = 1
    if not hasattr(club, 'year'):
        club.year = 2026
    if not hasattr(club, 'calendar_events'):
        club.calendar_events = []

    # Correct training event attendees and invited contacts
    for event in club.calendar_events:
        if event.event_type == 'training':
            # Ensure lists exist
            if not hasattr(event, 'attendees'):
                event.attendees = []
            if not hasattr(event, 'invited_contacts'):
                event.invited_contacts = []

            # Convert Player objects to dictionaries for consistency
            event.attendees = [
                {
                    'name': p.name,
                    'age': p.age,
                    'position': p.position,
                    'skill_level': p.skill_level,
                    'source': p.source
                } if isinstance(p, Player) else p for p in event.attendees
            ]
            event.invited_contacts = [
                {
                    'name': p.name,
                    'age': p.age,
                    'position': p.position,
                    'skill_level': p.skill_level,
                    'source': p.source
                } if isinstance(p, Player) else p for p in event.invited_contacts
            ]

def generate_random_player(source=None):
    """Generate a random player for recruitment"""
    import random

    first_names = ["John", "Mike", "David", "James", "Robert", "William", "Thomas", "Daniel", "Matthew", "Joseph"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]

    name = f"{random.choice(first_names)} {random.choice(last_names)}"
    age = random.randint(18, 35)
    positions = ["Forward", "Midfielder", "Defender", "Goalkeeper"]
    position = random.choice(positions)
    skill_level = random.randint(1, 5)  # Start with lower skilled players for grassroots

    return Player(name, age, position, skill_level, source)

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
    global club, available_players
    club_name = request.form.get('club_name')
    country = request.form.get('country')
    city = request.form.get('city')

    club = Club(club_name, city, country)
    available_players = []  # Reset available players
    return redirect(url_for('club_overview'))

@app.route('/club')
def club_overview():
    if club is None:
        return redirect(url_for('main_menu'))
    save_slots = get_save_slots()
    # Get week results from session and immediately clear them
    week_results = session.pop('week_results', None)
    return render_template('club.html', club=club, save_slots=save_slots, current_page='club', week_results=week_results)

@app.route('/squad')
def squad_view():
    if club is None:
        return redirect(url_for('main_menu'))
    save_slots = get_save_slots()
    return render_template('squad.html', club=club, save_slots=save_slots, current_page='squad')

@app.route('/training')
def training_view():
    if club is None:
        return redirect(url_for('main_menu'))
    save_slots = get_save_slots()

    # Get upcoming and recent training events
    upcoming_training_events = []
    recent_training_events = []
    if hasattr(club, 'calendar_events'):
        current_time = club.year * 52 + club.week
        for event in club.calendar_events:
            if event.event_type == 'training':
                # Sanitize attendees and invited_contacts to be lists of dicts
                if hasattr(event, 'attendees') and event.attendees:
                    event.attendees = [
                        {
                            'name': p['name'] if isinstance(p, dict) else p.name, 
                            'age': p['age'] if isinstance(p, dict) else p.age, 
                            'position': p['position'] if isinstance(p, dict) else p.position,
                            'skill_level': p['skill_level'] if isinstance(p, dict) else p.skill_level, 
                            'source': p['source'] if isinstance(p, dict) else p.source
                        } for p in event.attendees
                    ]
                
                if hasattr(event, 'invited_contacts') and event.invited_contacts:
                    event.invited_contacts = [
                        {
                            'name': p['name'] if isinstance(p, dict) else p.name, 
                            'age': p['age'] if isinstance(p, dict) else p.age, 
                            'position': p['position'] if isinstance(p, dict) else p.position,
                            'skill_level': p['skill_level'] if isinstance(p, dict) else p.skill_level, 
                            'source': p['source'] if isinstance(p, dict) else p.source
                        } for p in event.invited_contacts
                    ]

                event_time = event.year * 52 + event.week
                if event_time >= current_time:
                    upcoming_training_events.append(event)
                else:
                    # Check if the event is within the last 4 weeks
                    if current_time - event_time <= 4:
                        event.disappears_in = 4 - (current_time - event_time)
                        recent_training_events.append(event)

    # Sort upcoming events by the closest first
    upcoming_training_events.sort(key=lambda x: x.year * 52 + x.week)

    # Sort recent events by the most recent first
    recent_training_events.sort(key=lambda x: x.year * 52 + x.week, reverse=True)

    return render_template('training.html',
                           club=club,
                           save_slots=save_slots,
                           current_page='training',
                           upcoming_training_events=upcoming_training_events,
                           recent_training_events=recent_training_events)

@app.route('/marketing')
def marketing_view():
    if club is None:
        return redirect(url_for('main_menu'))
    save_slots = get_save_slots()
    return render_template('marketing.html', club=club, available_players=available_players, save_slots=save_slots, current_page='marketing')

@app.route('/advertise/<method>', methods=['POST'])
def advertise(method):
    if club is None:
        return redirect(url_for('main_menu'))

    # Ensure calendar_events attribute exists (for legacy saves)
    if not hasattr(club, 'calendar_events'):
        club.calendar_events = []

    week_offset = int(request.form.get('week_offset', 0))
    target_week = club.week + week_offset
    target_year = club.year

    # Handle year rollover
    if target_week > 52:
        target_week -= 52
        target_year += 1

    # Map advertising method names to display names and event types
    method_info = {
        'flyers': {'name': 'Flyer Distribution', 'type': 'marketing', 'cost': 50},
        'social_media': {'name': 'Social Media Post', 'type': 'marketing', 'cost': 0},
        'radio': {'name': 'Radio Advertisement', 'type': 'marketing', 'cost': 250},
        'tv': {'name': 'TV Commercial', 'type': 'marketing', 'cost': 750}
    }

    if method not in method_info:
        flash('Invalid advertising method!', 'error')
        return redirect(url_for('marketing_view'))

    info = method_info[method]

    # Check finances for paid methods
    if info['cost'] > 0 and club.finances < info['cost']:
        flash(f'Not enough funds! You need ${info["cost"]} but only have ${club.finances}.', 'error')
        return redirect(url_for('marketing_view'))

    # Create calendar event with metadata
    event = CalendarEvent(
        name=info['name'],
        event_type=info['type'],
        week=target_week,
        year=target_year,
        notes=f"advertising:{method}"  # Store the method type in notes for execution
    )

    club.calendar_events.append(event)

    week_display = f"week {target_week}" if week_offset == 0 else f"week {target_week} ({week_offset} week{'s' if week_offset > 1 else ''} from now)"
    flash(f'{info["name"]} scheduled for {week_display}!', 'success')

    return redirect(url_for('marketing_view'))

@app.route('/schedule_training/<method>', methods=['POST'])
def schedule_training(method):
    if club is None:
        return redirect(url_for('main_menu'))

    # Ensure calendar_events attribute exists (for legacy saves)
    if not hasattr(club, 'calendar_events'):
        club.calendar_events = []

    week_offset = int(request.form.get('week_offset', 0))
    target_week = club.week + week_offset
    target_year = club.year

    # Handle year rollover
    if target_week > 52:
        target_week -= 52
        target_year += 1

    # Map training method names to display names and costs
    training_info = {
        'open_training': {'name': 'Open Training Night', 'cost': 0}
    }

    if method not in training_info:
        flash('Invalid training method!', 'error')
        return redirect(url_for('training_view'))

    info = training_info[method]

    # Check finances for paid methods
    if info['cost'] > 0 and club.finances < info['cost']:
        flash(f'Not enough funds! You need ${info["cost"]} but only have ${club.finances}.', 'error')
        return redirect(url_for('training_view'))

    # Create calendar event with metadata
    event = CalendarEvent(
        name=info['name'],
        event_type='training',
        week=target_week,
        year=target_year,
        notes=f"training:{method}"  # Store the method type in notes for execution
    )

    club.calendar_events.append(event)

    week_display = f"week {target_week}" if week_offset == 0 else f"week {target_week} ({week_offset} week{'s' if week_offset > 1 else ''} from now)"
    flash(f'{info["name"]} scheduled for {week_display}!', 'success')

    return redirect(url_for('training_view'))

@app.route('/scout_players')
def scout_players_route():
    scout_players()
    return redirect(url_for('marketing_view'))

@app.route('/recruit_player/<int:player_index>')
def recruit_player(player_index):
    if club is None:
        return redirect(url_for('main_menu'))
    global available_players
    if 0 <= player_index < len(available_players):
        player = available_players.pop(player_index)
        club.squad.append(player)
        flash(f'{player.name} has been recruited to the squad!', 'success')
    return redirect(url_for('marketing_view'))

@app.route('/recruit_follow_up/<int:player_index>', methods=['POST'])
def recruit_follow_up(player_index):
    if club is None:
        return redirect(url_for('main_menu'))
    
    action = request.form.get('action')
    
    if 0 <= player_index < len(club.follow_up_players):
        player = club.follow_up_players[player_index]
        
        if action == 'ignore':
            club.follow_up_players.pop(player_index)
            flash(f'{player.name} has been ignored.', 'info')
        else:
            # Assume recruitment if action is not ignore (or default case)
            club.follow_up_players.pop(player_index)
            club.squad.append(player)
            flash(f'{player.name} has been recruited to the squad!', 'success')
            
    return redirect(url_for('marketing_view'))

@app.route('/invite_to_training/<int:player_index>', methods=['POST'])
def invite_to_training(player_index):
    if club is None:
        return {'success': False, 'error': 'No club'}, 400

    global available_players
    if 0 <= player_index < len(available_players):
        # Get upcoming training sessions
        upcoming_training = [event for event in club.calendar_events
                           if event.event_type == 'training'
                           and (event.year > club.year or (event.year == club.year and event.week >= club.week))]

        # Return player info and training sessions
        player = available_players[player_index]
        training_sessions = [
            {
                'index': i,
                'name': event.name,
                'week': event.week,
                'year': event.year
            }
            for i, event in enumerate(upcoming_training)
        ]

        return {
            'success': True,
            'player': {
                'name': player.name,
                'index': player_index
            },
            'training_sessions': training_sessions
        }

    return {'success': False, 'error': 'Invalid player index'}, 400

@app.route('/add_contact_to_training/<int:player_index>/<int:training_index>', methods=['POST'])
def add_contact_to_training(player_index, training_index):
    if club is None:
        return {'success': False, 'error': 'No club'}, 400

    global available_players
    if 0 <= player_index < len(available_players):
        # Get upcoming training sessions
        upcoming_training = [event for event in club.calendar_events
                           if event.event_type == 'training'
                           and (event.year > club.year or (event.year == club.year and event.week >= club.week))]

        if 0 <= training_index < len(upcoming_training):
            player = available_players.pop(player_index)

            # Ensure the event has invited_contacts list (for legacy saves)
            if not hasattr(upcoming_training[training_index], 'invited_contacts'):
                upcoming_training[training_index].invited_contacts = []

            # Add player to the training session's invited contacts
            upcoming_training[training_index].invited_contacts.append({
                'name': player.name,
                'age': player.age,
                'position': player.position,
                'skill_level': player.skill_level,
                'source': player.source
            })

            flash(f'{player.name} has been invited to {upcoming_training[training_index].name} (Week {upcoming_training[training_index].week})!', 'success')
            return {'success': True}

        return {'success': False, 'error': 'Invalid training index'}, 400

    return {'success': False, 'error': 'Invalid player index'}, 400

@app.route('/remove_contact/<int:player_index>', methods=['POST'])
def remove_contact(player_index):
    """Remove a contact from the available players list (e.g., for wrong number or not interested)"""
    if club is None:
        return {'success': False, 'error': 'No club'}, 400

    global available_players
    if 0 <= player_index < len(available_players):
        reason = request.args.get('reason', 'disconnected')
        removed_player = available_players.pop(player_index)

        if reason == 'not_interested':
            flash(f'{removed_player.name} was not interested and has been removed from contacts.', 'info')
        else:  # disconnected or any other reason
            flash(f"{removed_player.name}'s contact has been removed (disconnected number).", 'info')

        return {'success': True}

    return {'success': False, 'error': 'Invalid player index'}, 400

@app.route('/calendar')
def calendar_view():
    if club is None:
        return redirect(url_for('main_menu'))

    # Ensure calendar_events attribute exists (for legacy saves)
    if not hasattr(club, 'calendar_events'):
        club.calendar_events = []

    # Convert calendar events to dictionaries for JSON serialization
    events_data = [
        {
            'name': event.name,
            'event_type': event.event_type,
            'week': event.week,
            'year': event.year,
            'notes': event.notes
        }
        for event in club.calendar_events
    ]

    save_slots = get_save_slots()
    return render_template('calendar.html', club=club, calendar_events=events_data, save_slots=save_slots, current_page='calendar', event_colors=EVENT_COLORS)

@app.route('/add_calendar_event', methods=['POST'])
def add_calendar_event():
    if club is None:
        return {'error': 'No club'}, 400

    data = request.get_json()

    if not data or not all(k in data for k in ('name', 'event_type', 'week', 'year')):
        return {'error': 'Missing required fields'}, 400

    event = CalendarEvent(
        name=data['name'],
        event_type=data['event_type'],
        week=data['week'],
        year=data['year'],
        notes=data.get('notes', '')
    )

    club.calendar_events.append(event)
    return {'success': True}, 200

@app.route('/facilities')
def facilities_view():
    if club is None:
        return redirect(url_for('main_menu'))
    save_slots = get_save_slots()
    return render_template('facilities.html', club=club, save_slots=save_slots, facilities=adelaide_facilities, current_page='facilities')

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
    return render_template('competitions.html', club=club, save_slots=save_slots, competitions=competitions, current_competition=current_comp, current_page='competitions')


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

    import random

    week_results = []

    # Execute all scheduled events for the current week
    events_to_execute = [e for e in club.calendar_events if e.week == club.week and e.year == club.year]

    for event in events_to_execute:
        # Handle advertising events
        if event.notes and event.notes.startswith('advertising:'):
            method = event.notes.split(':')[1]

            if method == 'flyers':
                # Deduct cost
                club.finances -= 50
                num_players = random.randint(0, 3)
                for _ in range(num_players):
                    available_players.append(generate_random_player('Flyers'))
                if num_players > 0:
                    week_results.append(f'📋 Flyers distributed: {num_players} player(s) showed interest (Cost: $50)')
                else:
                    week_results.append('📋 Flyers distributed: No one showed interest (Cost: $50)')

            elif method == 'social_media':
                num_players = random.randint(0, club.reputation + 2)
                if num_players > 0:
                    for _ in range(num_players):
                        available_players.append(generate_random_player('Social Media'))
                    week_results.append(f'📣 Social media post: {num_players} player(s) responded')
                else:
                    week_results.append('📣 Social media post: No responses yet')

            elif method == 'radio':
                # Deduct cost
                club.finances -= 250
                num_players = random.randint(2, 8)
                for _ in range(num_players):
                    available_players.append(generate_random_player('Radio Ad'))
                week_results.append(f'📻 Radio advertisement: {num_players} player(s) showed interest (Cost: $250)')

            elif method == 'tv':
                # Deduct cost
                club.finances -= 750
                num_players = random.randint(5, 15)
                for _ in range(num_players):
                    available_players.append(generate_random_player('TV Commercial'))
                week_results.append(f'📺 TV commercial: {num_players} player(s) showed interest (Cost: $750)')

        # Handle training events
        elif event.notes and event.notes.startswith('training:'):
            method = event.notes.split(':')[1]

            if method == 'open_training':
                if not hasattr(event, 'attendees'):
                    event.attendees = []
                if not hasattr(event, 'invited_contacts'):
                    event.invited_contacts = []

                # Process invited contacts
                for contact in event.invited_contacts:
                    player = Player(
                        name=contact['name'],
                        age=contact['age'],
                        position=contact['position'],
                        skill_level=contact['skill_level'],
                        source=f'Invited to: {event.name}'
                    )
                    club.follow_up_players.append(player)
                    
                    # Store source in the attendee dict
                    contact['source'] = f'Invited to: {event.name}'
                    event.attendees.append(contact)

                # Add random walk-ins
                num_walkins = random.randint(0, 5)
                for _ in range(num_walkins):
                    player = generate_random_player(f'Open Training: {event.name}')
                    club.follow_up_players.append(player)
                    # Add to attendees for stats
                    event.attendees.append({
                        'name': player.name,
                        'age': player.age,
                        'position': player.position,
                        'skill_level': player.skill_level,
                        'source': player.source
                    })

                # Reset invited contacts after processing
                event.invited_contacts = []

                # Build results message
                if event.attendees:
                    week_results.append(f'⚽ {event.name}: {len(event.attendees)} player(s) attended and are waiting in your follow-up section.')
                else:
                    week_results.append(f'⚽ {event.name}: No one showed up')

    # Word of mouth: Passive player attraction based on reputation
    if random.random() < (club.reputation * 0.05):  # 5% per reputation point
        num_players = random.randint(0, max(1, club.reputation))
        if num_players > 0:
            for _ in range(num_players):
                available_players.append(generate_random_player('Word of Mouth'))
            week_results.append(f'💬 Word of mouth: {num_players} player(s) attracted')

    club.week += 1
    if club.week > 52:
        club.week = 1
        club.year += 1

    # Store results in session for the popup
    from flask import session
    session['week_results'] = week_results

    return redirect(url_for('club_overview'))

@app.route('/clear_week_results', methods=['POST'])

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
