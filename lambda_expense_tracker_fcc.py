def add_expense(expenses, amount, category):
    expenses = []
    expenses.append({'amount': amount, 'category': category})
    pass

def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')
    pass

def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))

def filter_expenses_by_category(expenses, category):
    pass