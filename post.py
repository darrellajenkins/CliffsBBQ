import sys
import time
from uuid import uuid4
import smtplib
import requests
import os
import funcs


today = time.ctime()
today_date = time.strftime('%B %d %Y')
today_time = time.strftime('%I:%M:%S %p')


class Survey:

    def __init__(self):
        self.location = ""
        self.survey_results = {}

    def __repr__(self):
        return f'Instance is associated with Class {type(self).__name__} = <__main__.Survey object at {hex(id(self))}>'

    def __str__(self):
        return f'Survey data: {self.location}. Name: {self.survey_results}'

    def locate(self):
        location = input("Please enter the location (city/town) of the store you visited today: ").lower()
        return location.title()

    def three_ques(self):
        ques_1 = input("On a scale of 1 to 5 (5 being the highest rating), please enter the number that best represents the quality of the barbeque you enjoyed today: ")
        ques_2 = input("On a scale of 1 to 5 (5 being the highest rating), please enter the number that best represents the service and friendliness you received from the staff today: ")
        ques_3 = input("On a scale of 1 to 5 (5 being the highest rating), please enter the number that best reflects the level of fun or enjoyment you enjoyed today: ")
        self.survey_results = {"Quality": ques_1, "Service/Friendliness": ques_2, "Fun/Enjoyment": ques_3}
        return self.survey_results

    def survey_contact(self, email):
        """This function is strictly an auto-emailer of a coupon to customers who take the survey and ask to be contacted."""
        voucher_id = str(uuid4())
        gmail = "pattycakelamb@gmail.com"
        pword = os.environ.get("PATTY_WORD")
        my_gmail = gmail
        password = pword
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_gmail, password=password)
        connection.sendmail(from_addr=my_gmail, to_addrs=email,
                             msg=f"Subject:Cliff's BBQ StandSurvey\n\nDear Valued Customer,\n\nThank you for filling out our anonymous survey. We would appreciate "
                                 f"hearing more about your experience. A manager will be contacting you soon.\n\n"
                                 f"In the meantime, please enjoy $2 off on your next visit to any of our stores! Coupon code: {voucher_id}. Good until Dec. 31, 2024.\n\n"
                                 f"Sincerely,\n\nPatty Cake Lamb\n570-846-0788")
        connection.quit()
        return voucher_id, email

    def record_survey(self, location, results):
        self.location = location
        self.survey_results = results
        with open(f"surveys_stamped_{today_date}.txt", "a") as file:
            file.write(f"{location}: {results}\n")

    def record_survey_details(self, data):
        with open(f"surveys_cust_details_{today_date}.txt", "a") as file:
            file.write(f"{data}\n")

    def survey_willingness(self):
        """Customer experience survey is offered with or without follow up contact from manager."""
        while True:
            take = input("Would you be willing to take a short 3 question survey? [Y]es or [N]o ")
            if take.lower() == 'y':
                print("Thank you.\n")
                break
            if take.lower() == 'n':
                print("Thank you stopping by!")
                sys.exit()
            if take.lower() != 'y' or take.lower() != 'n':
                continue
        while True:
            contact = input("Would you like to be contacted in connection with this survey? [Y]es or [N]o ")
            if contact.lower() == 'y':
                break
            if contact.lower() == 'n':
                print("No problem, your privacy is important to us!\n")
                self.location = self.locate()
                self.survey_results = self.three_ques()
                self.record_survey(self.location, self.survey_results)
                print(f"{funcs.purple}\nThank you for taking the time to share your observations!{funcs.clr}")
                sys.exit()
            if contact.lower() != 'y' or take.lower() != 'n':
                continue

    def get_survey_have_email(self, email):
            print("Thank you. We will contact you via the email address you provided earlier.")
            self.location = self.locate()
            self.survey_results = self.three_ques()
            self.record_survey(self.location, self.survey_results)
            print("Thank you for taking the time to share your observations!")
            return email

    def get_survey_ask_email(self):
            contact_method = input("Please enter your email address: ")
            self.location = self.locate()
            self.survey_results = self.three_ques()
            self.record_survey(self.location, self.survey_results)
            print("Thank you for taking the time to share your observations!")
            return contact_method

class Coupon:

    def __init__(self):
        self.discount_1 = 'please enjoy a $2 discount on your next visit.'.capitalize()
        self.discount_2 = 'please enjoy a 10% discount on your next visit.'.capitalize()
        self.discount_3 = 'please enjoy a 15% discount on your next visit.'.capitalize()
        self.discount_4 = 'empty slot.'.capitalize()

    def __repr__(self):
        return f'Instance is associated with Class {type(self).__name__} = <__main__.Coupon object at {hex(id(self))}>'

    def __str__(self):
        return f'Coupon types: {self.discount_1}, {self.discount_2}, {self.discount_3}, {self.discount_4}'

    def record_daily_vouchers(self, voucher_id, email, reason_for_coupon):
        with open(f"daily_vouchers_{today_date}.txt", "a") as file:
            file.write(f"Coupon code: {voucher_id} | Email: {email} | Reason: {reason_for_coupon}\n")

    def capture_coupon_email(self, discount_amount):
        cust = input("Please enter the specific email address where you wish to receive your coupon: ")
        voucher_id = str(uuid4())
        print("Thank you. This entry is completely separate and you will not receive any other notifications unless you previously requested for us to do so.")
        print("The email provided will receive a coupon in just a few minutes.")
        return cust, discount_amount, voucher_id

    def capture_both_coupon_emails(self, discount_amount):
        cust = input("Please enter the specific email address where you wish to receive your coupon: ")
        companion = input("Please enter the specific email address where we should send your companion's coupon: ")
        voucher_id1 = str(uuid4())
        voucher_id2 = str(uuid4())
        print("Thank you. These entries are completely separate and you will not receive any other notifications unless you previously requested for us to do so.")
        print("Each email provided will receive its own unique coupon in just a few minutes.")
        return cust, companion, discount_amount, voucher_id1, voucher_id2

    def cust_voucher(self, capture_coupon_email):
        """Emails a coupon to just one customer email."""
        email = capture_coupon_email[0]
        discount = capture_coupon_email[1].capitalize()
        voucher_id = capture_coupon_email[2]
        gmail = "pattycakelamb@gmail.com"
        pword = os.environ.get("PATTY_WORD")
        my_gmail = gmail
        password = pword
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_gmail, password=password)
        connection.sendmail(from_addr=my_gmail, to_addrs=email,
                             msg=f"Subject:Cliff's BBQ StandVoucher\n\nDear Valued Customer,\n\nThank you for visiting Cliff's BBQ Stand!\n\n"
                                 f"{discount} Coupon code: {voucher_id}. Good until Dec. 31, 2024.\n\nSincerely,\n\nCliff's BBQ Stand Management\n570-846-0788")
        connection.quit()

    def companion_voucher(self, capture_both_coupon_emails):
        """Emails one unique coupon each to the email addresses of both the customer and their companion."""
        email_1 = capture_both_coupon_emails[0]
        email_2 = capture_both_coupon_emails[1]
        discount = capture_both_coupon_emails[2].capitalize()
        voucher_id1 = capture_both_coupon_emails[3]
        voucher_id2 = capture_both_coupon_emails[4]
        gmail = "pattycakelamb@gmail.com"
        pword = os.environ.get("PATTY_WORD")
        my_gmail = gmail
        password = pword
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_gmail, password=password)
        connection.sendmail(from_addr=my_gmail, to_addrs=email_1,
                             msg=f"Subject:Cliff's BBQ StandVoucher\n\nDear Valued Customer,\n\nThank you for visiting Cliff's BBQ Stand!\n\n"
                                 f"{discount} Coupon code: {voucher_id1}. Good until Dec. 31, 2024.\n\nSincerely,\n\nCliff's BBQ Stand Management\n570-846-0788")
        connection.sendmail(from_addr=my_gmail, to_addrs=email_2,
                             msg=f"Subject:Cliff's BBQ StandVoucher\n\nDear Valued Customer,\n\nThank you for visiting Cliff's BBQ Stand!\n\n"
                                 f"{discount} Coupon code: {voucher_id2}. Good until Dec. 31, 2024.\n\nSincerely,\n\nCliff's BBQ Stand Management\n570-846-0788")
        connection.quit()
