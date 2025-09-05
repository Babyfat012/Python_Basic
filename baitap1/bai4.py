str = input("Enter string str: ")
print("str = ", str)
print(type(str))
nn 
print("Length of str =", len(str))

# print(str[0])

text = str.strip()
print("Length of trimmed str =", len(text))

words = text.split()
print("words =", words)
print("Number of words =", len(words))
for word in words:
    print(word) 


k = int(input("Enter k: "))
if 0 <= k < len(str):
    i = 0
    print("First k characters: ", end="")
    while i < k:
        print(str[i], end="")
        i += 1

    h = 0
    j = len(str) - 1
    print()
    print("Last k characters: ", end="")
    while h < k:
        print(str[j], end="")
        h += 1
        j -= 1
else:
    print("k is out of range")

k2 = int(input("\nEnter index k2: "))
if 0 <= k2 < len(str):
    n = int(input("Enter n: "))
    print("String n elements from index k2: ", str[k2:k2 + n])
else:
    print("k2 is out of range")