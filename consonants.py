# Count consonants in a string 

st = input("Enter string: ")
count = 0

for ch in st:
    if ch.isalpha and ch not in 'AEIOUaeiou':
        count += 1

print(count)