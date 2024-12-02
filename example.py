is_magician = False
is_expert = True

if((is_magician) and is_expert):
    print("you are a master magician")
elif(is_magician and (not(is_expert))):
    print("At Least you're getting there")
elif (is_magician):
    print("You are not a magician")



    # List , Set , Dictionary Comprehension
    some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']


duplicates = list(set([char for char in some_list if some_list.count(char) > 1]))
print(duplicates)


# List Comprehension: [char for char in some_list if some_list.count(char) > 1]

# This part creates a list comprehension that iterates over each character (char) in some_list and includes only those characters for which the count of that character in some_list is greater than 1. This effectively selects the duplicate elements from the list.
# Set Function: set(...)

# The list comprehension is then used as an argument to the set function. The set function creates a set, which is an unordered collection of unique elements.
# Since a set only contains unique elements, any duplicates in the list are automatically removed.
# List Function: list(...)

# Finally, the result is converted back to a list using the list function. This step is optional and is done to present the result as a list.
# Print the Result: print(duplicates)

# The duplicates list is then printed, which contains the unique duplicate elements from the original list.
# In summary, the code uses a combination of list comprehension, set creation, and list conversion to efficiently 
# find and print the unique duplicate elements from the original list some_list.
# strip() Method
# Remove Leading and Trailing Spaces Using the strip() Method
# The Python String strip() method removes leading and trailing characters from a string. The default character to remove is space
# Which method can be used to return a string in upper case letters? id upper()

# List  is collection  ordered, changeable, and allows duplicate members?



# the correct keyword to make the variable x belong to the global scope.


def myfunc():
  global x
  x = "fantastic"

# Insert the correct syntax to convert x into a complex number.

x = 5
x = complex(x)

age = 'Kevin'
txt = "My name is John, and I am {}"  #Can be used with String or numbers {}
print(txt.format(age))

fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]

fruits.update(more_fruits) # The update method  is used here to update the set fruits with the items of more_fruits
print(fruits)      # Output will be {'mango', 'banana', 'orange', 'grapes', 'apple', 'cherry'}



# In Python, both the `remove` and `discard` methods are used to remove elements from a set. 
# However, there is a key difference in how they handle the situation when the specified element is not present in the set.

### 1. `remove` Method:

# The `remove` method is used to remove a specified element from the set. If the element is not present, it raises a `KeyError`. Here's an example:


fruits = {"apple", "banana", "cherry"}

# Removing an existing element
fruits.remove("banana")
print(fruits)  # Output: {'apple', 'cherry'}

# Attempting to remove a non-existing element
try:
    fruits.remove("orange")
except KeyError as e:
    print(f"KeyError: {e}")


# In this example, the removal of "banana" is successful, but attempting
#  to remove "orange" raises a `KeyError` since "orange" is not present in the set.

### 2. `discard` Method:

# The `discard` method is used to remove a specified element from the set. 
    # If the element is not present, it does nothing (no error is raised). Here's an example:


fruits = {"apple", "banana", "cherry"}

# Removing an existing element
fruits.discard("banana")
print(fruits)  # Output: {'apple', 'cherry'}

# Attempting to remove a non-existing element
fruits.discard("orange")
print(fruits)  # Output: {'apple', 'cherry'}


# In this example, the removal of "banana" is successful, 
# and attempting to discard "orange" does nothing. The set remains unchanged, and no error is raised.

# # In summary, the key difference is that `remove` raises a `KeyError`
# #  if the element is not present, while `discard` does not raise any error 
# and simply does nothing in that case. Use `remove` when you expect the element to be present, and use `discard` 
# when the presence of the element is uncertain, and you want to avoid errors.


car.clear() # Here in case we have a dictionary this method help us to clear the dictionary




# Yes, `lambda` is a keyword in Python, and it is used to create anonymous functions, also known as lambda functions. 
# The `lambda` keyword allows you to create small, unnamed functions without using the `def` keyword.

# The syntax for a lambda function is as follows:


lambda arguments: expression


# Here's an example using your provided code:


x = lambda a: a
result = x(5)
print(result)


# In this example, a lambda function is assigned to the variable `x`. The lambda function 
# takes a single argument `a` and returns the value of `a`. When you call the lambda function with `x(5)`,
# # it returns `5`, and the result is printed.

# Lambda functions are often used for short, simple operations where a full 
# function definition with `def` would be overly verbose. They are commonly
#  used in functional programming constructs like `map`, `filter`, and `sorted`.