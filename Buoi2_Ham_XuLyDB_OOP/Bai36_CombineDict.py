dict1 = {
    'a': 100, 
    'b': 200
}
dict2 = {
    'a': 300, 
    'y': 200
}

def combine(dict1, dict2):
#Cach 1 :<
    listKeys1 = list(dict1.keys())
    listKeys2 = list(dict2.keys())
    for key1 in listKeys1:
        for key2 in listKeys2:
            if key2==key1:
                listKeys2.remove(key2)
                sumValue = dict1[key1] + dict2[key2]
                dict1[key1] = sumValue
    for i in listKeys2:
        listKeys1.append(i)
    newDict = {}
    for i in listKeys1:
        for key, value in dict2.items():
            if i==key:
                newDict[key]=value
        for key, value in dict1.items():
            if i==key:
                newDict[key]=value
    print(newDict)
#Cach 2:
    # dict = {**dict1, **dict2}
    # for key, value in dict.items():
    #     if key in dict1 and key in dict2:
    #         dict[key] = value + dict1[key]
    # print(dict)

combine(dict1, dict2)

