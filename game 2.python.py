import random
n = random.randint(1,100)
a = -1
guess = 0
while (a != n ):
    guess += 1
    a = int(input("guess the number : "))
    if (a>n):
        print("lower no please")
        guess +=1
    elif(a<n): 
        print("greater no pls")
        guess +=1
        
print(f"you have guess the no {n} correct in {guess} attempts")