lis = []
n = int(input("Nhap so luong phan tu trong danh sach: "))

for i in range(n):
    lis.append(int(input("Nhap phan tu thu " + str(i) + ": ")))

def Sum(lis):
    sum = 0
    for i in lis:
        sum += i
    return sum

print("Tong cac so trong danh sach la:", Sum(lis))