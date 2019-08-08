import species
import random
import gengraph
from csv import writer
"""
Main driver program for species generator
Contains all functions required to run the program
along with the main function
"""

# Create a counter for warrior ID's,
# tuple of five tribes, a dictionary to store all warrior
# instancesm and a dict of lists for first warriors
curr_id = 0
tribes = tuple(species.Tribe(n) for n in range(5))
all_warriors = dict()
first_warriors = {n: [] for n in range(5)}

def take_int_input(text):
    # Takes a message and repeatedly prints the message
    # and asks for input until an int input is given
    while True:
        var = input(text)
        try:
            int(var)
        except ValueError:
            print('Must be an int')
            continue
        break
    return int(var)
        
def check_invalid_trait(value):
    # Checks if the value given is within the range
    # for trait values
    if value > 100:
        print('Must be below 100')
        return True
    if value < -100:
        print('Must be above -100')
        return True
    return False
    
def init_setup():
    # Inputs initial variables: ranges for first populations,
    # ranges for next populations, size of first population
    # and number of years to simulate. Also performs validation
    # checks.
    while True:
        first_low = take_int_input("Enter lower trait value limit of first population: ")
        if check_invalid_trait(first_low):
            continue
        break

    while True:
        first_high = take_int_input("Enter higher trait value limit of first population: ")
        if check_invalid_trait(first_high):
            continue
        if first_high < first_low:
            print("Must be lower than previous value")
            continue
        break

    while True:
        next_low = take_int_input("Enter lower trait value limit of next population: ")
        if check_invalid_trait(next_low):
            continue
        break

    while True:
        next_high = take_int_input("Enter higher trait value limit of next population: ")
        if check_invalid_trait(next_high):
            continue
        if first_high < first_low:
            print("Must be lower than previous value")
            continue
        break

    while True:
        first_pop = take_int_input("Enter first population size for each tribe: ")
        if first_pop > 4:
            break
        print('Must be above 4')

    while True:
        years = take_int_input("Enter years to simulate: ")
        if years > 4:
            break
        print('Must be above 5')
    
    return first_low, first_high, next_low, next_high, first_pop, years

def mutual_add(warrior, friend):
    # Takes a warrior ID and a friend ID and adds them
    # to each others' friends set 
    all_warriors[friend].add_friend(warrior)
    all_warriors[warrior].add_friend(friend)


def mutual_del(warrior, friend):
    # Takes a warrior ID and a friend ID and deletes them
    # from each others' friends set
    all_warriors[warrior].del_friend(friend)
    all_warriors[friend].del_friend(warrior)


def add_to_total(id, warrior):
    # Adds warrior to total warriors
    all_warriors[id] = warrior


def add_to_tribe(id, tribe):
    # Adds warrior ID to tribe
    tribes[tribe].add_warrior(id)


def create_warrior():
    # Creates warrior: assigns warrior ID, random tribe,
    # random friends in tribe, random traits within the 
    # specified ranges. Adds warrior to tribe, to total warriors
    # and mutually adds friends with the generated set of friends.
    # Finally, increments counter for warriors
    global curr_id
    tribe = random.randint(0, 4)
    friends = {tribes[tribe].random_warrior() for i in range(3)}
    new_warrior = species.Warrior(tribe, friends, curr_id)
    for trait in species.TRAITS:
        new_warrior.traits[trait] = random.randint(next_low, next_high)
    add_to_tribe(curr_id, tribe)
    add_to_total(curr_id, new_warrior)
    for friend in friends:
        all_warriors[friend].add_friend(curr_id)
    curr_id += 1


def create_first_warrior(tribe):
    # Creates the first warriors: assigns a tribe, friends with all
    # current members of the tribe, warrior ID and an age between
    # 20 and 30. Assigns trait values within specified ranges, adds
    # warrior ID to respective tribe, adds to first warriors list
    # and adds to dict of all warriors. Finally, increments counter 
    # for warrior ID's
    global curr_id
    friends = set()
    new_warrior = species.Warrior(tribe, friends, curr_id)
    new_warrior.age = random.randint(20, 30)
    for trait in species.TRAITS:
        new_warrior.traits[trait] = random.randint(first_low, first_high)
    add_to_tribe(curr_id, tribe)
    first_warriors[tribe].append(curr_id)
    add_to_total(curr_id, new_warrior)
    curr_id += 1


def set_first_friends():
    # Makes each of the first warriors of each tribe
    # friends with each other
    for tribe in first_warriors.keys():
        for friend in first_warriors[tribe]:
            for warrior in first_warriors[tribe]:
                if friend != warrior:
                    mutual_add(warrior, friend)


def delete_warrior(warrior):
    # Deletes a warrior from its tribe and the dict
    # of all warriors
    tribe = warrior.tribe
    tribe.kill_warrior(warrior.id)
    all_warriors.pop(warrior.id)


def influence(warrior):
    # Makes the friends of the warrior influence the warrior's
    # traits, based on the age of the warrior. The higher the age,
    # the lesser he's influenced.
        for friend in all_warriors[warrior].friends:
            for trait in species.TRAITS:
                friend_value = all_warriors[friend].traits[trait]
                warrior_age = all_warriors[warrior].age + 1
                increase = friend_value*0.17*((61/warrior_age)/61)
                all_warriors[warrior].increase_trait(
                    trait, increase)

def sum_traits(tribe):
    # Sums all the traits of all the warriors in the given tribe
    # and returns the sum
    traits = 0
    for warrior in tribes[tribe].warriors:
        for trait in species.TRAITS:
            warrior_trait = all_warriors[warrior].traits[trait]
            traits += warrior_trait
    return traits


def inc_people():
    # Increases number of warriors by 4% by creating new warriors
    population = len(all_warriors)
    print(f"Population is: {population}")
    people_increase = int(population * 0.04)
    for i in range(people_increase):
        create_warrior()


def check_death():
    # Increases warriors' age, checks if a warrior is dead, 
    # and if so then removes it 
    # from its friends' lists, from its tribe and from the 
    # dict of all warriors
    deaths = set()
    for warrior in all_warriors.keys():
        dead = all_warriors[warrior].inc_age()
        if dead:
            for friend in all_warriors[warrior].friends:
                all_warriors[friend].del_friend(warrior)
            tribe = all_warriors[warrior].tribe
            deaths.add(warrior)
            tribes[tribe].kill_warrior(warrior)
    for warrior in deaths:
        all_warriors.pop(warrior)

def make_first_warriors(first_pop):
    # Driver to make first warriors and set friends
    # based on the first population specified for each tribe
    for i in range(first_pop):
        for j in range(5):
            create_first_warrior(j)
    set_first_friends()

def write_to_file():
    # Function to write output to the file 'data.csv'
    with open('data.csv', 'a+') as f:
        csv_writer = writer(f)
        traitsum = []
        for tribe in range(5):
            population = len(tribes[tribe])
            traitsum.append(str(sum_traits(tribe)/(population*12)))
        csv_writer.writerow(traitsum)

def break_friends(warrior):
    # randomly removes friend(s) of warrior
    deletions = set()
    for friend in all_warriors[warrior].friends:
        chance = random.random()
        if chance > 0.8:
            deletions.add(friend)
    for friend in deletions:
        mutual_del(warrior, friend)
    
def make_friends(warrior):
    # randomly adds friends of warrior (chance higher
    # than that of break_friends function)
    pot_frnds = set()
    war_tribe = all_warriors[warrior].tribe
    for i in range(3):
        pot_frnds.add(tribes[war_tribe].random_warrior())
    for pot_frnd in pot_frnds:
        if pot_frnd != warrior:
            chance = random.random()
            if chance > 0.75:
                mutual_add(warrior, pot_frnd)

def write_column_names():
    # Write column names on top of the csv file
    with open('data.csv', 'w+') as f: 
        csv_writer = writer(f)
        csv_writer.writerow(list(species.TRIBES))

def driver():
    # Driver function for the main program
    write_column_names()
    make_first_warriors(first_pop)
    for i in range(years):
        print(f"Year is {i+1}")
        inc_people()
        for warrior in all_warriors.keys():
            break_friends(warrior)
            make_friends(warrior)
            influence(warrior)
        check_death()
        write_to_file()

    gengraph.genplot()
    input()

# Setup initial variables
first_low, first_high, next_low, next_high, first_pop, years = init_setup()

# Call to driver
driver()
