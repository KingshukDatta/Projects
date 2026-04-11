# Importing the mysql.connector module to connect to a MySQL database and perform database operations.
import mysql.connector

# Establishing Database Connection to Mysql Database
db = mysql.connector.connect(
  host = "127.0.0.1",
  user = "root",
  password = "12345",
  database = "school"
)

# using cursor to execute SQL commands
cursor = db.cursor()

# using while loop to create a menu-driven program
# the loop will only exit only when the user chooses to exit.
while True:
  print("\n-----Student Manager app------")
  print("1. Add Student\n2. View Student\n3. Check Results\n4. Exit")
  
  choice = input("Enter Your Choice: ")
  
  ### Add Student to the database
  if choice == "1":
    name = input("Enter Student Name: ")
    roll_no = int(input("Enter Student Roll No: "))
    marks = float(input("Enter Student Marks: "))
    
    # using Sql insert statement to add student information to the database.
    sql = "INSERT  INTO students (name, roll_no, marks) VALUES (%s, %s, %s)"
    values = (name, roll_no, marks)
    
    # using exception handling.
    try:
      cursor.execute(sql, values)
      # for saving the changes to the database, we need to commit the transaction.
      db.commit()
      print(f"Student '{name}' added successfully.")
    except mysql.connector.Error as err:
      print(f"Error: {err}")
      db.rollback()  # Rollback the transaction in case of error.
  
  ### View Student's Information
  elif choice == "2":
    # Using SELECT query to get all student
    cursor.execute("SELECT name, roll_no, marks FROM students")
    # fetching all rows from query
    records = cursor.fetchall() 
    
    if not records:
      print("No student records found.")
    else:
      for name, roll_no, marks in records:
        print(f"Name: {name}, Roll No: {roll_no}, Marks: {marks}")
  
  ### Check Student's Result
  elif choice == "3":
    name = input("Enter Student Name: ")
    
    # query to find specific result of the student by name
    sql = "SELECT name, roll_no, marks FROM students WHERE name = %s"
    cursor.execute(sql, (name,))
    query = cursor.fetchone()  # fetching the first row of the result
    
    if query:
      number = query[2]  # marks of the student
      
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
    # closing database connection before exiting
    cursor.close()
    db.close()
    break
  
  ### Handle invalid choices
  else:
    print("Invalid choice. Please try again.") 