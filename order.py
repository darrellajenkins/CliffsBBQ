from uuid import uuid4
import sys
from funcs import clr, bold, blk, italic, red, green, yellow, blue, purple, cyan


class CustOrder:

    def __init__(self):
        self.cust_id = ""
        self.first = ""
        self.last = ""
        self.order = ""

    def __repr__(self):
        return f'Instance is associated with Class {type(self).__name__} = <__main__.CustOrder object at {hex(id(self))}>'

    def __str__(self):
        return f'Customer Account Number: {self.cust_id}. Name: {self.first.title()} {self.last.title()}.  Order: {self.order}'

    def run_order(self):
        ccb = False
        while True:
            place = input("Would you like to place an order? [Y]es, [N]o or [E]xit ")
            if place.lower() == 'y':
                self.cust_id = str(uuid4())
                print("Please enter the following information: ")
                self.first, self.last, self.order = input("\nFirst name: "), input("\nLast name: "), input("\nOrder: ")
                while True:
                    print(f"Your name is: {self.first} {self.last}, and your order is: {self.order}. Is this correct?")
                    yn = input("\t[Y]es, [N]o to go back and edit everything, or [C] to change only your order: ")
                    if yn.lower() == 'n':
                        break
                    if yn.lower() == 'y':
                        visitor = (f"Customer id: {self.cust_id}", self.first, self.last, self.order)
                        return visitor
                    if yn.lower() == 'c':
                        re_order = input("Please enter your corrected order: ")
                        self.order = re_order
                        visitor = (f"Customer id: {self.cust_id}", self.first, self.last, self.order)
                        return visitor
                    if yn != 'y'.lower()  and yn != 'n'.lower() and yn != 'c'.lower():
                        print(f"{bold}{blue}Please enter{clr}{red}{bold} 'Y'{clr}, {red}{bold}'N'{clr}, or {red}{bold}'C'{clr}")
                        continue

            if place.lower() == 'n':
                cb = False
                while True:
                    ques = input("Would you like to see the menu or would you like us to make a recommendation? ([M]enu, [R]ecommendation), [E]xit ")
                    if ques.lower() == 'e':
                        sys.exit()
                    if ques.lower() == 'm':
                        print("Menu")
                        break
                    if ques.lower() == 'r':
                        print("Recommendation")
                        break
                    if ques.lower() != 'm' and ques.lower() != 'r' and ques.lower() != 'e':
                        if cb:
                            print(f"{bold}{blue}Please enter{clr}{red}{bold} 'M'{clr}, {red}{bold}'R'{clr}, or {red}{bold}'E'{clr}")
                        else:
                            cb = True
                        continue
            if place.lower() == 'e':
                sys.exit()
            if place.lower() != 'y' and place.lower() != 'n' and place.lower() != 'e':
                if ccb:
                    print(f"{bold}{blue}Please enter{clr}{red}{bold} 'Y'{clr}, {red}{bold}'N'{clr}, or {red}{bold}'E'{clr}")
                else:
                    ccb = True
                continue
