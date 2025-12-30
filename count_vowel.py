# Count vowels in a string 

st = input("Enter string: ")
count = 0

for ch in st:
    if ch in 'AEIOUaeiou':
        count += 1

print(count)