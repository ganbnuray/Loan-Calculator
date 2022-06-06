import argparse
import math
parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--principal")
parser.add_argument("--payment")
parser.add_argument("--interest")
parser.add_argument("--periods")
args = parser.parse_args()

#Error cases
if args.type != "diff" and args.type != "annuity":
    print("Incorrect parameters!")
if args.interest == None:
    print("Incorrect parameters!")

#differentiated payment
if args.type=="diff" and args.principal!=None and args.periods!=None and args.interest!=None:
    if int(args.principal) < 0 and int(args.periods) < 0 and int(args.interest) < 0:
        print("Incorrect prameters")
    else:
        i = float(args.interest) / 1200
        sum_num = 0
        for month in range(1,int(args.periods)+1):
            mth_payment = math.ceil(int(args.principal) / int(args.periods) + i * (int(args.principal) - ((int(args.principal) * (month - 1)) / int(args.periods))))
            sum_num+=mth_payment
            print("Month {}: payment is {}".format(month,mth_payment))
        print()
        print("Overpayment = {}".format(sum_num - int(args.principal)))

#Loan principal payment
if args.type!=None and args.payment!=None and args.periods!=None and args.interest!=None:
    if int(args.payment)<0 and int(args.periods)<0 and int(args.interest)<0:
        print("Incorrect prameters")
    else:
        i = float(args.interest) / 1200
        monthly_payment = int(args.payment)
        number_months = int(args.periods)
        loan_principal = math.floor(monthly_payment / ((i * math.pow(1+i, number_months)) / (math.pow(1+i,number_months)-1)))
        overpayment = monthly_payment * number_months - loan_principal
        print("Your loan principal = {}!".format(loan_principal))
        print("Overpayment = {}".format(overpayment))


#Annuity payment
if args.type=="annuity" and args.principal!=None and args.periods!=None and args.interest!=None:
    if int(args.principal)<0 and int(args.periods)<0 and int(args.interest)<0:
        print("Incorrect parameters")
    else:
        i = float(args.interest)/1200
        loan_principal = int(args.principal)
        number_months = int(args.periods)
        monthly_payment = math.ceil((loan_principal * (i * math.pow(1+i,number_months))) / (math.pow(1+i,number_months) - 1))
        overpayment = monthly_payment * number_months - loan_principal
        print("Your annuity payment = {}!".format(monthly_payment))
        print("Overpayment = {}".format(overpayment))

#the time to pay the loan
if args.type=="annuity" and args.principal!=None and args.payment!=None and args.interest!=None:
    if int(args.principal)<0 and int(args.payment)<0 and int(args.interest)<0:
        print("Incorrect prameters")
    else:
        i = float(args.interest)/1200
        loan_principal = int(args.principal)
        monthly_payment = int(args.payment)
        number_months = math.ceil(math.log(monthly_payment / (monthly_payment - i * loan_principal), 1 + i))
        overpayment = monthly_payment * number_months - loan_principal
        years = number_months // 12
        months = number_months - years * 12
        if years==0:
            if months!=1 :
                print("It will take {} months to repay this loan!".format(months))
            elif months == 1:
                print("It will take {} month to repay this loan!".format(months))
        elif years == 1:
            if months ==0:
                print("It will take {} year to repay this loan!".format(years))
            elif months>1 :
                print("It will take {} year and {} months to repay this loan!".format(years, months))
            elif months == 1:
                print("It will take {} year and {} month to repay this loan!".format(years,months))
        elif years > 1:
            if months ==0:
                print("It will take {} years to repay this loan!".format(years))
            elif months>1 :
                print("It will take {} years and {} months to repay this loan!".format(years, months))
            elif months == 1:
                print("It will take {} years and {} month to repay this loan!".format(years,months))
        print("Overpayment = {}".format(overpayment))
