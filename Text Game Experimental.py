import random as rand


class GameRoom:
    room_type = ''
    desc = ''
    rooms = {}
    monster = ''
    campfire_rooms = {}
    campfire = bool

    def __init__(self):
        self.monster = get_monster()
        if self.campfire is True:
            GameRoom.campfire_rooms[self.room_type] = self
        GameRoom.rooms[self.room_type] = self

    def get_desc(self):
        return self.room_type + '\n' + self.desc + '\n' + self.monster


class StartingRoom(GameRoom):
    def __init__(self, directions):
        self.room_type = 'room'
        self.desc = """A small square room with a door on the opposite end."""
        self.campfire = True
        self.directions = directions
        super().__init__()

    @property
    def desc(self):
        if self.campfire is True:
            campfire = 'There is a campfire in the room.'
        else:
            campfire = 'There is not a campfire in the room.'
        return self._desc + '\n' + campfire

    @desc.setter
    def desc(self, value):
        self._desc = value


class Hallway1(GameRoom):
    def __init__(self, directions):
        self.room_type = 'hallway'
        self.desc = 'A long narrow corridor, too dark to see the end.'
        self.campfire = False
        self.directions = directions
        super().__init__()

    @property
    def desc(self):
        if self.campfire is True:
            campfire = 'There is a campfire in the room.'
        else:
            campfire = 'There is not a campfire in the room.'
        return self._desc + '\n' + campfire

    @desc.setter
    def desc(self, value):
        self._desc = value


class GameMovement:
    direction = ''
    is_available = bool
    room_list = ['startingroom', 'hallway1']

    def __init__(self):
        print('works')

    def get_desc(self):
        return self.direction


class Move(GameMovement):
    def __init__(self):
        self.direction = 'north'
        print(Character.room)
        super().__init__()

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value

    def check_availability(self, direction):
        room1 = self.room_list[Character.room]
        if room1 == 'startingroom':
            room1 = startingroom
        elif room1 == 'hallway1':
            room1 = hallway1
        directions = room1.directions
        if direction in directions:
            print('returning true')
            self.is_available = True
            return True
        elif direction not in directions:
            print('returning false')
            self.is_available = False
            return False
        else:
            print('something else is wrong')


class GameObject:
    class_name = ''
    desc = ''
    is_looted = bool
    objects = {}
    room = 0
    room_list = ['startingroom', 'hallway1']

    def __init__(self, name):
        self.name = name
        GameObject.objects[self.class_name] = self

    def get_desc(self):
        return self.class_name + '\n' + self.desc


class Goblin(GameObject):
    def __init__(self, name):
        self.class_name = 'goblin'
        self.desc = 'A foul creature'
        self.health = 3
        self.is_looted = False
        self.is_dead = False
        super().__init__(name)

    @property
    def desc(self):
        if self.health >= 3:
            return self._desc
        elif self.health == 2:
            health_line = 'It has a wound on its shoulder.'
        elif self.health == 1:
            health_line = 'Its right leg has been cut off.'
        elif self.health <= 0:
            health_line = 'The monster is dead.'
        return self._desc + '\n' + health_line

    @desc.setter
    def desc(self, value):
        self._desc = value


class Minotaur(GameObject):
    def __init__(self, name):
        self.class_name = 'minotaur'
        self.desc = 'Some kind of half-bull half-man creature'
        self.health = 2
        self.is_looted = False
        self.is_dead = False
        super().__init__(name)

    @property
    def desc(self):
        if self.health >= 2:
            return self._desc
        elif self.health == 1:
            health_line = 'It is nearly dead.'
        elif self.health <= 0:
            health_line = 'It is dead.'
        return self._desc + '\n' + health_line

    @desc.setter
    def desc(self, value):
        self._desc = value


class Character(GameObject):
    def __init__(self, name, health, room):
        self.class_name = 'character'
        self.desc = 'You'
        self.health = health
        self.full_health = health
        self.money = 0
        self.room = room
        self.in_room = self.room_list[self.room]
        super().__init__(name)

    @property
    def desc(self):
        money = 'You have {} gold pieces.'.format(self.money)
        if self.health >= self.full_health:
            health_line = 'You are at full health.'
        elif self.health > self.full_health / 2 and self.health < self.full_health:
            health_line = 'You are above half health.'
        elif self.health == self.full_health / 2:
            health_line = 'You are at half health.'
        elif self.health < self.full_health / 2 and self.health > 0:
            health_line = 'You are below half health.'
        elif self.health <= 0:
            health_line = 'You are dead.'
        return self._desc + '\n' + health_line + '\n' + money

    @desc.setter
    def desc(self, value):
        self._desc = value

    def money(self, amount):
        self.money += amount


def main():
    start()
    while True:
        if get_input() is False:
            break
        elif character.health <= 0:
            print('You have died.')
            break
        else:
            continue


def start():
    print("""
        As you enter the room you are facing north
        
        There is a monster in the room.
                
        Your adventure begins here. Good luck
    """)


def get_input():
    command = input(':').split()
    verb_word = command[0]
    if verb_word in verb_dict:
        verb = verb_dict[verb_word]
    elif verb_word == 'quit':
        print('You have quit the game')
        return False
    else:
        print('Unknown verb {}'.format(verb_word))
        return

    if verb_word == 'loot':
        if len(command) == 1:
            print('That verb requires a second argument')
        else:
            noun_word = command[1]
            thing = GameObject.objects[noun_word]
            print(command[1])
            if thing.is_looted is False and thing.is_dead is True:
                print(verb(noun_word))
                thing.is_looted = True
            elif thing.is_dead is False:
                print('The {} is not dead.'.format(noun_word))
            else:
                print('You have already looted that monster')
    elif len(command) >= 2:
        noun_word = command[1]
        print(verb(noun_word))
    elif len(command) == 1:
        if verb_word in verb_arg_list:
            print('That verb requires a second argument.')
        else:
            print(verb())
    else:
        print(verb('nothing'))


def rest(current_room):
    if current_room in GameRoom.campfire_rooms:
        you = GameObject.objects['character']
        you.health = you.full_health
        return 'You awake feeling renewed.'
    else:
        return 'There must be a campfire in the room for you to rest.'


def say(noun):
    return 'You said "{}"'.format(noun)


def hit(noun):
    if noun in GameObject.objects:
        thing = GameObject.objects[noun]
        if type(thing) == Goblin:
            thing.health -= 1
            if thing.health <= 0:
                msg = 'You killed the {}'.format(thing.class_name)
                thing.is_dead = True
            else:
                msg = 'You hit the {}'.format(thing.class_name)
                msg = msg + '\n' + attack_back(noun)
                thing.is_dead = False
        elif type(thing) == Minotaur:
            thing.health -= 1
            if thing.health <= 0:
                msg = 'You killed the {}'.format(thing.class_name)
                thing.is_dead = True
            else:
                msg = 'You hit the {}'.format(thing.class_name)
                msg = msg + '\n' + attack_back(noun)
                thing.is_dead = False
        elif type(thing) == Character:
            msg = 'You cannot hit yourself'
    else:
        msg = 'There is no {} here.'.format(noun)
    return msg


def attack_back(noun):
    if noun in GameObject.objects:
        num = rand.randint(1, 2)
        if num == 1:
            thing = GameObject.objects[noun]
            if type(thing) == Goblin:
                character.health -= 1
                msg = 'The {} hit back.'.format(noun)
            elif type(thing) == Minotaur:
                character.health -= 2
                msg = 'The {} hit back.'.format(noun)
        else:
            return 'The {} missed'.format(noun)
    return msg


def examine(noun):
    if noun == 'room':
        print(noun)
        current_room = GameObject.room_list[Character.room]
        if current_room == 'startingroom':
            current_room = startingroom
        elif current_room == 'hallway1':
            current_room = hallway1
        print(current_room)
        return GameRoom.get_desc(current_room)
    elif noun in GameObject.objects:
        return GameObject.objects[noun].get_desc()
    else:
        print(GameObject.objects, '\n', GameRoom.rooms)
        return 'There is no {} here'.format(noun)


def move(direction):
    available = Move.check_availability(moves, direction)
    if available is True:
        msg = 'You have moved {} and entered a new room'.format(direction)
        Character.room += 1
    elif available is False:
        msg = 'You cannot move in that direction.'
    else:
        msg = 'Something else is wrong.'
    return msg


def loot(noun):
    if noun in GameObject.objects:
        thing = GameObject.objects[noun]
        if type(thing) == Goblin:
            gold = rand.randint(7, 15)
            Character.money(character, gold)
            return 'You found {} gold pieces.'.format(gold)
        elif type(thing) == Minotaur:
            gold = rand.randint(10, 20)
            Character.money(character, gold)
            return 'You found {} gold pieces.'.format(gold)
    else:
        return 'There is no {} to loot.'.format(noun)


def get_monster():
    randint = rand.randint(1, 2)
    if randint == 1:
        msg = 'There is a Goblin in the room.'
        goblin = Goblin('Gobbly')
    elif randint == 2:
        msg = 'There is a Minotaur in the room.'
        minotaur = Minotaur('Taur Taur')
    return msg


startingroom_directions = ['north']
hallway1_directions = ['north']
character = Character('Geoffrey', 6, 0)
startingroom = StartingRoom(startingroom_directions)
hallway1 = Hallway1(hallway1_directions)
moves = Move()

room_list = ['startingroom', 'hallway1']
monster_list = ['minotaur', 'goblin']
direction_list = ['east', 'west', 'north', 'south']
verb_arg_list = ['say', 'examine', 'hit', 'rest', 'move', 'loot']
verb_dict = {'say': say, 'examine': examine, 'hit': hit, 'rest': rest,
             'move': move, 'loot': loot}

main()
