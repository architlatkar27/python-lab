#Write a script that asks a user for a number. The script adds 3 to that number.
#Then multiplies the result by 2, subtracts 4, subtracts twice the original number, adds 3, then prints the result.
num=int(input("enter a number "))
org=num
num+=3
num*=2
num-=4
num-=2*org
num+=3
print("result of this circus = {}".format(num))
