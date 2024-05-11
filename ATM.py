import datetime
import copy
from CARD import Card

class ValidationError(Exception):
    pass

class PinCodeError(Exception):
    pass

class AmountError(Exception):
    pass

class BillError(Exception):
    pass

class ATM:
    bills = dict()

    def __init__(self, model,id, five_t_amount = 100,two_t_amount= 100, one_t_amount= 100,five_h_amount= 100,two_h_amount= 100, one_h_amount= 100,fifty_amount= 100, ten_amount= 100):
        self.__model = model;
        self.__id = id
        self.bills[5000] = int(five_t_amount)
        self.bills[2000] = int(two_t_amount)
        self.bills[1000] = int(one_t_amount)
        self.bills[500] = int(five_h_amount)
        self.bills[200] = int(two_h_amount)
        self.bills[100] = int(one_h_amount)
        self.bills[50] = int(fifty_amount)
        self.bills[10] = int(ten_amount)
        self.cards = dict()
        self.all_bills = sum(self.bills.values())

    def __repr__(self):
        return (f"ATM(Model: {self.__model}, ID: {self.__id}) specifications: \n"
                f"5000 amount - {self.bills[5000]}\n"
                f"2000 amount - {self.bills[2000]}\n"
                f"1000 amount - {self.bills[1000]}\n"
                f"500  amount - {self.bills[500]}\n"
                f"200  amount - {self.bills[200]}\n"
                f"100  amount - {self.bills[100]}\n"
                f"50   amount - {self.bills[50]}\n"
                f"10   amount - {self.bills[10]}")

    def get_id(self):
        return self.__id

    def add_card(self, card):
        self.cards.setdefault(card.cardowner, list()).append(card)

    def validation(self):
        error = False
        card_is_found = False
        while not card_is_found:
            name_of_user = input("Please, enter an user_id/name: ")
            if name_of_user in self.cards.keys():
                card_of_user = input("Please, enter a card number: ")
                if card_of_user in list(map(lambda x: x.number, self.cards[name_of_user])):
                    for cards in self.cards[name_of_user]:
                        if cards.number == card_of_user:
                            break
                    count = 0
                    while count < 3:
                        pin_code_card = int(input("Please, enter a PIN-CODE: "))
                        if pin_code_card == cards.pin_code:
                            return (True, cards)
                        else:
                            count += 1
                            print(f"PIN-CODE is wrong! You have {3-count} atts.")
                            try:
                                if count == 3:
                                    raise PinCodeError("Sorry, I ate your card")
                            except PinCodeError as PC:
                                print(PC)
                                error = True
                                return (False, cards)
                else:
                    print("Sorry, card is not found. Enter user_id/name and number again")

            else:
                print("Sorry, user_id/name. Enter again")

    def withdrawn(self, amount):
        to_withdrawn = 0
        copied = copy.copy(self.bills)
        while amount > 0 and amount%10 == 0 and self.all_bills > 0:
            if amount > 5000 and self.bills[5000] > 0:
                    amount -= 5000
                    to_withdrawn += 5000
                    self.bills[5000] -= 1
            elif amount > 2000 and self.bills[2000] > 0:
                    amount -= 2000
                    to_withdrawn += 2000
                    self.bills[2000] -= 1
            elif amount > 1000 and self.bills[1000] > 0:
                    amount -= 1000
                    to_withdrawn += 1000
                    self.bills[1000] -= 1
            elif amount > 500 and self.bills[500] > 0:
                    amount -= 500
                    to_withdrawn += 500
                    self.bills[500] -= 1
            elif amount > 200 and self.bills[200] > 0:
                    amount -= 200
                    to_withdrawn += 200
                    self.bills[200] -= 1
            elif amount > 100 and self.bills[100] > 0:
                    amount -= 100
                    to_withdrawn += 100
                    self.bills[100] -= 1
            elif amount > 50 and self.bills[50] > 0:
                    amount -= 50
                    to_withdrawn += 50
                    self.bills[50] -= 1
            elif amount >= 10 and self.bills[10] > 0:
                    amount -= 10
                    to_withdrawn += 10
                    self.bills[10] -= 1
            else:
                self.all_bills = sum(self.bills.values())
                break
        if amount%10 != 0:
            raise  AmountError("The amount of money to be withdrawn is not a multiple of 10, the ATM will not be able to issue the full amount")
        elif amount !=0 and(self.all_bills == 0 or self.bills[10] == 0):
            print(f"Sorry, the ATM has not got enough bills to withdrawn. It can give you only {to_withdrawn}, if you agree, press 1, other button will stop operation")
            if int(input()) == 1:
                return to_withdrawn
            else:
                self.bills = copied
                raise BillError("Sorry, the ATM has not got enough bills to withdrawn")
        else:
            return to_withdrawn

    def operation_withdrawn(self):
        what = self.validation()
        user_card = what[1]
        if what[0] == True:
            while True:
                want_to_ext = int(input("Please, enter an amount money to withdrawn "))
                try:
                    withdraw = self.withdrawn(want_to_ext)
                    if want_to_ext <= user_card.balance and withdraw > 0:
                        user_card.balance -= withdraw
                        print(f"Operation completed successfully, your current balance now is {user_card.balance}")
                        break
                except AmountError as AE:
                    print(AE)
                    print("If you want to try again, please, enter 'AGAIN', something other will stop the operation")
                    if input().lower() != 'again':
                        break
                except BillError as BE:
                    print(BE)
                    break
        else:
            raise ValidationError

    def deposit(self, amount):
        to_deposit = 0
        while amount > 0 and amount % 10 == 0:
            if amount > 5000:
                amount -= 5000
                to_deposit += 5000
                self.bills[5000] += 1
            elif amount > 2000:
                amount -= 2000
                to_deposit += 2000
                self.bills[2000] += 1
            elif amount > 1000:
                amount -= 1000
                to_deposit += 1000
                self.bills[1000] += 1
            elif amount > 500:
                amount -= 500
                to_deposit += 500
                self.bills[500] += 1
            elif amount > 200:
                amount -= 200
                to_deposit += 200
                self.bills[200] += 1
            elif amount > 100:
                amount -= 100
                to_deposit += 100
                self.bills[100] += 1
            elif amount > 50:
                amount -= 50
                to_deposit += 50
                self.bills[50] += 1
            elif amount >= 10:
                amount -= 10
                to_deposit += 10
                self.bills[10] += 1
        if amount % 10 != 0:
            raise AmountError(
                "The amount of money to be deposit is not a multiple of 10, the ATM will not be able to issue the full amount")
        else:
            return to_deposit

    def operation_deposit(self):
        what = self.validation()
        user_card = what[1]
        if what[0] == True:
            while True:
                want_to_dep = int(input("Please, enter an amount money to deposit "))
                try:
                    deposit = self.deposit(want_to_dep)
                    user_card.balance += deposit
                    print(f"Operation completed successfully, your current balance now is {user_card.balance}")
                    break
                except AmountError as AE:
                    print(AE)
                    print("If you want to try again, please, enter 'AGAIN', something other will stop the operation")
                    if input().lower() != 'again':
                        break
        else:
            raise ValidationError

    def replenishment(self):
        bills = [5000, 2000, 1000, 500, 200, 100, 50, 10]
        while True:
            print(f"What bills you want to replenishment?")
            r_bill = int(input())
            if r_bill in bills:
                amout_of_bill = int(input("Amount: "))
                if amout_of_bill > 0:
                    self.bills[r_bill] += amout_of_bill
                else:
                    print("The number of bills must be natural")
            else:
                print("Error! There is no such bill")
            if input("If you want to stop, press any button, else press enter"):
                break
        print("Replenishment is over")
        self.all_bills = sum(self.bills.values())
        print(self)