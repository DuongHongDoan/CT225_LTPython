lis1 = []
n = int(input("Nhap so luong phan tu cua danh sach: "))
for i in range(n):
    lis1.append(int(input("Nhap phan tu thu " + str(i) + ": ")))

lis2 = []
m = int(input("Nhap so luong phan tu cua danh sach: "))
for i in range(m):
    lis2.append(int(input("Nhap phan tu thu " + str(i) + ": ")))

lis1.sort()
List1 = lis1.copy()
lis2.sort()
List2 = lis2.copy()

def merge(List1, List2):
    mergeList = []
    a = 0
    b = 0
    while a < len(List1) and b < len(List2):
        if List1[a] < List2[b]:
            mergeList.append(List1[a])
            a+=1
        else:
            mergeList.append(List2[b])
            b+=1
    while a < len(List1):
        mergeList.append(List1[a])
        a+=1
    while b < len(List2):
        mergeList.append(List2[b])
        b+=1 
    return mergeList
mergeList = merge(List1, List2)
mergeList.sort()
newAsList = mergeList.copy()
mergeList.reverse()
newDesList = mergeList.copy()
print("Danh sach sau khi merge tang dan:", newAsList)
print("Danh sach sau khi merge giam dan:", newDesList)