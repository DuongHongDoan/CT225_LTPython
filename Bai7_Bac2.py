import math
a = float(input("Nhap vao gia tri a: "))
b = float(input("Nhap vao gia tri b: "))
c = float(input("Nhap vao gia tri c: "))
if(a==0):
    if(b==0):
        if (c==0):
            print("Phuong trinh vo so nghiem")
        else:
            print("Phuong trinh vo nghiem")
    else:
        x = -c/b
        print("Phuong trinh co 1 nghiem duy nhat:", x)
elif (b==0):
    y = -c/a
    print("Phuong trinh co nghiem kep:", y)
else:
    delta = b*b - 4*a*c
    if delta < 0:
        print("Phuong trinh vo nghiem :<")
    elif delta == 0:
        z = -b/(2*a)
        print("Phuong trinh co nghiem kep:", z)
    else:
        x1=(-b + math.sqrt(delta))/(2*a)
        x2=(-b - math.sqrt(delta))/(2*a)
        print("Phuong trinh co 2 nghiem phan biet:", x1, " va", x2)
    
