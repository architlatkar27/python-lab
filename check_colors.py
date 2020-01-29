'''Write a program that asks a user to input a color.
If the color is black or white, output "The color was black or white".
If it starts with a letter that comes after "k" in the alphabet,
output "The color starts with a letter that comes after "k" in the alphabet".
(Optional: consider both capitalized and non-capitalized words.
Note: the order of the alphabet in Unix and Python is: symbols, numbers, upper case letters, lower case letters.)'''

color=input("enter your favourite color ")
if color=="black" or color=="white":
    print("color was "+color)
else:
    if color[0]>'k':
        print("color starts with letter after k")
    else:
        print("color starts with letter before k")
