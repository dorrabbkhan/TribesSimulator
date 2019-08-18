"""
Module file to generate graph from the generated
data for the trait sums of tribes and save to an image
"""

from numpy import genfromtxt
import matplotlib.pyplot as plt
# import dependencies


def genplot():
    """
    Function to generate graph and save to png
    """
    data = genfromtxt('data.csv', delimiter=',')
    # generate data from data.csv

    plt.xlabel('Year')
    plt.ylabel('Trait value per trait per capita')
    plt.title('Generational trait progression')
    # set labels and title

    plt.plot(data)
    plt.savefig('data.png')
    plt.show()
    # plot data, save to data.png and show plot
