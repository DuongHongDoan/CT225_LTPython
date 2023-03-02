# lis = []
# n = int(input("Nhap vao so luong phan tu trong danh sach: "))

# for i in range(n):
#     lis.append(input("Nhap phan tu thu " + str(i) + ": "))
str = input("Nhap mot chuoi: ")
newStr = str.split(" ")
lis = list(newStr)

def RemoveDuplicate(lis):
    newList = []
    for i in lis:
        if i not in newList:
            newList.append(i)
    return newList

print("Danh sach sau khi xoa phan tu trung:", RemoveDuplicate(lis))