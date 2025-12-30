# Sum of natural numbers 

def sumNatural(n):
    if(n == 0):
        return 0
    else:
        return n + sumNatural(n-1)


num = int(input("Enter number: "))
print(sumNatural(num))

