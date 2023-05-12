class product:
    Product_company = 'RioTinto'
    def __init__(self,prdid,prdname,prdqnty):
        self.prdid = prdid
        self.prdname = prdname
        self.prdqnty = prdqnty
        self.price = 475

    @classmethod
    def prduct_name_cal(cls):
        cls.Product_company = 'RioTint0 ltd'

    @staticmethod
    def total_qnty_price_cal(p,q):
        qnty_price = p*q
        return qnty_price
    def show(self):
        print('Product id::',self.prdid)
        print('Product name::',self.prdname)
        print('Product qnty::',self.prdqnty)
        print('Product price::',self.price)
        tqpc = self.total_qnty_price_cal(self.prdqnty,self.price)
        print('TQPC::',tqpc)
        print('product company name before ::',product.Product_company)
        self.prduct_name_cal()
        print('Pruduct company name after::',product.Product_company)

obj = product(101,'Copper',150)
obj.show()