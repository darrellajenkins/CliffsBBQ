import admin
import json
import order
import pay
import post
import random
import sys
import time
from funcs import clr, bold, blk, italic, red, green, yellow, blue, purple, cyan
from visitors import Visitors


today = time.ctime()
today_date = time.strftime('%B %d, %Y')  # Note there is a comma here. Files must be saved and read with the comma.
today_time = time.strftime('%I:%M:%S %p')


def new_session():
    """This is the core function that runs a new order session for a customer regardless of whether or not they have previously visited."""
    while True:
        start = input(f"[B]egin session or [S]ee reports? {bold}B or S{clr}:  ")
        if start.lower() != 'b'.lower() and start.lower() != 's'.lower():
            continue
        else:
            break
    if start.lower() == 'b':
        a = Visitors()
        a.new_cust = order.CustOrder()
        a.all_order_details = a.new_cust.run_order()
        a.order_details = a.all_order_details[0:-2]
        a.order_date = a.all_order_details[-2]
        a.order_time = a.all_order_details[-1]
        cc_pay = pay.run_payment()
        name_on_credit_card = cc_pay
        a.credit_card_name = name_on_credit_card
        print(f"{green}Order is in the name of: {a.orderer_name()}.  Name on credit card: {a.credit_card_name}.{clr}")

        a.establish_start_day()
        a.next_steps(a.visitor_descrp())

        if a.discount_given():
            a_coupon = post.Coupon()
            a.solo_or_companion()

            if a.companion:
                x = a_coupon.capture_both_coupon_emails(a.discount_type())
                a_coupon.companion_voucher(x)
                a_coupon.record_daily_vouchers(x[3], x[0], a.voucher_reasons())
                a_coupon.record_daily_vouchers(x[4], x[1], a.voucher_reasons())

            elif a.solo:
                y = a_coupon.capture_coupon_email(a.discount_type())
                a_coupon.cust_voucher(y)
                a_coupon.record_daily_vouchers(y[2], y[0], a.voucher_reasons())

        if Visitors.subscriber_info:
            a.save_cust_info(Visitors.subscriber_info)
            a.save_reasons_daily(Visitors.reasons_daily_totals)
            a.save_subscriber(Visitors.subscriber_info[0][0], Visitors.subscriber_info[0][3], Visitors.subscriber_info[0][4])
            a_survey = post.Survey()
            a_survey.survey_willingness()

            a_survey.get_survey_have_email(Visitors.subscriber_info[0][3])
            v = a_survey.survey_contact(Visitors.subscriber_info[0][3])

            if not a.discount_given():
                a_coupon = post.Coupon()

            if v:
                coupon = f"Coupon code: {v[0]}"
                survey_ctc_email = f"Survey contact email: {v[1]}"
                a_coupon.record_daily_vouchers(v[0], v[1], a.voucher_reason_5)
                a_survey.record_survey_details([a_survey.location, a_survey.survey_results, coupon, survey_ctc_email, Visitors.subscriber_info])

        if Visitors.non_subscriber_info:
            a.save_non_cust_info(Visitors.non_subscriber_info)
            a.save_reasons_daily(Visitors.reasons_daily_totals)
            a_survey = post.Survey()
            a_survey.survey_willingness()

            get_email = a_survey.get_survey_ask_email()
            vv = a_survey.survey_contact(get_email)

            if not a.discount_given():
                a_coupon = post.Coupon()

            if vv:
                coupon = f"Coupon code: {vv[0]}"
                survey_ctc_email = f"Survey contact email: {vv[1]}"
                a_coupon.record_daily_vouchers(vv[0], vv[1], a.voucher_reason_5)
                a_survey.record_survey_details([a_survey.location, a_survey.survey_results, coupon, survey_ctc_email, Visitors.non_subscriber_info])

    if start.lower() == 's':
        r = admin.Reports()
        rpt_date = None
        while True:
            reports = input(f"\nReport {yellow}[c]ustomers,{clr} {cyan}[r]easons,{clr} {red}[s]urveys,{clr} {green}[v]ouchers,{clr} {purple} [d]etails on "
                            f"surveys,{clr} {blue}[a]ll email subscribers,{clr} [p]revious menu, or [e]xit? ")
            if reports.lower() == 'e':
                sys.exit()
            elif reports.lower() == 'a':
                r.subscribers()
            elif reports.lower() == 'c':
                if rpt_date:
                    while True:
                        ques = input("Would you like to use the same date as before? [Y]es or [N]o ")
                        if ques.lower() == 'y':
                            r.report_custs(rpt_date)
                            break
                        elif ques.lower() == 'n':
                            rpt_date = r.get_date()
                            r.report_custs(rpt_date)
                            break
                        elif ques.lower() != 'y' or ques.lower() != 'n':
                            continue
                else:
                    rpt_date = r.get_date()
                    r.report_custs(rpt_date)
            elif reports.lower() == 'r':
                if rpt_date:
                    while True:
                        ques = input("Would you like to use the same date as before? [Y]es or [N]o ")
                        if ques.lower() == 'y':
                            r.report_reasons(rpt_date)
                            break
                        elif ques.lower() == 'n':
                            rpt_date = r.get_date()
                            r.report_reasons(rpt_date)
                            break
                        elif ques.lower() != 'y' or ques.lower() != 'n':
                            continue
                else:
                    rpt_date = r.get_date()
                    r.report_reasons(rpt_date)
            elif reports.lower() == 's':
                if rpt_date:
                    while True:
                        ques = input("Would you like to use the same date as before? [Y]es or [N]o ")
                        if ques.lower() == 'y':
                            r.report_surveys(rpt_date)
                            break
                        elif ques.lower() == 'n':
                            rpt_date = r.get_date()
                            r.report_surveys(rpt_date)
                            break
                        elif ques.lower() != 'y' or ques.lower() != 'n':
                            continue
                else:
                    rpt_date = r.get_date()
                    r.report_surveys(rpt_date)
            elif reports.lower() == 'd':
                if rpt_date:
                    while True:
                        ques = input("Would you like to use the same date as before? [Y]es or [N]o ")
                        if ques.lower() == 'y':
                            r.survey_contact_details(rpt_date)
                            break
                        elif ques.lower() == 'n':
                            rpt_date = r.get_date()
                            r.survey_contact_details(rpt_date)
                            break
                        elif ques.lower() != 'y' or ques.lower() != 'n':
                            continue
                else:
                    rpt_date = r.get_date()
                    r.survey_contact_details(rpt_date)
            elif reports.lower() == 'v':
                if rpt_date:
                    while True:
                        ques = input("Would you like to use the same date as before? [Y]es or [N]o ")
                        if ques.lower() == 'y':
                            r.report_daily_vouchers(rpt_date)
                            break
                        elif ques.lower() == 'n':
                            rpt_date = r.get_date()
                            r.report_daily_vouchers(rpt_date)
                            break
                        elif ques.lower() != 'y' or ques.lower() != 'n':
                            continue
                else:
                    rpt_date = r.get_date()
                    r.report_daily_vouchers(rpt_date)
            elif reports.lower() == 'p':
                new_session()
                break
            else:
                continue

new_session()
