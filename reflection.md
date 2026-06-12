# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

  The game seemed normal before I ran it. It oultined the instructions adequately so I knew how to play the game. The UI was a bit cluttered because of the debug section, but nothing that was too distracting.

- List at least two concrete bugs you noticed at the start  
   (for example: "the hints were backwards").

  One bug I noticed is that once you uncheck the "Show hint" box, you cannot get the hint back by checking it again. Another bug I noticed is that no matter what number I guessed, the hint told me to go lower. Even if the number was negative and below the lower bound of the question, the hint would tell me to go lower.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |:

| Guess of -1 | Too Low | Too High | None |
| Lowered Difficulty from Normal to Easy | More attempts | Attempts went from 7 to 5 | None |
| Clicked New Game | Score should reset | Score went down by 5 on first click, then stayed the same for every other click | Score went from -10 to -15 to -15, etc. |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  I used Claude Opus 4.8
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  One AI suggestion that was correct was that the root cause of the history not resetting on a New Game click was due to the st.session_state not resetting between runs. To verify this, I went into the code where the New Game logic was stored. Here, I found that the AI was correct, and that on a New Game click, only attempts was being reset to 0, when score, history, and status should also be reset.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  One thing the AI suggested that was incorrect was for the attempts to start at 1, even before the player tries to guess the number. The AI suggested this after I asked it to fix the New Game button no resetting as outlined above. I verified that this was incorrect because in App.py, attempts was set to 1 on a reset.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  First I skimmed the code that I thought would be affected by the fix briefly, looking for any glaring issues. Then, I read the AI blurb about the fix to see if my thoughts lined up with the AI. I then ran the code and tested the game by inputting many different numbers that I thought would satisfy both edge cases and non edge cases (e.g negative numbers, numbers above or below the range). Then I asked the AI to make test cases based on these edge cases, making sure to explicitly state what edge cases I wanted the tests to cover. Finally, I looked over the edge cases and ran them, making sure they all passed.
- Describe at least one test you ran (manual or using pytest)  
   and what it showed you about your code.
  I used AI to create a test case that checked if a negative number would result in a message of "Too Low" as it should. I chose this because, before any changes to the code, a guess of -1 would tell me to guess lower, even though it was lower than the range. After the AI fixes, this test case passed.
- Did AI help you design or understand any tests? How?
  Yes, AI helped design the tests, because I gave it edge cases and normal cases that I wanted it to check, and it created the tests for me. It then gave me a brief explanation of the code, so I could verify that the code was working for its intended purpose.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  Streamlit is an accessible python library for building web apps without writing code. Streamlit works by rerunning the entire code every time a website is interacted with. In the case of the guessing game, every New Game click or guess reruns the entire code, meaning normal variables are reset. Session state allows the programmer to save variables across reruns if it is information that needs to be saved (e.g the number to be guessed every time a guess is passed).

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
    One strategy that has been stressed by this class and that I would like to continue doing is making sure to verify everything the AI says. It can be easy to fall into a system of just taking what the AI has to say as fact, since I have already verified the same AI in dozens of other tasks in the past. However, falling into this mindset can be a way to introduce bugs or inconsistent logic into programs, a problem that is only exacerbated in large-scale collaborative projects,
- What is one thing you would do differently next time you work with AI on a coding task?
  One thing I would do differently when I work with AI for a coding task is not reading terminal commands very closely that the AI wants to execute. It did not result in any issues this time, but I can imagine that sometimes the terminal command the AI is showing me may not line exactly up with what I would like it to do. Next time, I should clearly read the entire command to see what it is doing, hopefully learning more about what terminal commands exist as well.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  Before this project, I saw AI as less of a tool and more of a crutch for those who did not know how to code. I thought of it as 'cheating' in a way. However, both the lectures and the project have given me a clearer picture of how inevitable AI coding is. It is something I need to get used to if I do not want to fall behind in the software field. Additionally, I learned that AI can be a good thing for my coding development if I don't just use it as a crutch. It is up to me how I use AI and if I supplement my coding journey with AI rather than just making it do everything for me.
