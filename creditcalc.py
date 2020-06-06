from math import ceil, log
from sys import argv


def diff_def(principal_par, monthes_par, percent_par):
    i = percent_par / (100 * 12)
    over_p = 0
    for m in range(int(monthes_par)):
        d = principal_par / monthes_par + i * (principal_par - ((principal_par * m) / monthes_par))
        print(f'Month {m + 1}: paid out {ceil(d)}')
        over_p += ceil(d)
    print(f'\nOverpayment = {over_p - int(principal_par)}')


def print_month_def(monthes_par):
    if 0 < monthes_par <= 1:
        print('You need 1 month to repay this credit!')
    elif 1 < monthes_par < 12:
        print(f'You need {ceil(monthes_par)} months to repay this credit!')
    elif monthes_par == 12:
        print('You need 1 year to repay this credit!')
    elif 12 < monthes_par < 23:
        if monthes_par % 12 == 1:
            print(f'You need 1 year and 1 month to repay this credit!')
        else:
            print(f'You need 1 year and {monthes_par % 12} months to repay this credit!')
    elif monthes_par % 12 == 0:
        print(f'You need {int(monthes_par / 12)} years to repay this credit!')
    elif monthes_par % 12 == 1:
        print(f'You need {int(monthes_par / 12)} years and 1 month to repay this credit!')
    else:
        print(f'You need {int(monthes_par / 12)} years and {int(monthes_par % 12)} months to repay this credit!')


def monthes_def(principal_par, payment_par, percent_par):
    i = percent_par / (100 * 12)
    monthes_result = log((payment_par / (payment_par - i * principal_par)), 1 + i)
    print_month_def(ceil(monthes_result))
    print(f'Overpayment = {int(payment_par * ceil(monthes_result) - int(principal_par))}')


def payments_def(principal_par, monthes_par, percent_par):
    i = percent_par / (100 * 12)
    payment_result = ceil(principal_par * ((i * (1 + i) ** monthes_par) / ((1 + i) ** monthes_par - 1)))
    print(f'Your annuity payment = {payment_result}!')
    print(f'Overpayment = {int(payment_result * monthes_par - int(principal_par))}')


def principal_def(payment_par, monthes_par, percent_par):
    i = percent_par / (100 * 12)
    principal_result = payment_par / ((i * pow(1 + i, monthes_par)) / (pow(1 + i, monthes_par) - 1))
    print(f'Your credit principal = {int(principal_result)}!')
    print(f'Overpayment = {int(payment_par * monthes_par - int(principal_result))}')


args = argv[1:]
# args = ['--type=diff', '--principal=30000', '--periods=-14', '--interest=10']
# print(args)
type_credit = None
principal = None
payment = None
percent = None
monthes = None
for el in args:
    if el[2:el.rfind('=')] == 'type':
        type_credit = el[el.rfind('=') + 1:]
    elif el[2:el.rfind('=')] == 'principal':
        if float(el[el.rfind('=') + 1:]) > 0:
            principal = float(el[el.rfind('=') + 1:])
    elif el[2:el.rfind('=')] == 'payment':
        if float(el[el.rfind('=') + 1:]) > 0:
            payment = float(el[el.rfind('=') + 1:])
    elif el[2:el.rfind('=')] == 'interest':
        if float(el[el.rfind('=') + 1:]) >= 0:
            percent = float(el[el.rfind('=') + 1:])
    elif el[2:el.rfind('=')] == 'periods':
        if float(el[el.rfind('=') + 1:]) > 0:
            monthes = float(el[el.rfind('=') + 1:])
    # else:
    #     print(el[2:el.rfind('=')])

# type_nap = input("""What do you want to calculate?
# type "n" - for count of months,
# type "a" - for annuity monthly payment,
# type "p" - for credit principal:\n""")

# if type_nap == 'n':
#     principal = float(input('Enter credit principal:\n'))
#     payment = float(input('Enter monthly payment:\n'))
#     percent = float(input('Enter credit interest:\n'))
#     monthes(principal, payment, percent)
# elif type_nap == 'a':
#     principal = float(input('Enter credit principal:\n'))
#     monthes = float(input('Enter count of periods:\n'))
#     percent = float(input('Enter credit interest:\n'))
#     payments(principal, monthes, percent)
# elif type_nap == 'p':
#     payment = float(input('Enter monthly payment:\n'))
#     monthes = float(input('Enter count of periods:\n'))
#     percent = float(input('Enter credit interest:\n'))
#     principal(payment, monthes, percent)
# else:
#     pass

if type_credit == 'diff':
    if principal is not None and monthes is not None and percent is not None and payment is None:
        diff_def(principal, monthes, percent)
    else:
        print('Incorrect parameters.')
elif type_credit == 'annuity':
    if principal is not None and monthes is not None and percent is not None:
        payments_def(principal, monthes, percent)
    elif principal is not None and payment is not None and percent is not None:
        monthes_def(principal, payment, percent)
    elif payment is not None and monthes is not None and percent is not None:
        principal_def(payment, monthes, percent)
    else:
        print('Incorrect parameters.')
else:
    print('Incorrect parameters.')
