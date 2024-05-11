import datetime

class Card:
    def __init__(self, number, cardowner, date, CVC,  pin_code, balance = 0):
        self.number = number
        self.cardowner = cardowner
        self.date = datetime.date(*list(map(int, date.split("-"))))
        self.CVC = int(CVC)
        self.pin_code = int(pin_code)
        self.balance = int(balance)

    def __repr__(self):
        return f"(NUMBER: {self.number}; CARDOWNER: {self.cardowner}; BALANCE: {self.balance}; DATE: {self.date.strftime('%m/%y')}; CVC: {self.CVC}; PIN_CODE: {self.pin_code})"