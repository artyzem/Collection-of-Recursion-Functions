# Recursively calculate factorial
def factorial(n):
  if n < 2:
    return 1
  return n*factorial(n-1)

print(factorial(5)) # Returns 120!


# Recursively calculate Fibonacci numbers
def fibonacci(n):
  if n == 1:
    return 1
  if n == 0:
    return 0
  return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(15)) # Returns 610!


# Given a list with nested lists, return a list with all elements in just 1 list
def flatten(my_list):
  result = []
  for item in my_list:
    if isinstance(item, list):
      print("List found!")
      flat_list = flatten(item)
      result.extend(flat_list) 
    else:
      result.append(item)
  return result

planets = ['mercury', 'venus', ['earth'], 'mars', [['jupiter', 'saturn']], 'uranus', ['neptune', 'pluto']]

print(flatten(planets)) # Returns list with no nested lists!


# Given a list of elements, use recursion to return its power set
def power_set(my_list):
    # base case: an empty list
    if len(my_list) == 0:
        return [[]]
    # recursive step: subsets without first element
    power_set_without_first = power_set(my_list[1:])
    # subsets with first element
    with_first = [ [my_list[0]] + rest for rest in power_set_without_first ]
    # return combination of the two
    return with_first + power_set_without_first
  
universities = ['Cambridge', 'Oxford', 'Warwick', 'Bath']
power_set_of_universities = power_set(universities)

for set in power_set_of_universities:
  print(set)


# Given a sorted list, create a binary search tree recursively
def build_bst(my_list):
  if my_list == []:
    return "No Child"
  middle_idx = len(my_list)//2
  middle_value = my_list[middle_idx]
  print("Middle index: " + str(middle_idx))
  print("Middle value: " + str(middle_value))
  tree_node = {"data": middle_value}
  tree_node["left_child"] = build_bst(my_list[:middle_idx])
  tree_node["right_child"] = build_bst(my_list[middle_idx + 1:])
  return tree_node

# For testing
sorted_list = [12, 13, 14, 15, 16]
binary_search_tree = build_bst(sorted_list)
print(binary_search_tree)
# Returns a dictionary of dictionaries, indicating left and right children of the tree!
