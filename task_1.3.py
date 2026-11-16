"""
Task Beschreib:

Here we are interested in the fractal dimension of the created structures. 
To estimate this dimension, it is not enough to create a single cluster, but you have to
take an average over multiple clusters. To this end adjust the functions created in Tasks 1
and 2 to return the resulting (L+1) x (L+1) grid containing the single cluster 
(cells with value 1, all other cells have value 0). 
Start this routine M times and add the resulting grids to obtain an accumulated grid G with
values between 0 and M. Visualize the structure represented by the accumulated grid G.

Calculate the fractal dimension of this structure as follows. For a given distance r 
from the seed particle, calculate the mass m(r) contained within the circle of radius r, 
centered at the seed particle. A mass of a grid node is simply the value of G at this node.
Create a double-logarithmic plot m(r) versus r. It should exhibit an initial linear increase,
followed by a leveling off to a constant value mfinal (this value is known from M and N).

Determine the fractal dimension Df governing the initial linear increase 
via its defining relationship

m(r) ∝ r^(D)*f

$by taking into account only those r values that correspond to m(r)≤0.8 mfinal. 
Also estimate the error bar for Df. Since you have two functions to choose from 
(the ones from Task1 and Task2), obtain Df using a sufficiently large M and compare the two
results.
"""