# Mutable  = can change, like List[].
# Immutable = can't change, like string & tuple().

fruits = ("apple", "banana", "orange");         # creating tuple.
print(fruits);          # Accessing Tuple.
print(fruits[1]);       # Tuple elements are accessed using indexes.
print(fruits[-1]);      # Accessing by negative indexing value.

numbers = (10, 70, 30, 40, 30)      # tuple
        #  0 ,  1,  2,  3,  4

#$ 1. Length function:-
print(f"\nCount length: {len(numbers)}");

#$ 2. "slice()", slicing is used to extract part of a tuple..
print("1st Slicing variable tuple: ", numbers[:])   # [include:exclude]
print("2nd Slicing variable tuple: ", numbers[1:4]) # [include:exclude]
print("3nd Slicing variable tuple: ", numbers[1:])  # [include:exclude]
print("4nd Slicing variable tuple: ", numbers[:4])  # [include:exclude]

#$ Count, index - same implimentation and working as list functions.