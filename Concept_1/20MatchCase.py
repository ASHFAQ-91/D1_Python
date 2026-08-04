# Match case has similar characteristics as Switch case.
print("*****Alexa*****".center(40))
day = int(input("""
1. Which fruit is best for EYE:
2. Which fruit is best for HEART:
3. Which fruit is best for BRAIN:
4. Which fruit is best for UTERUS:"""))

match day: 
    case 1: print("Oranges is best for EYE.")
    case 2: print("Tomatos is best for HEART.")
    case 3: print("Blueberries is best for BRAIN.")
    case 4: print("Avacado is best for UTERUS.") 