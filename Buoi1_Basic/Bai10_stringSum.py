str = input("Nhap chuoi so cach nhau boi dau \";\": ")
newStr = str.split(";")
print("Chuoi so da nhap:", str)
sum = 0
for i in newStr:
    sum += int(i)

print("Tong chuoi:", sum)