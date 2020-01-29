import random
count=5
lucky=random.randrange(1,10,1)
while count:
    guess=int(input("whats your guess? "))
    if guess==lucky:
        print("you have guessed correctly")
        break
    elif count!=0:
        print("nope ! try again ")
    count-=1
print("the lucky number was {}".format(lucky))
