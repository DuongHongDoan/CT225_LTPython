dict1 = {
    1: 10,
    2: 20,
    7: 15
}

dict2 = {
    3: 30,
    4: 40,
    5: 35,
    6: 45
}

def concatenate(dict1, dict2):
    listItems1 = list(dict1.items())
    listItems2 = list(dict2.items())
    for i in listItems2:
        listItems1.append(i)
    print(dict(listItems1))

concatenate(dict1, dict2)