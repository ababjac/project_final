# project_final
Project: Drum Machine

Authors: Ashley Babjac & Zoe Babyar

Description: Create your own rhythm from a set of sounds, note lengths, and BPM’s



STEP 1: SETTING UP
1.	Download python 3.7.0
  
    a.  https://www.python.org/downloads/release/python-370/
  
    b.	To check that python has installed, type: python --version

2.	Download pygame
  
    a.	Enter: pip3 install hg+http://bitbucket.org/pygame/pygame
  
    b.	Enter: import pygame

3.	Download pygame-menu
  
    a.	Enter: pip3 install pygame-Menu





STEP 2: GITHUB NAVIGATION //FIXME


STEP 3: HOW TO RUN	//FIXME
  
  1.	To see code: vi drum_machine_v_2.0.0.py
  
  2.	To run: python3 drum_machine_v_2.0.0.py





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
  1.	After approximately 20 seconds of playback, the rhythm falls slightly off-beat then quickly readjusts. In talking to    
      our TA, Brent Hurst, we determined that these slight timing errors may be a python issue as opposed to a program logic 
      issue. 
  

