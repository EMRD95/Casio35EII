num1 = int(input("Entrez le premier nombre : "))
num2 = int(input("Entrez le deuxième nombre : "))

if num1 > num2:
    minNum = num2
else:
    minNum = num1

for i in range(minNum, 0, -1):
    if(num1 % i == 0 and num2 % i == 0):
        print("Le pgcd est ", i)
        break