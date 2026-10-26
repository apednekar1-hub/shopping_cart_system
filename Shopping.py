# datetime module is used to figure out the date of the specifc day the user uses this program
# from date time, import date is used as another piece of the datetime module to land the specifc date
from datetime import datetime, date
# User's shopping cart, when they add something it falls in here
shopping_cart = []
# Lists of the products in the asignment
products = ["Chips", "Soda", "Candy", "Cookies", "Water", "Sandwich"]
prices = [2.00, 2.50, 1.50, 3.00, 1.00, 5.00]

program_running = True 
while program_running == True: # The whole entirety of the code is in a single huge while loop to loop the main menu of shopping cart
    in_product_menu = True
    # Main Menu of the shopping cart
    print()
    print("========== SMART SHOPPING CART ==========")
    print("1. View Available Products")
    print("2. Add Product to Cart")
    print("3. Remove Product from Cart")
    print("4. View Shopping Cart")
    print("5. View Current Total")
    print("6. Checkout")
    print()
    try: # Tries the object in the indentation, in this case it is user_choice = interger, if user enters something other than an int it will move on to except value Error python code gives
        user_choice = int(input("Enter your choice: "))
        print()
    except ValueError: # If user choice is something that is incorrect and will give an error in try, it will fall under here 
        print()
        print("Please enter a number.")
        # Continue will be used everywhere to prevent the main menu screen to reappear to soon, it looks better this way
        input("Continue?: ")
        continue


    if user_choice == 1:
        print()
        for i in range(len(products)):
            # in the for loop, it will look through the products and lists and list them out in order from which they were placed in
            print(f" {i + 1}. {products[i]}          ${prices[i]:.2f}")
        print()
        input("Would you like to go back? (yes/no): ")
            
    if user_choice == 2:
        print("========== AVAILABLE PRODUCTS ==========")
        print()
        print("What product would you like to add?")
        print()
        try:
            for i in range(len(products)):
                print(f" {i + 1}. {products[i]}          ${prices[i]:.2f}")

            print()
            product_selection = int(input("Please select a product: "))

        except ValueError:
            print()
            print("Please input a number.")
            input("Continue?: ")
            continue

        # Checks the number selected is in the range of the number of products in the products list
        if product_selection <= 6 and product_selection >= 1:
            # The append looks at the products by the number the user selected minus 1, this is because lists start at 0, so we need to account for the numbering to the number of products
            shopping_cart.append(products[product_selection - 1])
            print()
            # Specifc products was added to the cart, means it looks at the user's selection and minuses 1 to find the specifc item the user selected
            print(f"{products[product_selection - 1]} was added to your cart")
            input("Continue?: ")

        else:
            print()
            print("Command unregonised, please input a number in the range of 1 to 6")
            input("Continue?: ")

    if user_choice == 3:
        if not shopping_cart:
            print()
            print("Your shopping cart is empty!")
            print("There's nothing to remove.")
            print()
            input("Continue?: ")
            continue
        else:
             print()
             print("========== YOUR SHOPPING CART ==========")
             print()
        for i in range(len(shopping_cart)):
                # looks into the shopping cart of the user to print out the number of specifc items
                print(f"{i + 1}. {shopping_cart[i]}")

        while True: 
            print()
            if not shopping_cart:
                print("Your shopping cart is empty")
                print("There is nothing to remove.")
                print()
                input("Continue?: ")
                continue
                    # print(f"{i + 1}. {shopping_cart[i]}")

            print("Which item would you like to remove?")
            try:
                remove = int(input("Enter item number: "))
            except:
                print()
                print("Not a valid response!")

            if remove >= 1:
                # Converts the number to a zero-based index
                index_to_remove = remove - 1
                # The if statement makes sure the calculated index actually exists within the bounds of the cart by looking at shopping cart length
                if index_to_remove < len(shopping_cart):
                    # Removes and discards the item at that specific position from the list
                    shopping_cart.pop(index_to_remove)
                    print("\nItem has been removed!")
                    cancel = input("Would you like to cancel? (yes/no): ")

                
                    if cancel == "yes":
                        # Changes the true variable to false that is in the main menu section, ensuring the menu loop won't start up again
                        in_product_menu = False
                        break     
                        # breaks the while loop thatis existing in the 3rd menu when user inputs 3
                    elif cancel == "no":
                        continue
                        # Continues back to the while loop inside the 3rd menu

                else:
                    print()
                    print("Invalid item number. That item isn't in your cart.")
                    print()
                    input("Continue?: ")
                    break
                    
    if user_choice == 4:
        while True:
            print("========== YOUR SHOPPING CART ==========")
            print()
            if not shopping_cart:
                print("Your shopping cart is empty")
                print("There is nothing to view here!")
                print()
            else:
                # The length of shopping cart is given as a number, so you can use it like so
                print(f"You have {len(shopping_cart)} items in your cart.")
                print()
            for i in range(len(shopping_cart)):
                # prints the items in the shopping cart with the exact number list on the left
                print(f"{i + 1}. {shopping_cart[i]}")
            print()
            choice = input("Would you like to go back? (yes/no): ")
            print()

            # Continues in the View Products section if user inputs "no"
            if choice == "no":
                print()
                for i in range(len(shopping_cart)):
                    print(f"{i + 1}. {shopping_cart[i]}")
                print()
                choice = input("Would you like to go back? (yes/no): ")
            elif choice == "yes":
                break
            else:
                print()
                print("Invalid input, try again!")
                print()

    if user_choice == 5:
        print("========== CURRENT TOTAL ==========")
        print()
        total = 0

        if not shopping_cart:
            print("Theres nothing in your cart!")
            input("Continue?: ")
        else:
            # The for loop suggests for i and item in shopping cart, the item in the product (its number in the list) the user selected will be in the specific index placement,
            # The item number will then be stored in the temporary_index variable to be checked by the prices in the sum of the total, the for loop repeats this for how many items there are in the shopping cart
            # Start = 1 is used to create a list number from 0 to how ever many items the user chooses
            for i, item in enumerate(shopping_cart, start=1):
                temp_index = products.index(item)
                total += prices[temp_index] 
                print(f"{i - 1}. {item:<6}         ${prices[temp_index]:.2f}")

        
            print()
            print(f"Your total is ${total:.2f}")
            print()
            input("Continue?: ")

    if user_choice == 6:
        print("========== RECEIPT ==========")
        print()

        if not shopping_cart:
            print("You do not have anything to check out! please select a product.")
            input("Continue?: ")

        else:
            total = 0

            print()
            print(date.today()) 
            print()
            
            # The for loop suggests for i and item in shopping cart, the item in the product (its number in the list) the user selected will be in the specific index placement,
            # The item number will then be stored in the temporary_index variable to be checked by the prices in the sum of the total, the for loop repeats this for how many items there are in the shopping cart
            # Start = 1 is used to create a list number from 0 to how ever many items the user chooses
            for i, item in enumerate(shopping_cart, start=1):
                temp_index = products.index(item)
                total += prices[temp_index] 
                # item:<(x) aligns the both the product and price of product to be spaced apart in text
                print(f"{i - 1}. {item:<6} ${prices[temp_index]:.2f}")

            print()
            print(f"Sub Total: ${total:.2f}")
            print()

            if total >= 10 and total <= 20:
                # If total is greator or equal to 10 and total is less than or eqtual to 20, it will multiply total and the discount percent together to get the discount amount
                # Remember that total is prices plus the total and prices is the specifc item in the shopping list, so when we multiply total by the discount it will give the discount amount
                # When subtracting the total again by the discount amount, we will get the final total of the amount due in the shopping cart
                discount_amount = total * 0.05
                total = total - discount_amount
                print("Discount: 5%")

                print(f"Amount Saved: ${discount_amount:.2f}")

            elif total > 20 and total <= 40:
                # The program continues to this elif if user has a price thats greator than 20 and less than 40
                discount_amount = total * 0.10
                total = total - discount_amount
                print("Discount: 10%")
                print(f"Amount Saved: ${discount_amount:.2f}")
            elif total > 40:
                # The program continues to this elif if user has a price thats greator than 40
                discount_amount = total * 0.15
                total = total - discount_amount
                print("Discount: 15%")
                print(f"Amount Saved:, ${discount_amount:.2f}")
            else:
                # If user price is less than 10, then discount will be zero and amount saved will be $0.00
                print("Discount: 0%")
                print("Amount Saved: $0.00")



            print()
            print(f"Final Total: ${total:.2f}")
            print()
            print("Thank you for shopping!")
            input("Continue?: ")







     # In the main menu, if user choice is greator than the list of actions in the menu, user will be directed to this onscreen message
    if user_choice > 6 or user_choice < 1:
        print()
        print("Invalid input, please input a valid number in the list!")
        input("Continue?: ")

    
    
    