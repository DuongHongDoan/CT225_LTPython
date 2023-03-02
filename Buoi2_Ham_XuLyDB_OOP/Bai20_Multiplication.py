lis = []
n = int(input("Nhap so luong phan tu trong danh sach: "))

for i in range(n):
    lis.append(int(input("Nhap phan tu thu " + str(i) + ": ")))

def Multi(lis):
    multi = 1
    for i in lis:
        multi *= i
    return multi

print("Tong cac so trong danh sach la:", Multi(lis))