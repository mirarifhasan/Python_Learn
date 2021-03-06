#Function

# Printing the round value
print(round(3.024))
print(round(-3.024))
print(min(1, 2, 3))


#If we call the function without parameter, it uses the default value
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()


#Array passing in function
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]
my_function(fruits)
