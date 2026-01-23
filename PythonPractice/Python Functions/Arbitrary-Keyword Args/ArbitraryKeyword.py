#Using **kwargs to accept any number of keyword arguments:
def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname="Tobias", lname="Refsnes")

#Accessing values from **kwargs:
def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function(name = "Tobias", age = 30, city = "Bergen")

#Using **kwargs with Regular Arguments
def my_function(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)

my_function("emil123", age = 25, city = "Oslo", hobby = "coding") 

#Combining *args and **kwargs in a function
def my_function(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:")
  print("Keyword arguments", kwargs)

my_function("User info", "Emil", "Tobias", age=25, city="Oslo")

#Function t
