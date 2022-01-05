# program to illustrate different set operation

# define a set by user
set1 = set(input("Enter the elements of set1: ").split())
set2 = set(input("Enter the elements of set2: ").split())

# set union
print("Union of set1 and set2: ", set1.union(set2))

# set intersection
print("Intersection of set1 and set2: ", set1.intersection(set2))

# set difference
print("Difference of set1 and set2: ", set1.difference(set2))

# set symmetric difference
print("Symmetric difference of set1 and set2: ",
      set1.symmetric_difference(set2))
