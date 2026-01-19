import tkinter as tk
from tkinter import messagebox

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
# GUI Application
# -----------------------------
class GrassrootsManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Grassroots Football Manager")
        self.root.geometry("500x400")

        # Initialize a default club
        self.club = Club("Local United")

        # Show the main menu
        self.show_main_menu()

    def clear_window(self):
        """Remove all widgets from the window."""
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_main_menu(self):
        self.clear_window()

        title = tk.Label(self.root, text="Grassroots Football Manager", font=("Arial", 18, "bold"))
        title.pack(pady=20)

        start_btn = tk.Button(self.root, text="Start Season", width=20, height=2,
                              command=self.show_club_screen)
        start_btn.pack(pady=10)

        squad_btn = tk.Button(self.root, text="View Squad", width=20, height=2,
                              command=self.view_squad)
        squad_btn.pack(pady=10)

        exit_btn = tk.Button(self.root, text="Exit Game", width=20, height=2,
                             command=self.root.quit)
        exit_btn.pack(pady=10)

    def show_club_screen(self):
        self.clear_window()

        title = tk.Label(self.root, text="Club Overview", font=("Arial", 16, "bold"))
        title.pack(pady=10)

        summary = tk.Label(self.root, text=self.club.get_summary(), font=("Arial", 12), justify="left")
        summary.pack(pady=20)

        back_btn = tk.Button(self.root, text="Back to Menu", command=self.show_main_menu)
        back_btn.pack(pady=20)

    def view_squad(self):
        self.clear_window()

        title = tk.Label(self.root, text="Squad List", font=("Arial", 16, "bold"))
        title.pack(pady=10)

        if not self.club.squad:
            empty_msg = tk.Label(self.root, text="No players yet! Recruit some soon...", font=("Arial", 12))
            empty_msg.pack(pady=20)
        else:
            for player in self.club.squad:
                tk.Label(self.root, text=str(player)).pack()

        back_btn = tk.Button(self.root, text="Back to Menu", command=self.show_main_menu)
        back_btn.pack(pady=20)


# -----------------------------
# Run Application
# -----------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = GrassrootsManagerApp(root)
    root.mainloop()
