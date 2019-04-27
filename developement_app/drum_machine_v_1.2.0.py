# Import pygame and libraries
from pygame.locals import *
from random import randrange
import os
import pygame

# Import pygameMenu
import pygameMenu
from pygameMenu.locals import *

#menu constants
ABOUT = ['PygameMenu {0}'.format(' UTK Drum Machine V:0.2'),
         'Authors: {0}'.format(' Ashley Babjac and Zoe Babyar'),
         PYGAMEMENU_TEXT_NEWLINE,
         'GitHub Repo {0}'.format(" github.com/ababjac/project_final")]
COLOR_BACKGROUND = (210, 210, 210)
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_PURPLE = (67,6,71)
COLOR_BLUE = (32,147,150)
COLOR_BURG = (129,11,22)
FPS = 60.0
MENU_BACKGROUND_COLOR = (11, 129, 118) #teal
WINDOW_SIZE = (800, 600)

#init PyGame
pygame.init()

#------------------------------------------------------------------------------
#source for sounds https://freewavesamples.com/
#sound constants
HIHAT = [pygame.mixer.Sound('../sounds2/Closed-Hi-Hat-1.wav'),
         pygame.mixer.Sound('../sounds2/Kawai-K1r-Closed-Hi-Hat.wav'),
         pygame.mixer.Sound('../sounds2/Kawai-K1r-Closed-Hi-Hat.wav'),
         pygame.mixer.Sound('../sounds2/Korg-M1-Open-Hi-Hat.wav'),
         pygame.mixer.Sound('../sounds2/Korg-N1R-Pedal-Hi-Hat.wav'),
         pygame.mixer.Sound('../sounds2/Korg-NS5R-Power-Closed-Hi-Hat.wav')]

DRUM = [pygame.mixer.Sound('../sounds2/Bass-Drum-1.wav'),
          pygame.mixer.Sound('../sounds2/Bass-Drum-2.wav'),
          pygame.mixer.Sound('../sounds2/Bass-Drum-3.wav'),
          pygame.mixer.Sound('../sounds2/Deep-Kick.wav'),
          pygame.mixer.Sound('../sounds2/Dry-Kick.wav')]

SNARE = [pygame.mixer.Sound('../sounds2/E-Mu-Proteus-FX-Wacky-Snare.wav'),
         pygame.mixer.Sound('../sounds2/Ensoniq-ESQ-1-Snare.wav'),
         pygame.mixer.Sound('../sounds2/Ensoniq-VFX-SD-Snare.wav'),
         pygame.mixer.Sound('../sounds2/Hip-Hop-Snare-1.wav'),
         pygame.mixer.Sound('../sounds2/Kawai-K11-Bob-Snare.wav')]

TOM = [pygame.mixer.Sound('../sounds2/Electro-Tom.wav'),
       pygame.mixer.Sound('../sounds2/Ensoniq-ESQ-1-Hi-Synth-Tom.wav'),
       pygame.mixer.Sound('../sounds2/Floor-Tom-1.wav'),
       pygame.mixer.Sound('../sounds2/Hi-Tom-1.wav'),
       pygame.mixer.Sound('../sounds2/Kawai-K5000W-Melo-Tom.wav')]

CLAP = [pygame.mixer.Sound('../sounds2/Clap-1.wav'),
        pygame.mixer.Sound('../sounds2/E-Mu-Proteus-FX-Wacky-Crash-Cymbal.wav'),
        pygame.mixer.Sound('../sounds2/Boom-Kick.wav')]

# -----------------------------------------------------------------------------
# Init pygame environement
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Create pygame screen and objects
surface = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('UTK Drum Machine V1.2')
clock = pygame.time.Clock()
dt = 1 / FPS

I=[0] #helps in choose_sound
PAUSE  = False
BPM = [80]
SOUND = [HIHAT[0]]*8 #number of channels defualt supported
BARS = [4]
SIGNATURE = [4]

SECS = 60 / BPM[0]
LAST = 0
NOW = 0

# -----------------------------------------------------------------------------
#GAME LOGIC
def choose_bpm(t):
    print ('Selected beats: {0}'.format(t))
    BPM[0] = t
    SECS = 60 / BPM[0]

def choose_sound(s):
    print ('changing to sound: {0}'.format(s))
    SOUND[I[0]] = s
    I[0] += 1

def choose_bars(b):
    print ('selected bars: {0}'.format(b))
    BARS[0] = b

def choose_signature(s):
    print ('selected signature: {0}'.format(s))
    SIGNATURE[0] = s

#def signature_3():
#    while(True):
#        NOW = pygame.time.get_ticks()
#        if(NOW - LAST == SECS[0]):
#            print("playing 1\n")
#            pygame.mixer.find_channel(True).play(sound[0])
#            pygame.time.wait(SECS[0])
#
#            if(i >= 1):
#                print("playing 2\n")
#                pygame.mixer.find_channel(True).play(SOUND[1])
#            pygame.time.wait(SECS[0])
#
#            if(i >= 2):
#                print("playing 3\n")
#                pygame.mixer.find_channel(True).play(SOUND[2])
#            pygame.time.wait(SECS[0])
#
#            LAST = pygame.time.get_ticks()

#def signature_4():
#    while(True):
#        NOW = pygame.time.get_ticks()
#        if(NOW - LAST >= SECS[0]):
#            print("playing 1\n")
#            pygame.mixer.find_channel(True).play(SOUND[0])
#            pygame.time.wait(SECS[0])
#
#            if(i >= 1):
#                print("playing 2\n")
#                pygame.mixer.find_channel(True).play(SOUND[1])
#            pygame.time.wait(SECS[0])
#
#            if(i >= 2):
#                print("playing 3\n")
#                pygame.mixer.find_channel(True).play(SOUND[2])
#            pygame.time.wait(SECS[0])
#
#            if(i >= 3):
#                print("playing 4\n")
#                pygame.mixer.find_channel(True).play(SOUND[3])
#            pygame.time.wait(SECS[0])
#
#            LAST = pygame.time.get_ticks()

#------------------------------------------------------------------------------
def play_function(self, timing, sound):
    print('playing sounds\n')

    if(PAUSE == True):
        pygame.mixer.unpause()
    else:
        LAST = pygame.time.get_ticks()

        while(True):
            NOW = pygame.time.get_ticks()
            if(NOW - LAST >= SECS):
                print("playing 1\n")
                pygame.mixer.find_channel(True).play(SOUND[0])
                pygame.time.wait(int(SECS))

                if(I[0] >= 1):
                    print("playing 2\n")
                    pygame.mixer.find_channel(True).play(SOUND[1])
                    pygame.time.wait(int(SECS))

                if(I[0] >= 2):
                    print("playing 3\n")
                    pygame.mixer.find_channel(True).play(SOUND[2])
                pygame.time.wait(int(SECS))

                if(SIGNATURE[0] == 4):
                    if(I[0] >= 3):
                        print("playing 4\n")
                        pygame.mixer.find_channel(True).play(SOUND[3])
                    pygame.time.wait(int(SECS))

            LAST = pygame.time.get_ticks()
#-------------------------------------------------------------------------------
#stops and pauses
def stop_function(timing, sound):
    print('stopping sounds\n')
    pygame.mixer.stop()

def pause_function(self, timing, sound):
    print('pausing sounds\n')
    pygame.mixer.pause()
    PAUSE = True

#-------------------------------------------------------------------------------
#fills background
def main_background():
    surface.fill(COLOR_BACKGROUND)

#------------------------------------------------------------------------------
#PLAY MENU
play_menu = pygameMenu.Menu(surface,
                        bgfun=main_background,
                        font=pygameMenu.fonts.FONT_BEBAS,
                        font_color=COLOR_BLACK,
                        color_selected=COLOR_WHITE,
                        font_size=30,
                        menu_alpha=100,
                        menu_color=COLOR_BLUE,
                        menu_color_title=COLOR_WHITE,
                        menu_height=int(WINDOW_SIZE[1] * 0.5),
                        menu_width=int(WINDOW_SIZE[0]),
                        option_shadow=False,
                        title='Game Options',
                        window_height=WINDOW_SIZE[1],
                        window_width=WINDOW_SIZE[0]
                        )

play_menu.add_option('Start', play_function, BPM, SOUND[0],
                 pygame.font.Font(pygameMenu.fonts.FONT_FRANCHISE, 30))
play_menu.add_option('Pause', pause_function, BPM, SOUND[0],
                 pygame.font.Font(pygameMenu.fonts.FONT_FRANCHISE, 30))
play_menu.add_option('Stop', stop_function, BPM, SOUND[0])
play_menu.add_option('Add Another Sound', PYGAME_MENU_BACK)
play_menu.add_option('Exit', PYGAME_MENU_EXIT)

#------------------------------------------------------------------------------
#SOUND_TYPE MENU
sound_type_menu = pygameMenu.Menu(surface,
                        bgfun=main_background,
                        color_selected=COLOR_WHITE,
                        font=pygameMenu.fonts.FONT_BEBAS,
                        font_color=COLOR_BLACK,
                        font_size=30,
                        menu_alpha=100,
                        menu_color=MENU_BACKGROUND_COLOR,
                        menu_color_title=COLOR_PURPLE,
                        menu_height=int(WINDOW_SIZE[1] * 0.8),
                        menu_width=int(WINDOW_SIZE[0]),
                        onclose=PYGAME_MENU_DISABLE_CLOSE,
                        option_shadow=False,
                        title='Sound Options',
                        window_height=WINDOW_SIZE[1],
                        window_width=WINDOW_SIZE[0]
                        )

sound_type_menu.add_option('Next', play_menu, BPM, SOUND[0],
                  pygame.font.Font(pygameMenu.fonts.FONT_FRANCHISE, 30))
sound_type_menu.add_selector('Hi-Hats', [('Closed Hi-Hat', HIHAT[0]), ('Kawai Hi-Hat', HIHAT[1]),
                            ('Open Hi-Hat', HIHAT[2]), ('Pedal Hi-Hat', HIHAT[3]),
                            ('Power Hi-Hat', HIHAT[4])],
                  onreturn=choose_sound,
                  onchange=None)
sound_type_menu.add_selector('Drums', [('Bass Drum 1', DRUM[0]), ('Bass Drum 2', DRUM[1]),
                            ('Bass Drum 3', DRUM[2]), ('Deep Kick', DRUM[3]), ('Dry Kick', DRUM[4])],
                  onreturn=choose_sound,
                  onchange=None)
sound_type_menu.add_selector('Snares', [('Wacky Snare', SNARE[0]), ('ESQ Snare', SNARE[1]),
                            ('VFX Snare', SNARE[2]), ('Hip-Hop Snare', SNARE[3]),
                            ('Kawai Snare', SNARE[4])],
                  onreturn=choose_sound,
                  onchange=None)
sound_type_menu.add_selector('Toms', [('Electro Tom', TOM[0]), ('ESQ Synth Tom', TOM[1]),
                            ('Floor Tom', TOM[2]), ('Hi-Tom', TOM[3]), ('Kawai Melo Tom', TOM[4])],
                  onreturn=choose_sound,
                  onchange=None)
sound_type_menu.add_selector('Crashes', [('Clap', CLAP[0]), ('Wacky Crash Cymbal', CLAP[1]),
                            ('Boom', CLAP[2])],
                  onreturn=choose_sound,
                  onchange=None)

#------------------------------------------------------------------------------
#runs next set of menus
def menu_helper(self):
    while True:

        # Tick
        clock.tick(60)

        # Application events
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                exit()

            # sound type menu
            sound_type_menu.mainloop(events)

        # Flip surface
        pygame.display.flip()

#------------------------------------------------------------------------------
#TIMING MENU
timing_menu = pygameMenu.Menu(surface,
                        bgfun=main_background,
                        color_selected=COLOR_WHITE,
                        font=pygameMenu.fonts.FONT_BEBAS,
                        font_color=COLOR_BLACK,
                        font_size=30,
                        menu_alpha=100,
                        menu_color=MENU_BACKGROUND_COLOR,
                        menu_color_title=COLOR_PURPLE,
                        menu_height=int(WINDOW_SIZE[1] * 0.8),
                        menu_width=int(WINDOW_SIZE[0]),
                        onclose=PYGAME_MENU_DISABLE_CLOSE,
                        option_shadow=False,
                        title='Timing Options',
                        window_height=WINDOW_SIZE[1],
                        window_width=WINDOW_SIZE[0]
                        )

timing_menu.add_option('Next', menu_helper,
                  pygame.font.Font(pygameMenu.fonts.FONT_FRANCHISE, 30))
timing_menu.add_selector('Change BPM', [('60', 60), ('70', 70), ('80', 80), ('90', 90), ('100', 100)],
                   onreturn=None,
                   onchange=choose_bpm)
timing_menu.add_selector('Choose Number of Bars', [('1', 1), ('2', 2), ('3', 3), ('4', 4)],
                   onreturn=None,
                   onchange=choose_bars)
timing_menu.add_selector('Choose Time Signature', [('3/4', 3), ('4/4', 4)],
                   onreturn=None,
                   onchange=choose_signature)
timing_menu.add_option('Return to main menu', PYGAME_MENU_BACK)

#-------------------------------------------------------------------------------
# ABOUT MENU
about_menu = pygameMenu.TextMenu(surface,
                                 bgfun=main_background,
                                 color_selected=COLOR_WHITE,
                                 font=pygameMenu.fonts.FONT_BEBAS,
                                 font_color=COLOR_BLACK,
                                 font_size_title=30,
                                 font_title=pygameMenu.fonts.FONT_8BIT,
                                 menu_color=MENU_BACKGROUND_COLOR,
                                 menu_color_title=COLOR_WHITE,
                                 menu_height=int(WINDOW_SIZE[1] * 0.8),
                                 menu_width=int(WINDOW_SIZE[0] * 0.8),
                                 onclose=PYGAME_MENU_DISABLE_CLOSE,
                                 option_shadow=False,
                                 text_color=COLOR_BLACK,
                                 text_fontsize=20,
                                 title='About',
                                 window_height=WINDOW_SIZE[1],
                                 window_width=WINDOW_SIZE[0]
                                 )
for m in ABOUT:
    about_menu.add_line(m)

about_menu.add_line(PYGAMEMENU_TEXT_NEWLINE)
about_menu.add_option('Return to menu', PYGAME_MENU_BACK)

#------------------------------------------------------------------------------
# MAIN MENU
main_menu = pygameMenu.Menu(surface,
                            bgfun=main_background,
                            color_selected=COLOR_WHITE,
                            font=pygameMenu.fonts.FONT_BEBAS,
                            font_color=COLOR_BLACK,
                            font_size=30,
                            menu_alpha=100,
                            menu_color=MENU_BACKGROUND_COLOR,
                            menu_color_title=COLOR_BURG,
                            menu_height=int(WINDOW_SIZE[1] * 0.9),
                            menu_width=int(WINDOW_SIZE[0] * 0.9),
                            onclose=PYGAME_MENU_DISABLE_CLOSE,
                            option_shadow=False,
                            title='Main menu',
                            window_height=WINDOW_SIZE[1],
                            window_width=WINDOW_SIZE[0]
                            )
main_menu.add_option('Lets Get Started!', timing_menu)
main_menu.add_option('About', about_menu)
main_menu.add_option('Quit', PYGAME_MENU_EXIT)


# -----------------------------------------------------------------------------
# MAIN LOOP
# run through menu's to choose options
while True:

    # Tick
    clock.tick(60)

    # Application events
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            exit()

    # Main menu
    main_menu.mainloop(events)

    # Flip surface
    pygame.display.flip()

pygame.quit()
quit()
