def read(lst, n):
    print("Enter ", n, "values")
    for i in range(n):
        element = int(input())
        lst.append(element)
    return lst


def display(lst):
    for i in lst:
        print(i, end=" ")


def findcount(lst):
    ecount = ocount = 0
    for i in lst:
        if i % 2 == 0:
            ecount += 1
        else:
            ocount += 1
    return ecount, ocount


lst1 = []
lst2 = []
n1 = int(input("Enter the size of the list 1:"))
read(lst1, n1)
n2 = int(input("enter the size of list 2:"))
read(lst2, n2)
print("List1 contents are:")
display(lst1)
print("list 2 contents are:")
display(lst2)
e1count, o1count = findcount(lst1)
e2count, o2count = findcount(lst2)
if e1count == e2count and o1count == o2count:
    print("List are symmetrical")
else:
    print("List are not symmetrical")
