def bsearch(lst, key):
    low = 0
    high = len(lst)-1
    while (low <= high):
        mid = (low+high)//2
        if key == lst[mid]:
            return mid+1
        elif key < lst[mid]:
            high = mid-1
        else:
            low = mid+1
    return -1


n = int(input("enter the size:"))
lst = []
print("enter the elements:")
for i in range(n):
    element = int(input())
    lst.append(element)
    lst.sort()
print("the lst is:")
print(lst)
for i in lst:
    print(i, end="")
key = int(input("Enter the key:"))
pos = bsearch(lst, key)
if pos == -1:
    print("Position not found")
else:
    print("the key", key, "is found at position:", pos)
