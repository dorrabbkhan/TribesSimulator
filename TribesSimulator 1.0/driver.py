"""
Main driver program for species generator
Contains all functions required to run the program
along with the main function
"""

import random
from csv import writer
import species
import gengraph

CURR_ID = 0
TRIBES = tuple(species.Tribe(n) for n in range(5))
ALL_WARRIORS = dict()
FIRST_WARRIORS = {n: [] for n in range(5)}
# Create a counter for warrior ID's,
# tuple of five TRIBES, a dictionary to store all warrior
# instancesm and a dict of lists for first warriors


def take_int_input():
    """
    Takes a message and repeatedly prints the message
    and asks for input until an int input is given
    """

    while True:
        try:
            var = input()
            int(var)
        except ValueError:
            print('Must be an int')
            continue
        break
    # repeat taking input until input is int

    return int(var)


def check_invalid_trait(value):
    """
    Checks if the value given is within the range
    for trait values
    """

    if value > 100:
        print('Must be below 100')
        return True
    if value < -100:
        print('Must be above -100')
        return True
    return False
    # must be between -100 and 100, returns true if invalid


def trait_input():
    """
    input a valid trait value and return
    """
    while True:
        trait = take_int_input()
        if check_invalid_trait(trait):
            continue
        break
    return trait
    # keep inputting trait values until valid input is given


def init_setup():
    """
    Inputs initial variables: ranges for first populations,
    ranges for next populations, size of first population
    and number of YEARS to simulate. Also performs validation
    checks.
    """
    print("Enter lower trait value limit of first population: ")
    first_low = trait_input()
    # input valid lower limit of trait value for first population

    while True:
        print("Enter higher trait value limit of first population: ")
        first_high = trait_input()
        if first_high < first_low:
            print("Must be lower than previous value")
            continue
        break
    # keep asking for input until valid higher limit of trait value
    # is given which is also not smaller than the lower limit

    print("Enter lower trait value limit of next population: ")
    next_low = trait_input()
    # input a valid lower limit of trait value for next population

    while True:
        print("Enter higher trait value limit of next population: ")
        next_high = trait_input()
        if next_high < next_low:
            print("Must be lower than previous value")
            continue
        break
    # keep asking for input until valid higher limit of trait value
    # is given which is also not smaller than the lower limit

    while True:
        print("Enter first population size for each tribe: ")
        first_pop = take_int_input()
        if first_pop > 4:
            break
        print('Must be above 4')
    # keep asking for number of starting population until it is
    # greater than 4

    while True:
        print("Enter years to simulate: ")
        years = take_int_input()
        if years > 4:
            break
        print('Must be above 5')
    # keep asking for number of years to simulate until at least 4
    # are given

    return first_low, first_high, next_low, next_high, first_pop, years
    # return all generated variables


def mutual_add(warrior, friend):
    """
    Takes a warrior ID and a friend ID and adds them
    to each others' friends set
    """
    ALL_WARRIORS[friend].add_friend(warrior)
    ALL_WARRIORS[warrior].add_friend(friend)


def mutual_del(warrior, friend):
    """
    Takes a warrior ID and a friend ID and deletes them
    from each others' friends set
    """
    ALL_WARRIORS[warrior].del_friend(friend)
    ALL_WARRIORS[friend].del_friend(warrior)


def add_to_total(warrior_id, warrior):
    """
    Adds warrior to total warriors dict
    """
    ALL_WARRIORS[warrior_id] = warrior


def add_to_tribe(warrior_id, tribe):
    """
    Adds warrior ID to tribe
    """
    TRIBES[tribe].add_warrior(warrior_id)


def create_warrior():
    """
    Creates warrior: assigns warrior ID, random tribe,
    random friends in tribe, random traits within the
    specified ranges. Adds warrior to tribe, to total warriors
    and mutually adds friends with the generated set of friends.
    Finally, increments counter for warriors
    """
    global CURR_ID
    # check global CURR_ID for warrior ID of new warrior

    tribe = random.randint(0, 4)
    # generate a random tribe number

    friends = {TRIBES[tribe].random_warrior() for i in range(3)}
    # generate 3 random warriors from  tribe to be new warrior's friends

    new_warrior = species.Warrior(tribe, friends, CURR_ID)
    # generate the new warrior object
    # with tribe ID, friends, and warrior ID

    for trait in species.TRAITS:
        new_warrior.traits[trait] = random.randint(NEXT_LOW, NEXT_HIGH)
    # assign random trait values within
    # user-specified ranges for each trait

    add_to_tribe(CURR_ID, tribe)
    # add new warrior to tribe

    add_to_total(CURR_ID, new_warrior)
    # add new warrior to total_warriors dict

    for friend in friends:
        ALL_WARRIORS[friend].add_friend(CURR_ID)
        # add new warrior to friends set of his newly generated friends

    CURR_ID += 1
    # increment current ID


def create_first_warrior(tribe):
    """
    Creates the first warriors: assigns a tribe, friends with all
    current members of the tribe, warrior ID and an age between
    20 and 30. Assigns trait values within specified ranges, adds
    warrior ID to respective tribe, adds to first warriors list
    and adds to dict of all warriors. Finally, increments counter
    for warrior ID's
    """

    global CURR_ID
    # check global CURR_ID for warrior ID of new warrior

    friends = set()
    # make a new set for this warrior's friends

    new_warrior = species.Warrior(tribe, friends, CURR_ID)
    # generate new warrior with the specified tribe, empty list
    # of friends and current warrior ID

    new_warrior.age = random.randint(20, 30)
    # assign random age between 20 and 30

    for trait in species.TRAITS:
        new_warrior.traits[trait] = random.randint(FIRST_LOW, FIRST_HIGH)
    # assign random trait values within
    # user-specified ranges for each trait

    add_to_tribe(CURR_ID, tribe)
    # add this warrior to the warrior list of its tribe

    FIRST_WARRIORS[tribe].append(CURR_ID)
    # add this warrior to the list of the first warriors of their tribe

    add_to_total(CURR_ID, new_warrior)
    # add this warrior to dict of total warriors

    CURR_ID += 1
    # increment CURR_ID


def set_first_friends():
    """
    Makes each of the first warriors of each tribe
    friends with each other
    """

    for tribe in range(4):
        # for each tribe that first warriors are in

        for friend in FIRST_WARRIORS[tribe]:
            # for each friend ID in first warriors of that tribe

            for warrior in FIRST_WARRIORS[tribe]:
                # for each warrior ID in first warriors of that tribe
                if friend != warrior:
                    # if friend ID and warrior ID are not identical

                    mutual_add(warrior, friend)
                    # mutually add both to each other's friends list


def delete_warrior(warrior):
    """
    Deletes a warrior from its tribe and the dict
    of all warriors
    """
    tribe = warrior.tribe
    # select the warrior's tribe

    tribe.kill_warrior(warrior.id)
    # kill the warrior from the tribe

    ALL_WARRIORS.pop(warrior.id)
    # remove the warrior from the all warriors dict


def influence(warrior):
    """
    Makes the friends of the warrior influence the warrior's
    traits, based on the age of the warrior. The higher the age,
    the lesser he's influenced.
    """
    for friend in ALL_WARRIORS[warrior].friends:
        # for each friend in the warrior's friend list

        for trait in species.TRAITS:
            # for each trait

            warrior_age = ALL_WARRIORS[warrior].age + 1
            # extract the warrior's age, add 1 to avoid div by 0 below

            friend_value = ALL_WARRIORS[friend].traits[trait]
            # select the friend's value

            increase = friend_value*0.17*((61/warrior_age)/61)
            # calculate increase according to the formula that
            # depends on friend's trait value and the warrior's age

            ALL_WARRIORS[warrior].increase_trait(
                trait, increase)
            # increase the trait value of the warrior


def sum_traits(tribe):
    """
    Sums all the traits of all the warriors in the given tribe
    and returns the sum
    """
    traits_sum = 0
    # initialize sum of traits

    for warrior in TRIBES[tribe].warriors:
        # for each warrior in the tribe

        for trait in species.TRAITS:
            # for each trait

            warrior_trait = ALL_WARRIORS[warrior].traits[trait]
            traits_sum += warrior_trait
            # extract the warrior's trait and add to traits_sum

    return traits_sum


def inc_people():
    """
    Increases number of warriors by 4% by creating new warriors
    """
    population = len(ALL_WARRIORS)
    # check current population

    print(f"Population is: {population}")
    # print population

    people_increase = int(population * 0.04)
    # calculate increase in population

    for i in range(people_increase):
        create_warrior()
        # create new warriors


def check_death():
    """
    Increases warriors' age, checks if a warrior is dead,
    and if so then removes it
    from its friends' lists, from its tribe and from the
    dict of all warriors
    """
    deaths = set()
    # initialize empty deaths set

    for warrior in ALL_WARRIORS:
        # for each warrior

        dead = ALL_WARRIORS[warrior].inc_age()
        # see if inc_age returns True for death of warrior

        if dead:
            for friend in ALL_WARRIORS[warrior].friends:
                # for each of this warrior's friends

                ALL_WARRIORS[friend].del_friend(warrior)
                # delete this warrior from their friend's list

            tribe = ALL_WARRIORS[warrior].tribe
            # select the warrior's tribe

            deaths.add(warrior)
            # add warrior to deaths

            TRIBES[tribe].kill_warrior(warrior)
            # remove warrior from tribe

    for warrior in deaths:
        ALL_WARRIORS.pop(warrior)
        # pop each warrior in deaths set from the dict of all warriors


def make_first_warriors(first_pop):
    """
    Driver to make first warriors and set friends
    based on the first population specified for each tribe
    """
    for i in range(first_pop):
        # for each new warrior

        for j in range(5):
            # for each tribe create warrior
            create_first_warrior(j)

    set_first_friends()
    # set starting friendships


def write_to_file():
    """
    Function to write output to the file 'data.csv
    """
    with open('data.csv', 'a+', newline='') as data_file:
        # open the file in append+ mode

        csv_writer = writer(data_file)
        trait_per_capita = []
        # initialize value per trait per capita, writer object

        for tribe in range(5):
            # for each tribe

            population = len(TRIBES[tribe])
            # extract population of tribe

            tribe_sum = sum_traits(tribe)
            # extract sum of traits for all tribe

            traits_per_capita = tribe_sum/population
            # calculate sum of all traits per capita

            trait_per_capita.append(str(traits_per_capita/12))
            # append value per trait per capita to trait_per_capita

        csv_writer.writerow(trait_per_capita)
        # write row to file


def break_friends(warrior):
    """
    randomly removes friend(s) of warrior
    """
    deletions = set()
    # initialiize set of deletions

    for friend in ALL_WARRIORS[warrior].friends:
        # for each friend of warrior

        chance = random.random()
        # select chance

        if chance > 0.8:
            deletions.add(friend)
            # add friend to deletions of chance > 0.8

    for friend in deletions:
        mutual_del(warrior, friend)
        # delete all of this warrior's friends in deletions


def make_friends(warrior):
    """
    randomly adds friends of warrior (chance higher
    than that of break_friends function)
    """
    pot_frnds = set()
    # initialize potential friends

    war_tribe = ALL_WARRIORS[warrior].tribe
    # initialize warrior tribe

    for i in range(3):
        pot_frnds.add(TRIBES[war_tribe].random_warrior())
        # add random warriors to potential friends

    for pot_frnd in pot_frnds:
        # for each potential friend

        if pot_frnd != warrior:
            # if potential friend is not warrior itself

            chance = random.random()
            # select random chance

            if chance > 0.75:
                mutual_add(warrior, pot_frnd)
                # make friend if chance > 0.75


def write_column_names():
    """
    Write heading names on top of the csv file
    """
    with open('data.csv', 'w+', newline='') as data_file:
        # open csv file

        csv_writer = writer(data_file)
        csv_writer.writerow(list(species.TRIBES))
        # initialize writer object and write names of TRIBES as headings


def driver():
    """
    Driver function for the main program
    """

    write_column_names()
    make_first_warriors(FIRST_POP)
    # write column names and make first warriors

    for i in range(YEARS):
        # for each year

        print(f"Year is {i+1}")
        # print year

        inc_people()
        # increase population

        for warrior in ALL_WARRIORS:
            # for each warrior

            break_friends(warrior)
            make_friends(warrior)
            # break and make random friends

            influence(warrior)
            # randomly influence traits

        check_death()
        # check death of each warrior

        write_to_file()
        # write new data to file

    gengraph.genplot()
    # generate plot

    input()
    # wait for input


# Setup initial variables
FIRST_LOW, FIRST_HIGH, NEXT_LOW, NEXT_HIGH, FIRST_POP, YEARS = init_setup()

# Call to driver
driver()
