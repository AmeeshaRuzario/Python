n1 = int(input("Enter the value of n1:"))
f1 = 0
f2 = 1
count = 0
if n1 == 1:
    print("the first number in fibonacci series is : ", f1)
elif n1 == 2:
    print("The first 2 number in fibo series is: ", f1, f2)
else:
    print(" the fibonacci series :")
    while count < n1:
        print(f1)
        f3 = f2+f1
        f1 = f2
        f2 = f3
        count = count + 1
