from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]


#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?


#1
def cap_all(item):
    return item.upper()
print(list(map(cap_all, my_pets)))

#2
my_numbers.sort()
print(list(zip(my_numbers, my_strings)))

#3
def over_fifty(item):
    return item > 50
list_over_fifty = list(filter(over_fifty, scores))
list_over_fifty.sort()
print(list_over_fifty)

#4
def accumulate_scores(acc, item):
    return acc + item

print(reduce(accumulate_scores, (my_numbers + scores)))