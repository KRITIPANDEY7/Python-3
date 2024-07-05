class Transaction:
    

    def __init__(self, date, description, amount, category):
        """
        Initializes a Transaction object with the following attributes:

        Args:
            date (str): The date of the transaction in YYYY-MM-DD format.
            description (str): A brief description of the transaction.
            amount (float): The amount of the transaction (positive for income, negative for expense).
            category (str): The category the transaction belongs to (e.g., "Food", "Transportation").
        """

        self.date = date
        self.description = description
        self.amount = amount
        self.category = category

        # Input validation (optional)
        if not isinstance(amount, (int, float)):
            raise ValueError("Amount must be a number")


class ExpenseTracker:
   
    def __init__(self):
        
        self.transactions = []

    def add_transaction(self, transaction):
        
        self.transactions.append(transaction)

    def view_transactions(self):
       
        if not self.transactions:
            print("No transactions found.")
            return

        print("Transactions:")
        for transaction in self.transactions:
            print(f"{transaction.date} - {transaction.description} - ${transaction.amount:.2f} - {transaction.category}")

    def get_total_expenses(self):
        
        total_expenses = sum(transaction.amount for transaction in self.transactions if transaction.amount < 0)
        return total_expenses

    def get_total_income(self):
        
        total_income = sum(transaction.amount for transaction in self.transactions if transaction.amount > 0)
        return total_income

    def get_balance(self):
        
        return self.get_total_income() - self.get_total_expenses()


if __name__ == "__main__":
    tracker = ExpenseTracker()

    # Add sample transactions with input validation
    try:
        tracker.add_transaction(Transaction("2024-05-04", "Groceries", 100.0, "Food"))
    except ValueError as e:
        print("Error:", e)

    tracker.add_transaction(Transaction("2024-06-03", "Gas", 30.0, "Transportation"))
    tracker.add_transaction(Transaction("2024-06-20", "Dinner", 110.0, "Food"))

    # View all transactions
    tracker.view_transactions()

    # Calculate and display totals
    total_expenses = tracker.get_total_expenses()
    total_income = tracker.get_total_income()
    balance = tracker.get_balance()

    print(f"\nTotal Expenses: ${total_expenses:.2f}")
    print(f"Total Income: ${total_income:.2f}")
    print(f"Balance: ${balance:.2f}")

        
       