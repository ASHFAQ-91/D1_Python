# use for loop in program.
list1 = [["MASQ", 6], ["Manu", 5], ["Yash", 4], ["Kanishk", 3]]

for item, meal_time in list1:
    print(item, "Eat food in a day ", meal_time)

dict1 = dict(list1)
print("\n")
for item, meal_time in dict1.items():
    print(item, "Eat food in a day", meal_time)

items = [int, float, "Masq", 2, 3, 4, 8, 10, 14, 25, 11, "%"]
print("\n")
for item in items:
    if str(item).isnumeric() and item > 10:
        print(item)
