ipstr = input("enter the string:")
pattern = '’!()-[]{};:’’’,\,<>,/,?,@,#,$,%^&*_~'
opstr = ""
for ch in ipstr:
    if ch not in pattern:
        opstr = opstr+ch
print("ipstr:", ipstr)
print("opstr:", opstr)
