# Dictionary is nothing but key value pairs.
d1 = {}           # creating empty dict
print(type(d1), "\n")   # type

d2 = {"MASQ":"Energy-Bar",
      "City":"Jaipur",
      "Frds":{"manu":"Ice-cream", "yash":"Pan", "kanu":"Juice"}}

#* READ
#$ 1. without method, throw an error if value doesnot exist.
print(d2)
print(d2["City"])
print(d2["Frds"]["yash"])
#$ 2. "get()", it safely retrieves a value, without giving error.
print(d2.get("City"))
print(d2.get("Frds", {}).get("yash"))

#* Update or Add value:-
#$ 1. - "without function", to Add/Update new value in Dictionary.
d2["City"] = "Dubai"
print(f"\nCity is {d2.get("City")}")

#$ 2. "update()", to Add/Update new value in Dictionary.
d2.update({"Avinash":"Burger"})
print("Added new Frd: \n", d2)

#* Delete value:-
#$ 1. "pop()", Removes a key and Returns its value.
print(f"\n{d2.pop("Avinash")}");
print(f"POP: {d2} ")

#$ 2. "del()", Removes a key and its value.
del d2["Frds"]["kanu"];
print(f"DELETE: {d2} \n")

#$ 3. "clear()", Remvoes all items form the dict.
# d2.clear();

# copy(), update(), 

# d3 = d2.copy()
# del d3["Yash"]
# print("\nCopy Function: \n", d2)

print(d2.keys())              # Return all keys.
print(d2.values())            # Return all values.
print(d2.items())             # Returns key value pairs as tuples.