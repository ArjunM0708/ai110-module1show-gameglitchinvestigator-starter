# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect. Also the on click event when pressing enter to submit a guess is also faulty.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

The user interface displayed as expected.

- List at least two concrete bugs you noticed at the start  
  The hints fluctuated. For examply when I submitted 6 it displayed go lower, but when I submitted 5 it displayed go higher. This is impossible since the input should be integers.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I implemented Claude Code for the project.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
AI had pointed out that previous guesses were carrying over to the next game. I verified this myself by testing it on the game, and it was true. AI had proposed a fix for this problem in lines 133-138, I carefully reviewed it before finalizing the changes.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
When fixing the attempt decrementer, the AI had proposed fixes to already functionally correct code which would've been unecessary.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I would rerun the game and observe the changes. If the errors I was attempting to fix were seemingly gone, I would proceed.
- Describe at least one test you ran (manual or using pytest)  
With the hints in particular, I kept guessing different numbers to test the logic.
  
- Did AI help you design or understand any tests? How?
Claude explained how I can use Copilot to generate different kinds of tests. 

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.

After every streamlit rerun, the secret was changing after each attempt. The number would stay the same but it was change between int and strings.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
A streamlit rerun essentially saves the changes you made to the code, and you're able to test the changes you made in real time using the rerun feature on streamlit.
- What change did you make that finally gave the game a stable secret number?
Both values were cast to int before comparing.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
Taking my time to document the observable bugs. This ensured that I knew the order I wanted to tackle each of the problems in.
  
- What is one thing you would do differently next time you work with AI on a coding task?
I would've made better use of Github Copilot. I used Claude Code mainly for this project, however for future projects I intent to implement Github Copilot more as well.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
I realized AI generated code should also be reviewed just as thoughrougly as code written by human. Prompts require you to be specific, naming the minute details and edge cases.
