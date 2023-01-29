#Script to calculate mortgage payments!

import time

print("Running Mortgage Calculator!")

def calculate_mortgage_payment(principal, rate, term):
    r = rate / 12 / 100
    n = term * 12
    payment = (principal * r) / (1 - (1 + r)**(-n))
    return payment

def calculate_loan_interest(principal, rate, term):
    r = rate / 12 / 100
    n = term * 12
    payment = calculate_mortgage_payment(principal, rate, term)
    interest = payment * n - principal
    return interest

principal = float(input("Enter the loan amount: "))
rate = float(input("Enter the interest rate (in percentage): "))
term = float(input("Enter the loan term in years: "))

payment = calculate_mortgage_payment(principal, rate, term)
interest = calculate_loan_interest(principal, rate, term)
time.sleep(1)

print(f"Monthly Mortgage Payment: ${payment:.2f}")
print(f"Total Loan Interest: ${interest:.2f}")



