from numpy import genfromtxt
import matplotlib.pyplot as plt
"""
Module file to generate graph from the generated
data for the trait sums of tribes and save to an image
"""
def genplot():
    # Function to generate graph and save to png 
    per_data = genfromtxt('data.csv', delimiter=',')
    plt.xlabel('Year')
    plt.ylabel('Trait value per trait per capita')
    plt.title('Generational trait progression')
    plt.plot(per_data)
    plt.savefig('data.png')
    plt.show()
    