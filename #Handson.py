#Handson

print("Welcome to Personal Expense Tracker!\n")
print("1. Add Expense")
print("2. View Expenses")
print("3. Monthly Summary")
print("4. Exit")
choice = int(input("Enter your choice: "))

#Enter category (e.g., Food, Travel): Food
#Enter amount: 200
#Enter date (YYYY-MM-DD): 2024-12-23
#Expense added successfully!
#(Expense recorded in expenses.txt)
if choice == 1:
    
    print("Expense added successfully!")
    print("(Expense recorded in expenses.txt)")

ipCatagory = input("Enter category (e.g., Food, Travel):")
ipamount = (input("Enter amount:"))
ipDate = input("Enter date (YYYY-MM-DD):")



#1. Amount: 200 - Date: 2024-12-23
#
#Travel:
#No expenses recorded.
#

with open('expenses.txt','w') as f:
    f.write('Category, Amount, Date\n')
    f.write(ipCatagory)
    f.write(ipamount)
    f.write(ipDate)


with open('expenses.txt','r') as fr:
    content = fr.read()
    print(content)


if choice == 2:
    print('Expenses:\n')
    print('Food:\n')
    print(f'1. Amount:{ipamount} - Date: {ipDate}\n')
    print(f'Travel:\n')
    print('No expenses recorded.')

if choice == 3:
    print('Total Expenses:')
    print('By Category:\n')
    print('Food:',ipamount)
    print('Travel:0\n')



    



    










