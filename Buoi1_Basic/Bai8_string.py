str = input("Nhap vao 1 chuoi: ")

# in ra chiều dài chuỗi
print("Chieu dai chuoi la:", len(str))

#in ra ký tự đầu
print("Ky tu dau trong chuoi la:", str[0])

#in ra ký tự cuối
print("Ky tu cuoi trong chuoi la:", str[-1])

#in ra các ký tự từ vị trí i đến vị trí j
i = int(input("Nhap vao vi tri bat dau: "))
j = int(input("Nhap vao vi tri ket thuc: "))
print("Chuoi ky tu tu vi tri {0} den vi tri {1} la:".format(i,j), str[i:j])