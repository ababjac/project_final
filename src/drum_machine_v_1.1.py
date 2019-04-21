# Import pygame and libraries
from pygame.locals import *
from random import randrange
import os
import pygame

# Import pygameMenu
import pygameMenu
from pygameMenu.locals import *

#menu constants
ABOUT = ['PygameMenu {0}'.format(' UTK Drum Machine V:1.1'),
         'Authors: {0}'.format(' Ashley Babjac and Zoe Babyar'),
         PYGAMEMENU_TEXT_NEWLINE,
         'GitHub Repo {0}'.format(" github.com/ababjac/project_final")]
COLOR_BACKGROUND = (224, 224, 224)
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
FPS = 60.0
MENU_BACKGROUND_COLOR = (0, 142, 100)
WINDOW_SIZE = (800, 600)

#init PyGame
pygame.init()

#sound constants
HIHAT = pygame.mixer.Sound('../sounds2/Closed-Hi-Hat-1.wav')
KICK = pygame.mixer.Sound('../sounds2/Bass-Drum-1.wav')
SNARE = pygame.mixer.Sound('../sounds2/E-Mu-Proteus-FX-Wacky-Snare.wav')
RIMSHOT = pygame.mixer.Sound('../sounds2/Electro-Tom.wav')
SHAKER = pygame.mixer.Sound('../sounds2/Clap-1.wav')

# -----------------------------------------------------------------------------
# Init pygame environement
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Create pygame screen and objects
surface = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('UTK Drum Machine V0.1')
clock = pygame.time.Clock()
dt = 1 / FPS

BPM = [80]
SOUND = [HIHAT]
BARS = [4]
SIGNATURE = [4]

SECS = 60 / BPM[0]

# -----------------------------------------------------------------------------
#GAME LOGIC
def choose_bpm(t):
    print ('Selected beats: {0}'.format(t))
    BPM[0] = t
    SECS = 60 / BPM[0]

def choose_sound(s):
    print ('selected sound: {0}'.format(s))
    SOUND[0] = s

def choose_bars(b):
    print ('selected bars: {0}'.format(b))
    BARS[0] = b

def choose_signature(s):
    print ('selected signature: {0}'.format(s))
    SIGNATURE[0] = s

def play_function(self, timing, sound):
    print('playing sounds\n')

    b = 0
    while(b < BARS[0]):
        b = b + 1
        s = 0
        while(s < SIGNATURE[0]):
            pygame.time.wait(int(1000*SECS))
            pygame.mixer.Sound.play(SOUND[0])
            s = s + 1

def stop_function(self, timing, sound):
    print('stopping sounds\n')
    pygame.mixer.Sound.stop(SOUND[0])

def pause_function(self, timing, sound):
    print('pausing sounds\n')
    pygame.mixer.Channel.pause()

#fills background
def main_background():
    surface.fill(COLOR_BACKGROUND)

#------------------------------------------------------------------------------
#GAME MENU
game_menu = pygameMenu.Menu(surface,
                        bgfun=main_background,
                        color_selected=COLOR_WHITE,
                        font=pygameMenu.fonts.FONT_BEBAS,
                        font_color=COLOR_BLACK,
                        font_size=30,
                        menu_alpha=100,
                        menu_color=MENU_BACKGROUND_COLOR,
                        menu_height=int(WINDOW_SIZE[1] * 0.8),
                        menu_width=int(WINDOW_SIZE[0]),
                        onclose=PYGAME_MENU_DISABLE_CLOSE,
                        option_shadow=False,
                        title='Game Options',
                        window_height=WINDOW_SIZE[1],
                        window_width=WINDOW_SIZE[0]
                        )

game_menu.add_option('Start', play_function, BPM, SOUND[0],
                 pygame.font.Font(pygameMenu.fonts.FONT_FRANCHISE, 30))
#pause and stop will not work until we get to channels and chnage timing to work off events
#game_menu.add_option('Pause', pause_function, BPM, SOUND[0],
#                 pygame.font.Font(pygameMenu.fonts.FONT_FRANCHISE, 30))
game_menu.add_option('Stop', stop_function, BPM, SOUND[0],
                 pygame.font.Font(pygameMenu.fonts.FONT_FRANCHISE, 30))
game_menu.add_selector('Choose sound', [('hi-hat', HIHAT), ('kick', KICK), ('snare', SNARE), ('rimshot', RIMSHOT), ('shaker', SHAKER)],
                   onreturn=None,
                   onchange=choose_sound)
game_menu.add_selector('Change BPM', [('80', 80), ('90', 90), ('100', 100), ('110', 110), ('120', 120)],
                   onreturn=None,
                   onchange=choose_bpm)
game_menu.add_selector('Choose Number of Bars', [('1', 1), ('2', 2), ('3', 3), ('4', 4)],
                   onreturn=None,
                   onchange=choose_bars)
game_menu.add_selector('Choose Time Signature', [('2/4', 2), ('3/4', 3), ('4/4', 4)],
                   onreturn=None,
                   onchange=choose_signature)
game_menu.add_option('Return to main menu', PYGAME_MENU_BACK)

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
                            menu_height=int(WINDOW_SIZE[1] * 0.9),
                            menu_width=int(WINDOW_SIZE[0] * 0.9),
                            onclose=PYGAME_MENU_DISABLE_CLOSE,
                            option_shadow=False,
                            title='Main menu',
                            window_height=WINDOW_SIZE[1],
                            window_width=WINDOW_SIZE[0]
                            )
main_menu.add_option('Begin Drumming!', game_menu)
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
