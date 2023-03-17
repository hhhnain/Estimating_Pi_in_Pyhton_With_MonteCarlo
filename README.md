# Estimating_Pi_in_Pyhton_With_MonteCarlo
Here we will use the power of monte carlo to estimate Pi in Python


Imagine a perfect square where there is a perfect circle inside touching all sides, so the diameter of the circle is the lenght of the square.
Diameter is simply 2 * radius (r) so the area of the square is 2*r * 2*r, 4r^2, and we know the area of a cricle is pi*r squared
comparing the ratio of circle area to square area we get pi*r^2 / 4*r^2
The r^2 cancels and we are left with area_ratio = pi/4
to find pi, we simple multiply area_ratio by 4

to get the area ratio, we generate random x and y points between 1 and -1 and plot them

Then by counting the total points inside the circle we can divide it by the total points to get the area ratio, then its simple, multiply by 4 to get pi

To check if a point falls inside a circle, we do a simple check by using the circle equation of (x^2 + y^2) <= 1

Code in Main.py
