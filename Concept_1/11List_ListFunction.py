# Mutable  = can change, like List[], dictionary.
# Immutable = can't change, like String & Tuple().

fruits = ["apple", "banana", "orange"];         # creating list.
print(fruits);          # Accessing List.
print(fruits[1]);       # List elements are accessed using indexes.
print(fruits[-1]);      # Accessing by negative indexing value.
fruits[1] = "grapes";   # mutable, Modifying List Items.
print(fruits)


numbers = [10, 70, 30, 40, 30]
        #  0 ,  1,  2,  3,  4

#$ 1. Length function:-
print(f"\nCount length: {len(numbers)}");

#$ 2. slice_func.
print("1st Slicing variable list: ", numbers[:])        # [include:exclude]
print("2nd Slicing variable list: ", numbers[1:4])      # [include:exclude]
print("3nd Slicing variable list: ", numbers[1:])       # [include:exclude]
print("4nd Slicing variable list: ", numbers[:4])       # [include:exclude]

#* SORTING LIST:-
numbers.sort()
print("\nAscending Sort list: ", numbers)       #* It'll change the original list.

numbers.reverse()
print("Reverse variable list: ", numbers)       #* It'll change the original list.

#* FINDING ELEMENTS:-
#$ "index()", Returns the index of the first occurrence of a value
print("\nIndex value is: ", numbers.index(40))

#$ "count()", Counts how many times a value appears in the list.
print("Occurrence: ", numbers.count(30))

#$ "in()", Use the in keyword to check if an element exists in a list.
print("70" in numbers);

#* COPY LIST:-
#$ "copy()", Creates a shallow copy of the list.
num2 = numbers.copy()
num2[1] = 0 
print("\nCopy list: ", num2)

#* MIN & MAX:0
print("\nMaximum value: ", max(numbers))        #$ max_func.

print("Minimum value: ", min(numbers))          #$ min_func.


#* ADDING ELEMENTS:-
#$ 1. "Append()" Adds an element to the END of the list.
numbers.append(42)
print("\nAdd new value in list: ", numbers)

#$ 2. "Insert()" Add new value at a specific index. 1st value show the Index position.
numbers.insert(3, 69)
print("Insert new value in list: ", numbers)

#$ 3. "Extend()" Adds multiple elements from another list.
more_numbers = [100, 110]
numbers.extend(more_numbers)
print("Extend existing list: ", numbers)

#* REMOVE ELEMENTS:-
#$ 1. "Remove()" Removes the first occurrence of a value.
numbers.remove(30)
print("\nRemove value from the list: ", numbers)

#$ 2. "Pop()" Removes and returns an element at a given index. If NO index is provided, it removes the LAST element.
print(f"By default, Last value pop: {numbers.pop()}");          # delete by default.
print(numbers);
print(f"Removing value using Index value: {numbers.pop(6)}");   # delete by index value.
print(numbers);

#$ 3. "Clear()" Removes all elements from the list.
numbers.clear()
print(f"Empty list: {numbers}");