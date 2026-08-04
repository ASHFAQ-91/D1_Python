# A SET "does not allow duplicate values" and "does not maintain any specific order". 

se1 = set()                 # creating empty set.
print(type(se1))            # type
se1 = set(["Apple", "Mango"])   # creating set.
print(se1)

#* Adding value:-
#$ 1. "add()", Adds a single element to the set.
se1.add("Banana")
print(f"\n{se1}")

#$ 2. "update()", Add multi element to the set.
se1.update(["Guava", "Peach"]);
print(f"{se1}")

#* Deleting value:-
#$ 3. "remove()", Removes a specified element. Raises an error if the element does not exist.
se1.remove("Mango")
print(f"\n{se1}")

#$ 4. "pop()", Removes and returns a random element.
se1.pop()
print(f"{se1}")

#* Mathematical Operations:-
se1 = set([1,2,3])
se2 = set([3,4,5])
#$ 5. "Union()", Combines elements from both sets.
result = se1.union(se2)
print(f"\nUnion set: {result}");

#$ 6. "Intersection()", Returns common elements between sets.
result = se1.intersection({3,4,5})
print("Intersection value: ", result)

#$ Basic function:
# print("\nSets type: ", type(se1))
# print("\nSets Length: ", len(se1))
# print("Sets Max value: ", max(se1))
# print("Sets Min Value: ", min(se1))

#$ Type Casting:-
li = [10, 20, 30, 20]   # creating list
print(f"\n{li}")            # list_value
print(f"{type(li)}")        # type
li_to_se = set(li)      # converting to set
print(li_to_se)             # set_value
print(type(li_to_se))       # type