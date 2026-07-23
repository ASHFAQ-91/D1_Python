# String function in Python.
name = "masq Ashfaq"
xyz = "orion"

#$ 1. len() - length
print("1", len(name))   # lenght function start counting from the 1, not 0.

#$ 2. str.endswith('')
print("2", name.endswith('faq'))     # true or false.

#$ 3. str.count('')
print("3", name.count('A'))  # occurrences of any character.

#$ 4. str.capitalize()
print("4", xyz.capitalize())  # Capitalize the first letter.

#$ 5. str.find('')
print("5", name.find('sh'))  # returns the index of first occurrence

#$ 6. str.replace('')
print("6", name.replace('q', 'k'))   # replace the old word with new word

#$ 7. str[inclue, exclude]
print("7", name[0: 7])

#$ 8. str.upper() & str.lower()
print("8", xyz.upper())
print("8", xyz.lower())

#$ 9. str.split('')
xyz = "Hello! My name is MASQ"
print("9", xyz.split(" "))

#$ 10. str.center(50)
print("10", name.center(50))  # center() method aligns the string to the center.

#$ 11. str.isalnum()
xyz = "WelcomeToTheConsole911"
print("11", xyz.isalnum())

#$ 12. str.isalpha()
print("12", xyz.isalpha())

#$ 13. str.islower()
print("13", xyz.islower())

#$ 14. str.isspace()
print("14", name.isspace())  # return True if only 'space' contain.

#* 11. isalnum() method -  returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.
#* 12. isalpha method -  returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False.