# Import pygame and libraries
from pygame.locals import *
import sys, os
import pygame

# Import pygameMenu
import pygameMenu
from pygameMenu.locals import *

#-------------------------------------------------------------------------------
#menu constants
ABOUT = ['PygameMenu {0}'.format(' UTK Drum Machine V:2.0'),
         'Authors: {0}'.format(' Ashley Babjac and Zoe Babyar'),
         PYGAMEMENU_TEXT_NEWLINE,
         'GitHub Repo {0}'.format(" github.com/ababjac/project_final")]

#color constants
COLOR_BACKGROUND = (210, 210, 210)
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_PURPLE = (67,6,71)
COLOR_BLUE = (32,147,150)
COLOR_BURG = (129,11,22)
COLOR_TEAL = (11, 129, 118)
COLOR_DARK_TEAL = (10, 71, 65)

#window constant
WINDOW_SIZE = (1150, 525)

#------------------------------------------------------------------------------
#init PyGame
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()

# Init pygame environement
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Create pygame screen and objects
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('UTK Drum Machine V2.0')
clock = pygame.time.Clock()

#classes modified from https://pythonprogramming.net/pygame-python-3-part-1-intro/
#-------------------------------------------------------------------------------
#BUTTON CLASS
#helps streamline placing buttons
class button(object):
    #initialize buttons (constructor)
    def __init__(self, text, x,y,w,h, pushed, color0, color1, border = 0):
        self.x, self.y, self.w, self.h = x, y, w, h
        # x, y is coords of top left position of rectangle, and w, h, is width height of rect.
        self.pushed = pushed
        self.border = border  # if border = 0 then rectangle is filled, 1 is not filled
        self.color0 = color0  # unpressed color
        self.color1 = color1  # pressed color
        self.coords = self.x, self.y
        Rect1 = (self.x, self.y, self.w, self.h)
        self.Return_rect = pygame.draw.rect(screen, (255, 0, 0), Rect1, self.border)
        font = pygame.font.SysFont("reesansbold.ttf", 14) #use system font
        width, height = font.size(text)
        self.txt = font.render(text, True, (0, 0, 0))
        xoffset = (self.w-width) // 2 #offset border
        yoffset = (self.h-height) // 2
        self.coords = self.x + xoffset, self.y + yoffset

    #draw the button to the screen
    def draw(self, screen):
        Rect = (self.x, self.y, self.w, self.h)
        if self.pushed: #draw with pressed color
            pygame.draw.rect(screen, self.color1, Rect, self.border)
            screen.blit(self.txt, self.coords)
        else: #otherwise button is unpressed
            pygame.draw.rect(screen, self.color0, Rect, self.border)
            screen.blit(self.txt, self.coords)

    #allows for pushing of buttons
    def push(self):
        if self.pushed == False: #press and release
            self.pushed = True
        else:
            self.pushed = False
        self.draw(screen)

    #returns if button is pressed
    def is_pushed(self):
        return self.pushed

    #helps with button press
    def button_rect(self):
        return self.Return_rect

#-------------------------------------------------------------------------------
#TEXT CLASS
#creates "buttons" formatted on screen with centered text
class CenteredText(object):

    #centered text button constructor
    def __init__(self, text, font_size, x,y,w,h, color, border = 0):
        self.x, self.y, self.w, self.h = x, y, w, h
        # x, y is coords of top left position of rectangle, and w, h, is width height of rect
        self.border = border  # if border = 0 then rectangle is filled, 1 is not filled
        self.color = color
        self.font_size = font_size
        font = pygame.font.SysFont("reesansbold.ttf", self.font_size)
        width, height = font.size(text)
        xoffset = (self.w-width) // 2 #offset rectangles
        yoffset = (self.h-height) // 2
        self.coords = self.x + xoffset, self.y + yoffset
        self.txt = font.render(text, True, color)

    #draw a button to the screen
    def draw(self, screen):
        Rect = (self.x, self.y, self.w, self.h)
        pygame.draw.rect(screen, COLOR_BLACK, Rect, self.border)
        screen.blit(self.txt, self.coords)

    #return the rectangle that will act as border for buttons
    def get_border_rect(self):
        Rect1 = (self.x, self.y, self.w, self.h)
        R = pygame.draw.rect(screen, COLOR_BLACK, Rect1, self.border)
        return R

    #helper
    def get_text(self):
        return self.text

#------------------------------------------------------------------------------
#SOUND CLASS
#allows for easy playing of pyGame audio files
class sample(object):

    #constructor for sounds
    def __init__(self, file):
        self.file = pygame.mixer.Sound(file)

    #play the sound
    def play_sound(self):
        self.file.play()

#-------------------------------------------------------------------------------
#fills background
def main_background():
    screen.fill(COLOR_BACKGROUND)

#-------------------------------------------------------------------------------
button_dict = {}
border_dict = {}

#initialize drum buttons
button_number = 0
for x in range(182, 1142, 30):
    for y in range(120, 460, 30):
        button_dict['button%s' % button_number] = button('', x, y, 20, 20, False, COLOR_BLUE, COLOR_DARK_TEAL, 0)
        border_dict['border%s' % button_number] = button('', x, y, 19, 19, False, COLOR_BURG, COLOR_BURG, 2)
        button_number += 1

#initialize buttons for timing
button_dict['start_button'] = button('Play/Stop', 178, 25, 120, 79, False, COLOR_BURG, COLOR_PURPLE, 0)
button_dict['Clear'] = button('Clear', 897, 25, 120, 38, False, COLOR_BURG, COLOR_PURPLE, 0)
button_dict['Return'] = button('Return to Main Menu', 897, 65, 120, 38, False, COLOR_BURG, COLOR_PURPLE, 0)
button_dict['4'] = button('1/4', 617, 50, 50, 50, False, COLOR_BURG, COLOR_PURPLE, 0) #422
button_dict['8'] = button('1/8', 677, 50, 50, 50, False, COLOR_BURG, COLOR_PURPLE, 0)
button_dict['16'] = button('1/16', 737, 50, 50, 50, False, COLOR_BURG, COLOR_PURPLE, 0)
button_dict['32'] = button('1/32', 797, 50, 50, 50, False, COLOR_BURG, COLOR_PURPLE, 0)
button_dict['60'] = button('60', 345, 50, 50, 50, False, COLOR_BURG, COLOR_PURPLE, 0) #180
button_dict['80'] = button('80', 405, 50, 50, 50, False, COLOR_BURG, COLOR_PURPLE, 0)
button_dict['100'] = button('100', 465, 50, 50, 50, False, COLOR_BURG, COLOR_PURPLE, 0)
button_dict['120'] = button('120', 525, 50, 50, 50, False, COLOR_BURG, COLOR_PURPLE, 0)

#initialize sounds
sample_dict = {}
for i in range(0,32):
    sample_dict['button%s' %(1+(i*12)-1)] = sample('../sounds2/Bass-Drum-1.wav')
    sample_dict['button%s' %(2+(i*12)-1)] = sample('../sounds2/Hip-Hop-Snare-1.wav')
    sample_dict['button%s' %(3+(i*12)-1)] = sample('../sounds2/Electro-Tom.wav')
    sample_dict['button%s' %(4+(i*12)-1)] = sample('../sounds2/Ensoniq-ESQ-1-Hi-Synth-Tom.wav')
    sample_dict['button%s' %(5+(i*12)-1)] = sample('../sounds2/E-Mu-Proteus-FX-Wacky-Crash-Cymbal.wav')
    sample_dict['button%s' %(6+(i*12)-1)] = sample('../sounds2/Clap-1.wav')
    sample_dict['button%s' %(7+(i*12)-1)] = sample('../sounds2/Korg-M1-Open-Hi-Hat.wav')
    sample_dict['button%s' %(8+(i*12)-1)] = sample('../sounds2/Korg-NS5R-Power-Closed-Hi-Hat.wav')
    sample_dict['button%s' %(9+(i*12)-1)] = sample('../sounds2/Korg-N1R-Pedal-Hi-Hat.wav')
    sample_dict['button%s' %(10+(i*12)-1)] = sample('../sounds2/Bass-Drum-2.wav')
    sample_dict['button%s' %(11+(i*12)-1)] = sample('../sounds2/Dry-Kick.wav')
    sample_dict['button%s' %(12+(i*12)-1)] = sample('../sounds2/Deep-Kick.wav')

#initialize borders
step_border_dict = {}
step_border_number = 0
for x in range (177, 1080, 120):
    step_border_dict['step_border%s' % step_border_number] = CenteredText('', 14, x , 115, 120, 360, COLOR_BLACK, 1)
    step_border_number += 1

#initialize labels for drum machine
label_dict = {}
label_dict['BPM'] = CenteredText('BPM', 20, 341, 25, 240, 20, COLOR_BLACK, 1) #176
label_dict['Timing'] = CenteredText('Timing', 20, 612, 25, 240, 20, COLOR_BLACK, 1) #417
label_dict['border1'] = CenteredText('', 20, 612, 46, 240, 59, COLOR_BLACK, 1)
label_dict['border2'] = CenteredText('', 20, 341, 46, 240, 59, COLOR_BLACK, 1)
label_dict['By'] = CenteredText('By: Ashley Babjac and Zoe Babyar', 17, 50, 485, 1088, 22, COLOR_BLACK, 1)
label_dict['Bass_Drum1'] =  CenteredText('Bass Drum 1', 14, 50, 120, 120, 20, COLOR_PURPLE, 1)
label_dict['Bass Drum2'] = CenteredText('Bass Drum 2', 14, 50, 150, 120, 20, COLOR_PURPLE, 1)
label_dict['Tom1'] = CenteredText('Electro Tom', 14, 50, 180, 120, 20, COLOR_PURPLE, 1)
label_dict['Tom2'] = CenteredText('Synth Tom', 14, 50, 210, 120, 20, COLOR_PURPLE, 1)
label_dict['Cymbal'] = CenteredText('Cymbal', 14, 50, 240, 120, 20, COLOR_PURPLE, 1)
label_dict['Clap'] = CenteredText('Clap', 14, 50, 270, 120, 20, COLOR_PURPLE, 1)
label_dict['Hi Hat1'] = CenteredText('Open Hi Hat', 14, 50, 300, 120, 20, COLOR_PURPLE, 1)
label_dict['Hi Hat2'] = CenteredText('Closed Hi-Hat', 14, 50, 330, 120, 20, COLOR_PURPLE, 1)
label_dict['Hi Hat3'] = CenteredText('Pedal Hi-Hat', 14, 50, 360, 120, 20, COLOR_PURPLE, 1)
label_dict['Snare'] = CenteredText('Hip-Hop Snare', 14, 50, 390, 120, 20, COLOR_PURPLE, 1)
label_dict['DryKick'] = CenteredText('Dry Kick', 14, 50, 420, 120, 20, COLOR_PURPLE, 1)
label_dict['DeepKick'] = CenteredText('Deep Kick', 14, 50, 450, 120, 20, COLOR_PURPLE, 1)

#-------------------------------------------------------------------------------
#helper function to clear and stop all sounds currently selected
def clear(sound_queue_dict):
    if button_dict['Clear'].is_pushed():
        for q in range (0, 384):
            q_str = (str(q))
            if button_dict['button%s' % q_str].is_pushed():
                button_dict['button%s' % q_str].push()
                button_dict['button%s' % q_str].draw(screen)
                if 'button%s' % q_str in sound_queue_dict:
                     del sound_queue_dict['button%s' % q_str]
        button_dict['Clear'].push()
        button_dict['Clear'].draw(screen)

#-------------------------------------------------------------------------------
#returns the user to the main menu
def return_to_main(sound_queue_dict):
    clear(sound_queue_dict)

    #turn off sounds
    for i in button_dict:
        if button_dict[i].is_pushed():
            button_dict[i].push()

    main_loop()

#-------------------------------------------------------------------------------
#helper function to set up screen
def screen_setup():
    for k in step_border_dict:
        step_border_dict[k].draw(screen)

    for k in button_dict:
         button_dict[k].draw(screen)

    for k in label_dict:
        label_dict[k].draw(screen)

#-------------------------------------------------------------------------------
#helper function to check and turn off buttons
def turn_off(k):
    if button_dict[k].is_pushed():
        button_dict[k].push()
        button_dict[k].draw(screen)

#-------------------------------------------------------------------------------
#helper function to update sound buttons
def update_sound_buttons(sound_queue_dict, mouse_pos):
    for k in button_dict:
        if button_dict[k].button_rect().collidepoint(mouse_pos):
            button_dict[k].push()
            button_dict[k].draw(screen)

            if button_dict[k].is_pushed():
                sound_queue_dict[k] = 0
            else:
                del sound_queue_dict[k]

#insporation for drum machine design comes from https://drumbit.app/
#-------------------------------------------------------------------------------
#runs the drum machine
def play_function():
    print('playing sounds\n')

    #set background to grey
    main_background()

    #organize sounds to be played for timing
    sound_queue_dict = {}

    #update screen
    screen_setup()

    #helper constants
    button_counter_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    sound_queue_dict['32'] = 0
    timing_list =  ['4', '8', '16', '32']
    timing_list_copy = ['4', '8', '16', '32']
    bpm_list = ['60', '80', '100', '120']
    bpm_list_copy = ['60', '80', '100', '120']
    BPM = 120
    milliseconds_per_step = 0
    change_timer = True

    #initialize timing buttons on screen
    button_dict['32'].push()
    button_dict['32'].draw(screen)

    button_dict['120'].push()
    button_dict['120'].draw(screen)

    while True: # game loop
         #get the mouse position for button clicks
         mouse_pos = pygame.mouse.get_pos()

         #if the BPM was changed
         if change_timer:
              for x in timing_list:
                  if button_dict[x].is_pushed():
                      x_int = int(x)
                      divisor = x_int // 4
                      BPM_in_milliseconds = 50000 // BPM #update BPM
                      milliseconds_per_step = BPM_in_milliseconds // divisor
              #time the drum beats
              pygame.time.set_timer(pygame.USEREVENT, milliseconds_per_step)
              change_timer = False

         #clear buttons
         clear(sound_queue_dict)

         #go back to main menu
         if button_dict['Return'].is_pushed():
             return_to_main(sound_queue_dict)

         #check user button presses or mouse mvt
         for event in pygame.event.get():
            if event.type == pygame.QUIT:   #allows for user to quit
                pygame.quit() #exit game
                sys.exit()

            #use timer set earlier
            if event.type == pygame.USEREVENT:  #timer
                #update button on screen
                for k in button_dict:
                    button_dict[k].draw(screen)

                #start playing
                if button_dict['start_button'].is_pushed():
                    #draw the borders on current beat
                    for x in button_counter_list:
                        x_str = str(x)
                        border_dict['border%s' % x_str].draw(screen)

                    #check if sound at current beat is in sound queue and play
                    for w in button_counter_list:
                        w_str = str((w))
                        button_str = 'button' + w_str
                        if button_str in sound_queue_dict:
                            sample_dict[button_str].play_sound()

                    #update button counter for next beat
                    next_counter_list = []
                    for x in button_counter_list:
                         x += 12
                         next_counter_list.append(x)
                    button_counter_list = next_counter_list

                    #if we reach the end of the loop start over
                    if button_counter_list[0] > 380:
                         button_counter_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
                else:
                    button_counter_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

            #update pressed button
            if event.type == pygame.MOUSEBUTTONDOWN:
                #button for sounds
                update_sound_buttons(sound_queue_dict, mouse_pos)

                #update button for timing
                for i in timing_list:
                    #find which button is pressed
                    if button_dict[i].button_rect().collidepoint(mouse_pos):
                        timing_list_copy.remove(i)
                        print(i)

                        #turn off all non pressed buttons
                        for l in timing_list_copy:
                            turn_off(l)

                        #update timer
                        change_timer = True
                        timing_list_copy = ['4', '8', '16', '32']

                #update button for bpm
                for i in bpm_list:
                    #find which button is pressed
                    if button_dict[i].button_rect().collidepoint(mouse_pos):
                        bpm_list_copy.remove(i)
                        BPM = int(i)
                        print(BPM)

                        #turn off all non pressed buttons
                        for l in bpm_list_copy:
                            turn_off(l)

                        #update timer
                        change_timer = True
                        bpm_list_copy = ['60', '80', '100', '120']


         #update display
         pygame.display.flip()
         clock.tick(60)

#-------------------------------------------------------------------------------
# ABOUT MENU
about_menu = pygameMenu.TextMenu(screen,
                                 bgfun=main_background,
                                 color_selected=COLOR_WHITE,
                                 font=pygameMenu.fonts.FONT_BEBAS,
                                 font_color=COLOR_BLACK,
                                 font_size_title=30,
                                 font_title=pygameMenu.fonts.FONT_8BIT,
                                 menu_color=COLOR_BLUE,
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
    about_menu.add_line(m) #format

about_menu.add_line(PYGAMEMENU_TEXT_NEWLINE)
about_menu.add_option('Return to menu', PYGAME_MENU_BACK) #go back from submenu

#-------------------------------------------------------------------------------
# MAIN MENU
main_menu = pygameMenu.Menu(screen,
                            bgfun=main_background,
                            color_selected=COLOR_WHITE,
                            font=pygameMenu.fonts.FONT_BEBAS,
                            font_color=COLOR_BLACK,
                            font_size=30,
                            menu_alpha=100,
                            menu_color=COLOR_TEAL,
                            menu_color_title=COLOR_BURG,
                            menu_height=int(WINDOW_SIZE[1] * 0.92),
                            menu_width=int(WINDOW_SIZE[0] * 0.92),
                            onclose=PYGAME_MENU_DISABLE_CLOSE,
                            option_shadow=False,
                            title='Main menu',
                            window_height=WINDOW_SIZE[1],
                            window_width=WINDOW_SIZE[0]
                            )
main_menu.add_option('Begin Drumming!', play_function) #call the drum function
main_menu.add_option('About', about_menu) #author info
main_menu.add_option('Quit', PYGAME_MENU_EXIT) #exit game

#examples of pygameMenu can be found at https://github.com/ppizarror/pygame-menu
# -----------------------------------------------------------------------------
# MAIN LOOP
# run through menu's to choose options
def main_loop():
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

#-------------------------------------------------------------------------------
#MAIN EXECUTION
#run game
main_loop()

#end game
pygame.quit()
sys.exit()
quit()
