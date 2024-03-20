str = input("Enter the input string")
count = 0
for i in range(len(str)):
    if str[i].isupper():
        count += 1
        print("character ", str[i], " is at position ", i+1)
print("Total count :", count)
