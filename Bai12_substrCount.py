str = input("Nhap vao mot chuoi: ")
newStr = str.split()
count = {}
for i in newStr:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

print(count)