class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        # Private attributes to store category details securely
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget

    # Getter method for category name
    def get_category_name(self):
        return self.__category_name

    # Setter method for category name
    def set_category_name(self, new_name):
        self.__category_name = new_name

    # Getter method for allocated budget
    def get_allocated_budget(self):
        return self.__allocated_budget

    # Setter method for allocated budget
    def set_allocated_budget(self, new_budget):
        if new_budget < 0:
            print("Budget cannot be negative!")
        else:
            self.__allocated_budget = new_budget

    # Method to display budget details
    def display_details(self):
        print(f"Category: {self.__category_name}, Allocated Budget: ${self.__allocated_budget:.2f}")

# Demonstration Script
if __name__ == "__main__":
    # Creating instances of BudgetCategory
    food_budget = BudgetCategory("Food", 500.00)
    entertainment_budget = BudgetCategory("Entertainment", 200.00)

    # Display initial details
    print("Initial Budgets:")
    food_budget.display_details()
    entertainment_budget.display_details()

    # Modify category name and budget using setter methods
    food_budget.set_category_name("Groceries")
    food_budget.set_allocated_budget(600.00)
    entertainment_budget.set_allocated_budget(-50.00)  # Invalid input

    # Display updated details
    print("\nUpdated Budgets:")
    food_budget.display_details()
    entertainment_budget.display_details()

class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        # Private attributes to store category details securely
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.__remaining_budget = allocated_budget  # Tracks remaining budget after expenses

    # Getter method for category name
    def get_category_name(self):
        return self.__category_name

    # Setter method for category name
    def set_category_name(self, new_name):
        if not new_name.strip():
            print("Category name cannot be empty!")
        else:
            self.__category_name = new_name

    # Getter method for allocated budget
    def get_allocated_budget(self):
        return self.__allocated_budget

    # Setter method for allocated budget
    def set_allocated_budget(self, new_budget):
        if new_budget < 0:
            print("Allocated budget must be a positive number!")
        else:
            self.__allocated_budget = new_budget
            self.__remaining_budget = new_budget  # Reset remaining budget to match new allocation

    # Getter for remaining budget
    def get_remaining_budget(self):
        return self.__remaining_budget

    # Method to add an expense to the budget category
    def add_expense(self, expense_amount):
        if expense_amount <= 0:
            print("Expense amount must be a positive number!")
        elif expense_amount > self.__remaining_budget:
            print(f"Insufficient budget! You only have ${self.__remaining_budget:.2f} remaining.")
        else:
            self.__remaining_budget -= expense_amount
            print(f"Expense of ${expense_amount:.2f} added to {self.__category_name}. Remaining budget: ${self.__remaining_budget:.2f}")

    # Method to display budget details
    def display_details(self):
        print(f"Category: {self.__category_name}")
        print(f"Allocated Budget: ${self.__allocated_budget:.2f}")
        print(f"Remaining Budget: ${self.__remaining_budget:.2f}")
        print("-" * 30)


# Demonstration Script
if __name__ == "__main__":
    # Creating instances of BudgetCategory
    food_budget = BudgetCategory("Food", 500.00)
    entertainment_budget = BudgetCategory("Entertainment", 200.00)

   
    print("Initial Budgets:")
    food_budget.display_details()
    entertainment_budget.display_details()

   
    food_budget.set_category_name("Groceries")
    food_budget.set_allocated_budget(600.00)

    
    print("\nAdding Expenses:")
    food_budget.add_expense(100.00)  # Valid expense
    food_budget.add_expense(550.00)  # Expense exceeds remaining budget
    entertainment_budget.add_expense(50.00)  # Valid expense

    # Display updated details
    print("\nUpdated Budgets:")
    food_budget.display_details()
    entertainment_budget.display_details()

