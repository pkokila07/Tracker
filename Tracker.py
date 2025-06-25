expenses = []

def show_expenses():
    if not expenses:
        print("No expenses recorded.")
    else:
        print("\nExpense List:")
        for idx, expense in enumerate(expenses, 1):
            print(f"{idx}. {expense['category']} - ${expense['amount']}")

def add_expense():
    category = input("Enter the expense category (Food, Transport): ")
    try:
        amount = float(input("Enter the expense amount: $"))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return
    expenses.append({"category": category, "amount": amount})
    print(f"Expense added: {category} - ${amount}")

def total_expenses():
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total expenses: ${total}")

def main():
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Show expenses")
        print("2. Add expense")
        print("3. Show total expenses")
        print("4. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            show_expenses()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
