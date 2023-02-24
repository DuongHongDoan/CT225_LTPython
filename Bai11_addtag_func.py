tag = input("Nhap tag html: ")
str = input("Nhap chuoi: ")

def add_tags(tag, str):
    print("<{0}>{1}</{0}>".format(tag, str))

add_tags(tag, str)