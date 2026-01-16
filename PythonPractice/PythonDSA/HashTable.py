
my_list = [None, None, None, None, None, None, None, None, None, None]

#step 2: Define a simple hash function
def hash_function(value):
    sum_of_chars = 0
    for char in value: 
        sum_of_chars += ord(char)
    return sum_of_chars % len(my_list)
print("'Bob' has hash code", hash_function("Bob"))  # Example usage

#step 3: Insert values into the hash table
def add(name):
    index = hash_function(name)
    my_list[index] = name
add("Bob")
print(my_list)

#Lookup values in the hash table
def contains(name):
    index = hash_function(name)
    return my_list[index] == name

#Handling Collisions 
#1: create a list of empty buckets(lists)
my_list = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    []
]

#2: Modify the add function to handle collisions
def add(name):
    index = hash_function(name)
    my_list[index].append(name)
add("Bob")
add("Alice")
print(my_list)