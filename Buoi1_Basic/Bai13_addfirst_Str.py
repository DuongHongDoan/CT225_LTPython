
def addfirst(str):
    string =  """Bai thuc hanh 1\nHoc lap trinh Python\nThem chuoi vao dau tat ca cac dong\nHay viet ham!!!"""
    for i in string.split("\n"):
        i = str + i
        print(i)
    
str = input("Nhap chuoi noi: ")
addfirst(str)
# n = int(input("Nhap so dong: "))
    # lisStr = list()
    # for i in range(n):
    #     string = input("Nhap chuoi %d: " %(i))
    #     lisStr.append(string)
    # print("lisStr: ",lisStr)
    # newstr = ''.join(lisStr)
    # print("newstr: ",newstr)
    # print("newstr.split: ",newstr.split(" "))
    

    # for i in string.split("\n"):
    #     i = str + i
    #     print(i)