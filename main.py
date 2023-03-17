import random                                                #used for generating random numbers 
import matplotlib.pyplot as plt                              #used for visualizing the method
import numpy as np                                           #used to square root values

inside_circle = 0                                            #Initial points inside circle
tot_points = 1000                                            #Total points we want to generate

for i in range(tot_points):
    x = random.uniform(-1, 1)                                #x point 
    y = random.uniform(-1, 1)                                #y point
    
    if np.sqrt(x**2 + y**2) <=1:                             #see if x and y points fall inside the circle, eqn of circle is x^2 + y^2 = r^2                
        inside_circle = inside_circle + 1                    #add point to inside circle, if points inside the circle
        plt.scatter(x,y,color='b')                           #plot the point blue, if its in the circle
    else:
        plt.scatter(x,y,color='r')                           #otherwise plot points red if outside circle
        
ratio_Area = inside_circle / tot_points                      #area ratio of points inside the circle and total points
estimated_pi = ratio_Area * 4                                # multiple area ratio by 4 to get pi
print('estimated pi',estimated_pi)                           #print estimate of pi
print('actual pi, 3.14159265359')                            #compare to real pi
