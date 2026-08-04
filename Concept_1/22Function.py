# User-defined Function.
# 1. Required/With Argument.
# 2. Default Argument.
# 3. Keywords Argument.
# 4. Variable length Argument.

#$ 1. With Argument function.
def greet(fname, lname):  # func_definition with Required_Argument.
    print(f"Good morning {fname} {lname}")

greet("MASQ_", "Ashfaq")    # func_call


#$ 2. Default Argument function.
def hello(name="User"):
    print(f"Hello {name}");
hello();

def add(a, b):
    return a+b; 

c = add(10, 20)
print("After return: ", c)