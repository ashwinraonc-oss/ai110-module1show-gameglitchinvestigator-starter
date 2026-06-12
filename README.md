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
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: _"How do I keep a variable from resetting in Streamlit when I click a button?"_
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- The game's purpose is for fun. The user tries to guess a secret number that only the game knows. Every time the user guesses it right, they increase their score. Every time they guess wrong they decrease their score. They have a limited number of attempts that change based on difficulty.
- The bugs I found:
- Difficulty not properly changing number of attempts - changing difficulty from normal to hard decreased the number of attempts allowed
- Guessing a number below the range told the under to guess lower - Guess of -1 in a range of 1 to 100 told me that the guess was too low.
- New Game reset button was not resetting - Clicking new game would not reset the score or the history of guesses.
  The fixes I applied:
- Swapped "Too High" and "Too Low" labels, so that a guess that was too low actually resulted in a message of "Too Low"
- On st.session_state reset, the history, score, attempts, and status were all reset on a New Game click. Attempts and Score were set to 0 in a New Game.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User chooses difficulty in side panel based on if they want more guesses or less guesses (Easy or Hard)
2. User enters guess of 3
3. Game returns "too low" message and score and number of tries decrease. Attempts increments.
4. User guesses again and process repeats
5. User guesses correctly --> game ends

**Screenshot** _(optional)_: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
tests/test_game_logic.py::test_guess_too_high PASSED                                                                                                                                               [ 14%]
tests/test_game_logic.py::test_guess_too_low PASSED                                                                                                                                                [ 21%]
tests/test_game_logic.py::test_too_high_message_says_go_lower PASSED                                                                                                                               [ 28%]
tests/test_game_logic.py::test_too_low_message_says_go_higher PASSED                                                                                                                               [ 35%]
tests/test_game_logic.py::test_negative_guess_is_too_low PASSED                                                                                                                                    [ 42%]
tests/test_game_logic.py::test_negative_guess_below_negative_secret PASSED                                                                                                                         [ 50%]
tests/test_game_logic.py::test_guess_above_range_is_too_high PASSED                                                                                                                                [ 57%]
tests/test_game_logic.py::test_guess_below_range_is_too_low PASSED                                                                                                                                 [ 64%]
tests/test_game_logic.py::test_in_range_guess_too_high PASSED                                                                                                                                      [ 71%]
tests/test_game_logic.py::test_in_range_guess_too_low PASSED                                                                                                                                       [ 78%]
tests/test_game_logic.py::test_correct_answer PASSED                                                                                                                                               [ 85%]
tests/test_game_logic.py::test_correct_answer_at_lower_bound PASSED                                                                                                                                [ 92%]
tests/test_game_logic.py::test_correct_answer_at_upper_bound PASSED                                                                                                                                [100%]

========================================================================================== 14 passed in 0.03s ===========================================================================================
```

## 🚀 Stretch Features -

```
The above fenced code block included the basic test case as well as the stretch goal test cases.
```

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]

```

```
