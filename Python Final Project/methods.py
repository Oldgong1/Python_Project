max_withdrawal=2000
fammy_momo_account={'name':'fammy','balance':3000,'pin':1234,'number':'0247999531'}
tammy_momo_account={'name':'Frimpong','balance':10000,'pin':2345,'number':'0506226661'}
momo_account = {'0244444444':fammy_momo_account,'0255555555':tammy_momo_account}
momo_account2 = {'1234':fammy_momo_account,'2345':tammy_momo_account}



def get_selection():
    options = "  Welcome to momo\n  =========================\n  Press 1 to check balance\n  Press 2 for Withdrawal\n  Press 3 for Deposit\n  Press 4 to Transfer\n  Press 5 for account details\n  ============================\n  choose an option: "
    
    selection = input(options)
    if selection == '1':
        return 1
    elif selection == '2':
        return 2
    elif selection == '3':
        return 3
    elif selection == '4':
        return 4
    elif selection == '5':
        return 5
    else:
        print("  Select a valid option")
        print(main())


def check_balance():
    verify = input('\n''Please enter your 4 digit pin: ')
    verified = momo_account2.get(verify)
    if verified:
        print('Your account balance is GHc{}'.format(momo_account2[verify]['balance']))
        print(main())
    elif verify != momo_account2:
        print('Invalid pin!')


    

def withdrawal():
    number = input('\n''Please enter your mobile number: ')
    verify = input('Please enter your 4 digit pin: ')
    verify2 = input('Confirm your 4 digit pin: ')
    verified = momo_account2.get(verify) and momo_account.get(number) 
    if verify == verify2:
        print()
        
    
    elif verify != verify2:
        print('Your pin does not match!')
        exit()
    if verified:
        (int(input('Enter 1 to continue: ')))
        subtraction = input('Enter withdrawal amount: ')
        if int(subtraction)>momo_account2[verify]['balance']:
            print('Your amount is greater than your balance')
        elif int(subtraction)<momo_account2[verify]['balance']:
            momo_account2[verify]['balance'] = momo_account2[verify]['balance'] - int(subtraction)
            print('Your account balance is GHc{}'.format(momo_account2[verify]['balance']))
            print(main())
    else:
        print('Invalid account')
    

def deposit():
    verify = input('\n''Enter your mobile number: ')
    verified = momo_account.get(verify)
    if verified:
        addition = input('Please Enter the amount you want to deposit: ')
        momo_account[verify]['balance'] = momo_account[verify]['balance'] + int(addition)
        print('your account balance is Ghc{}'.format(momo_account[verify]['balance']))
        print(main())
    else:
        print('invalid account')
        
            
    

def transfer():
    verify = input('\n''Enter your pin: ')
    verify2 = input('Confirm your pin: ')
    verified = momo_account2.get(verify)
    if verify == verify2:
        (int(input('Enter 1 to continue: ')))
    else:
        if verify!= verify2:
            print('Pins do not match!')
            print(main())
        
    if verified:
        to = input('Enter mobile number: ')
        to2 = input('Confirm mobile number: ')
        if to == to2:
            subtraction = input('Enter transfer amount: ')
            input('Enter reference: ')
            print('You are about to transfer this amount GHc{} to this number {},'.format(subtraction,to))
            input('Enter 1 to confirm or 2 to cancel: ')
            momo_account2[verify]['balance'] = momo_account2[verify]['balance'] - int(subtraction)
            print('You have transfered this amount Ghc{} to this number {}, your account balance is GHc{}'.format(subtraction,to,momo_account2[verify]['balance']))
            print(main())
        elif to != to2:
            print('\n''Numbers do not match')
            
        


def getAccount():
    verify = input('Please enter your 4 digit pin: ')
    verify2 = input('Confirm your 4 digit pin: ')
    verified = momo_account2.get(verify)
    if verify == verify2:
        print()
        
    
    elif verify != verify2:
        print('Your pin does not match!')
        exit()
    if verified:
        print(momo_account2[verify])
        print(main())
    else:
        print('invalid account')
        exit()
    
    
    
    
            
def main():
    transaction = get_selection()
    if transaction == 1:
        check_balance()
        return
    elif transaction == 2:
        withdrawal()
        return
    elif transaction == 3:
        deposit()
        return
    elif transaction == 4:
        transfer()
        return
    elif transaction == 5:
        getAccount()
        return
    if __name__ == "_main_":
        main()
        
print(main())

    


    
            
    
        
            
            
            
            
        
        
        
    
        
    
    





                            
                    
                    
                
                
        
                 
                
                
                
                    
                    

