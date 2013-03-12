#!/usr/bin/env python

""" linear_regression.py
    In this example we will create some 'data' then fit an linear curve to it.
"""

#import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

def main():
    """
    """
    # Set a number of datapoints   
    n = 100
    t = np.linspace(0, 10, n)
    
    # Set the parameters for the line
    a = 1
    b = 0

    print "Initial Parameters: a = {:g} b = {:g}".format(a,b)

    # Create a line a*t +b and add noise to it.
    xerr = np.random.randn(n)
    x = np.polyval([a, b], t) + xerr
    xerr /= np.sqrt(2)

    # Preform Linear Regression
    (ar, br) = np.polyfit(t, x, 1)

    # Create a line for the regression
    xr = np.polyval([ar, br], t)

    # root-mean-square-error
    rmserr = np.sqrt(sum((xr-x)**2)/n)

    print "Results of linear regression:",
    print "a = {:g}, b = {:g}, rmserr = {:g}".format(ar, br, rmserr)

    plt.figure(1)
    plt.title("Linear Regression")
    plt.plot(t, x, '.', label='Data')
    plt.plot(t, xr, '--', label='Linear Fit')
    plt.legend(loc='lower right')
    plt.show()

    """
    # Plot a least squares fit with error in mind
    weights = [1/z for z in xerr]
    (arls, brls) = np.polyfit(t, xr, 1, w=weights)
    xrls = np.polyval([arls, brls], t)
    
    rmserrls = np.sqrt(sum((xrls-x)**2)/n)

    plt.figure(2)
    plt.errorbar(t, x, yerr=xerr, fmt='.', label='Data')
    plt.plot(t, xrls, '--', label="Least Squares Fit")
    plt.legend(loc='lower right')
    plt.show()
    """

if __name__ == '__main__':
    main()
