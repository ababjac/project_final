# Import pygame and libraries
from pygame.locals import *
from random import randrange
import os
import pygame

# Import pygameMenu
import pygameMenu
from pygameMenu.locals import *

#menu constants
ABOUT = ['PygameMenu {0}'.format(' UTK Drum Machine V:0.1'),
         'Authors: {0}'.format(' Ashley Babjac and Zoe Babyar'),
         PYGAMEMENU_TEXT_NEWLINE,
         'GitHub Repo {0}'.format(" github.com/ababjac/project_final")]
#COLOR_BACKGROUND = (224, 224, 224)
COLOR_BACKGROUND = (238,238,238)
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
FPS = 60.0
MENU_BACKGROUND_COLOR = (11,129,118)
#MENU_BACKGROUND_COLOR = (0, 142, 100)
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
#os.environ['SDL_VIDEO_CENTERED'] = '1'

# Create pygame screen and objects
surface = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('UTK Drum Machine V0.1')
clock = pygame.time.Clock()
dt = 1 / FPS

TIMING = [80]
SOUND = ['HI-HAT']


# -----------------------------------------------------------------------------
#GAME LOGIC
def change_timing(t):
    print ('Selected beats: {0}'.format(t))
    TIMING[0] = t

def choose_sound(s):
    print ('selected sound: {0}'.format(s))
    SOUND[0] = s

def play_function(self, timing, sound):
    print('playing sounds\n')

def stop_function(self, timing, sound):
    print('stopping sounds\n')

#def play_function(timing, font):

    #difficulty = difficulty[0]
    #assert isinstance(difficulty, str)

    #if difficulty == 'EASY':
    #    f = font.render('Playing as baby', 1, COLOR_WHITE)
    #elif difficulty == 'MEDIUM':
    #    f = font.render('Playing as normie', 1, COLOR_WHITE)
    #elif difficulty == 'HARD':
    #    f = font.render('Playing as god', 1, COLOR_WHITE)
    #else:
    #    raise Exception('Unknown difficulty {0}'.format(difficulty))

    # Draw random color and text
    #bg_color = random_color()
    #f_width = f.get_size()[0]

    # Reset main menu and disable
    # You also can set another menu, like a 'pause menu', or just use the same
    # main_menu as the menu that will check all your input.
    #main_menu.disable()
    #main_menu.reset(1)

    #while True:

        # Clock tick
        #clock.tick(60)

        # Application events
        #playevents = pygame.event.get()
        #for e in playevents:
        #    if e.type == QUIT:
        #        exit()
        #    elif e.type == KEYDOWN:
        #        if e.key == K_ESCAPE and main_menu.is_disabled():
        #            main_menu.enable()

                    # Quit this function, then skip to loop of main-menu on line 217
        #            return

        # Pass events to main_menu
        #main_menu.mainloop(playevents)

        # Continue playing
        #surface.fill(bg_color)
        #surface.blit(f, ((WINDOW_SIZE[0] - f_width) / 2, WINDOW_SIZE[1] / 2))
        #pygame.display.flip()

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
                        menu_height=int(WINDOW_SIZE[1] * 0.5),
                        menu_width=int(WINDOW_SIZE[0]),
                        onclose=PYGAME_MENU_DISABLE_CLOSE,
                        option_shadow=False,
                        title='Game Options',
                        window_height=WINDOW_SIZE[1],
                        window_width=WINDOW_SIZE[0]
                        )

game_menu.add_option('Start', play_function, TIMING, SOUND,
                 pygame.font.Font(pygameMenu.fonts.FONT_FRANCHISE, 30))
game_menu.add_option('Stop/Pause', stop_function, TIMING, SOUND,
                 pygame.font.Font(pygameMenu.fonts.FONT_FRANCHISE, 30))
game_menu.add_selector('Choose sound', [('hi-hat', HIHAT), ('kick', KICK), ('snare', SNARE), ('rimshot', RIMSHOT), ('shaker', SHAKER)],
                   onreturn=None,
                   onchange=choose_sound)
game_menu.add_selector('Change timing', [('80', 80), ('90', 90), ('100', 100), ('110', 110), ('120', 120)],
                   onreturn=None,
                   onchange=change_timing)
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
