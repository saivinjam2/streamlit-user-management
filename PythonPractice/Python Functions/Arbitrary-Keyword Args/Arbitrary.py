#Arbitrary Arguments:
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

#Accessing Arguments:
def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_function("Emil", "Tobias", "Linus")

#Using *args with Regular Arguments
def my_function(greeting, *names):
  for name in names:
    print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus")

#Function that calculates the sum of all arguments
def my_function(*numbers):
  total = 0
  for number in numbers:
    total += number
  return total

#Finding the maxium value:
def my_function(*numbers):
    if len(numbers) == 0:   
        return None
    max_value = numbers[0]
    for number in numbers:
        if number > max_value:
            max_value = number
    return max_value

#fib_seq
def fib_seq(n):
    x = 0
    y = 1
    sequence = []
    for _ in range(n):
        sequence.append(x)
        temp = x
        x = y
        y = temp + y
    return sequence
print(fib_seq(10))