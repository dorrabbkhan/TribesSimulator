"""
File for classes to use in the tribe simulator
"""

import random

TRAITS = (
    'strength',
    'bravery',
    'discipline',
    'aggression',
    'wisdom',
    'endurance',
    'belief',
    'desire',
    'synergy'
)

TRIBES = (
    'Tribe 1',
    'Tribe 2',
    'Tribe 3',
    'Tribe 4',
    'Tribe 5',
)
# initialize arbitrary traits, tribe names


class Tribe:
    """
    Tribe class
    """

    def __init__(self, tribe_id):
        """
        Attributes are name, tribe ID and set of warriors ID's
        """
        self.name = TRIBES[tribe_id]
        self.tribe_id = tribe_id
        self.warriors = set()

    def add_warrior(self, warrior_id):
        """
        Add warrior to tribe
        """
        self.warriors.add(warrior_id)

    def kill_warrior(self, warrior_id):
        """
        Remove warrior from tribe
        """
        self.warriors.remove(warrior_id)

    def __len__(self):
        """
        Return number of warriors in tribe
        """
        return len(self.warriors)

    def random_warrior(self):
        """
        Return a random warrior from tribe
        """
        warrior = self.warriors.pop()
        self.warriors.add(warrior)
        return warrior

    def __str__(self):
        """
        Return a text representation of the tribe
        """
        ret = f"Tribe's name is {self.name}\n"
        ret += f"Tribe's warriors are {sorted(self.warriors)}\n"
        return ret


class Warrior:
    """
    Warrior class
    """
    def __init__(self, tribe, friends, warrior_id):
        """
        Attributes are tribe, traits, set of friends, age and ID
        """
        self.tribe = tribe
        self.traits = {trait: random.randint(-12, 15) for trait in TRAITS}
        self.friends = friends
        self.age = 0
        self.warrior_id = warrior_id

    def increase_trait(self, trait, inc):
        """
        Increase a trait's value by inc (max trait value is 100)
        """
        if (self.traits[trait] +
                inc) < 100 and (self.traits[trait] + inc) > -100:
            self.traits[trait] += inc
        elif inc > 0:
            self.traits[trait] = 100
        else:
            self.traits[trait] = -100

    def add_friend(self, friend):
        """
        Add a friend to friend list
        """
        if friend not in self.friends:
            self.friends.add(friend)

    def del_friend(self, friend):
        """
        Remove a friend from friend list
        """
        if friend in self.friends:
            self.friends.remove(friend)

    def inc_age(self):
        """
        Increment age
        """
        self.age += 1
        return self.age >= 60
