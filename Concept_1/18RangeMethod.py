# Range Method.
# range(start, stop, step_size)

for i in range(5):          # by default, (0: 5)
    print(i+1, end=" ")
    if(i+1==5):
        print()

for i in range(1, 9):       # start(include): 1, stop(exclude): 9.
    print(i, end=" ")
print()

for i in range(1, 20, 2):   # range(include, exclude, jump/step)
    print(i, end=" ")