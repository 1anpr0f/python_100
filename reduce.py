#Reduce iterable to a single value
from functools import reduce
numbers = [1,2,3,4,5,6,7,8,9]
red = reduce(lambda x,y : x + y ,numbers)
print(red)
