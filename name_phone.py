'''Write a script that asks someone to input their first name, last name and phone number.'''
'''If the user does not type at least some characters for each of these, print "Do not leave any fields empty"
otherwise print "Thank you". (Hint: if a variable is empty, its value will be "false".)'''
'''Change the script so that the script prints "Thank you" if either the first name or the last name or the phone number is supplied.
Print "Do not leave all fields empty" otherwise.'''
'''Change the script so that only first name and last name are required. The phone number is optional.'''

accepted=False
while not accepted:
    fname=input("enter first name ")
    lname=input("enter last name")
    phone=input("enter phone number")
    if not phone or not lname or not fname:
        print("donot leave any field blank")
    else:
       print("your response was accepted")
       accepted=True
