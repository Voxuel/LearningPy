# map, filter, zip and reduce

from functools import reduce

li = [1,2,3]
liu = [10,20,30]
def multiply_by2(item):
    return item*2

def check_odd(item):
    return item % 2 != 0

def accumulator(acc, item):
    return acc + item

map(multiply_by2, [1, 2, 3]) # Gives map object of func used.

print(list(map(multiply_by2, li))) # casts result object as list and prints to console. ( [2,4,6] )

print(list(filter(check_odd, li))) # gets each true valued return cast as list of results.

print(list(zip(li,liu))) # combines two iterables into one grouped 2 and 2 with one object from each collection.
# zipping togheter multiple collections is possible more then twice.

print(reduce(accumulator, li, 0)) # Accumulates the collection down to the last core combination.
# while given 0, we add 0 at the initial cycel but changing to for example 10, starts the reducation at 10.


