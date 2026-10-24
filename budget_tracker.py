# Personal Budget & Expense Tracker

def calculate_budget():
    print("========================================")
    print("     PERSONAL BUDGET CALCULATOR         ")    
    print("========================================")
    
    # Get total monthly income
    income = float(input(" Enter your total monthly income ($): "))

    # Get expense amounts by category 
    print("\nEnter your total spending for each category")
    food = float(input(" Food & Snacks ($): "))
    entertainment = float(input(" Entertainment & Fun ($): "))
    bills = float(input(" Utilities and Subscriptions ($): "))
    other = float(input(" Other expenses ($): "))

    # Calculations
    total_expenses = food + entertainment + bills + other
    remaining balance = income - total_expenses
    savings_rate = (remaining_balance / income * 100) if income > 0 else 0
    # Summary report
    print("\n----------------------------------")
    print("     FINANCIAL SUMMARY              ")
    print("------------------------------------")
    print(f"Total Income:       ${income:,. 2f}")
    print(f"Remaining Balance:  ${remaining_balance:,.2f}")
    print(f"Savings Rate:       ${savings_rate:.1f}%"

    # Category Breakdown Percentages
    if total_expenses > 0:
        print("\n--- Expense Breakdown ---")
        print(f" Food:       {(food / total_expenses * 100):.1f}%")
        print(f" Entertainment {(entertainment / total expenses * 100):.1f}%")
        print(f" Bills:          {(bills / total_expenses * 100):.1f}%")
        print(f" Other:         {(other / total_expenses * 100):.1f}%")

       # Financial Status Advice 
       print("\n---Status ---")
       if remaining balance > 0:
           print("Great job! You are living within your budget")
       elif remaining_balance == 0:
           print("You broke even this month. Try saving more next time")
      else:
          print("Warning: You are over budget! Consider reducing unnecessary costs
    print("=============================================")

  if __name__ == "__main__":
       calculate_budget()
        

     


