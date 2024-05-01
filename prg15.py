import matplotlib.pyplot as plt
f1 = open("keys.txt")
line = f1.readline()
keys = line.split()
f1.close()

f1 = open("marks.txt")
marks = []
name = []
print("ttoal marks of each subject is:")
for line in f1:
    ans = line.split()
    total = 0
    for i in range(1, len(ans)):
        if ans[i] == keys[i-1]:
            total = total+1
    print(ans[0], total)
    marks.append(total)
    name.append(ans[0])
high = max(marks)
index = marks.index(high)
print("top score:", high)
print("student name:", name[index])
r1 = r2 = r3 = 0
for values in marks:
    if values >= 0 and values <= 2:
        r1 += 1
    elif values >= 3 and values <= 6:
        r2 += 1
    else:
        r3 += 1
x = ["0-2", "3-6", "7-10"]
y = [r1, r2, r3]
plt.bar(x, y, width=0.2, color=['r', 'g', 'b'])
plt.title("performance mcq")
plt.xlabel("score")
plt.ylabel("no.of student")
plt.show()
