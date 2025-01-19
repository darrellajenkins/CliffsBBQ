import calendar
import string
import sys
import time
from tqdm import tqdm


# SIMULATED CC PAYMENT


clr = "\033[39m\033[0m"
bold = "\033[1m"
italic = "\033[3m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
purple = "\033[35m"
cyan = "\033[36m"


curr_2digit_year = time.strftime('%y')
curr_month = time.strftime('%m')


def run_payment():
    """Processes credit card payment and properly handles if user decides to exit before payment."""
    while True:
        typ = input("\nWe only accept, VISA, Mastercard, or Discover.  Please enter the first digit of your credit card number [or Q to quit]: ")
        if typ[0].lower() == 'q':
            print(f"\n{bold}Your session is now closed at your request. \nPlease return when you are ready to submit payment or have the accepted payment "
                  f"method.{clr}")
            sys.exit()
        elif typ[0] == '4':
            print("Thank you for choosing VISA. You may continue with this card or enter a Mastercard or Discover.")
            break
        elif typ[0] == '5':
            print("Thank you for choosing Mastercard.  You may continue with this card or enter a VISA or Discover.")
            break
        elif typ[0] == '6':
            print("Thank you for choosing Discover.  You may continue with this card or enter a VISA or Mastercard.")
            break
        else:
            print(f"{red}We only accept, VISA, Mastercard, or Discover.{clr}")
            continue

    paid = True
    while True:
        cc = input("If you are ready to make payment, please enter your credit card number [or Q to quit]: ")
        if cc[0].lower() == 'q':
            paid = False
            print(f"\n{bold}Your session is now closed at your request. \nPlease return when you are ready to submit payment or have the accepted payment "
                  f"method.{clr}")
            return paid
        elif len(cc) != 16:
            print(f"\nInvalid credit card number. It must contain exactly 16 digits, but you entered {len(cc)} digits.")
            continue
        elif int(cc[0]) <=3 or int(cc[0]) >= 7:
            print(f"\n{red}It looks like you may have mis-typed the first digit. We only accept, VISA, Mastercard, or Discover.{clr}")
            continue
        elif cc[0] == '4':
            cc = cc[0:4] + " " + cc[4:8] + " " + cc[8:12] + " " + cc[12:]
            print(f"You entered VISA number: {cc}. Is this correct?")
        elif cc[0] == '5':
            cc = cc[0:4] + " " + cc[4:8] + " " + cc[8:12] + " " + cc[12:]
            print(f"You entered Mastercard number: {cc}. Is this correct?")
        elif cc[0] == '6':
            cc = cc[0:4] + " " + cc[4:8] + " " + cc[8:12] + " " + cc[12:]
            print(f"You entered Discover number: {cc}. Is this correct?")
        yn = input("\tY or N: ")
        if yn.lower() != 'y':
            continue
        elif yn == 'Y'.lower():
            break

    credit = credit_name()

    while True:
        month_and_year = input(f"Please enter the card's expiration 2-digit month and 2-digit year (separated by a '/', for example < {bold}{red}01/30{clr} "
                               f">: ")
        month_entered = month_and_year[0:2]
        year_entered = month_and_year[3:5]

        if len(month_and_year) != 5 or "/" not in month_and_year:
            print(f"{red}You either forgot to enter the '/', entered too many numbers, or possibly left out a number in the 2-digit month or 2-digit year.{clr}")
            continue
        if month_entered not in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']:
            print(f"{red}You entered an invalid month. Please enter a 2 digit month between 01 and 12.{clr}")
            continue
        if not month_entered.isdigit():
            print("Please enter a 2 digit month.")
            continue
        if not year_entered.isdigit():
            print("Please enter a 2 digit year.")
            continue
        if int(year_entered) < int(curr_2digit_year):
            print(f"{red}You entered a year in the past.{clr}")
            continue
        if int(month_entered) < int(curr_month) and int(year_entered) == int(curr_2digit_year):
            print(f"{red}You entered a month in the past.{clr}")
            continue
        else:
            month_and_year = month_and_year.split("/")
            print(f"You entered expiration: {month_and_year[0]}/{month_and_year[1]}")
            print("Is this correct? ")
            yn = input("\tY or N: ")
            if yn == 'Y'.lower():
                break
            elif yn.lower() != 'y':
                continue
        break

    while True:
        sec_code = input("Next, please enter the 3-digit security code found on the back of your card: ")
        if len(sec_code) != 3 and not sec_code.isdigit():
            continue
        else:
            break
    print()

    # The actual payment processing would be here (e.g., Stripes). If payment accepted and goes through paid = True, else False.
    for _ in tqdm(range(0, 100), desc=f'{red}Processing your payment. Please wait...', bar_format="{l_bar}{bar:50}", colour="green"):
        time.sleep(0.08)
    time.sleep(0.55)
    print("\nYour credit card has been processed.", end=' ')
    print(f"{blue}{bold}Thank you for your payment!{clr}")
    if paid:
        return credit

def credit_name():
    while True:
        name = input("Please enter your name exactly as shown on your card: ")
        for letter in name:
            if letter in string.punctuation:
                name = name.replace(letter, " ")
        name = name.split()
        cleaned_up = " ".join(name)
        print(f"The name on your card is: {cleaned_up}")
        print("Is this correct? ")
        yn = input("\tY or N: ")
        if yn == 'Y'.lower():
            break
        elif yn.lower() != 'y':
            continue
        break
    return cleaned_up.title()
