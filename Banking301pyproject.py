class Bank():
    def __init__(self,amount):
        self.amount=amount
    def deposit(self,todeposit):
        old = self.amount
        if todeposit>0:
            self.amount+=todeposit
        with open('file.txt','a') as f:
            f.write(f'amount increased to {self.amount} from {old} increased by {todeposit}\n')
        return self.amount
    def withdraw(self,towithdraw):
        old = self.amount
        if towithdraw<=self.amount:
            self.amount-=towithdraw
        else:
            print('invalid')
            
        with open('file.txt','a') as f:
            f.write(f'amount decreased to {self.amount} from {old} decreased by {towithdraw}\n')
                
        return self.amount        
bank = Bank(2000)
while True:
    inp = input('w or d or b')
    amount = int(input('amount'))
    if inp=='w':
        print(bank.withdraw(amount))
    elif inp=='d':
        print(bank.deposit(amount))
    else:
        break        
