import pandas as pd
import matplotlib.pyplot as plt
df1 = pd.read_csv("sample.csv")
avgscr = pd.Series()
for i in range(1, len(df1.columns), 2):
    code = df1.columns[i][:5]
    avg = (df1.iloc[::, i].mean(0)+df1.iloc[::, i+1].mean(0))/2
    avgscr[code] = avg
print("highest marks:", avgscr.max())
print("subject code:", avgscr.idxmax())
avgcie = df1.iloc[::, 1::2].mean(1)
avgsee = df1.iloc[::, 2::2].mean(1)
x1 = []
x2 = []
ticks = []
w = 0.2
usn = df1['USN']
for i in range(len(usn)):
    x1.append(i)
    x2.append(i+w)
    ticks.append(i+w/2)

# to set the graph size to prevent overlapping(width,height)
plt.figure(figsize=(10, 5))
plt.bar(x1, avgcie, width=w, color='r', label="CIE")
plt.bar(x2, avgsee, width=w, color='g', label="SEE")
plt.xticks(ticks, usn)  # to add usn label on x axis
plt.xlabel("Student USNs")
plt.ylabel("CIE vs SEE score")
plt.title("Student performance Average CIE vs SEE")
plt.legend()
plt.show()
