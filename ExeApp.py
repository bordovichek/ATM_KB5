import random

from Card import Card
from ATM import ATM

class ExeApp:
    def __init__(self):
        self.atms = list()
        self.cards = list()

    def creat(self, int_choise = 0):
        Flag_atm = False
        Flag_card = False
        choise = ""
        if int_choise == 0:
            choise = input("What you want to create? (ATM or Card) " )
        if choise.upper() == "ATM" or int_choise == 1:
            while Flag_atm is False:
                characteristics = input("You MUST enter the following data: model and ID, as well as the OPTIONAL number of bills to store in the ATM (by default, the size for each bill is 100).\nEnter banknotes in order for 5000, 2000, 1000, 500, 200, 100, 50, 10. You cannot enter data only for certain bills: either for all or none.\nThank you!\n").split()
                if len(characteristics) == 2 or len(characteristics) == 10:
                    Atm = ATM(*characteristics)
                    for card in self.cards:
                        Atm.add_card(card)
                    Flag_atm = True
                    self.atms.append(Atm)
                else:
                    print("Characteristics are wrong, try again")
        elif choise.lower() == "card" or int_choise == 2:
            while Flag_card is False:
                characteristics = input("You MUST enter the following data: card number, cardholder name, expiration date in 'YYYY-MM-DD' format, CVC code, PIN code and balance (default is 0)\n").split()
                if len(characteristics) == 6:
                    card = Card(*characteristics)
                    Flag_card = True
                    self.cards.append(card)
                    for atm in self.atms:
                        atm.add_card(card)
                else:
                    print("Characteristics are wrong, try again")
        else:
            print("Something went wrong")


    def execution(self):
        choise = -1
        while choise != 10:
            print("Welcome to the menu. Choose your variant:")
            print("1) Create ATM")
            print("2) Create Card")
            print("3) Replenish the ATM with banknotes")
            print("4) Withdrawn money from card")
            print("5) Deposit money from card")
            print("10) End of work")
            choise = int(input())
            if choise == 1:
                self.creat(1)
            elif choise == 2:
                self.creat(2)
            elif choise == 3:
                if not self.atms:
                    print("Sorry, there are not ATM in system")
                else:
                    found = False
                    the_atm = input("Please, enter the ATM ID: ")
                    for atm in self.atms:
                        if atm.get_id() == the_atm:
                            atm.replenishment()
                            found = True
                            break
                    if not found:
                        print("Sorry, the ATM is not found")
            elif choise == 4:
                if self.atms:
                    random.shuffle(self.atms)
                    self.atms[0].operation_withdrawn()
                else:
                    print("Sorry, there are not ATM in system")
            elif choise == 5:
                if self.atms:
                    random.shuffle(self.atms)
                    self.atms[0].operation_deposit()
                else:
                    print("Sorry, there are not ATM in system")
            elif choise == 10:
                break
        print("Work is over!")
