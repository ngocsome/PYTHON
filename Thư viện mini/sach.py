class Sach : 
    def __init__( self , ma_sach , ten_sach , tac_gia , nam_xb ) : 
        self.ma_sach = ma_sach 
        self.ten_sach = ten_sach 
        self.tac_gia = tac_gia 
        self.nam_xb = nam_xb 
    def __str__(self ) : 
        return f" {self.ma_sach} - {self.ten_sach } - {self.tac_gia} - {self.nam_xb}"