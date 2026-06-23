# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

When I first ran the game, it appeared functional but several parts of the logic behaved incorrectly. The biggest issue was that the hints were backwards. When a guess was too high, the game told the player to go higher, and when a guess was too low, it told the player to go lower. I also noticed that starting a new game ignored the selected difficulty range and that decimal values were accepted as guesses instead of being rejected.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guess 60 when secret is 50 | Hint says go lower | Hint says go higher | None |
| Start New Game on Hard difficulty | Secret should be between 1 and 50 | Secret could be generated outside the range | None |
| Enter 12.9 | Reject invalid input | Converted to 12 and accepted | None |

---

## 2. How did you use AI as a teammate?

I used ChatGPT to review the game code and identify the source of several bugs. One correct suggestion was moving the game logic functions from app.py into logic_utils.py and fixing the reversed hint messages in check_guess(). I verified the fix by running the Streamlit application and confirming the hints matched the user's guesses.

One misleading suggestion was assuming the secret number was changing every time the Submit button was pressed because the README mentioned that bug. After reviewing the actual code and testing the application, I determined that the secret number was not being regenerated on every submission. This showed me that I should verify AI suggestions against the code instead of assuming they are always correct.

---

## 3. Debugging and testing your fixes

I decided a bug was fixed only after verifying it in both the code and the running application. After making each change, I reviewed the logic, ran the Streamlit app, and tested the behavior that originally caused the bug. This helped confirm that the fix worked in practice and not just in theory.

One test I ran was checking the hint logic. When the secret number was lower than my guess, the game correctly displayed "Go LOWER!" instead of the incorrect message from before. I also ran python -m pytest and confirmed that all five tests passed, which verified that the core game logic behaved as expected.

AI helped me understand which functions should be tested and suggested test cases for winning guesses, high guesses, and low guesses. I still reviewed the generated tests myself to make sure they actually matched the intended behavior of the game.

---

## 4. What did you learn about Streamlit and state?

I learned that Streamlit reruns the entire script whenever a user interacts with the app, such as clicking a button or entering data. Because of this behavior, variables that are not stored properly can appear to reset or lose their values between interactions.

I would explain session state to a friend as a special storage area that remembers information between reruns. Without session state, values like the secret number, score, and attempt count would be recreated every time the page refreshes, making it difficult to build an interactive game.

---

## 5. Looking ahead: your developer habits

One strategy I want to reuse is writing and running tests whenever I fix a bug. Having automated tests made it much easier to confirm that my changes worked and did not break other parts of the program. I also found it useful to make small commits as I completed different stages of the project.

Next time I work with AI on a coding task, I will spend more time verifying its suggestions before applying them. Some suggestions were helpful, but others required checking the actual code and testing the behavior before trusting them.

This project showed me that AI-generated code should be treated like code written by any other developer. AI can speed up debugging and development, but human review and testing are still necessary to ensure the solution is correct.