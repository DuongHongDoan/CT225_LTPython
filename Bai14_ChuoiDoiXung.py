str = input("Nhap vao 1 chuoi: ")
lis = list(str)
lis.reverse()
newStr = ''.join(lis)
if str == newStr:
    print("Chuoi cho doi xung")
else:
    print("Chuoi cho khong doi xung")