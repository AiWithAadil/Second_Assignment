items = input("Enter your items, please use ',' when your first item is done: ").split(',')

yes_or_no = input("Do you want to delete some items? Enter 'yes' or 'no': ")

if yes_or_no == "no":
    print(f"This is your items list: {items}")
  

elif yes_or_no == "yes":
    delete_items = input("Enter the items you want to remove, please use ',' after each item: ").split(',')

    for item in delete_items:
        if item in items:
            items.remove(item)
            print(f"This is your updated items list: {items}")
        else:
            print(f"{item} not found in the items list.")

else:
    print("Invalid input. Bye bye.")

    