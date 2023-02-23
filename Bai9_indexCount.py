str = input("Nhap vao 1 chuoi: ")

newStr = str.replace(" ", "") #thay the cho nao co cho trong thanh k co cho trong
lis = list(newStr) #tach tung chu trong chuoi ra thanh 1 danh sach
count = {}
for i in lis:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
print(count)