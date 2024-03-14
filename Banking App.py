import pickle
import os
import pathlib
import datetime


class Account:
    currenttime = datetime.datetime.now()
    formattedtime = currenttime.strftime("%Y-%m-%d %H:%M:%S")
    accNo = [0]
    firstname = ""
    lastname = ""
    dob=""
    deposit = 0
    interest = 0
    type = ""
    password = ""
    passwordconifrm = ""
    address = ""
    phone = [""]
    street = [""]
    currenttime = ""

    def createAccount(self):
        # infromation needed upon creation of account
        self.accNo = input("Enter the account no : ")
        self.address = input("Enter Address: ")
        self.street = input("Enter street number only: ")
        self.phone = input("Enter phone number: ")
        self.firstname = input("Enter the account holder First name : ")
        self.lastname = input("Enter the account holder Last name : ")
        self.dob= input("Enter your date of birth in dd/mm/yy format: ")
        self.deposit = int(input("Enter The Initial amount(>=500 for Saving and >=1000 for current):"))
        self.password = input("Enter a 4 digit password: ")
        self.passwordconfirm = input("Re-enter the same password: ")
        # password needed to Activate account
        while self.passwordconfirm != self.password:
            print("\n\nThe passwords did not match please try again")
            self.password = input("Enter a 4 digit password: ")
            self.passwordconfirm = input("Confirm password: ")
            break
        self.passwordconfirm = self.password
        currenttime = datetime.datetime.now()
        formattedtime = currenttime.strftime("%Y-%m-%d %H:%M:%S")

        print("Account created sucessfully on:", formattedtime)


def intro():
    print(
        "\t\t\t\t*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*\n\t\t\t\t-----WelCOME TO ʕ•ᴥ•ʔ BEAR BANK-----\n\t\t\t\t*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*"
    )


# creating a class called an account
def writeAccount():
    account = Account()
    account.createAccount()
    writeAccountsFile(account)


# We created fuction for System Administration so that they can get acces to every accounts that exists
# Bank officials can access this accounts list too.
def displayAll():
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open("accounts.data", "rb")
        mylist = pickle.load(infile)
        for item in mylist:
            print(
                "__________________________________________________________________________________________________________________________________________________________________________________________________________________________________________"
            )
            print(
                f"ACCOOUNT Number: {item.accNo}      ||First name: { item.firstname}     ||Lastname: {item.lastname}         ||ACCOUNT TYPE: {item.type}||INTERESt RATE: {item.interest} ||AVAILABLE BALANCE: ${item.deposit}     ||Address: {item.address}            ||Tel: {item.phone} ||Time: {item.formattedtime}"
            )
            print(
                "__________________________________________________________________________________________________________________________________________________________________________________________________________________________________________"
            )

        infile.close()
    else:
        print("No records to display")


# this is used to check balance
# you will need your account number and password to check balance
# anyone with account number and password can display the balance
def displayBal(num, num2):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open("accounts.data", "rb")
        mylist = pickle.load(infile)
        infile.close()
        for item in mylist:
            if item.accNo == num:
                if item.passwordconfirm == num2:
                    print(
                        f"Your account Balance is:$ {item.deposit} on {item.formattedtime}"
                    )
                else:
                    print("Either you user account or password is incorrect ! ")
                    print("TRY AGAIN!")
    else:
        print("No records to Search")


# This function is used to deposite money
# without password and account number you cannot deposite money
def makeadeposit(num, num2):
    file = pathlib.Path("accounts.data")
    mylist = []
    if file.exists():
        infile = open('accounts.data', 'rb')
        mylist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in mylist:
            if item.accNo == num:
                if item.passwordconfirm == num2:
                    amount = int(input("Enter the amount to deposit : "))
                    item.deposit += amount
                    print("Deposit Sucessfull! 🎉 🎊 ")
                    print(f"Your new balance is $ {item.deposit} on {item.formattedtime}")
                else:
                    print(" Either user password is wrong")
            break
    else:
        print(" We do not have account with that information")
    outfile = open('newaccounts.data', 'wb')
    pickle.dump(mylist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')


def withdrawmoney(num, num2):
    file = pathlib.Path("accounts.data")
    mylist=[]
    if file.exists():
        infile = open("accounts.data", "rb")
        mylist = pickle.load(infile)
        infile.close()
        os.remove("accounts.data")
        for item in mylist:
            if item.accNo == num:
                if item.passwordconfirm == num2:
                    amount = int(input("Enter the amount to Withdraw $: "))
                    if amount <= item.deposit:
                        item.deposit -= amount
                        print("Withdraw Sucessfull! 🎉 🎊 ")
                        print(
                            f"Your new balance is: ${item.deposit} on {item.formattedtime}"
                        )

                    else:
                        print("    Withdraw unsucessfull due insufficient Balance.  ")
                        print(f"   Please withdraw with in:  ${item.deposit}          ")

                else:
                    print("We do not have account with that information")
                    print("Please enter correct information")

    else:
        print(" We do not have account with that information")
    outfile = open("newaccounts.data", "wb")
    pickle.dump(mylist, outfile)
    outfile.close()
    os.rename("newaccounts.data", "accounts.data")


def deleteAccount(num, num2):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open("accounts.data", "rb")
        oldlist = pickle.load(infile)
        infile.close()

        newlist = []
        found = False
        for item in oldlist:
            if item.accNo == num and item.passwordconfirm == num2:
                found = True
            else:
                newlist.append(item)

        if not found:
            print(f"The account with number {num} does not exist. Deletion cancelled.")
            return

        os.remove("accounts.data")
        outfile = open("accounts.data", "wb")
        pickle.dump(newlist, outfile)
        outfile.close()
        print("Sad to see you go :(")
        print("Hope you will be back soon: :)")
        print("Account deleted successfully.")

def modifyAccount(num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        with open('accounts.data', 'rb') as infile:
            oldlist = pickle.load(infile)
        for item in oldlist:
            if item.accNo == num:
                item.firstname = input("Enter the account holder First name : ")
                item.lastname = input("Enter the Account Holder last Name: ")
                item.password = input("Enter your password:")
                item.passwordconfirm = input("re-enter the password:")
                if item.password == item.passwordconfirm:
                    print(f"Congratulations!,Changes saved successfully on: {item.formattedtime}")
                    break
                else:
                    print("Oops! we cannot accept your request please try again later")
                    print("Either your password or account number did not match")
                    return
        else:
            print("Account not found")
            return
        with open('newaccounts.data', 'wb') as outfile:
            pickle.dump(oldlist, outfile)
        os.rename('newaccounts.data', 'accounts.data')
    else:
        print("No accounts found")

# This function is used to re write the information and delete the old information
def writeAccountsFile(account):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open("accounts.data", "rb")
        oldlist = pickle.load(infile)
        oldlist.append(account)
        infile.close()
        os.remove("accounts.data")
    else:
        oldlist = [account]
    outfile = open("newaccounts.data", "wb")
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename("newaccounts.data", "accounts.data")


def bankOfficialLogin(user):
    while True:
        print("Enter Bank Official user name and password")

        username = input("UserName: ")
        password = input("Pass: ")

        for i in BANK_OFFICIAL:
            if (username == i["username"]) and (password == i["password"]):
                if user == "admin":
                    return username
                elif user == "official":
                    if i["enabled"] == False:
                        print(
                            "This account is disable, please login with a different account or re-enable"
                        )
                        return False
                    else:
                        return username

        print("Invalid login info")
        return False


def sysAdminLogin():
    while True:
        print("Enter System Admin user name and password")

        username = input("UserName: ")
        password = input("Pass: ")

        for i in SYS_ADMIN:
            if (username == i["username"]) and (password == i["password"]):
                return True
        print("Invalid login info")
        return False


def createBearAccount():
    print("Enter new user name and password")

    username = input("New User Name: ")
    password = input("New Password: ")

    BANK_OFFICIAL.append({"username": username, "password": password, "enabled": True})
    print("New Bear Official account added. User name is: ", username)


def createUserAccount():
    print("Enter new user name and password")

    username = input("New User Name: ")
    password = input("New Password: ")

    USER.append(
        {
            "username": username,
            "password": password,
            "lastLogin": "",
            "accounts": [],
        }
    )
    print("New user account added. User name is: ", username)


def userLogin():
    while True:
        print("Enter user name and password")

        username = input("UserName: ")
        password = input("Pass: ")

        for i in USER:
            if (username == i["username"]) and (password == i["password"]):
                i["lastLogin"] = datetime.datetime.now()
                print(i)
                return username
        print("Invalid login info")
        return False


def retrieveUser():
    firstName = input("Enter first name: ")
    lastName = input("Enter last name: ")

    for user in USER:
        for acc in user["accounts"]:
            if (acc.firstname == firstName) and (acc.lastname == lastName):
                return user
    print("No user with Given name")
    return False


SYS_ADMIN = [
    {"username": "admin", "password": "password", "enabled": True},
]


BANK_OFFICIAL = [
    {"username": "u1", "password": "p1", "enabled": True},
    {"username": "u2", "password": "p2", "enabled": False},
]

USER = [{"username": "h1", "password": "h1", "lastLogin": "", "accounts": []}]


ch = ""

num = 0
intro()

while True:
    user = int(
        input(
            "\t\t\t\t*_*_*_*_*_*_*_*_*_*_*_*_*_*\n\t\t\t\t       ʕ•ᴥ•ʔ  BEAR BANK\n\t\t\t\t*_*_*_*_*_*_*_*_*_*_*_*_*_*\n1.BANK OFFICIALS\n2.SYSTEM ADMINSTRATORS\n3.ACCOUNT HOLDER\n4. Exit\nChoose User type: "
        )
    )
    if user == 1:
        if bankOfficialLogin(user="official") == False:
            continue

        while True:
            print("\t                                                       ")
            print("  ┌────────────────┐  ╭───────────────────────╮           ")
            print("  |                |  | ▶︎ 0 • Add User account|            ")
            print("  │  ╭┼┼╮          │  │ ▶︎ 1 • Create Account  │           ")
            print("  │  ╰┼┼╮          │  ├───────────────────────┴─────╮     ")
            print("  │  ╰┼┼╯          │  │ ▶︎ 2 • DEPOSIT MONEY   │     ")
            print("  │                │  ├────────────────────────────┬╯     ")
            print("  │  B E A R       │  │ ▶︎ 3 • WITHDRAW MONEY  │      ")
            print("  │  B A N K       │  ├───────────────────────┬────╯      ")
            print("  │                │  │ ▶︎ 4 • BALANCE ENQUIRY  │           ")
            print("  │                │  ├───────────────────────┴────╮      ")
            print("  │                │  │ ▶︎ 5 • ALL ACCOUNT HOLDER LIST  │ ")
            print("  │                │  ├────────────────────────────┴╮     ")
            print("  │ ║│┃┃║║│┃║│║┃│  │  │ ▶︎ 6 • DELETE AN ACCOUNT  │     ")
            print("  │ ║│┃┃║║│┃║│║┃│  │  ├────────────────────┬────────╯     ")
            print("  │                │  │ ▶︎ 7 • MODIFY AN ACCOUNT  │     ")
            print("  |                |  | ▶                            |")
            print("  |                |  |      9. Exit                 |")
            print("  |                |  |   Choose an Option between 1 to 9")
            print("  └────────────────┘  ╰────────────────────╯              ")
            print("What is your pick: ")
            ch = input()

            if ch == "0":
                createUserAccount()
                # break
            elif ch == "1":
                writeAccount()
            elif ch == "2":
                if user == 1 or user == 3:
                    # this only allows the bank officials and customers to be able to make deposits on the account
                    # this will require password
                    num = input("\tEnter the Account number: ")
                    num2 = input("\tEnter the Password: ")
                    makeadeposit(num, num2)
                else:
                    print(" You can't perform this action")

            elif ch == "3":
                if user == 1:
                    num = input("\tEnter The account No. : ")
                    num2 = input("\tEnter the password: ")
                    withdrawmoney(num, num2)
                else:
                    print(" You can't perform this action")

            elif ch == "4":
                # to get the Balance you need a password from the account holder
                # only the valid Bear BAnk account holder can see the balance
                num = input("\tEnter The account No. : ")
                num2 = input("\tEnter the Password:")
                displayBal(num, num2)
            elif ch == "5":
                if user == 1 or user == 2:
                    displayAll()
                else:
                    print("  You can't perform this action")
            elif ch == "6":
                if user == 1:
                    num = input("\tEnter The account No. : ")
                    num2 = input("Enter the password: ")
                    deleteAccount(num, num2)
                else:
                    print(" You can't perform this action")
            elif ch == "7":
                if user == 1:
                    num = input("\tEnter The account No. : ")
                    num2 = input("Enter the password: ")
                    modifyAccount(num)
                else:
                    print(" You can't perform this action")

            elif ch == "9":
                print("\tThanks for using BEAR bank")
                break
            else:
                print("Invalid choice")

            # ch = input("\nEnter your choice (yes to go back to main menu ): ")

    if user == 2:
        while not sysAdminLogin():
            continue

        while True:
            print("│ ▶︎ 1 • Create Bear Official Account")
            print("│ ▶︎ 2 • Enable/Disable Account")
            print("│ ▶︎ 3 • Retrieve User")
            print("| ▶︎ 0 • Exit")
            print("| CHOOSE YOUR PICK: ")
            ch = input()
            if ch == "1":
                createBearAccount()
            elif ch == "2":
                username = bankOfficialLogin(user="admin")
                while True:
                    print("Enable or disable account")
                    print("1. Enable")
                    print("2. Disable")
                    print("0. Exit")

                    choice = input("Choice: ")
                    if choice == "1":
                        for i in BANK_OFFICIAL:
                            if i["username"] == username:
                                i["enabled"] = True
                        break
                    elif choice == "2":
                        for i in BANK_OFFICIAL:
                            if i["username"] == username:
                                i["enabled"] = False
                        break
                    elif choice == "0":
                        break
            elif ch == "3":
                user = ""
                while True:
                    user = retrieveUser()
                    if user == False:
                        continue
                    else:
                        break

                print("User id is: ", user["username"])
                while True:
                    print("Change password?")
                    print("1. Yes")
                    print("2. No")
                    choice = input()
                    if choice == "1":
                        newPassword = input("Input new password: ")
                        user["password"] = newPassword
                        print("password changed")
                    elif choice == "2":
                        break

            elif ch == "0":
                print("\tThanks for using BEAR bank")
                break
            else:
                print("Invalid choice")

    if user == 3:
        while True:
            print("\t                                                       ")
            print("  ┌────────────────┐  ╭───────────────────────╮           ")
            print("  │  ╭┼┼╮          │  │ ▶︎                  │           ")
            print("  │  ╰┼┼╮          │  ├───────────────────────┴─────╮     ")
            print("  │  ╰┼┼╯          │  │ ▶︎ 2 • DEPOSIT MONEY   │     ")
            print("  │                │  ├────────────────────────────┬╯     ")
            print("  │  B E A R       │  │ ▶︎ 3 • WITHDRAW MONEY  │      ")
            print("  │  B A N K       │  ├───────────────────────┬────╯      ")
            print("  │                │  │ ▶︎ 4 • BALANCE ENQUIRY  │           ")
            print("  |                |  |      9. Exit              |   ")
            print("  CHOOSE YOUR PICK:                   ")
            ch = input()

            if ch == '2':
                if user == 3:
                    # this only allows the bank officials and customers to be able to make deposits on the account
                    # this will require password
                    num = input("\tEnter the Account number: ")
                    num2 = input("\tEnter the Password: ")
                    makeadeposit(num, num2)
                else:
                    print(" We don't have any information about your account")


            elif ch == '3':
                if user == 3:
                    # this only allows the bank officials and customers to be able to make withdraws and deposits on the account
                    # this will require password
                    num = input("\tEnter The account No. : ")
                    num2 = input("\tEnter the password: ")
                    withdrawmoney(num, num2)
                else:
                    print(" We don't have any information about your account")

            elif ch == '4':
                # to get the Balance you need a password from the account holder
                # only the valid Bear BAnk account holder can see the balance
                num = input("\tEnter The account No. : ")
                num2 = input("\tEnter the Password:")
                displayBal(num, num2)
            elif ch == "9":
                print("Thank you for using bear bank")
                break
            else:

                print("Invalid choice")

            ch = input("\nEnter your choice (yes to go back to main menu ): ")
