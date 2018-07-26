#Chapter 8 challenges

#challenge 1
""" call a different function from the statistics module """
import statistics
m = [4, 8, 19, 36, 72, 132, 148, 171, 264, 332, 627, 664, 1332, 1577, 4884, 12284]
statistics.mean(m)
print(m)

#challenge 2
""" Create a module named cubed whose function returns a number cubed, then import and call the function from another module. """
#inside tstp >>cubed.py and cubed2.py
#cubed.py
def cube(x):
    return x**3

#cubed2.py
import cubed

result = cubed.cube(3)
print(result)
