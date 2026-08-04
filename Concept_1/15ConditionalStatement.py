# Conditional Statement.
# 1. if
# 2. if-else
# 3. if-else-elif
# 4. nested if-else-elif

#$ if-else
print(f"*****Car Eligibility*****".center(40))
age = int(input("Enter your Age: "))

if(age>17):
    print("You can Drive.\n")
else:
    print("You can't Drive.\n")


#$ if-else-elif
print("*****Check Greater Value*****".center(40))
score = 91;
if score >= 80:
    print("Grade A")
elif score >= 60:
    print("Grade B")
else:
    print("Grade C")

print()
#$ nested-if-else
grocery = ["Cadbury", "Dora-cake", 7, 91.2, True]
if 7 in grocery:
    print("Yes, 7 is present")
    if "AS" in "MASQ":
        print("YES, AS is Pesent\n")
