class Tak_safare:
    def __init__(self,tedad_safar):
        self.tedad_safar = tedad_safar
    
    def use(self):
        if self.tedad_safar > 1:
            print("safar mojaz nist ")
        elif self.tedad_safar == 1 :
            print("safar mojaz ast")


class Credit_card:
    def __init__(self , tedad_safar , credit):
        self.credit = credit
        self.credit_remain = None
        super().__init__(tedad_safar)

    def credit(self):
        if self.tedad_safar > self.credit:
            print("tedad safar mojaz nist ")
        else:
            print("safar mojaz ast")

    def add(self,add_credit):
        self.add_credit = add_credit
        self.credit_remain = self.credit - self.tedad_safar +self.add_credit
        print(f'your totall credit id : {self.credit_remain}')
    


def menu():
    while  True:
        print("1- Tak safare\n2- Etebari\n3- Etebari/zamani ")
        key = int(input("ticket type : "))
        if key == 1:
            a = int(input("Tedad safar : "))
            x = Tak_safare(a)
            x.use()
        if key == 2:
            tedad_safar = int(input("Tedad safar : "))
            t_credit = int(input("enter totall credit :"))
            a = Credit_card(tedad_safar,t_credit)
            a.credit()
            x = int(input("enter credit to add in your card :"))
            a.add(x)


menu()