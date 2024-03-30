#Want to make a password AND store it so we can access it with "get password"
#Can probably do it by writing data to a file/appending and searching that file when need to retrieve
passwords = {} # Creates empty dictionary

def add_password(account, password):
    i = 0

    while i != 'stop':
        
        account = input("Input new account name: ")
        password = input("\nInput new password: ")
        passwords[account] = password # Dictionary where password is the label and  account is the value and password is the key
        print("\n These are your new accounts usernames and passwords:", passwords)

        stop_condition = input("\nInput 'stop' to stop or press any other key to continue: ")
        if (stop_condition == 'stop'):
            break
        else:
            continue
    return passwords # returns dictionary with passwords into the global passwords dictionary
#---------------------------------------------------------------------------------------------------------------
        

def get_password(account):
    account = input("Input account name to retrieve password: ")

    for account in passwords:
        return passwords[account]
    else:
        return "Account not found"
    
#----------------------------------------------------------------------------------------------------------------
a = 0
p = 0

passwords = add_password(a , p)
print("\n", passwords)

x = get_password(passwords)

print("\n the password for your selected account is: ", x)

passwords.append(x)

print(passwords)
