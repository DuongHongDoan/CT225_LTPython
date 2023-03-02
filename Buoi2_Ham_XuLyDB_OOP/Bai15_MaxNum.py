n = int(input("Nhap so luong phan tu trong danh sach: "))
lis = []
for i in range(n):
    lis.append(int(input("Nhap gia tri " + str(i) + ": ")))

def maxNum(lis):
    max = 0
    for i in lis:
        if i > max:
            max = i
    return max

print("So lon nhat trong danh sach la:", maxNum(lis))