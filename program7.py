'''Write a Python program to build a 'Digital Bank & Account Analyzer' using Functions and 
Recursion. The program must demonstrate three core concepts:
1.
Basic Function & Default Parameters: Create a function currency_converter to convert a given 
amount from USD to INR, using a default parameter for the conversion rate.
2.
Standard Function with Loop: Create a function calculate_average_balance that takes a list 
of monthly account balances and calculates their average.
3.
Recursive Function: Create a recursive function recursive_transaction_history to print all 
the transactions from a list one by one without using any loops.'''

print("===Digital Bank & Account Analyzer===")

def currency_converter(usd,rate=90):
    inr = usd*rate
    print(f"{usd} USD is {inr} in INR ")
    return inr

def calculate_average_balance(listt):
    sum=0
    i=0
    while i<len(listt):
        sum=sum + listt[i]
        i+=1
    avg=sum/len(listt)
    print(f"Average Salary is {avg}")
    return avg

def recursive_transaction_history(history,idx=0):
    if idx==len(history):
        print("End of history")
        return 
    print(f"Transaction {idx+1}: {history[idx]}")
    recursive_transaction_history(history,idx +1)

dollar= 20.4
currency_converter(dollar) #(dollar, any current rate )

Salary= [100000,50000,75000,25000]
calculate_average_balance(Salary)
print(calculate_average_balance(Salary))

recent_transactions = [
    "Credited ₹5000 (UPI)", 
    "Debited ₹1200 (Amazon)", 
    "Credited ₹25000 (Salary)", 
    "Debited ₹450 (Zomato)"
]
recursive_transaction_history(recent_transactions)