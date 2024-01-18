grocery_items = input("Enter your items, please use ',' after each item: ").split(',')

yes_no_add = input("Do you want to delete some items? Enter 'yes' otherwise 'no' and add some thing Enter 'add': ")

if yes_no_add == "no":
    print(f"This is your grocery items list: {grocery_items}")
  

elif yes_no_add == "yes":
    delete_items = input("Enter the items you want to remove, please use ',' after each item: ").split(',')

    for item in delete_items:
        if item in grocery_items:
            grocery_items.remove(item)
            print(f"This is your updated items list: {grocery_items}")
        else:
            print(f"{item} not found in the items list.")
elif  yes_no_add == "add":
      add_items = input("Enter items please use ',' after each item: ").split(',')
      grocery_items.append(add_items) 
      print(f"This is your mote items list {grocery_items}")  
     
else:
    print("Invalid input. Bye bye.")

print(grocery_items)
