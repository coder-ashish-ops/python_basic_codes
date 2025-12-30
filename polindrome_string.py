# Palindrome string 

st = input("Enter your nume: ")
rev = st[::-1]

if(st == rev):
    print(f"Polindrome : {rev}")

else:
    print(f"Not polindrome: {rev}")
    