# Use different types of datatypes & concate the string var. as well as sum of 2 var.
var1 = "Hello Everyone"     # string
var2 = ", I'm MASQ."        # string
var3 = 4                    # int
var4 = 37.7                 # float
var5 = complex(8, 2)        # complex
var6 = True                 # boolean

print(var1)         # print variable value

print(type(var1))   # find datatype

print(var3 + var4)  # to add two variables

# print(var1 + var3)  #BUG: Error will show both are different data types.

print(var1 + var2)      # CONCATENATION 2 string


# Moderate Level
list1 = []
t1 = ()
d1 = {}

print("\n", type(list1))      # list (like JS array)

print(type(t1))         # tuple (immutable array)

print(type(d1))   # Dictionary (like JS Object)


#$ Strings are immutable