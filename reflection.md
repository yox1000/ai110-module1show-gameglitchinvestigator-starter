# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

The first time I ran the game, it looked normal on the surface, but the behavior was inconsistent and confusing once I started guessing. I expected the hint text, scoring, and attempt tracking to match the game rules shown in the UI. Instead, several parts of the logic contradicted what the game claimed it was doing.

1. Hint direction bug:
Expected: If my guess was too high, the game should tell me to go lower, and if it was too low, it should tell me to go higher.
Actual: The messages were flipped, so a too-high guess told me to go higher and a too-low guess told me to go lower.

2. Secret number type-switch bug:
Expected: The secret should stay a stable integer every round so comparisons are always numeric.
Actual: On even attempts, the secret was converted to a string, which caused mixed-type comparison behavior and unreliable hint/outcome logic.

3. Attempt counter off-by-one bug:
Expected: The game should start at attempt zero and only consume attempts in a predictable way, so the "Attempts left" display is accurate.
Actual: Attempts started at 1 and were incremented before validation, so the remaining-attempt count and related scoring behavior were shifted from what a player would expect.

---

## 2. How did you use AI as a teammate?

I mostly used GitHub Copilot as a coding teammate while debugging and refactoring.

1. Example where AI suggestion was correct:
Copilot suggested moving game logic out of `app.py` into `logic_utils.py` and fixing hint direction in `check_guess`. That was correct because it made the code easier to test and fixed the player feedback bug (too high now says LOWER, too low now says HIGHER). I verified this by checking the updated `check_guess` code, manually testing game behavior, and running pytest after adding regression tests.

2. Example where AI suggestion was incorrect/misleading:
Copilot got stuck in a repeated loop around installing pytest and kept treating test failures like a missing-package issue. That was misleading, because the real blocker was pytest reading a bad parent config/encoding and then scanning outside the repo. I verified this by reading the actual terminal errors (`UnicodeDecodeError` and permission errors), then fixing test execution with a local `pytest.ini` and rerunning tests successfully.

---

## 3. Debugging and testing your fixes

I treated each fix as complete only after it passed both logic review and behavior checks in the game. For the hint bug, I verified that higher guesses now return "Too High" with a LOWER hint, and lower guesses return "Too Low" with a HIGHER hint. For the type-switch issue, I confirmed the app now passes the numeric session secret directly and added a regression test that checks `check_guess(9, "50")` behaves correctly. Copilot helped draft and refine the test cases, and I used pytest to validate everything with a clean result of `5 passed`. Clear summary of repairs: we refactored game logic into `logic_utils.py`, fixed hint direction, removed the risky secret string-conversion path from app flow, and added regression tests so these issues are less likely to come back.

---

## 4. What did you learn about Streamlit and state?

I would explain Streamlit reruns like this: every button click re-executes the script from top to bottom, so normal variables reset unless you store values in `st.session_state`. Session state is the app's memory between reruns, and it is where values like `secret`, `attempts`, and `score` should live. This project made it obvious that even small type changes across reruns can create weird bugs, especially in comparison logic. I also learned that UI output can look fine while hidden state logic is broken, so debugging state directly is important.

---

## 5. Looking ahead: your developer habits

One habit I want to keep is writing small regression tests immediately after I fix a bug, because it prevents the same issue from returning during refactors. Next time, I will challenge AI suggestions sooner instead of following repeated advice when evidence says otherwise; during this project, Copilot got stuck in a pytest-install loop and that delayed me until I checked the real error output. I will also ask AI for narrower, evidence-based steps (for example, "read this exact traceback and propose one fix") instead of broad troubleshooting. This project changed how I see AI-generated code: it is a useful accelerator, but it still needs careful verification, especially around state and tooling errors.
