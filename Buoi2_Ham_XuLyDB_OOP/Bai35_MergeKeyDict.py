#Khoa trong 2 dict giong nhau, thi khi merge lai chi lay khoa cua dict2
dict1 = {
    'a': 100, 
    'b': 200
}
dict2 = {
    'a': 300, 
    'y': 200,
    'a': 400
}
def mergeKey(dict1, dict2):
#Tu viet
    listKeys1 = list(dict1.keys())
    listKeys2 = list(dict2.keys())
    for key1 in listKeys1:
        for key2 in listKeys2:
            if key1==key2:
                listKeys1.remove(key1)
    for i in listKeys2:
        listKeys1.append(i)
    newDict = {}
    for i in listKeys1:
        for key, value in dict1.items():
            if i==key:
                newDict[key]=value
        for key, value in dict2.items():
            if i==key:
                newDict[key]=value
    print(newDict)
#Tham khao :<
    # dict3 = {k: v for d in (dict1, dict2) for k, v in d.items()}
    # print(dict3)
    
mergeKey(dict1, dict2)
