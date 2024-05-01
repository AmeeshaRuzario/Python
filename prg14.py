class country:
    def __init__(self, name, capital, population):
        self.__name = name
        self.__capital = capital
        self.__population = population

    def display(self):
        print("Capital:", self.__capital)
        print("Population:", self.__population)


clist = []
cname = []
plist = []
while True:
    print("\nEnter")
    print("1:Enter Details\n2:Get Capital")
    print("3:Highest population\n4:Exit\n")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        name = input("enter the country name:")
        if name in cname:
            print("country already exists")
        else:
            capital = input("enter the capital:")
            population = int(input("enter the population:"))
            new = country(name, capital, population)
            clist.append(new)
            cname.append(name)
            plist.append(population)
    elif ch == 2:
        name = input("enter the country name:")
        if name in cname:
            print("details:")
            index = cname.index(name)
            clist[index].display()
        else:
            print("country does nit exists")
    elif ch == 3:
        if len(plist) == 0:
            print("no data exists:")
        else:
            high = max(plist)
            index = plist.index(high)
            print("highest population :", high)
            print("country name is:", cname[index])
    else:
        break
