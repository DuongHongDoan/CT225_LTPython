import math
n = int(input("Nhap so luong phan tu trong danh sach: "))
lis = []

for i in range(n):
    lis.append(int(input("Nhap phan tu " + str(i) + ": ")))

lis.sort()
#Tim gia tri trung binh trong danh sach
def mean(lis):
    sum = 0
    for i in lis:
        sum += i
        avg = sum//len(lis)
    return avg

#Tim phan tu trung vi trong danh sach
def median(lis):
    if len(lis)%2 != 0:
        med = (len(lis)//2)
        print("Phan tu trung vi la:", lis[med])
    else:
        before = (len(lis)//2)
        after = before - 1
        med = (lis[after] + lis[before])//2
        print("Phan tu trung vi la:", med)

#Tinh do lech chuan
def standDevia(lis):
    m = mean(lis)
    newlis = []
    tongBinhPhuong = 0
    for i in lis:
        newlis.append(i-m)
    for i in newlis:
        tongBinhPhuong += i**2
    phuongSai = tongBinhPhuong/len(newlis)
    Deviation = math.sqrt(phuongSai)
    print("Do lech chuan la:", Deviation)

print("Gia tri trung binh la:", mean(lis))
median(lis)
standDevia(lis)