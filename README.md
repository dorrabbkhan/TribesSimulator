
# Tribes Simulator

  

Simulation of battles between tribes for the control of a radiation bunker, inspired from Netflix show 'The 100'

  

## Concept

  
This hit me after watching Season 4 (I think) of The 100, where 12 different tribes fight for the control of a bunker to protect themselves from an incoming radiation wave in a post-apocalyptic world. Pretty geeky, I know. The idea for this program is to simulate the growth of the tribes starting from 5 or more warriors each. This can give a visual representation of how the development of a tribe varies depending on the number and starting traits of the first warriors, and the starting traits of each newborn in the tribe. Each warrior (including the first warriors) has 12 traits, with values ranging from -100 to 100, and the population of each tribe grows by 4% per year. A warrior dies after reaching 60 years of age. The user specifies the range for the starting traits for the first warriors and for the newborns. Warriors that are friends with each other would influence each other's traits. The sum of all traits for all warriors for each of the five tribes are counted and stored each year, and in the end a representation of the progress of these sums is shown.

  

## Warrior class

The warrior class has the following attributes:

| Attribute | Description |
|--|--|
| ID | (Int) Unique ID for each warrior |
| Friends |(List) ID's of their friends within their tribe |
| Tribe | (Int) ID of the tribe they belong to |
|Traits| (Dict) A list of traits along with a trait value |
|Age|(Int) The warrior's age|

There are 12 traits, and each trait has a trait value (-100 to 100) that describes how developed the warrior's respective trait is.  



## Tribe class

The tribe class has the following attributes:

| Attribute | Description |
|--|--|
| Name | (Str) Name of the tribe (randomly generated) |
| ID | (Int) Unique ID for each tribe |
| Warriors | (Set) ID's of warriors belonging to the tribe |



## Dependencies

The following packages are required to run this simulation:

- Random
- NumPy
- Matplotlib

## How to execute

Install independencies, and run driver.py. Enter the ranges for the trait values of the first population (-100 to 100), trait values of the next newborns (-100 to 100), the size of the first population to begin the simulation with, and the number of years to simulate. The simulation will be generated, its data will be saved to data.csv, representing the sum of all traits for all warriors in each tribe over time. A graph will be generated for the data and will also be saved to data.png.

## Future plans

- Add functionality for user-specified influence rates, i.e. how much the warriors are influenced by their friends
- Add functionality for user-specified number of tribes (default is 5)
- Add functionality for user-specified time of death (default is 60)
- Refactor and optimize!

## Interesting results

(Yet to be filled)

---
Feel free to fork the repository, to suggest changes to the program and to hit me up if you're a fan of The 100! 