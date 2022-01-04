List = open("yeet.txt").readlines()
for i in range(len(List)):
    List[i] = List[i].lower()
DictNames = {}
for name in List:
    if name in DictNames:
        DictNames[name] += 1
    else:
        DictNames[name] = 1
def ReadableDict():
    for key in DictNames:
        print(key + ": " + str(DictNames[key]))
ReadableDict()
x = 0
for key in DictNames:
    x += 1
print(x)