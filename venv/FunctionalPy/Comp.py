# Comprehensions

# Without
my_list = []

for char in 'hello':
    my_list.append(char)

print(my_list)

# With
# Creates a forloop for set variable inside list setting -
# over set iterable.
my_list2 = [param for param in 'hello']
my_list3 = [num for num in range(0,10)]
my_list_multiply = [num*2 for num in range(0,10)]
my_list_even = [num**2 for num in range(0,20)
                if num % 2 ==0]
print(my_list2) # prints ['h', 'e', 'l', 'l', 'o']
print(my_list3) # prints [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list_multiply) # prints [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print(my_list_even) # prints [0, 4, 16, 36, 64, 100, 144, 196, 256, 324]

# With given expression inside [] makes it possible to get a more advanced and -
# compact list with the negativ effect of losing readability at lower levels.


# Same for set

my_set = {char for char in 'hello'}
print(my_set) # prints {'l', 'o', 'e', 'h'} since set only allows non-duplicate values

# and dict
simple_dict = {
    'a' : 1,
    'b' : 2
}
my_dict = {key:value**2 for key,value in simple_dict.items()}
print(my_dict) # prints {'a': 1, 'b': 4}, by doing the power of 2 to each value.
