from flask import Flask, render_template

# -----------------------------
# Core Data Classes
# -----------------------------
class Club:
    def __init__(self, name):
        self.name = name
        self.finances = 1000       # starting money
        self.reputation = 1        # starts as unknown
        self.squad = []            # will add later
        self.facilities = "Public Park"

    def get_summary(self):
        return (
            f"Club: {self.name}\n"
            f"Finances: ${self.finances}\n"
            f"Reputation: {self.reputation}\n"
            f"Facilities: {self.facilities}"
        )


# -----------------------------
# Flask Web Application
# -----------------------------
app = Flask(__name__)

# Initialize a default club
club = Club("Local United")

@app.route('/')
def main_menu():
    return render_template('index.html')

@app.route('/club')
def club_overview():
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
