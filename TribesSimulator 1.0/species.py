import random
"""
File for classes to use in the tribe simulator
"""

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

    def __init__(self, id):
        """
        Attributes are name, tribe ID and set of warriors ID's
        """
        self.name = TRIBES[id]
        self.id = id
        self.warriors = set()

    def add_warrior(self, warriorid):
        """
        Add warrior to tribe
        """
        self.warriors.add(warriorid)

    def kill_warrior(self, warriorid):
        """
        Remove warrior from tribe
        """
        self.warriors.remove(warriorid)

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
    def __init__(self, tribe, friends, id):
        """
        Attributes are tribe, traits, set of friends, age and ID
        """
        self.tribe = tribe
        self.traits = {trait: random.randint(-12, 15) for trait in TRAITS}
        self.friends = friends
        self.age = 0
        self.id = id

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
