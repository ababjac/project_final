# project_final
Project: Drum Machine

Authors: Ashley Babjac & Zoe Babyar

Description: Create your own rhythm from a set of sounds, note lengths, and BPM’s



STEP 1: SETTING UP
1.	Download python 3.7.0

    a.  https://www.python.org/downloads/release/python-370/

    b.	To check that python has installed, Enter: python --version

2.	Download pygame

    a.	Enter: pip3 install hg+http://bitbucket.org/pygame/pygame

    b.	Enter: import pygame

3.	Download pygame-menu

    a.	Enter: pip3 install pygame-Menu



STEP 2: GITHUB NAVIGATION

The finished app is in the finished_app folder. It is called drum_machine_v_2.0.0.py. Previous development versions are under the development folders (some of these do not compile but the code can be referenced).


STEP 3: HOW TO RUN

  1.	To see code: vi finished_app/drum_machine_v_2.0.0.py

  2.	To run: cd finished_app; python3 drum_machine_v_2.0.0.py



STEP 4: USING THE PROGRAM

Main Menu:

  •	Navigation: Use the up and down arrow keys to navigate through options. Use the ENTER key to select an option.

  •	Options:

      o	Begin Drumming!-  Enters the Drum Machine program

      o	About-            Lists the title, authors, and GitHub repository

      o	Quit-             Exits the program

Drum Machine:

  •	Sound Selection:

      o	The grid is separated into sounds (rows) and 4-beat bars (columns). Sound names are in a list to the left of the grid
        which each correspond to a row. Left-click on a square to select a sound and its place in the rhythm.

  •	Timing:

      o	Left-click on a Timing square to choose the note spacing. For example, selecting the “1/8” square will turn all      
        selected sounds into eighth-notes.

  •	BPM:

      o	Left-click to select a BPM square. The BPM determines the speed, in beats per minute, of your rhythm.

  •	Play/Stop:

      o	Left-click to begin playback, then left-click again to end playback

  •	Clear:

      o	Left-click to clear the grid of all selected sounds and rhythms

  •	Return to Main Menu:

      o	Left-click to return to main menu




KNOWN BUGS
  1. On SOME Linux machines (like mine -- Mint Cinnamon 19.1), the error "ALSA lib pcm.c:8306:(snd_pcm_recover) underrun occurred" will pop up in the terminal during run time. This does not affect the running or functionality of the program. It has to do with the type of sound player that is the default on the machine and is not actually a problem with our program, but should be noted.
  
NOTES
    1. For this program we used Python version 3.7.0; however, it will be compatable with newer versions of python. It should also work for any version of Python 3 (but I have not tested this). It is not compatable with Python versions 1 or 2. 
