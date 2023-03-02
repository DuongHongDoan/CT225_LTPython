str = input("Nhap mot chuoi: ")
def reverseStr(str):
    newStr = ""
    for i in str:
        newStr = i + newStr
    return newStr

print("Chuoi nghich dao cua '{0}' la '{1}'".format(str, reverseStr(str)))