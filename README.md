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

- [x] Describe the game's purpose: The app is a Streamlit number-guessing game where the player uses higher/lower feedback to find a secret number within a limited number of attempts.
- [x] Detail which bugs you found: The hint direction was reversed, the secret could be treated as a string and break comparisons, and the attempt counter behavior was off-by-one.
- [x] Explain what fixes you applied: Core logic was refactored into `logic_utils.py`, hint logic was corrected, unsafe secret-type handling was removed from app flow, and regression tests were added.

## 📸 Demo

- [x] Ran the fixed app locally with Streamlit and verified the win flow and hint behavior.
- [x] Verified test coverage with pytest: `5 passed`.

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
