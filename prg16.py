import pandas as pd
import matplotlib.pyplot as plt
df1 = pd.read_csv("sample.csv")
total = df1.iloc[::, 1::].sum(1)
maxmarks = total.max()
maxidx = total.idxmax()
print("highest marks:", maxmarks)
print("student usn is:", df1.iloc[maxidx, 0])
sgrade = pd.Series()
agrade = pd.Series()
fgrade = pd.Series()
for i in range(1, len(df1.columns), 2):
    code = df1.columns[i][:5]
    total = df1.iloc[::, [i, i+1]].sum(1)
    scount = acount = fcount = 0
    for marks in total:
        if marks >= 90:
            scount += 1
        elif marks >= 80 and marks < 90:
            acount += 1
        elif marks < 40:
            fgrade += 1
    sgrade[code] = scount
    agrade[code] = acount
    fgrade[code] = fcount
x1 = []
x2 = []
x3 = []
w = 0.2
ticks = []
subcode = sgrade.index
for i in range(len(subcode)):
    x1.append(i)
    x2.append(i+w)
    x3.append(i+2*w)
    ticks.append(i+w)
plt.figure(figsize=(10, 7))
plt.bar(x1, sgrade, width=w, color='r', label="sgrade")
plt.bar(x2, agrade, width=w, color='g', label="agrade")
plt.bar(x3, fgrade, width=w, color='b', label="fgrade")
plt.xticks(ticks, subcode)
plt.xlabel("ssds")
plt.ylabel("no os students")
plt.title("top")
plt.legend()
plt.show()
