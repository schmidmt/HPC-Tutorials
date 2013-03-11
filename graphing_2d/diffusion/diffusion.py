#!/usr/bin/env python

"""
diffusion.py: A tutorial on how to do scatter plots and histagrams
              with matplotlib.
"""              




import sys
import random

# Usually I like to import whole namespaces as their true name
# however, with numpy and matplotlib, the names get out of hand
# fairly quickly.
import numpy as np
import matplotlib
import matplotlib.pylab as plt

class particle:
    """ A class to describe a random walking particle.
    """
    def __init__(self, loc):
        """ Setup a particle class
            INPUT:
                   loc - a tuple describing the location of the particle.
        """
        self.location = list(loc)
        self.dims = len(self.location)

    def rWalk(self):
        """ Tell the particle to random walk one step.
        """
        for i in xrange(0,self.dims):
            self.location[i] += random.uniform(-1,1)

    def getLoc(self):
        """ Return the location of the particle.
        """
        return self.location

def main():

    ##########
    # Config #
    ##########
    particle_count = 10**4
    steps          = 10**2
    graph_steps    = [0, 10, 90]
    binwidth       = 0.50
    ##########
    
    nullfmt = matplotlib.ticker.NullFormatter()

    
    # definitions for the axes
    left, width = 0.1, 0.65
    bottom, height = 0.1, 0.65
    bottom_h = left_h = left+width+0.02
    rect_scatter = [left, bottom, width, height]
    rect_histx = [left, bottom_h, width, 0.2]
    rect_histy = [left_h, bottom, 0.2, height]

    fignum = 1

    # Create a list of particle classes
    particles = list()
    for i in xrange(0, particle_count):
        particles.append(particle((random.uniform(-1,1), random.uniform(-1,1))))


    # Do iterative time steps in which particles will random walk
    for timestep in xrange(0, steps):
        # If this time step is designated, show a plot
        if timestep in graph_steps:
            plt.figure(fignum, figsize=(8,8))
            fignum += 1
            axScatter = plt.axes(rect_scatter)
            axHistx   = plt.axes(rect_histx)
            axHisty   = plt.axes(rect_histy)

            # no labels
            axHistx.xaxis.set_major_formatter(nullfmt)
            axHisty.yaxis.set_major_formatter(nullfmt)

            x = list()
            y = list()
            # generate the x,y lists for particles
            for part in particles:
                ltmp = part.getLoc()
                x.append(ltmp[0])
                y.append(ltmp[1])
            
            # Plot the points
            axScatter.scatter(x, y)
            
            # Determine some limits
            xymax = np.max( [np.max(np.fabs(x)), np.max(np.fabs(y))] )
            lim = ( int(xymax/binwidth) + 1) * binwidth
            
            # Set the limits on the histagrams
            axScatter.set_xlim( (-lim, lim) )
            axScatter.set_ylim( (-lim, lim) )

            # bin for the histagram
            bins = np.arange(-lim, lim + binwidth, binwidth)
            axHistx.hist(x, bins=bins)
            axHisty.hist(y, bins=bins, orientation='horizontal')


            axHistx.set_xlim( axScatter.get_xlim() )
            axHisty.set_ylim( axScatter.get_ylim() )

            #plt.show()


        for part in particles:
            part.rWalk()

    
    # Show figures
    plt.show()


if __name__ == '__main__':
    main()

