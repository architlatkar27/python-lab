#Write a program that asks users for their favorite color.
#Create the following output (assuming "red" is the chosen color).
#Use "+" and "*".
'''
    redredredredredredredredredred
    red                        red
    red                        red
    redredredredredredredredredred
'''
color=input("enter your favourite color ")
str1=color*10
str2=color+8*(len(color)*" ")+color
print(str1)
print(str2)
print(str1)
