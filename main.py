# Basic Budgeting System

import json

# reading categories in json file
with open("Budgeting Categories.json", "r") as f:
    categories = json.load(f)

# update the different categories in the file
while True:
    update_prices = input("Would you like to update any of the prices (y/n)?: ")
    if update_prices == "n":
        break

    elif update_prices == "y":
        print("Categories: Subcategories:")
        print("Entertainment: Netflix; Amazon; Hulu Plus; Disney Plus, Movie Tickets")
        print("Bills: Phone; Light; Rent; Gas; Insurance")
        print("Food: Groceries; Fast Food/ Delivery; Restaurants")
        print("Clothing: Clothes; Shoes")

        category = input("Enter Category: ")
        sub_category = input("Enter Subcategory: ")
        # checks to see if the category is in the dictionary and checks if subcategories exist
        if category in categories and sub_category in categories[category]:
            new_price = float(input("Enter value: "))
            # sets a new value to a specific subcategory in a category
            categories[category][sub_category] = float(new_price)
            print("Price has been updated!")
            print("If price does not update go in file and change price to the appropriate prices")
        else:
            print("Invalid category or subcategory")
    else:
        print("Invalid Input! Try Again: ")
# write the new value to the file
with open("Budgeting Categories.json", "w") as f:
    json.dump(categories, f)

# keep track of total spending in all categories together
total_spending = 0
# Iterates through category and keeps track of the categorical spending
for category in categories:
    # Keeps track of category spending
    category_spending = 0
    # loops through each subcategory within the dictionary of categories
    for sub_category in categories[category]:
        # Check if the value of the subcategory is none
        if categories[category][sub_category] is not None:
            # code is adding the values of a subcategory to the total spending of a category
            category_spending += categories[category][sub_category]
        # total spending of all the categories combined
        total_spending += category_spending

    print(category, ": $", category_spending)
print("Complete total of spending is", total_spending)

HoursWorked = float(input("How many hours do you work?: "))
Pay = float(input("How much do you get paid?: "))
Weeks = float(input("How many weeks per month do you work?: "))
Income = HoursWorked * Pay * Weeks
print(f"Your income should be making {Income} per month! ")
Budget = float(input("How Much would you like to save per month "))

if Income > total_spending:
    print("Your budgeting is great!")
    print("If you would like to save more check the categories and cut back on necessities!")

elif Income < total_spending:
    print("ALERT!!!!")
    print("Please decrease your spending if you ")
