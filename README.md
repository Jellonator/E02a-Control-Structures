
# E02a-Control-Structures

Let's start experimenting with some Python code! This is a set of exercises for MSCH-C220; they should give you the tools to help build your first game.
 
This exercise assumes that you have already installed Python, GitHub Desktop, and VS Code, and that you have already created a GitHub account. If that is not the case, please refer to previous exercises.

This repository contains several files that you will need to alter to complete the assignment. Fork this repository (instructions below) and edit the files. Commit and push the changes back to GitHub and turn in the URL to your repository on Canvas.

Comments in Python are marked by a # sign (for single-line comments) or three matching quotation marks (''' or """) if a comment requires more than one line. They should also appear in a different color in VS Code. The Python Interpreter ignores comments, so you can safely include any information you want there.

*If you wish your exercise to be graded, please edit the LICENSE file (add the current year and your name).*

Edit README.md to answer the following questions:

- Open main01.py. Before running it, what do you expect this program to do?

  I expect this program to ask for an input and do nothing else, since the answer I input is not stored anywhere.

  - Now right click on the main1.py window and select “Run Python File in Terminal”. Click in the bottom panel, and answer the question. Describe what happened.

    The program asked me for my favorite color, then did nothing else.

  - What do you think the program did with what you typed in answer to the question?

    The program did not do anything with the answer that I typed.

- Open main02.py. Before running it, describe how this is different than main01.py.

  This program has a print statement after asking for input which will print out the color that I responded with.

  - What do you think the color = input() will do?

    This will take the answer that I input and store it in a variable named 'color'.

  - Run the program in the terminal and answer the question. Did the program do what you expected?

    Yes, it printed out the color that I input.

- Open main03.py. Before running it, describe how this is different than main02.py.

  This program uses an if statement to check if the answer is "Red"; answers such as "purple", "keyboard", or "red" would result in the else block being executed instead, and print "Sorry, try again.". If the answer is "Red", then the program will print "Correct!".

  - What is happening on lines 9–12?

    There is an if statement checking if the answer is "Red".

  - Why are lines 10 and 12 indented?

    In Python, indentation is used to mark blocks of code. In this case, the indented line on line 10 is only executed if the answer is "Red", otherwise the indented line on line 12 is executed.

  - Run the program and answer the question. What happens if you don’t capitalize Red?

    If my answer is not capitalized, then the program tells me "Sorry, try again.".

  - What does this tell you about "color"?

    String data types are case-sensitive, even for comparisons.

- Open main04.py. Before running it, describe how this is different than main03.py.

  This program checks if the answer that I input is either "Red" or "red".

  - What problem is this trying to solve?

    The problem that is solved by this is when the user inputs "red" but the program does not consider that to be correct.

  - Run the program and answer the question. What happens if you use some other capitalization scheme (i.e., “RED” or “reD“)?

    The program does not consider any other capitalization scheme to be correct; "RED" tells the user "Sorry, try again.".

- Open main05.py. What do you expect line 9 to do?

  Line 9 first makes color lowercase; each character in the string is changed to its lowercase form, if it has one (e.g. "PurpLE" becomes "purple"), then compares this answer to "red".

  - What problem is it trying to solve?

    This solves the program of the user inputting answers like "RED" or "rED" being considered incorrect, allowing the user to capitalize whichever letters they see fit. 

  - Run the program and answer the question. What happens if you add spaces before or after the word (i.e., “ RED “ or “ red”)?

    Answers with spaces at the start or end of the input are considered incorrect,
    since spaces are characters too.

- Open main06.py. How is line 9 different than in main05.py?

  This program also calls the `strip` function on the string after calling the `lower` function.

  - What would you guess .strip() is doing?

    The `strip` function removes the spaces from the start and end of the string.

  - Run the program and answer the question. Is there another way of writing “red” that will break this logic?

    The answer `r e d` is considered incorrect, but at this point, would any sane person answer the question this way?

    The anser `"red"` is also incorrect, I'm sure theres someone out there who would try this.

- Open main07.py. Before running this program, how do you expect this to be different than main06.py?

  If I answer "pink" instead of "red", the program will tell me that I'm close to the actual answer.

  - What is happening on line 12?

    There is an `elif` case inserted between the if and else clause of this if statement. If the answer is not "red" but the answer is "pink", then the string "Close!" will be printed.

  - Run the program and answer the question.
- Open main08.py. What is the purpose of line 9?

  Line 9 repeats the question until the user correctly answers the question.

  - Why are lines 10–17 indented?

    These lines are indented because they are part of the while loop's block, which is executed on each iteration of the loop.

  - Run the program. What would happen if line 10 were moved before line 9 (and no longer indented)?

    The program would only ask for an answer once. If the answer were "red" (not "Red", "rED" or "  red ", since the `strip` and `lower` functions would not have been called yet), then the loop would never run to tell me that the answer is correct, and the program would end. If the answer were something like "rED" or "  red ", then the program would tell me that I'm correct, and the program ends. If the answer were some form of "pink", then the program would loop endlessly telling me that I'm "Close!", otherwise the program would loop endlessly to tell me "Sorry, try again.".

  - Make that change and run the program again. (To end any Python program, you can type ctrl-c)
- Open main09.py. What is happening on line 13?

  The program adds `1` to the variable `count`, then stores the result in the variable `count`.

  - What is the purpose of “count”?

    The `count` variable is used to count how many guesses it takes to get the correct answer.

  - What is happening on line 21?

    The program uses the string `format` method to format a string with an integer in it. In this case, the "{}" is substituted with the value of `count`.

  - Run the program.
- *Extra credit:* open main10.py. Add a comment to each line describing what it is doing (a comment follows a pound sign [#]).
- *Extra credit:* open main11.py. What is happening on lines 6-11?

  The program defines a function 'choose_color' which takes a single argument and returns a string. This function chooses a random color from a predetermined list of colors, and makes sure that the color that is returned is not equal to 'last_color'. This is so that the game does not have the same answer twice in a row.
  
Commit your changes and push them back to the repository.
 

---

Instructions for forking this repository:
 
Log into your account on [github.com](https://github.com)

Go to the [exercise template page](https://github.com/BL-MSCH-C220-S20/E02a-Control-Structures) on GitHub

There is a button in the top right corner of the page labeled "Fork". Press that now

This will create an independent copy of this repository in your account that you can control and edit

Go to your GitHub home page, and select the new E02a-Control-Structures repository

On that page, you will see a green button labeled "Clone or download". Press that now. You will see a drop down box. Press the "Open in Desktop" button.

This should launch GitHub Desktop. It will ask you for a location (on your computer) where the repository may be cloned (downloaded). Choose a location that will be easy for you to find, and press the blue "Clone" button.

Once GitHub Desktop has cloned (downloaded) the code, it will be responsible for keeping the code on your local computer synchronized with the repository in your GitHub account. Now, open Visual Studio Code, and choose File->Open. Find the folder of the cloned repository and select Open.

In the left (File Explorer) panel, you should see a list of files that comprise this repository

First, edit the file called LICENSE. Replace year and name with the current year and your name. Save this file

Then open README.md. Feel free to remove any extraneous information, and then answer the questions posed in the file. You can add your answers after each question

When the time comes for you to run any of the python files, you can do so by clicking the green arrow in the top right corner of the window or by right-clicking on the code and selecting "Run Python File in Terminal". The results will appear at the bottom. If you don't see "Run Python File in Terminal" in the contextual menu, that is because VS Code doesn't have the Python extension installed. You can do that here: [https://marketplace.visualstudio.com/items?itemName=ms-python.python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

When you are done editing the files, return to GitHub Desktop. In the left panel, you should see a list of the files that have changed

At the bottom of the leftmost area, you should see a text box labeled "Summary (required)". Add a message that describes what you have done; these messages are typically stated in the active-present tense. For example, "Updates the LICENSE, README.md, and completes the assignment." Push the blue "Commit to master" button

In the top bar of the window, you should see a button that is labeled "Push origin", push that now

Check out your page on GitHub. You should see the changes you made reflected there, Repeat steps 10 through 16 as necessary

When you are satisfied with your efforts, turn in a URL to your repository on Canvas

---
If you try to push your changes, and you receive a permission error, it is likely that you are trying to edit the BL-MSCH-C220-S20 copy of the repository rather than your own. Make sure you don't skip the step of forking your own copy and cloning that.

---

The grading criteria will be as follows:
 
[1 point] Repository contains a description of the project in README.md

1 point will be awarded for answering the questions associated with each of the files

10 points total (+2 points extra credit)
