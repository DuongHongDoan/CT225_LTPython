lis = []
AscendList = []
n = int(input("Nhap vao so luong phan tu trong danh sach: "))

for i in range(n):
    lis.append(int(input("Nhap phan tu thu " + str(i) + ": ")))


def AscendSort(lis):
    for i in range(n):
        minNum = i
        for j in range(i+1, n):
            if (lis[j] < lis[minNum]):
                minNum = j
        lis[i], lis[minNum] = lis[minNum], lis[i]
    
AscendSort(lis)
print("Sap xep tang:", lis)

def DescendSort(lis):
    for i in range(n):
        minNum = i
        for j in range(i+1, n):
            if (lis[j] > lis[minNum]):
                minNum = j
        lis[i], lis[minNum] = lis[minNum], lis[i]
    
DescendSort(lis)
print("Sap xep giam:", lis)

# Khong viet ham
# lis.sort()
# AscendList = lis.copy()
# lis.reverse()
# DescendList = lis.copy()
# print("Sap xep tang dan:", AscendList)
# print("Sap xep giam dan:", DescendList)