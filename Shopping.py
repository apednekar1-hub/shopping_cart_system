from datetime import datetime, date

shopping_cart = []

products = ["Chips", "Soda", "Candy", "Cookies", "Water", "Sandwich"]
prices = [2.00, 2.50, 1.50, 3.00, 1.00, 5.00]

program_running = True 
while program_running == True:
    in_product_menu = True
    print()
    print("========== SMART SHOPPING CART ==========")
    print("1. View Available Products")
    print("2. Add Product to Cart")
    print("3. Remove Product from Cart")
    print("4. View Shopping Cart")
    print("5. View Current Total")
    print("6. Checkout")
    print()
    try:
        user_choice = int(input("Enter your choice: "))
        print()
    except ValueError:
        print()
        print("Please enter a number.")
        input("Continue?: ")
        continue


    if user_choice == 1:
        print()
        for i in range(len(products)):
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


        if product_selection <= 6 and product_selection >= 1:
            shopping_cart.append(products[product_selection - 1])
            print()
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
                index_to_remove = remove - 1
                if index_to_remove < len(shopping_cart):
                    shopping_cart.pop(index_to_remove)
                    print("\nItem has been removed!")
                    cancel = input("Would you like to cancel? (yes/no): ")

                
                    if cancel == "yes":
                        in_product_menu = False
                        print(f"Cancel is equal to {cancel}")
                        break     
                    elif cancel == "no":
                        continue

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
                print(f"You have {len(shopping_cart)} items in your cart.")
                print()
            for i in range(len(shopping_cart)):

                print(f"{i + 1}. {shopping_cart[i]}")
            print()
            choice = input("Would you like to go back? (yes/no): ")
            print()
            
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

            for i, item in enumerate(shopping_cart, start=1):
                temp_index = products.index(item)
                total += prices[temp_index] 
                print(f"{i - 1}. {item:<6}         ${prices[temp_index]:.2f}")

            print()
            print(f"Sub Total: ${total:.2f}")
            print()

            if total >= 10 and total <= 20:
                
                discount_amount = total * 0.05
                total = total - discount_amount
                print("Discount: 5%")
                print(f"Amount Saved: ${discount_amount:.2f}")

            elif total > 20 and total <= 40:

                discount_amount = total * 0.10
                total = total - discount_amount
                print("Discount: 10%")
                print(f"Amount Saved: ${discount_amount:.2f}")
            elif total > 40:

                discount_amount = total * 0.15
                total = total - discount_amount
                print("Discount: 15%")
                print(f"Amount Saved:, ${discount_amount:.2f}")
            else:
                print("Discount: 0%")
                print(f"Amount Saved: ${discount_amount:.2f}")



            print()
            print(f"Final Total: ${total:.2f}")
            print()
            print("Thank you for shopping!")
            input("Continue?: ")








    if user_choice > 6 or user_choice < 1:
        print()
        print("Invalid input, please input a valid number in the list!")
        input("Continue?: ")

    
    
    