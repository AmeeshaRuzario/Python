filename = input("enter the file name:")
f1 = open(filename)

print("marks of student:")
for line in f1:
    print("Subjects mark:", line)
    lst = line.split()
    total = 0
    for mark in lst:
        total = total+int(mark)
print("total marks:", total)
print("Average:", total/len(lst))
f1.close()
