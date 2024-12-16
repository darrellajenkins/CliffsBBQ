import json
import time
from funcs import clr, bold, blk, italic, red, green, yellow, blue, purple, cyan


class Reports:
    """Provides daily reports by date for customers, reasons for visiting, survey data, vouchers issued, and additional details from surveys."""
    def __init__(self):

        self.name = ""
        self.pword = ""

    def get_date(self):
        """Gets date from the user and assembles into the format needed by each report method. Allows for 2 or 3 letter abbreviations for the month."""
        months = {'ja': 'January', 'jan': 'January', 'fe': 'February', 'fb': 'February', 'feb': 'February', 'mc': 'March', 'mrc': 'March', 'mar': 'March',
                   'ap': 'April', 'ar': 'April', 'my': 'May', 'may': 'May', 'jn': 'June', 'jne': 'June', 'jun': 'June', 'jul': 'July', 'jly': 'July',
                  'au': 'August', 'ag': 'August', 'se': 'September', 'sp': 'September', 'st': 'September', 'oc': 'October', 'ot': 'October', 'no': 'November',
                  'nv': 'November', 'de': 'December', 'dc': 'December'}
        month = ""

        while True:
            current = input("Press [T] to see today's report or [A] to select a different date: ")
            if current.lower() == 't':
                month = time.strftime('%B')
                day = time.strftime('%d')
                year = time.strftime('%Y')
                return [month, day, year]
            if current.lower() == 'a':
                break
            if current.lower() != 't' and current.lower() != 'a':
                continue
        while True:
            a = input("Month (name or abbreviation): ")
            if len(a) < 2:
                print("Please enter at least 2 letters.")
                continue
            if not a.isalpha():
                print("Please enter at least 2 letters.")
                continue
            elif a.lower() == 'ma' or a.lower() == 'ju':
                print("In this case please enter at least 3 characters.")
                continue
            elif a[0:2].lower() not in months and a[0:3].lower() not in months:
                print("Please make sure you have correctly spelled the month.")
                continue
            elif len(a) >= 2 and a.lower() != 'ma' and a.lower() != 'ju':
                for key, value in months.items():
                    if a[0:2].lower() == key or a[0:3].lower() == key:
                        month = value
                break

        while True:
            two_digit_day = input("Two digit day: ")
            if len(two_digit_day) < 2:
                print("Please enter at least 2 digits.")
                continue
            if not two_digit_day.isdigit():
                print("Please enter at least 2 digits.")
                continue
            if two_digit_day not in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
                                     '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']:
                print("Please enter a 2 digit day between 01 and 31.")
                continue
            if len(two_digit_day) == 2 and two_digit_day.isdigit():
                break
        day = two_digit_day

        while True:
            four_digit_year = input("Four digit year: ")
            if len(four_digit_year) < 4:
                print("Please enter at least 4 digits.")
                continue
            if not four_digit_year.isdigit():
                print("Please enter at least 4 digits.")
                continue
            if not int(four_digit_year) >= 2024:
                print("Please enter a year 2024 or later.")
                continue
            if len(four_digit_year) == 4 and four_digit_year.isdigit():
                break
        year = four_digit_year

        return [month, day, year]

    def report_custs(self, date):
        """All daily customers report. Format must include the month as a string, 2-digit day, and 4-digit year."""
        month, day, year = date[0], date[1], date[2]
        date_text = f"{month} {day}, {year}"
        try:
            with open(f"daily_custs_{month} {day} {year}.txt", 'r') as file_4:
                contents = file_4.read()
                print(f"{bold}{yellow}\nHere is a list containing details of each customer who placed an order at one of our stores on {date_text}.{clr}")
                print(f"\n{contents}")
            with open(f"daily_custs_{month} {day} {year}.txt", 'r') as file_4a:
                for e, line in enumerate(file_4a, start=1):
                    pass
                print(f"\n{bold}{yellow}There was a total of {e} customer order(s) on {date_text}.{clr}")
        except FileNotFoundError:
            print(f"Report not found for the date requested or no customer orders have been taken or completed on {date_text}.")

    def report_reasons(self, date):
        """Daily reasons overview report."""
        month, day, year = date[0], date[1], date[2]
        date_text = f"{month} {day}, {year}"
        try:
            with open(f"reasons_daily_dict_{month} {day} {year}.txt") as file_5:
                contents = file_5.read()
                print(f"{bold}{purple}\nHere is a summary of the reasons that brought our customers into one of our stores on {date_text}.{clr}\n")
                reasons = json.loads(contents)
                for num, line in reasons.items():
                    if num != '10':
                        print(num + ".","   ", line[0], f"{cyan}", line[1], f"{clr}")
                    else:
                        print(num + ".","  ", line[0], f"{cyan}", line[1], f"{clr}")
        except FileNotFoundError:
            print(f"No customer orders were taken and completed on {date_text}.")

    def report_surveys(self, date):
        """Daily surveys report."""
        month, day, year = date[0], date[1], date[2]
        date_text = f"{month} {day}, {year}"
        try:
            with open(f"surveys_stamped_{month} {day} {year}.txt") as file_6:
                contents = file_6.read()
                print(f"{bold}{cyan}\nHere are all of the customer surveys submitted on {date_text}.{clr}")
                print(f"\n{contents}")
            with open(f"surveys_stamped_{month} {day} {year}.txt", 'r') as file_6a:
                for e, line in enumerate(file_6a, start=1):
                    pass
                print(f"{bold}{cyan}There was a total of {e} customer survey(s) submitted on {date_text}.{clr}")
        except FileNotFoundError:
            print(f"No surveys were taken and completed on {date_text}.")

    def survey_contact_details(self, date):
        """Detailed data on customers who requested to be contacted by a Cliff's BBQ Stand manager in response to their survey."""
        month, day, year = date[0], date[1], date[2]
        date_text = f"{month} {day}, {year}"
        try:
            with open(f"surveys_cust_details_{month} {day} {year}.txt") as file_8:
                contents = file_8.read()
                print(f"{bold}{cyan}\nHere are all details related to customers who asked to be contacted about their survey submitted on {date_text}.{clr}")
                print(f"\n{contents}")
            with open(f"surveys_cust_details_{month} {day} {year}.txt", 'r') as file_8a:
                for e, line in enumerate(file_8a, start=1):
                    pass
                print(f"{bold}{cyan}There was a total of {e} customer(s) who asked to be contacted about their survey(s) submitted on {date_text}.{clr}")
        except FileNotFoundError:
            print(f"No customer has requested contact about their survey completed on {date_text}.")

    def report_daily_vouchers(self, date):
        month, day, year = date[0], date[1], date[2]
        date_text = f"{month} {day}, {year}"
        try:
            with open(f"daily_vouchers_{month} {day} {year}.txt") as file_7:
                contents = file_7.read()
                print(f"{bold}{red}\nHere is a list of all coupons that were issued on {date_text}.{clr}")
                print(f"\n{contents}")
            with open(f"daily_vouchers_{month} {day} {year}.txt", 'r') as file_7a:
                for e, line in enumerate(file_7a, start=1):
                    pass
                print(f"{bold}{cyan}There was a total of {e} separate coupon(s) issued on {date_text}.{clr}")
        except FileNotFoundError:
            print(f"\nNo coupons were issued on {date_text}.")
