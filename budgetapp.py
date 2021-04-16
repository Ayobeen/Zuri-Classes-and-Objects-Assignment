"""
Budget App
Create a Budget class that can instantiate objects based on different budget categories like food, clothing, 
and entertainment. These objects should allow for
1.  Depositing funds to each of the categories
2.  Withdrawing funds from each category
3.  Computing category balances
4.  Transferring balance amounts between categories

Push your code to GitHub, and submit the repo link.
"""     

class Budget:
    def __init__(self, bCategory=["FOOD","CLOTHING","ENTERTAINMENT"], cBalance=[0,0,0]):
        #cBance at index 0 = foodBalance, index 1 = clothing and index 2 = entertainment
        self.cBalance = cBalance
        self.bCategory = bCategory
        print ("These are the available categories")
        print ("1. food")
        print ("2. clothing")
        print ("3. entertainment")

    def deposit(self):
        category = int(input("Select an option to continue: "))
        if category not in [1,2,3]:
            print("You must enter 1, 2 or 3 to continue")
            category = int(input("Select an option to continue: "))
        category = category - 1
        amount = int(input("Enter amount to deposit: "))
        self.cBalance[category] = self.cBalance[category] + amount
        print("Deposit successful, your {} current balance: {}".format(self.bCategory[category], self.cBalance[category]))

    def withdraw(self):
        category = int(input("Select an option to continue: "))
        if category not in [1,2,3]:
            print("You must enter 1, 2 or 3 to continue")
            category = int(input("Select an option to continue: "))
        category = category - 1
        amount = int(input("Enter amount to withdraw: "))
        if self.cBalance[category] < amount:
            print("Insufficient balance")
        else: 
            self.cBalance[category] = self.cBalance[category] - amount
            print("Withdrawal successful, your {} balance remain: {}".format(self.bCategory[category], self.cBalance[0]))
    
    def check_balance(self):
        category = int(input("Select an option to continue: "))
        if category not in [1,2,3]:
            print("You must enter 1, 2 or 3 to continue")
            category = int(input("Select an option to continue: "))
        category = category - 1
        print("Your {} balance is: {}".format(self.bCategory[category], self.cBalance[category]))

    def transfer(self):
        category = int(input("Select category to transfer from: "))
        if category not in [1,2,3]:
            print("You must enter 1, 2 or 3 to continue")
            category = int(input("Select category to transfer from: "))
        amount = int(input("Enter the amount: "))
        category = category - 1
        rCategory = int(input("Enter category to tranfer to: "))
        while category == rCategory:
            print("You can not tranfer to the same category")
            rCategory = int(input("Enter category to tranfer to: "))
        rCategory = rCategory -1
        self.cBalance[category] = self.cBalance[category] - amount 
        self.cBalance[rCategory] = self.cBalance[rCategory] + amount
        print("You have successfully transfered {} from  {} category to {} category".format(amount, self.bCategory[category], self.bCategory
        [rCategory] ))
    

print ("Welcome to budget app")
c = Budget()
task = ["deposit","withdraw","check_balance","tranfer"]
print ("What do you want to do")
print ("1. deposit")
print ("2. withdraw")
print ("3. check balance")
print ("4. transfer")
userInput = int(input("Enter an option to continue: "))
userInput = userInput - 1
taskAction = c.userInput[task]()

