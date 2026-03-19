# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience


Game:
- [Glitchy Guesser is a number guessing game where the player tries to guess a randomly generated secret number within a limited number of attempts. The difficulty setting controls the number range and attempt limit. After each guess, the game provides a hint (Too High / Too Low) and updates the player's score rewarding faster correct guesses and penalizing wrong ones.

The twist is that the game was intentionally shipped with several bugs — inverted hints, broken scoring, wrong difficulty ranges — making it unwinnable until the bugs are identified and fixed.] 


Bugs:
- [ Inverted hints "Too High" said "Go HIGHER!" and vice versa
String comparison bug — secret passed as string on even attempts caused wrong comparisons
Swapped difficulty ranges — Normal was 1–100, Hard was 1–50 (backwards)
Wrong score on bad guesses  even-attempt "Too High" guesses rewarded +5 instead of -5
Win points off by one attempt  attempt_number + 1 shifted scores down unnecessarily
Score could go negative  no floor of 0
New Game didn't reset status  game stayed won/lost, blocking new play
New Game didn't clear history old guesses carried over
New Game ignored difficulty range hardcoded randint(1, 100)
Attempts started at 1 silently reduced available guesses by 1
Hardcoded range in UI always showed "1 and 100" regardless of difficulty
Enter key didn't submit no form wrapping the input] 


Fixes:
- [Flipped hint messages  "Too High" now says "Go LOWER!", "Too Low" says "Go HIGHER!"
Normalized types in check_guess both guess and secret cast to int before comparison
Swapped difficulty ranges Normal now 1–50, Hard now 1–100
Simplified wrong-guess scoring — both "Too High" and "Too Low" always deduct 5, floored at 0
Removed + 1 from win formula points now correctly based on attempt_number
Added max(0, ...) floor — score can't go negative
Reset status on New Game set back to "playing" so the game is unblocked
Clear history on New Game old guesses no longer carry over
New Game respects difficulty uses randint(low, high) instead of hardcoded randint(1, 100)
Attempts initialized at 0 full attempt count now available each game
Dynamic range in UI banner displays correct {low} and {high} per difficulty
Wrapped input in st.form Enter key now submits a guess alongside the button ] 

## 📸 Demo

![alt text](<Screenshot (20).png>)

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
