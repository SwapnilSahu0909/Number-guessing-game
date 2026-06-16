import random
n=random.randint(1,100)
print("--------Welcome to Number Guessing Game---------")
guesses=0
a=-1
while(a!=n):
    guesses+=1
    a=int(input("Enter the number: "))
    if(a>n):
        print("Lower Number please")
    elif(a<n):
        print("Higher Number please")

print(f"You have guessed the number in {guesses} attempts")