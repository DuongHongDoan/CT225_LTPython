dict = {
    "Coc": 15,
    "Oi": 10,
    "Mia": 7,
    "Cam": 12
}
def AsDict(dict):
    listValues = sorted(list(dict.values()))
    newDict = {}
    for i in listValues:
        for key, values in dict.items():
            if i==values:
                newDict[key] = values
    print("Sap xep tang:",newDict)
#Goi ham sap xep gia tri tang dan trong dict    
AsDict(dict)

def DesDict(dict):
    listValues = sorted(list(dict.values()), reverse=True)
    newDict = {}
    for i in listValues:
        for key, values in dict.items():
            if i==values:
                newDict[key] = values
    print("Sap xep giam:",newDict)
#Goi ham sap xep gia tri giam dan trong dict    
DesDict(dict)