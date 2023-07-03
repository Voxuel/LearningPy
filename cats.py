class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# Instansiate class with 3 objects
cat1 = Cat('Joe', 15)
cat2 = Cat('Roger', 19)
cat3 = Cat('Sandra', 7)


# Create a func for finding the oldest

def find_oldest_cat(*args):
    return max(args)


print(f'The oldest cat is {find_oldest_cat(cat1.age, cat2.age, cat3.age)} years old')
