str = input("Nhap vao mot chuoi: ")
newStr = str.split(" ")

def represent(newStr):
    lis = []
    for i in newStr:
        if i not in lis:
           lis.append(i) 
    return lis
print("Danh sach cac phan tu dai dien:", represent(newStr))