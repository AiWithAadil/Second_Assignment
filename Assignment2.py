#Scenario 1: Grocery Shopping List

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


#Scenario 2: Student Grades 

student_grades = {}

student_frequency = int(input("Enter student frequency: "))

for student in range(student_frequency):
    name = input("Enter your name: ")
    grade = input("Enter you grade in Capital")
    student_grades.update({name:grade})
    
average_grade = "B"  
average_student = ""

for name, grade in student_grades.items():
    if grade == average_grade:
           average_grade = grade
           average_student = name
           print(f"{average_student} has the AVERAGE grade: {average_grade}")




#Scenario 3: Word Frequency Counter

word_list = ["apple", "banana", "apple", "orange", "banana", "grape", "apple"]

A = word_list.count("apple")
print(f"Apple: {A}")

B = word_list.count("banana")
print(f"Banana: {B}")

O = word_list.count("orange")
print(f"Orange: {O}")

G = word_list.count("grape")
print(f"Grape: {G}")