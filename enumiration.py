#	Add index to iterable

numbers = [1,2,3,4,5,6,7,8,9]
enum = enumerate(numbers,start=1)
print(list(enum))
#any(): Returns True if at least one element in the iterable is True
print(any(numbers))
#all(): Returns True if all elements in the iterable are True.
print(all(numbers))