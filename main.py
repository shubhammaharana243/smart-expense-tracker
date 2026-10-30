from datetime import datetime
import json

current_date = datetime.now().strftime("%d-%m-%Y")

with open("expense.json", "r") as f:
    data_in_file = json.load(f)



def add_expense():
    print("===== ADD EXPENSE =====")
    while True:
        try:
            amt = int(input("Enter amount: "))
            cate = input("Enter category: ")
            des = input("Enter description: ")

            break

        except ValueError :
            print("\n Please enter valid details\n")
            
            


    data = {
    "id": 1,
    "date": current_date,
    "category": cate.capitalize(),
    "amount": amt,
    "description": des.capitalize()
    }

    if len(data_in_file) ==0:
        data['id']=1
    elif 'id' in data_in_file[-1]:
        data['id'] = data_in_file[-1]['id'] + 1

    data_in_file.append(data)

    with open("expense.json", "w") as f:
        json.dump(data_in_file, f, indent=4)

    print("\nExpense added successfully! ✅")
    

def view_expense():
    total_amt=0
    print("\n===== ALL EXPENSES =====\n")

    print("ID    Date          Category        Amount      Description")
    print("-----------------------------------------------------------")
    for i in data_in_file:
        total_amt +=i['amount']
        print(f"{i['id']:<6}{i['date']:<14}{i['category']:<16}{i['amount']:<12}{i['description']}")


    print("-----------------------------------------------------------")
    print(f"Total Expenses: ₹{total_amt}")
    

def search_expense():

    total_found= 0
    total_amt=0
    
    print("\n===== SEARCH EXPENSE =====\n")

    print("Search by:\n"
           "1. Category\n"
           "2. Description\n"
           "3. Amount\n"
           "4. Date\n")
    while True:
        try:
            src_choose = input("Choose: ")
            break
        except ValueError :
            print("\n Please enter 1/2/3/4-\n")
        
    if src_choose == "1":
        src_data = input("Enter category: ").capitalize()
    elif src_choose == "2":
        src_data = input("Enter description: ").capitalize()
    elif src_choose == "3":
        while True:
            try:
                src_data = int(input("Enter amount: "))
                break
            except ValueError:
                print("Enter correct amount")
    elif src_choose == "4":
        while True:
            try:
                src_data = input("Enter Date(dd-mm-yyyy): ")
                break
            except ValueError:
                print("Enter date in valid formate (dd-mm-yyyy)")
    else:
        print("Enter valid options(1-4)")
        

    print("\n===== SEARCH RESULTS =====\n")
    print("ID    Date          Category        Amount      Description")
    print("-----------------------------------------------------------")

    for i in data_in_file:
        for j in i:
            if i[j]==src_data:
                total_amt +=i['amount']
                print(f"{i['id']:<6}{i['date']:<14}{i['category']:<16}{i['amount']:<12}{i['description']}")

                total_found +=1
    print(f"\nTotal found: {total_found}")
    print(f"Total spent: ₹{total_amt}")
    
                
def monthly_summary():
    no = 0
    monthly_total=0
    highest_expense = 0
    lowest_expense=0
    list =[]
    dic = {}
    data_in_month= []

    def monthname(m):
        if m=='01':
            print(f"\n===== JANUARY {y} =====\n")
        elif m=='02':
            print(f"\n===== FEBRUARY {y} =====\n")
        elif m=='03':
            print(f"\n===== MARCH {y} =====\n")
        elif m=='04':
            print(f"\n===== APRIL {y} =====\n")
        elif m=='05':
            print(f"\n===== MAY {y} =====\n")
        elif m=='06':
            print(f"\n===== JUNE {y} =====\n")
        elif m=='07':
            print(f"\n===== JULY {y} =====\n")
        elif m=='08':
            print(f"\n===== AUGUST {y} =====\n")
        elif m=='09':
            print(f"\n===== SEPTEMBER {y} =====\n")
        elif m=='10':
            print(f"\n===== OCTOBER {y} =====\n")
        elif m=='11':
            print(f"\n===== NOVEMBER {y} =====\n")
        elif m=='12':
            print(f"\n===== DECEMBER {y} =====\n")
 
    while True:
        try:
            
            m = input("Enter month(MM): ")
            y = input("Enter year(YYYY): ")

            break

        except ValueError :
            print("\n Please enter valid details\n")

    data_found = False

    for i in data_in_file:
        if f"{m}-{y}" in i['date']:
            data_found = True  

    if not data_found:
        print("No data found for this month in the data file.")

    if data_found:
        monthname(m)
            

    for i in data_in_file:
        if i['category'] not in list:
            list.append(i['category'])


           
    for i in data_in_file:
        date_in_list = i['date'].split('-')

        if date_in_list[1]==m and date_in_list[2]==y:    
            data_in_month.append(i)

            monthly_total+= i['amount']
            no +=1
            if i['amount']> highest_expense:
                highest_expense=i['amount']

    for i in data_in_month:    
        if i['category'] not in dic:
            dic[i['category']]=i['amount']
        else:
            dic[i['category']] += i['amount']
                        
    lowest_expense = min(data_in_month, key=lambda x:x['amount'])        
    print(f"Total Expenses: ₹{monthly_total}\n")
    print(f"Number of Expenses: {no}\n")
    print(f"Highest Expense: ₹{highest_expense}")
    print(f"Lowest Expense: ₹{lowest_expense['amount']}")
    print(f"Avarage Expense: ₹{(monthly_total/no):.2f}\n")

    print("Highest Spending Category:")
    highest_expense_in_dic = max(dic, key=dic.get)
    print(f"{highest_expense_in_dic} -> ₹{dic[highest_expense_in_dic]}\n")

    print("Lowest Spending Category:")
    lowest_expense_in_dic = min(dic, key=dic.get)
    print(f"{lowest_expense_in_dic} -> ₹{dic[lowest_expense_in_dic]}")
  

def category_analysis():
    list = []
    dic ={}
    total_expenses = 0
    for i in data_in_file:
        total_expenses +=i['amount']

    for i in data_in_file:
        if i['category'] not in list:
            list.append(i['category'])

    for i in data_in_file:
        for j in range(0,len(list)):
            if list[j]==i['category']:
                if i['category'] not in dic:
                    di = {i['category']:i['amount']}
                    dic.update(di)
                else:
                    dic[i['category']] = dic[i['category']] + i['amount']
    



    print("\n===== CATEGORY ANALYSIS =====\n")

    sorted_dict = sorted(dic.items(), key=lambda item: item[1], reverse =True)
    for key, value in sorted_dict:
        print(f"{key.capitalize():<16} ₹{value}")
        
    print("------------------------------")
    t="Total"
    print(f"{t:<16} ₹{total_expenses}")
    
    
def budget_status():
    total_expenses = 0
    for i in data_in_file:
        total_expenses +=i['amount']
    while True:
        try:
            monthly_budget = int(input("Enter your monthly budget: ₹"))
            
            break
        
        except ValueError :
            print("\n Please enter valid details\n")


    print("\n===== BUDGET STATUS =====\n")

    print(f"Monthly Budget:    ₹{monthly_budget}")
    print(f"Total Spent:       ₹{total_expenses}")
    print(f"Remaining:         ₹{monthly_budget-total_expenses}")

    print(f"\nUsed: {(total_expenses/monthly_budget*100):.2f}%")

    if monthly_budget>total_expenses:
        print("\nStatus: ✅ Within Budget")
    else:
        print("\nStatus: ⚠️ BUDGET EXCEEDED\n")
        print(f"You have exceeded your budget by ₹{total_expenses-monthly_budget}.\n")


def exit():
    print("\n===== SMART EXPENSE TRACKER =====\n")

    print("Thank you for using Smart Expense Tracker! \n")
    print("Your data has been saved successfully.\n")
    print("Goodbye!")


def main():
    print("\n===== SMART EXPENSE TRACKER =====")

    while True:
        print("\nHere are the available options:\n"
                "1. Add Expense\n"
                "2. View Expenses\n"
                "3. Search Expense\n"
                "4. Monthly Summary\n"
                "5. Category Analysis\n"
                "6. Budget Check\n"
                "7. Exit\n")
        while True:
            try:
                choose = input("Choose: ")
                break
            except ValueError :
                print("\n Please enter 1/2/3/4/5/6/7\n")

        if choose == "1":
            add_expense()
        elif choose == "2":
            view_expense()
        elif choose == "3":
            search_expense()
        elif choose == "4":
            monthly_summary()
        elif choose == "5":
            category_analysis()
        elif choose == "6":
            budget_status()
        elif choose == "7":
            exit()
            break
        else:
            print("\n⚠️Please enter avilable option(1-7)")

if __name__ == "__main__":
    main()
