#!/usr/bin/env python

"""
lineplot.py: A simple plot of a function
"""

import sys
import math

# Usually I like to import whole namespaces as their true name
# however, with numpy and matplotlib, the names get out of hand
# fairly quickly.
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def main():

    # Create a function to plot
    f = lambda x, tau : math.exp(-float(x)/tau)

    # Specify the limits of x to plot
    xlimits = (0, 10)
    # Specify the delta x between steps
    dx = 0.01


    # Compute the number of steps required to plot the range of x
    steps = int(math.ceil((xlimits[1]-xlimits[0])/dx))

    # Generate a list of xvalues to plot
    x = [xlimits[0]+n*dx for n in xrange(0, steps)]

    # Compute the f(x) for different values of tau
    y1 = [f(z,1) for z in x]
    y2 = [f(z,2) for z in x]
    y3 = [f(z,3) for z in x]

    # Initialize a figure
    plt.figure("Function Demo")
    
    # Set the title, x label, and y label for the figure
    plt.title('Exp Example')
    plt.xlabel('x')
    plt.ylabel(r'$e^{x/\tau}$')

    plt.plot(x, y1, 'r-', label=r'$ \tau = 1 $')
    plt.plot(x, y2, 'b--', label=r'$ \tau = 2 $')
    plt.plot(x, y3, 'g:', label=r'$ \tau = 3 $')
    
    plt.legend(loc='upper right')

    plt.show()


if __name__ == '__main__':
    main()
