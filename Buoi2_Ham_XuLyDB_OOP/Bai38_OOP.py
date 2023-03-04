class SinhVien:
    def __init__(self, fullname, gender):
        self.fullname = fullname
        self.gender = gender
    def diemdanh(self):
        print("%s: Toi la sinh vien nganh khac" %self.fullname)
class SV_CNTT(SinhVien):
    def diemdanh(self):
        print("%s: Toi la sinh vien CNTT" %self.fullname)
class SV_MMT(SinhVien):
    def diemdanh(self):
        print("%s: Toi la sinh vien TT-MMT" %self.fullname)

sv1 = SinhVien("Tran Van B", "nam")
sv1.diemdanh()

sv2 = SV_MMT("Duong Hong Doan", "nu")
sv2.diemdanh()
sv4 = SV_MMT("Duong Van Doan", "nam")
sv4.diemdanh()

sv3 = SV_CNTT("Nguyen Van A", "nam")
sv3.diemdanh()