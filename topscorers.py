dict = {
    "John": 78.4,
    "Jack": 90.4,
    "Jill": 99.5,
    "Harry": 80.5,
    "Addu": 87.9
}
mlist = list(dict.values())
mlist.sort(reverse=True)
sortdict = {}
sum = 0
for i in mlist:
    for key in dict.keys():
        if dict[key] == i:
            sortdict[key] = i
            sum = sum+i
            nlist = list(sortdict.keys())
print("Top 3 scorers")
for i in range(3):
    print(nlist[i], ":", mlist[i])
print("Average:", sum/len(dict))
