# String Basic.
#$ 1. String is IMMUTABLE, so its not allowed to change specific index value. But you can replace the whole string. 

var1 = "Salam"     # string
# var1[3] = "d"     #! This is not allowed.
var1 = "Bonjour"
print(var1);

#$ 2. f-String.
name = input("Whats your name: ");
work = "KAF"
live = "Dubai"

# Hacktic, more confusing & hard to read. 👎
print(name + " work at " + work + " and lives in " + live);

#* Easy (use this) 👍
print(f"{name} work at {work} and lives in {live}")

"""
f-strings (formatted string literals) are an easy and modern way to format strings in Python. They were introduced in Python 3.6.
To use an f-string, you add an f before the string and place variables or expressions inside {}.
"""