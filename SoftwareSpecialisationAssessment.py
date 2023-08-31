# Section 2: Coding Questions [24 marks]
#  2.1   A) Write a function that takes in a string and returns the number of unique consonants [10 marks]
def count_unique_consonants(s):
    # Define consonants
    consonants = set("bcdfghjklmnpqrstvwxyz")

    # Convert string to lowercase
    lower_s = s.lower()

    unique_consonants = []

    for ch in consonants:
        if lower_s.count(ch) == 1:
            unique_consonants.append(ch)
            
    # Return the count of unique consonants
    return len(unique_consonants)

# Test cases
print(count_unique_consonants("cat"))       # Output: 2
print(count_unique_consonants("cataract"))  # Output: 1


#   B)  What is the time and space complexity of your solution?
#  If you are making any assumptions in your calculations, list them. 

# ANSWERS:
# The time complexity of the function is now O(n*m).
# Assumption: Iterating over the consonants and counting occurrences in the string are the dominant factors for the time complexity.

# The space complexity remains O(1).
# Assumption: The number of letters in any language is constant. For example in English it's 26.


# 2.2    Write a function that finds how many squares are in a X by X grid.
def total_squares(x):
    if x == 1:
        return 1
    else:
        return x ** 2 + total_squares(x - 1)


# Section 3: Theory Challenge - Hashing  [25 points]
# 3.1    Design a basic hash function, keeping in mind memory constraints and how you would deal with hash collisions. 
# A function that will be used to hash strings:
def simple_hash(key, size):
    sum = 0
    for char in key:
        sum += ord(char)
        
    return sum % size
# In terms of hash collision utilizing open addressing (linear probing), 
# we can handle collisions by finding the next available slot.
def insert(hash_table, key, value):
    index = simple_hash(key, len(hash_table))
    
    while hash_table[index] is not None:
        if hash_table[index][0] == key:
             # Update
            hash_table[index] = (key, value)
            return
        # Move to the next slot
        index = (index+1) % len(hash_table) 
    
    # Insert new item
    hash_table[index] = (key, value)


# 3.2   Walkthrough your function with an example where there is no hash collision.
# Example: 
simple_hash("CFG", 10) 
# ASCII values are: 'C' = 67, 'F' = 70, 'G' = 71. The sum is 67 + 70 + 71 = 208.
# tresults in `208 % 10 = 8`. So, the "CFG" key is hashed to the 8th index in the hash table:
# It will look like: [None, None, None, None, None, None, None, None, ("CFG", value), None]


# 3.3    Walkthrough your function with an example of a hash collision
# We can assume we already have the "CFG" key stored in the hash table. Now, we plan to insert another key, "GFC". 
# This key has the same ASCII sum as "CFG", which is 208. Therefore, when we hash "GFC", it results in the same hash (8).
# But during our insertion process, we find that the 8th index in the hash table is already occupied by "CFG". 
# So, we resolve this collision by moving to the next index—found by taking `(8+1) % 10 = 9`.
# Our hash table will become:
# [None, None, None, None, None, None, None, None, ("CFG", value1), ("GFC", value2), None]


# Section 4: Coding Challenge - OOP [25 points]
# 4.1    Design a parent class called Planet
class Planet:
    def __init__(self, name, distance_from_sun, planet_type):
        self.name = name
        self.distance_from_sun = distance_from_sun # in km
        self.planet_type = planet_type
    
    def get_distance_to_earth(self):
        # Assuming the distance from the sun to the earth is 147 million km
        distance_to_earth = abs(self.distance_from_sun - 147_000_000)
        return {'distance to earth': distance_to_earth}

# 4.2    Design a child class called Mercury, which inherits from the Planet class
class Mercury(Planet):
    @staticmethod
    def happy_new_year():
        print("A year in Mercury lasts 88 Earth days!")
# test
mercury = Mercury('Mercury', 58_000_000, 'Terrestrial')

print(mercury.name)
print(mercury.distance_from_sun)
print(mercury.planet_type)
print(mercury.get_distance_to_earth())
mercury.happy_new_year()



# 4.3    Design a child class called Jupiter, which inherits from the Planet class
class Jupiter(Planet):
    def __init__(self, name, distance_from_sun, planet_type, number_of_moons):
        super().__init__(name, distance_from_sun, planet_type)
        self.number_of_moons = number_of_moons

    @staticmethod
    def happy_new_year():
        print("A year in Jupiter lasts 4,332.59 Earth days!")
# test
jupiter = Jupiter('Jupiter', 778_500_000, 'Gas giant', 79)

print(jupiter.name)
print(jupiter.distance_from_sun)
print(jupiter.planet_type)
print(jupiter.number_of_moons)
print(jupiter.get_distance_to_earth())
jupiter.happy_new_year()
