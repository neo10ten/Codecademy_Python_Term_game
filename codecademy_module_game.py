# A Journey Through - Simulated Existence, or Not?
# Explore the Order of the Elementis to find out!

# Import necessary py-modules and libraries:

import random


# Create class for player to use in game:

class Player:
    def __init__(self, player):
        self.name = ''
        self.life_container = 0
        self.item_container = []
        self.player = player
        Player.player_name_input()

    def __repr__(self):
        print('Well done, you made it this far. Now finish the bloody code!')
    def player_name_input():
        print ('What is your name?')
        name_input = input ('Type your name and press enter: ')
        while name_input != '':
            Player.name.append(name_input)
            print(Player())
            Game.journey_trigger()
        else:
            name_input = input ('You must speak to be heard. Tell me your name: ')

# Create class for game - will contain main bulk of code:

class Game:
    player_choice = ''
    def __init__(self):
        Game.journey_trigger(Player.name)

    def game_init():
        player_input = input (start_command)
        while player_input != 'start':
            player_input = input (start_command)
        else:
            player = 'Player 1'
            Player(player)

    def journey_trigger(self):
        print ('Now {name}, it is time to make your choice.'.format(name = self.name))
        print ( '''
            These are the Elementis of the Journey:
            - Cosmos
            - Flame
            - Aqua
            - Mystic
            - Chaos
            - Order
            You must make a selection for your own journey to begin.
            Choose wisely, it could effect your entire existence...''')
        choice = input ('What do you choose? ')
        while choice not in elementis_list:
            choice = input ('You did not select one of the Elemetis. Choose again: ')
        else:
            Player.start_journey(choice)
            
    def start_journey(self):
        print('''
        Player {name} has decided to start the Journey with {choice}.
        We will now begin the journey.'''.format(name = self.name, choice = self.choice))
        answer = input ('Are you ready, {name}? Y/N'.format(name = self.name))
        while answer != 'y' and answer != 'n':
            answer = input ('Are you ready, {name}? Y/N'.format(name = self.name))
        if answer == 'y':
            Player.question_for_answer()
        else:
            print('Fret not. When you are ready, return to start your Journey Through')
    def question_for_answer(self):
        pass

# Create class for item storage for player during game:

class Item_container:
    def __init__(self):
        self.container_name = Player.name+'\'s Item Container'
        self.items = []

# Create life container to hold life object for each player life during game:

class Life_container:
    pass


# Elemntis list and dict create:

elementis_list = ['cosmos', 'flame', 'aqua', 'mystic', 'chaos', 'order']

elementis_dict = {
              'cosmos' : {'question' : 'Using modern sciences, is it possible to quantify the Cosmos completely?',
                             'answers' : {1 : 'Yes, with the right instruments',
                                          2 : 'Only partially',
                                          3 : 'Impossible to quantify limitless',
                                          4 : 'No, but one day'},
                             'correct answer': '3',
                             'reward' : 'An Origin of Journey'},
              'flame' : {'question' : 'Can one find the source of the Healing Flame',
                         'answers' : {1 : 'Yes, by exploring the cosmos',
                                      2 : 'It is not found, but achieved',
                                      3 : 'No',
                                      4 : 'Yes, can be created by craftsman'},
                         'correct answer' : '2',
                         'reward' : 'Ember of Burning Spirit'},
              'aqua' : {'question' : 'In the Waters of Forever, how does one survive?',
                        'answers' : {1 : 'No survival, you will become one with it',
                                     2 : 'Learn to breathe inside',
                                     3 : 'Drink it all',
                                     4 : 'Hold your breath'},
                        'correct answer' : '1',
                        'reward' : 'Drink of the One True'},
              'mystic' : {'question' : 'In the Arcane, is there any limitation true?',
                          'answers' : {1 : 'Yes, the Rule of Law',
                                       2 : 'No, not according to the rules in place',
                                       3 : 'Yes, spells contained in spellbooks',
                                       4 : 'One can never be restricted if one\'s mind is endless'},
                          'correct answer' : '4',
                          'reward' : 'Enchantment of Expanse'},
              'chaos' : {'question' : 'Was there ever truly order in the Expanse?',
                         'answers' : {1 : 'Yes, all things have order',
                                      2 : 'No, the ever changing cannot be ordered',
                                      3 : 'No, we just believe there is',
                                      4 : 'Yes, but only in the beginning'},
                         'correct answer' : '2',
                         'reward' : 'Flow of Chaos Arc'},
              'order' : {'question' : 'All things have order, whilst nothing has none. Does any One Being see the Truth?',
                         'answers' : {1 : 'Yes, everyone can if thhey look properly',
                                      2 : 'No, how can one see the intangible?',
                                      3 : 'Yes, make peace with Chaos to see Truth',
                                      4 : 'Nothing ever truly exists to be ordered'},
                         'correct answer' : '4',
                         'reward' : 'Sight of Ordered Emptiness'}
                    }

# Base code for dict quick create template - copy and paste.
base_code = {'question' : '', 'answers' : {1 : '', 2 : '', 3 : '', 4 : ''}, 'correct answer' : '', 'reward' : ''}

# Global variables for setup:
start_command = 'Type "start" to begin a new game: '

# Test run through using new player instance:
Game.game_init()


