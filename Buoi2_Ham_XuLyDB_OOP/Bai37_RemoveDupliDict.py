dict1 = {
    1: 10,
    5: 30,
    2: 20,
    3: 30,
    4: 40,
    6: 10
}

newDict = {}
def removeDupli(dict1):
    for k, v in dict1.items():
        if v not in newDict.values():
            newDict[k] = v
    print(newDict)
    
removeDupli(dict1)
