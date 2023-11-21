class calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

my_calc = calculator()

while True:
    print("1:add")
    print("2:sub")
    print("3:mul")
    print("4:div")
    print("5:exit")

    ch = int(input("enter any number:"))

    if ch in (1, 2, 3, 4, 5):
        if ch == 5:
            break
        
        a = int(input("enter any number:"))
        b = int(input("enter any number:"))

        if ch == 1:
            print(a, "+", b, "=", my_calc.add(a, b))
        elif ch == 2:
            print(a, "-", b, "=", my_calc.sub(a, b))
        elif ch == 3:
            print(a, "*", b, "=", my_calc.mul(a, b))
        elif ch == 4:
            print(a, "/", b, "=", my_calc.div(a, b))

    else:
        print("invalid input")




class Banking:
    def __init__(self):
        print(
            "_____________________________________________________________________WELOCOME TO ABC BANK______________________________________________________________________"
        )
        print()
        self.admin_login = {"password": "1234"}
        self.all = [{}]
        self.menu()

    def menu(self):
        while True:
            print(
                """Our banking services
                            1.New user registration 
                            2.Login into Netbanking
                            3.Contact Branch/Admin
                            
                    For New user press 1 , To login press 2, Contact Branch/Admin press 3 """
            )
            n = input()
            if n == "1":
                self.register()
            elif n == "2":
                self.login()
            elif n == "3":
                self.branch()
            
            else:
                print(
                    "________________________________ERROR-505__________________________________ "
                )
                self.menu()

    def register(self):
        self.empdata = {}
        self.id = input("Enter your User-id ")
        for d in self.all:
            if self.id in d:
                print("Sorry user-id Unavailable , Create your user-id again ")
                self.con = True
                break

        else:
            while True:
                self.password = input("Enter your password")
                self.password_2 = input("Re-Enter your password")
                if self.password == self.password_2:
                    self.empdata[self.id] = self.password_2
                    self.empdata["Name"] = input("Enter your full name")
                    self.empdata["Mobile"] = input("Enter your mobile number")
                    self.empdata["Balance"] = 0
                    self.empdata["Cards"] = "N/A"
                    self.empdata["Loan"] = "N/A"
                    print(
                        f"{self.empdata.get('Name')} has been registered successfully "
                    )
                    self.all.append(self.empdata)
                    self.con = False
                    e = input("Press any key continue")
                    break
                else:
                    print(
                        "Wrong password please enter your password again and Re-Enter your password"
                    )
        if self.con:
            self.register()

    def login(self):
        id = input("Enter your user-id")
        password = input("Enter your password")
        for i in range(int(len(self.all))):
            if id in self.all[i]:
                if password == self.all[i].get(id):
                    print("_____________________Logged in succesfully________________")
                    print(
                        """Our banking services
                            1.Show Balance 
                            2.Money withdrawal
                            3.Add money
                            4.Credit card/Debit Card
                            5.Loan 
                            6.Contact Branch
                    For Balance press 1 , To Withdrawal press 2, For Adding money pres 3,For credit card press 4, For loan press 5, To contact branch press 6 """
                    )
                    n = input()
                    if n == "1":
                        print(self.all[i].get("Balance"))
                        s = input("press any key to continue")
                        break
                    elif n == "2":
                        print(f"your Account Balance: {self.all[i].get('Balance')}")
                        w = int(input("Enter amount to withdrwala"))
                        if w < int(self.all[i].get("Balance")):
                            self.all[i]["Balance"] = int(self.all[i].get("Balance")) - w
                            print(
                                "---------Amount Withcdrawal Succesfull------------------"
                            )
                            print(f"Remaining Balance = {self.all[i].get('Balance')}")
                            s = input("press any key to continue")
                            break
                        else:
                            print(
                                "---------------Insufficient Balance in your account----------------- "
                            )
                            s = input("Press any key to continue")
                            break
                    elif n == "3":
                        print(f"your Account Balance: {self.all[i].get('Balance')}")
                        w = int(input("Enter amount to add into your account"))
                        self.all[i]["Balance"] = int(self.all[i].get("Balance")) + w
                        print(
                            "---------Transaction Succesfull, Amount Succesfully deposited into your account------------------"
                        )
                        print(f"Updated  Balance = {self.all[i].get('Balance')}")
                        s = input("press any key to continue")
                        break
                    elif n == "4":
                        print(f"Your cards = {self.all[i].get('Cards')}")
                        print("To update or modify contact Hello Bank")
                        self.branch()
                        s = input("press any key to continue")
                        break
                    elif n == "5":
                        print(f"Your cards = {self.all[i].get('Loan')}")
                        print("To update or modify contact Hello Bank")
                        self.branch()
                        break
                    elif n == "6":
                        self.branch()
                        break
                    else:
                        print("          Invalid Option         ")
                        s = input("Press any key to continue")
                        break
                else:
                    print(
                        "--------------------Incorrect Password----------------------"
                    )
                    s = input("Press any key to continue")
                    break
        else:
            print(
                "------------------------------------Invalid user-Id----------------------------------"
            )
            s = input("Press any key to continue")

    

s = Banking()