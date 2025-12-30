# Palindrome number  

num = int(input("Enter number: "))
rev = 0
original = num

while(num > 0):
    digit = num % 10
    rev = (rev * 10) + digit
    num = num // 10

if(original == rev):
    print(f"Polindrome number: {rev}")

else:
    print(f"Not polindrome: {rev}")
    


