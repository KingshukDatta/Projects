# Create a dictionary to store student information
# Initially the "student" dictionary is empty.
student = {}

# using while loop to create a menu-driven program
# the loop will only exit only when the user chooses to exit.
while True:
  print("\n-----Student Manager app------")
  print("1. Add Student\n2. View Student\n3. Check Results\n4. Exit")
  
  choice = input("Enter Your Choice: ")
  
  ### Add Student to dictionary. For Storing student information.
  if choice == "1":
    name = input("Enter Student Name: ")
    roll_no = int(input("Enter Student Roll No: "))
    marks = float(input("Enter Student Marks: "))
    
    # taking inputs and storing them in the dictionary with name as key and roll_no and marks as values in a list.
    student[name] = [roll_no, marks]
    # output to confirm that the student has been added successfully.
    print(f"Student '{name}' added successfully!!!")
  
  ### View Student's Information
  elif choice == "2":
    # if the student dictionary is empty or not found, it will print a message indicating that no student information is available.
    if not student:
      print("No student information found.")
    else:
      # if the student dictionary is not empty, it will print the name, roll number, and marks of each student in the dictionary.
      for name, item in student.items():
        roll_no = item[0]  # roll number of the student
        marks = item[1]    # marks of the student
        print(f"Name: {name}, Roll No: {roll_no}, Marks: {marks}")
  
  ### Check Student's Result
  elif choice == "3":
    name = input("Enter Student Name: ")
    
    # using "get" method to access and retrieve info from dictionary.
    # it will return none if the name is not found in the dictionary, otherwise it will return the value associated with the name key.
    query = student.get(name)
    if query:
      number = query[1]  # marks of the student
      
      # checking the marks and printing the result accordingly.
      if number >=80 and number <= 100:
        print(f"{name} got A+ grade and the number is {number}")
      elif number >= 70 and number <80:
        print(f"{name} got A grade and the number is {number}")
      elif number >= 60 and number < 70:
        print(f"{name} got A- grade and the number is {number}")
      elif number >= 50 and number < 60:
        print(f"{name} got B grade and the number is {number}")
      elif number >= 40 and number < 50:
        print(f"{name} got C grade and the number is {number}")
      elif number >= 33 and number < 40:
        print(f"{name} got D grade and the number is {number}")
      else:
        print(f"{name} got F grade and the number is {number}")
    else:
      print(f"No information found for student '{name}'.")
      
  ### Exit the program
  elif choice == "4":
    print("Exiting the program. Goodbye!")
    break
  
  ### Handle invalid choices
  else:
    print("Invalid choice. Please try again.") 