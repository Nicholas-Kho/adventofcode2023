import re
from math import sqrt
import math
time, distance = open("day6part2.txt").read().split("\n")

time = int(time.split(":")[1].replace(" ", ""))
records = int(distance.split(":")[1].replace(" ", ""))
print(time, records)

first_solution = math.ceil((-time + sqrt(time**2 - (4*-1*-records)))/(2*-1))
second_solution = math.floor((-time - sqrt(time**2 - (4*-1*-records)))/(2*-1))
print(second_solution - (first_solution - 1))
print(math.ceil((-time + sqrt(time**2 - (4*-1*-records)))/(2*-1)) - math.floor((-time - sqrt(time**2 - (4*-1*-records)))/(2*-1)))