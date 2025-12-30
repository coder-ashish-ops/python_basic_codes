# A number is prime 

num = int(input("Enter number: "))

if(num <= 1):
    print(f"Not prime: {num}")

else:
    for i in range(2,num):
        if(num % i == 0):
            print(f"Not a prime: {num}")
            break

    else:
        print(f"Prime: {num}")