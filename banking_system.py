#loging in
username = input('Please enter the username: ').lower()
password = input('Please enter the password: ')
print('Logging in to your account...')
account_balance = 0

#amount deposition
def deposit(amount):
    global account_balance
    account_balance += amount
    print(f'Rs.{amount} credited to your account. Your available balance is Rs.{account_balance}')

#amount withdrwal
def withdraw(amount):
    global account_balance
    if amount > account_balance:
        print("Insufficient funds.")
    else:
        account_balance -= amount
        print(f'Rs.{amount} debited from your account. Your account balance is Rs.{account_balance}')

#balance checking
def check_balance():
    global account_balance
    print(f'Your account balance is Rs.{account_balance}')

#password changing
def change_password():
    global password
    old_password = input('Enter your current password: ')
    if old_password == password:
        new_password = input('Enter your new password: ')
        password = new_password
        print('Your password has been changed.')
    else:
        print('Incorrect password. Please try again.')

while True:
    print('Select your option:')
    print('1. Deposit amount\n2. Withdraw amount\n3. Check balance\n4. Change password\n5. Logout')
    choice = input('Select an option: ')
    if choice == '1':
        amount = int(input('Enter the amount you want to deposit: '))
        deposit(amount)
    elif choice == '2':
        amount = int(input('Enter the amount you want to withdraw: '))
        withdraw(amount)
    elif choice == '3':
        check_balance()
    elif choice == '4':
        change_password()
    elif choice == '5':
        print('Logging out.')
        break
    else:
        print('Invalid option. Please select again.')
