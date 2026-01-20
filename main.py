from flask import Flask, render_template, request, redirect, url_for

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

    def get_summary(self):
        return (
            f"Club: {self.name}\n"
            f"City: {self.city}\n"
            f"Country: {self.country}\n"
            f"Finances: ${self.finances}\n"
            f"Reputation: {self.reputation}\n"
            f"Facilities: {self.facilities}"
        )


# -----------------------------
# Flask Web Application
# -----------------------------
app = Flask(__name__)

# Initialize a default club
club = None

@app.route('/')
def main_menu():
    return render_template('index.html')

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
    return render_template('club.html', club=club)

@app.route('/squad')
def squad_view():
    return render_template('squad.html', club=club)

@app.route('/exit')
def exit_game():
    return render_template('exit.html')


# -----------------------------
# Run Application
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
