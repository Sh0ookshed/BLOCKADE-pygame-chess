# BLOCKADE PYGAME CHESS (Written in Pygame and Rust)
This is a Rust chess Program with a Pygame GUI. Officially named Blockade!

<img src="assets/BLOCKADE LOGO.png" width="400" height="300" />

# Table of Contents
* [What is this software?](#what-is-this-software)

* [Features of the program](#features-of-the-program)

* [If you think this project is interesting](#if-you-think-this-project-is-interesting)

* [Screenshots of the current program](#screenshots-of-the-current-program)

* [Personal goals with this project](#personal-goals-with-this-project)
# What is this software?
This is a chess program that contains Rust backend and Python frontend allowing the user to play against a chess program. I'm trying to make this in a unique way that allows for a frontend Python GUI using Pygame and then a Rust backend. These two will then be linked together using the PY03 module to link the Rust backend functions to self created Python modules. This will allow for chess to be played in a Pygame program that runs off of Rust logic. This improves speed and accuracy. The program will have a variety of features and it is designed to be used casually, furthermore the program won't link to any databases or external websites making it an offline experience. 

# Features of the program:
* An interactive main menu.
* Customisable settings through settings menu including:
  * Turning match feedback on/off.
  * Setting match feedback to be in-game or post-game.
  * Changing the time limit (Chess Clock) for each chess match.
  * and more.. (Potentially)
* A win statistics window to view the amount of times you have won, drawn or lost your chess matches (Which saves to a txt file).
* Recieving feedback on moves you make against the chess program (In-game or post-game).
* A Fully functional chess program you can play against through a game window.
* Amazing(ish) image assets that I drew myself using Aseprite which is a 2D pixel art creation software.

# If you think this project is interesting
I will include all of my documentation and planning for this project inside of this repository for anyone to access to see my thought process and how i designed certain parts of the code.

This project is a big learning experience for me because alongside creating it, I am also learning how to use GIT / GitHub so forgive any poor early commits as they will hopefully get better. Also this project could obviously have very large code refactors due to me not having done any chess programming before, so previous commits could end up looking quite different from newer ones. (Mainly due to me having to change half of the code due to problems I forgot to consider previously).

I will continue to do version releases of the project until it reaches v1.0 (completed version) or a version that I am satisfied with.

# Screenshots of the current program
These screenshots are just to preview what the program looks like and more screenshots will come as the program is developed further. This means that the current UI is subject to change.

**The main menu window where you can access all other sections / features of the program:**
<img width="800" height="800" alt="Screenshot 2026-01-29 112817" src="https://github.com/user-attachments/assets/d0f7d729-a5a8-412b-b6e4-22f51011f57e" /> <br>


**The win statistics window which will link to a txt file to save match results:**
<img width="800" height="800" alt="Screenshot 2026-01-29 112852" src="https://github.com/user-attachments/assets/d898e024-bcd2-4bd8-a465-0cf7c3b59378" /> <br>


**The settings menu window where you can customise your experience:**
<img width="800" height="800" alt="Screenshot 2026-01-29 112943" src="https://github.com/user-attachments/assets/70325c28-5db7-4f8e-8375-2db5d76cf4fa" /> <br>

# Personal Goals with this project
While this project repository is mainly to contain the Pygame chess program described above, I will also be using this repository to practice a lot of skills that can better me as a programmer. This means that maybe some of the commits that add to the README (or other files) may seem unecessary or excessive, however this is all for my own benefit. Therefore while commits may be inconsistent, I will be improving.

**examples of personal goals are:**
* To get better at creating a good and informative README file using HTML and Markdown along with learning to use scripts that directly add interactable content to my README.
* Improving my coding skills in both Rust and Python.
* Getting better at drawing pixel art such as chess pieces (Which I am currently horrific at).
* Learning how to package my projects and release them as EXEs through different version releases that can be downloaded and used by anyone.
* Getting better at using Git (using console commands) and improving my commit messages to make them informative, but also more concise.
* Committing useful additions in small stable and effective commits instead of cramming loads of features into one commit or doing loads of commits that barely add anything.
