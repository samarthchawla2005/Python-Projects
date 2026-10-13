expenses = []

add_exp = 'Y'

while add_exp == 'Y':

    while True:
        try:
            expense_numbers = int(
                input("\nEnter the number of expenses you want to enter: ")
            )
            if expense_numbers <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Caution! Enter numbers only.")

    for i in range(len(expenses) + 1,
                   len(expenses) + expense_numbers + 1):

        print(f"\nExpense {i}")

        expense_name = input("Enter expense name: ")

        while True:
            try:
                expense_amount = int(input("Enter amount: "))

                if expense_amount <= 0:
                    print("Amount must be greater than zero.")
                    continue

                break

            except ValueError:
                print("Caution! Enter numbers only.")

        expense_category = input("Enter category: ").strip()

        expenses.append([
            expense_name, expense_amount, expense_category
        ])

        print("\nExpense added successfully!")
        print("\n==== EXPENSE DETAILS ====")
        print(
            f"Name: {expense_name}\n"
            f"Amount: {expense_amount}\n"
            f"Category: {expense_category}"
        )

    add_exp = input(
        "\nDo you want to add more expenses? (Y/N): "
    ).strip().upper()

    while add_exp not in ('Y', 'N'):
        print("Invalid input! Please enter 'Y' or 'N'.")
        add_exp = input(
            "\nDo you want to add more expenses? (Y/N): "
        ).strip().upper()


print("\n=== ALL EXPENSES ===")
print("Name\tAmount\tCategory")

total_exp_amt = 0

for expense in expenses:
    print(f"{expense[0]}\t{expense[1]}\t{expense[2]}")
    total_exp_amt += expense[1]

print("\nTotal Expenses =", total_exp_amt)


yn = input(
    "\nDo you want to search a category? (Y/N): "
).strip().upper()

while yn not in ('Y', 'N'):
    print("You can only enter 'Y' for Yes or 'N' for No.")
    yn = input(
        "\nDo you want to search a category? (Y/N): "
    ).strip().upper()

while yn == 'Y':

    found = False

    catg_search = input(
        "\nEnter a category to search: "
    ).strip()

    print(f"\n=== {catg_search} EXPENSES ===")

    for expense in expenses:
        if expense[2].lower() == catg_search.lower():
            print(f"{expense[0]} - {expense[1]}")
            found = True

    if not found:
        print("No expenses found for this category.")

    yn = input(
        "\nDo you want to search another category? (Y/N): "
    ).strip().upper()

    while yn not in ('Y', 'N'):
        print("Invalid input! Please enter 'Y' or 'N'.")
        yn = input(
            "\nDo you want to search another category? (Y/N): "
        ).strip().upper()


print("\n=== CATEGORY SUMMARY ===")

catg_total = {}

for expense in expenses:
    category = expense[2].strip().title()
    amount = expense[1]

    if category in catg_total:
        catg_total[category] += amount
    else:
        catg_total[category] = amount

print("\nCategory\tTotal")

for category, total in catg_total.items():
    print(f"{category}\t-\t{total}")