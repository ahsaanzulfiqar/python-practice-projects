import random
n = random.randint(1,5)
tries = 0
while True:
    guess = int(input("Enter number then check can you reach at random number:> "))
    if guess==n:
        tries+=1
        print(f"ohh!thats great you can find the random number {n}")
        break
    elif guess>n:
        tries+=1
        print("This is high! Go some little")
    elif guess<n:
        tries+=1
        print("This is low! Go some high")
    else:
        print("ooops! You don't find try again! ")
print(f"Yes this {n} is a random number that system generate and you find it in {tries} tries")