import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("placement.csv")
branchtotal = df.iloc[:, 1::].sum(axis=1)
bmax = branchtotal.max()
bidx = branchtotal.idxmax()
print("Highest branch placement:", bmax)
print("Name of the branch:", df.iloc[bidx, 0])

companytotal = df.iloc[:, 1::].sum()
print("Highest placement companywise:", companytotal.max())
print("companytotal:", companytotal.idxmax())

maxnumber = df.iloc[:, 1::].max(axis=1)
maxidx = df.iloc[:, 1::].idxmax(axis=1)

dct = {"company ": maxidx,
       "count ": maxnumber
       }
df2 = pd.DataFrame(data=dct)
df2.index = df["Branch"]
print(df2)

plt.Figure(figsize=(8, 8))
plt.pie(branchtotal, labels=df2.index)
plt.show()

plt.Figure(figsize=(8, 8))
plt.pie(companytotal, labels=df.columns[1:])
plt.show()
