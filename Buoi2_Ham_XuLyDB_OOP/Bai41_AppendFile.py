f = open("D:\hello.txt", "a")
str = input("Nhap vao mot chuoi: ")
f.write(str)
f.close()
f = open("D:\hello.txt", "r")
print(f.read())
f.close()