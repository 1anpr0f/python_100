#	Apply a function to each element

numbers = [1,2,3,4,5,6,7,8,9]
mapping = map(lambda x: x ** 2 ,numbers)
print(list(mapping))
