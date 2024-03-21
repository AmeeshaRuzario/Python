filename = input("enter the filename:")
f1 = open(filename)
lcount = wcount = ccount = 0
for line in f1:
    lcount = lcount+1
    lst = line.split()
    wcount = wcount+len(lst)
    for word in lst:
        ccount = ccount+len(word)

print("linecount:", lcount)
print("wordcount:", wcount)
print("charcount:", ccount)
f1.close()
