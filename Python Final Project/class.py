import random
saved_data={}
class Account:
    def __init__(self,balance):
        self.balance=balance
        self.balance=30000
        
        self.max_withdrawal=1000
        self.amount_today=0
        self.withdrawals_today=0
        self.limit_a_day=4
        


    def getBalance(self):
        print(self.balance)
    
    def withdraw(self):
        can_withdraw=True
        amount=int(input('enter amount here:'))
        if amount>self.max_withdrawal:
             can_withdraw=False
             print('Your amount is greater than the maximum withdrawals for the day')
        if amount>self.balance:
             can_withdraw=False
             print('Your amount is greater than your balance')
             
        if amount+self.amount_today>=self.max_withdrawal:
             can_withdraw=False
             print('You have reached the amount you can withdraw for today')
             
        if self.withdrawals_today>=self.limit_a_day:
             can_withdraw=False
             print('Youve reached the limit for today')
             
        else:
             self.withdrawals_today+=1
             self.amount_today+=amount
             self.balance -= amount
             print('Your new balance is {}.'.format(self.balance)) 






    def deposit(self):
        amount=int(input('Enter the amount you want to deposit here: '))
        new_balance=self.balance + amount
        
        print('Your new balance is {}'.format(new_balance))

    def transfer(self):
        can_transfer=True
        
        
        fammyNum = ('0247999531')
        tammyNum = ('0247999531')
        pin1=(input("Enter receiver's mobile number: "))
        pin2=(input("Confirm receiver's mobile number: "))
        tries = 1
        if tries == 1 and pin1!= pin2:
            can_transfer=True
            print('The number you enetered does not match!')
            
        if pin1 == pin2 == fammyNum and tries == 1:
                 (int(input('Enter 1 to continue:')))
                 amount=input('Enter amount:')
        elif pin1 == pin2 == tammyNum and tries == 1:
                 (int(input('Enter 1 to continue:')))
                 amount=input('Enter amount:')
                 
        else:
            print('Number does not exist!')
            exit()
        
               
        while pin1 == pin2:
             if tries < 3 and pin1!= pin2:
                 tries+=1
                 pin2=int(print('The number you enetered does not match'))
                 if tries == 3 and pin1!= pin2:
                     print()
             else:
                 if pin1 == pin2 and tries < 4:
                     input('Enter reference:')
                     print("You are about to transfer this amount GHc{} to this number {}".format(amount, pin1))
                     input('Enter 1 to confirm or 2 to cancel:')
            
                     print('You have transfered this amount GHc{} to this number {}'.format(amount, pin1))
                     pin=True
                     break
                    
    def getBalance(self):
        joePin = (1121)
        FrimpongPin = (1001)
        pin1=(int(input('Enter your pin: ')))
        pin2=(int(input('Confirm your pin: ')))
        tries = 1
        if tries == 1 and pin1!= pin2:
            print('The pin you enetered does not match! Back to Main Menu')
            
            
        if pin1 == pin2 == joePin  and tries == 1:
                 print('Your new balance is {}.'.format(self.balance))
        elif pin1 == pin2 == FrimpongPin  and tries == 1:
                 print('Your new balance is {}.'.format(self.balance))
        else:
            print('pin does not exist')

    def getAccount(self):
        fammyAccount = ('Josiah', 3000, 1121)
        tammyAccount = ('Frimpong', 3000, 1001)
        
        fammyPin = (1121)
        tammyPin = (1001)
        pin1=(int(input('Enter your pin: ')))
        pin2=(int(input('Confirm your pin: ')))
        tries = 1
        if tries == 1 and pin1!= pin2:
            print('The pin you enetered does not match! Back to Main Menu')
            
            
        if pin1 == pin2 == fammyPin  and tries == 1:
                 print('Your account is {}.'.format(fammyAccount))
        elif pin1 == pin2 == tammyPin  and tries == 1:
                 print('Your account is {}.'.format(tammyAccount))
        else:
            print('pin does not exist')
                 
        
        


def displayMenu():
    print('*'*50)
    print('\nWelcome to MOMO')
    print('\nChoose an option')
    print('\nPress 1 to withdraw')
    print('\nPress 2 to deposit')
    print('\nPress 3 to transfer')
    print('\nPress 4 to check balance')
    print('\nPress 5 to get account')
    print('\nPress 6 to quit\n')
   
    print('*'*50)


    



def momotransaction():
    keepOn = True
    while keepOn:
    
        displayMenu()
        userOption = int(input('Choose an option: '))
        a=Account(30000)

        if userOption == 1 :
            a.withdraw()    
        elif userOption == 2 :
            a.deposit()
        elif userOption == 3 :
            a.transfer()
        elif userOption == 4 :
            a.getBalance()
        elif userOption == 5 :
            a.getAccount()
        else:
            keepOn = False
            print('*'*50)
            print('\nGoodbye\n')
            exit()
            print('*'*50)
        







momotransaction()





