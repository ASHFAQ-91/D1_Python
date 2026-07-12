# Single Line, multiple line comments, Escape Sequence Character as well as how to print String.

# for Single line comment use Hashtag in the beginning.
"""
for
Multiple
Line Comment
write text btw the triple single or double Quote.
"""

# Escape Sequence Character like - \n, \t, \", sep="", end=""
# START:
print("Hello, \nMy name is \"Ashfaq\"")
print("Hey", 6, 7, sep="--||--")

print("St. Xavier", end="'s ")
print("College, Jaipur")
# END:


# Placeholder like - "pass", ellipsis - "...", docstring - """ """
if 50 > 20:
    pass        # no action is required.
else:
    print("else code") 

"""Placeholder:-
-In Python, Placeholder is a null statement. When it executes, absolutely nothing happens. Placeholder is used because Python relies on indentation to define code blocks (like loops, functions, and if statements). If you leave a code block completely empty, Python will throw a SyntaxError.

-Placeholder allows you to write syntactically correct code while leaving the actual implementation for later.

-Think of a placeholder as a "temporary stand-in." Its like putting a sticky note on a wall that says "I will hang a painting here later" so the wall doesn't look unfinished."""