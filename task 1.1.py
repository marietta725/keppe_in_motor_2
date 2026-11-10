"""
Task Beschreib:

Create a (L+1) x (L+1) regular 2D grid filled with zeros (= empty). 
The grid spacing is assumed to be 1. A so-called seed particle (unit cell with value 1) is added in the center of the grid, and it will remain there forever. 
This seed particle is the first member of an emerging cluster of particles. Next, a so-called random walker (cell with value 1) starts at a random, still empty, position on the grid. 
The walker makes random steps in any of the 4 directions (taking into account periodic boundary conditions) until it touches the existing cluster. 
At this moment, the walker becomes part of the growing cluster. Add N - 1 more random walkers the same way until the cluster contains N+1 particles (the seed particle plus N random walkers).
Choose L=200 and N=1000. Visualize the resulting cluster (as shown below). Measure the cpu time required to run this simulation.
"""

import matplotlib.pyplot as plt