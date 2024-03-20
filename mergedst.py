str1 = input("Enter the string1:")
str2 = input("Enter the string2:")
str3 = " "
for ch in str1+str2:
    if ch.isupper():
        str3 = str3+ch
print("str1:", str1)
print("str2:", str2)
print("Str3:", str3)
