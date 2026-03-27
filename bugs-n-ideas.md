## Latest feature added
Recently did the follow up section.

## Bug fixes needed
The source badge changes for those who have been to a training - source should remain the same but a note about training should appear below the info.
Upcoming training should not display position and skill level

## Where to go next

## 🏁 First: Finish What You're On

The player attraction → training → joining squad pipeline is the **core loop of the whole game**. Everything else hangs off it. Getting that fully working (including the phone call system, which is marked under construction) is the right priority before anything else. Don't get distracted — close it out.

---

## ⚡ Quick Wins (Low Effort, High Impact)

These are things you could give to Cline with minimal design thinking needed:

**1. Finances display & weekly deductions**
You already track finances and have facility costs. Just make the weekly "Next Week" tick deduct rent, and show a running balance with a simple income/expense log. Instantly makes the game feel alive.

**2. Squad page improvement — player stats display**
Players already have skill level, age, position. Add a basic "form" or "fitness" stat that degrades slightly each week if no training is scheduled. No gameplay change needed — just makes the squad page feel meaningful.

**3. Word of Mouth automation**
It's listed as "automatic weekly execution" but make sure it actually scales visibly with reputation. Even a small changelog in the weekly results popup ("Word of mouth brought in 1 interested player") makes progression feel real.

**4. CHANGELOG-driven version bump display**
You already have a CHANGELOG.md. Show the current version in the footer automatically. Tiny task, nice polish.

---

## 🎮 The "Playable" Milestone

For the game to feel genuinely playable, you need one complete **season loop**. That means:

**1. Actual Matches**
This is the big one. You need a match simulation — even a very simple one. At minimum: scheduled match week executes, a result is calculated (influenced by squad size/skill), and the result shows in the weekly popup. No tactics needed yet, just a dice roll weighted by your squad quality vs. a generated opponent.

**2. League Table**
Once matches exist, you need a table. Even a static fake one with 6-8 AI clubs that gets updated as results come in. This is what gives the season a sense of stakes.

**3. Season End / New Season**
At week 52, something should happen — a summary screen, promotion/relegation (even just a message), and a reset into a new season. This closes the loop and makes the game replayable.

**4. Financial Jeopardy**
Right now there's no real consequence to spending. Add a game-over or warning state when finances hit zero. Suddenly every decision has weight.

---

## 🗺️ Slightly Further Out (But Worth Designing Now)

- **Player morale / retention** — players might leave if you don't train them or go bankrupt
- **Opposition clubs** — even procedurally generated names/stats give the league life
- **Reputation system that does something** — currently reputation is tracked but doesn't seem to feed back into the game meaningfully; tie it to word-of-mouth strength and match attendance income

---

## My Suggested Order

1. ✅ Finish the training/joining pipeline (you're nearly there)
2. ⚡ Weekly finance deductions + balance display
3. 🎮 Basic match simulation + results
4. 🎮 League table with AI clubs
5. 🎮 Season end summary screen
6. ⚡ Financial game-over state