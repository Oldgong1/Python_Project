#%%
print("*"*50)
print("\nWelcome to MOMO")
print("\nChoose from Options")
print("*"*50)
Tries = 3
momo_accounts = [123, 100, 'fammy']


tabmenu = "select an option number\n 1: Deposit\t 2: Withdrawal\t 3: Transfer\t 4: Check Balance\t"
selected_option = input(tabmenu)
if selected_option == '1':
    deposited_amount = input("Enter amount to be deposited\n")
    momo_accounts[1] = momo_accounts[1] - int(deposited_amount)
    print('Your new balance is {}'.format(momo_accounts[1])) 


elif selected_option == '2':
    can_withdraw = True
    max_withdrawal = 90
    amount = int(input('enter amount here:'))
    
    if amount > max_withdrawal:
      can_withdraw = False
      print('Your amount is greater than the maximum withdrawals for the day')
    if amount > momo_accounts[1]:
      can_withdraw = False
      print('Your amount is greater than balance')  
    else:
      if amount < momo_accounts[1]:
        momo_accounts[1] = momo_accounts[1] - int(amount)
        print('your balance is Ghc{}'.format(momo_accounts[1]) )
      #can_withdraw = True

elif selected_option =='3':
  pin = int(input('Enter your pin: '))
  if pin == momo_accounts[0]:
     number = input('Enter Mobile Number: ')
     amount = int(input('Enter amount: '))
     momo_accounts[1] = momo_accounts[1] - int(amount)
     print('You have transfered Ghc {} to {} your balance is Ghc{}'. format(amount,number,momo_accounts[1]))
  else:
    print('Invalid pin')


elif selected_option == '4':
  pin = int(input('Enter your pin: '))
  if pin == momo_accounts[0]:
    print('Your balance is Ghc {}'.format(momo_accounts[1]))
  else:
    print('Invalid pin')
  

    

  

    
       
            

       
  
   



  



     



  # %%
