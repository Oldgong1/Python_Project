#%%
print("WELCOME COME TO MOMO")
restart = ('y')
reload = 3
balance = 500
while reload >=0:
    pin = int(input('Enter your password to continue''\n'))
    if pin == (1234):
        print('Your been has been verified, continue: ')
        while restart not in ('n', 'NO', 'no', 'N'):
            print("*******************************************")
            print("=====  MOBILE MONEY TANSACTION SYSTEM  ====")
            print("*******************************************")
            print("========   1.    Check balance     ========")
            print("========   2.    Deposit Cash      ========")
            print("========   3.    Withdraw Cash     ========")
            print("========   4.    Transfer money    ========")
            print("========   5.    Quit              ========")
            print("*******************************************")
            option = int(input('select an option to continue''\n'))
            if option == 1:
                number = int(input('enter phone number' '\n'))
                print('Your account balance is Ghc', balance, '\n')
                restart = input('Would you like to go back?' '\n')
                if restart in ('n', 'NO', 'no', 'N'):
                    print('You are welcome')
                    break
            elif option == 2:
                print('Deposit')
                number = int(input('enter phone number' '\n'))
                deposit = float(input('How much are you depositing' '\n'))
                balance = balance + deposit
                print('\n Deposit sucessful, your balance is now Ghc ', balance)
                restart = input('Would you like to go back?''\n')
                if restart in ('n', 'NO', 'no', 'N'):
                    print('Thank you')
                    break
            elif option == 3:
                withdrawal = float(input('How much would you like to withdraw?''\n'))
                number = int(input('enter phone number' '\n'))
                number1 = int(input('repeat phone number' '\n'))
                balance = balance - withdrawal
                print('Withdrawal successful, balance is now Ghc', balance, '\n')
                restart = input('Would you like to go back?  ')
            if restart in ('n', 'NO', 'no', 'N'):
                    break
            elif option == 4:
                transfer = float(input('Enter amount to transfer''\n'))
                number = int(input('enter phone number' '\n'))
                number1 = int(input('repeat phone number' '\n'))
                balance = balance - transfer
                print('Amount sent successfuly'), print('your balance is now Ghc', balance, '\n')
                restart = input('Would you like to go back?  ')
                if restart in ('n', 'NO', 'no', 'N'):
                    break
            elif option == 5:
                if input("are you sure you want to quit? (y/n)" '\n') != "y":
                    exit()
                print('thanks for your time')
                break


# ============== end of momo account =============
# %%
