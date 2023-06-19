# A Journey Through - Simulated Existence, or Not?
# Explore the Order of the Elementis to find out!

# Import necessary py-modules and libraries:

import random

def programme_start():
    player_name = ''
    input_start = input ('--> Type "start" and press enter to begin a new game: ')
    while input_start != 'start':
        input_start = input ('--> Type "start" and press enter to begin a new game: ')
    else:
        player_name = input ('--> Now, type your name and press enter to start your Journey: ')
        while player_name == '':
            player_name = input ('--> I said, type your name and press enter to start your Journey: ')
        else:
            return player_name.title()

# Create class for Player in game:

class Player:
    
    def __init__(self, name):
        self.player = 'Player 1'
        self.name = name
        self.life = 10
        self.item_container = []
        
    def __repr__(self):
        return ('''
        --> Welcome {name} to the start of your Journey!
            From here you will be faced with a series of questions that will give you to all Elementis.
            As is the way of All, you shall be given {life} lives and an item container to complete your journey.
            Your item container currently contains {number} items.
            Once it has been loaded with all items of the Elementis, you shall see the Truths of the Elementis.
        '''.format(name = self.name, life = self.life, number = len(self.item_container)))

    def get_reward(self, elementis):
        print('--> Your reward for this is {reward}'.format(reward = elementis.reward))
        player_1.item_container.append(elementis.reward)
        print('--> Your item container now holds {items}.'.format(items = player_1.item_container))
        if len(self.item_container) == 6:
            Game.win_game(self)

    def store_reward(self, elementis_reward):
        self.items.append(elementis_reward)

    def lose_a_life(self):
        self.life -= 1
        if self.life > 0:
            print('''
            --> That is not the correct answer.
                You now have {lives} lives remaining.'''.format(lives = self.life))
        else:
            print('''
            --> GAME OVER!
                Better luck next time =}''')

# Create class for Elementis:
class Elementis:
    
    def __init__(self, elementis):
        self.name = elementis_dict[elementis]['name']
        self.question = elementis_dict[elementis]['question']
        self.answers = elementis_dict[elementis]['answers']
        self.correct_answer = elementis_dict[elementis]['correct answer']
        self.reward = elementis_dict[elementis]['reward']
    
    def __repr__(self):
        return ('--> This Elementis is the {name}.'.format(name = str(self.name)))

# Create class for Game - will contain main bulk of code:

class Game:
    
    def __init__(self, player):
        self.game_elementis_list = ['cosmos', 'flame', 'aqua', 'mystic', 'chaos', 'order']
        self.correctly_answered = []
        print(player)
        Game.game_init(self, player)

    def __repr__(self):
        pass

    def game_init(self, player):
        print('--> Is it time to start?')
        y_n = input ('--> Type Y/N and press enter: ')
        while y_n != 'y' and y_n != 'n':
             y_n = input ('--> Type Y/N and press enter: ')
        if y_n == 'n':
            print ('--> Come back when you are ready, for the Journey.')
            quit()
        else:
            Game.journey_trigger(self, player)

    def journey_trigger(self, player):
        print ('--> {name}, it is time to make your choice.'.format(name = player.name))
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
        start_choice = input ('--> What do you choose? ')
        while start_choice not in elementis_dict.keys():
            start_choice = input ('--> You did not select one of the Elementis. Choose again: ')
        if start_choice == 'cosmos':
            elementis = cosmos
            Game.start_journey(self, player_1, elementis)
        elif start_choice == 'flame':
            elementis = flame
            Game.start_journey(self, player_1, elementis)
        elif start_choice == 'aqua':
            elementis = aqua
            Game.start_journey(self, player_1, elementis)
        elif start_choice == 'mystic':
            elementis = mystic
            Game.start_journey(self, player_1, elementis)
        elif start_choice == 'chaos':
            elementis = chaos
            Game.start_journey(self, player_1, elementis)
        elif start_choice == 'order':
            elementis = order
            Game.start_journey(self, player_1, elementis)
            
    def start_journey(self, player, trigger_choice):
        choice = trigger_choice
        print('''
        --> {name} has decided to start the Journey with {choice}.
            We will now begin the journey.'''.format(name = player.name, choice = choice.name))
        answer = input ('--> Are you ready, {name}? Y/N: '.format(name = player.name))
        while answer != 'y' and answer != 'n':
            answer = input ('--> Are you ready, {name}? Y/N: '.format(name = player.name))
        if answer == 'y':
            Game.ask_question(self, choice)
        else:
            print('--> Fret not. When you are ready, return to start your Journey Through.')
    
    def win_game(player):
        if player_1.life == 10:
            print('''
            --> You have mastered the Elementis and completed your Journey Through.
                Go forth and seek.''')
            quit()
        elif player_1.life == 1:
            print('''
            --> You end your Journey Through with one life only.
                This is the life you should live, now experience the Journey of a Single Life.''')
            quit()
        else:
            print('''
            --> Congratulations you have completed the Journey.
                If ever you are lost, return to A Journey Through again to find a path.''')
            quit()

    def ask_question(self, elementis):
        print ('--> {question}'.format(question = elementis.question))
        print('''
        -->> 1) {answer_1}
        -->> 2) {answer_2}
        -->> 3) {answer_3}
        -->> 4) {answer_4}
        '''.format(answer_1 = elementis.answers[1],
                   answer_2 = elementis.answers[2],
                   answer_3 = elementis.answers[3],
                   answer_4 = elementis.answers[4]))
        answer = input ('--> Choose a number and press enter: ')
        while answer == '':
            answer = input ('--> Choose a number and press enter: ')
        if answer == elementis.correct_answer:
            Game.correct_answer(self, elementis)
        else:
            Game.wrong_answer(self)

    def correct_answer(self, elementis):
        print('--> Well done! You have chosen the correct answer!')
        player_1.get_reward(elementis)
        self.correctly_answered.append(elementis.name)
        self.game_elementis_list.remove(elementis.name.lower())
        next_elementis = Game.elementis_rand_select(self)
        Game.ask_question(self, next_elementis)

    def wrong_answer(self):
        print('--> Oh no! You have chosen the wrong answer!')
        player_1.lose_a_life()
        next_elementis = Game.elementis_rand_select(self)
        Game.ask_question(self, next_elementis)

    def elementis_rand_select(self):
        next_elementis = random.choice(self.game_elementis_list)
        if next_elementis == 'cosmos':
            return cosmos
        elif next_elementis == 'flame':
            return flame
        elif next_elementis == 'aqua':
            return aqua
        elif next_elementis == 'mystic':
            return mystic
        elif next_elementis == 'chaoos':
            return chaos
        elif next_elementis == 'order':
            return order
        

#Creat dict of Elementis for object inits:

elementis_dict = {
                        'cosmos' : {
                            'name' : 'Cosmos',
                            'question' : 'Using modern sciences, is it possible to quantify the Cosmos completely?',
                                    'answers' : {1 : 'Yes, with the right instruments',
                                                2 : 'Only partially',
                                                3 : 'Impossible to quantify limitless',
                                                4 : 'No, but one day'},
                                    'correct answer': '3',
                                    'reward' : 'An Origin of Journey'},
                        'flame' : {
                            'name' : 'Flame',
                            'question' : 'Can one find the source of the Healing Flame?',
                                    'answers' : {1 : 'Yes, by exploring the cosmos',
                                                2 : 'It is not found, but achieved',
                                                3 : 'No',
                                                4 : 'Yes, can be created by craftsman'},
                                    'correct answer' : '2',
                                    'reward' : 'Ember of Burning Spirit'},
                        'aqua' : {
                            'name' : 'Aqua',
                            'question' : 'In the Waters of Forever, how does one survive?',
                                    'answers' : {1 : 'No survival, you will become one with it',
                                                2 : 'Learn to breathe inside',
                                                3 : 'Drink it all',
                                                4 : 'Hold your breath'},
                                    'correct answer' : '1',
                                    'reward' : 'Drink of the One True'},
                        'mystic' : {
                            'name' : 'Mystic',
                            'question' : 'In the Arcane, is there any limitation true?',
                                    'answers' : {1 : 'Yes, the Rule of Law',
                                                2 : 'No, not according to the rules in place',
                                                3 : 'Yes, spells contained in spellbooks',
                                                4 : 'One can never be restricted if one\'s mind is endless'},
                                    'correct answer' : '4',
                                    'reward' : 'Enchantment of Expanse'},
                        'chaos' : {
                            'name' : 'Chaos',
                            'question' : 'Was there ever truly order in the Expanse?',
                                    'answers' : {1 : 'Yes, all things have order',
                                                2 : 'No, the ever changing cannot be ordered',
                                                3 : 'No, we just believe there is',
                                                4 : 'Yes, but only in the beginning'},
                                    'correct answer' : '2',
                                    'reward' : 'Flow of Chaos Arc'},
                        'order' : {
                            'name' : 'Order',
                            'question' : 'All things have order, whilst nothing has none. Does any One Being see the Truth?',
                                    'answers' : {1 : 'Yes, everyone can if thhey look properly',
                                                2 : 'No, how can one see the intangible?',
                                                3 : 'Yes, make peace with Chaos to see Truth',
                                                4 : 'Nothing ever truly exists to be ordered'},
                                    'correct answer' : '4',
                                    'reward' : 'Sight of Ordered Emptiness'}
                    }
# Base code for dict quick create template - copy and paste.
base_code = {'name' : '', 'question' : '', 'answers' : {1 : '', 2 : '', 3 : '', 4 : ''}, 'correct answer' : '', 'reward' : ''}

# Initiate Elementis and create list - initiate new and add as necessary (if needed):

cosmos = Elementis('cosmos')
flame = Elementis('flame')
aqua = Elementis('aqua')
mystic = Elementis('mystic')
chaos = Elementis('chaos')
order = Elementis('order')
elementis_list = [cosmos, flame, aqua, mystic, chaos, order]


# Object instance creation to run terminal game:

name_start = programme_start()
player_1 = Player(name_start)
new_game = Game(player_1)

