from math import sqrt

# put your python code here
a, b, c = int(input()), int(input()), int(input())

p = (a + b + c) / 2
print(sqrt(p * (p - a) * (p - b) * (p - c)))
