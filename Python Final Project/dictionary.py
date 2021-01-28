#%%
fammy_momo_account = {'name': 'fammy', 'balance':234, 'pin': 1234}
tammy_momo_account = {'name': 'tammy', 'balance': 123, 'pin': 2345}
momo_account = {'0247999531': fammy_momo_account, '0506226661': tammy_momo_account}
momo_account2 = {'1234': fammy_momo_account, '2345': tammy_momo_account}

prompt_message = 'select an option number\n 1: Deposit\t 2:Cashout\t 3:Transfer\t 4: Check Balance\t'
selected_option = input(prompt_message)
if selected_option == "1":
    account = input('Enter your momo account: ')
    if account in momo_account:
        deposited_amount = input("Enter amount to be deposited\n")
        momo_account[account]['balance'] = momo_account[account]['balance'] + int(deposited_amount)
        print('Your new balance is {}'.format(momo_account[account]['balance']))
    else:
        print('Your account does not exist in our dictionary')

elif selected_option == "2":
    verify = (input('Enter your pin: '))
    verified=momo_account2.get(verify)
    if verified:
        amount = int(input('enter amount here: '))
        momo_account2[verify]['balance'] = momo_account2[verify]['balance'] - int(amount)
        print('Your new balance is Ghc{}'.format(momo_account2[verify]['balance']))
    else:
        print('Invalid pin')

elif selected_option == "3":
    verify = (input('Enter your pin: '))
    verified=momo_account2.get(verify)
    if verified:
        number = input('Enter momo account number: ')
        amount = int(input('Enter amount here: '))
        momo_account2[verify]['balance'] = momo_account2[verify]['balance'] - int(amount)
        print('You have transfered Ghc {} to {} your balance is Ghc{}'. format(amount,number,momo_account2[verify]['balance']))
    else:
        print('Enter correct pin') 

else:
    account = input('Enter your momo account: ')
    if account in momo_account:
        print('Your new balance is {}'.format(momo_account[account]['balance']))






            





#     print("Cashout")
# elif selected_option == "3":
#     print("Transfer Money")
# elif selected_option == "4":
#     print("Check Balance")

# def deposit():
#     print("Deposit called")
#     pin1 = input('Enter your pin')




      


# %%
