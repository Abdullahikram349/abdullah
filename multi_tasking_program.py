while True:
    print("\n                                        MAIN MENU")
    print("1. To-Do List")
    print("2. Basic Calculator")
    print("3. Class Attendance")
    print("4. Exit")
    
    choice = input("Choose any one option between(1-4):   ")
    
    if choice == '1':
        tasks = []
        while True:
            print("\n                                    TO-DO LIST:-")
            print("1. Add your task")
            print("2. View your tasks")
            print("3. Go back to main menu")
            
            opt = input("Choose any one option between (1-3):   ")
            
            if opt == '1':
                task = input("Enter your task:   ")
                tasks.append(task)
                print("                 YOUR TASK IS ADDED.")
            elif opt == '2':
                print("\n    YOUR TO DO LIST:-")
                count = 1
                for task in tasks:
                    print("____________________________________")
                    print("               ",count, ".", task)
                    print("____________________________________")
                    count += 1 
            elif opt == '3':
                break
            else:
                print("Please choose between 1 and 3.")

    elif choice == '2':
        print("\n                            WELCOME TO MY BASIC ARITHMATIC CALCULATOR:-")
        print("                                ENTER THE NUMBER YOU WANT TO CALCULATE")
        num1 = float(input("Your first number:   "))
        print("                            ENTER THE NUMBER YOU WANT TO CALCULATE WITH")
        num2 = float(input("Your second number:   "))
        
        print("Choose an operation:")
        print("Add","             -   ","+")
        print("Subtract","    -    "," -")
        print("Multiply","     -    ","*")
        print("Divide","         -   ","/")
        
        operators = input("Choose an operation from +, -, *, /: ")
        
        if operators == '+':
            result = num1 + num2
            print("_________________________________________________")
            print("                             Your Result:", result)
            print("_________________________________________________")
        elif operators == '-':
            result = num1 - num2
            print("_________________________________________________")
            print("                             Your Result:", result)
            print("_________________________________________________")
        elif operators == '*':
            result = num1 * num2
            print("_________________________________________________")
            print("                              Your Result:", result)
            print("_________________________________________________")
        elif operators == '/':
            if num2 != 0:
                result = num1 / num2
                print("_________________________________________________")
                print("                            Your Result:", result)
                print("_________________________________________________")
            else:
                print(" You Cannot Divide By Zero.")
        else:
            print("Invalid operation.")

    elif choice == '3':
        students = []
        attendance = []
        
        while True:
            print("\n                          MAINTAIN YOUR CLASS ATTENDANCE:-")
            print("1. Add a student and mark attendance")
            print("2. View student attendance list")
            print("3. Go back to main menu")
            
            option = input("Choose an option between(1-3):   ")
            
            if option == '1':
                student = input("Enter student name:   ")
                students.append(student)
                present = input("Present (y/n): ")
                if present.lower() == 'y':
                    attendance.append("Present")
                else:
                    attendance.append("Absent")
                print("Attendance marked.")
                
            elif option == '2':
                print("\nClass Attendance List:  ")
                if not students:  
                    print("No students have been added.")
                else:
                    count = 0
                    for student in students:
                        print(student, "              --               ", attendance[count])
                        count += 1
                    
            elif option == '3':
                break
            else:
                print("Invalid option. Please choose between 1 and 3.")
                
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a number between 1 and 4.")

while True:
    print("\n                                        MAIN MENU")
    print("1. To-Do List")
    print("2. Basic Calculator")
    print("3. Class Attendance")
    print("4. Exit")
    
    choice = input("Choose any one option between(1-4):   ")
    
    if choice == '1':
        tasks = []
        while True:
            print("\n                                    TO-DO LIST:-")
            print("1. Add your task")
            print("2. View your tasks")
            print("3. Delete your task")
            print("4. Go back to main menu")
            
            opt = input("Choose any one option between (1-4):   ")
            
            if opt == '1':
                task = input("Enter your task:   ")
                tasks.append(task)
                print("                 YOUR TASK IS ADDED.")
            elif opt == '2':
                print("\n    YOUR TO DO LIST:-")
                if not tasks:
                    print("No tasks have been added.")
                else:
                    count = 1
                    for task in tasks:
                        print("____________________________________")
                        print("               ",count, ".", task)
                        print("____________________________________")
                        count += 1 
            elif opt == '3':
                if not tasks:
                    print("No tasks have been added.")
                else:
                    print("\n    YOUR TO DO LIST:-")
                    count = 1
                    for task in tasks:
                        print("____________________________________")
                        print("               ",count, ".", task)
                        print("____________________________________")
                        count += 1 
                    task_num = int(input("Enter the task number to delete: "))
                    if task_num > 0 and task_num <= len(tasks):
                        del tasks[task_num - 1]
                        print("Task deleted.")
                    else:
                        print("Invalid task number.")
            elif opt == '4':
                break
            else:
                print("Please choose between 1 and 4.")

    elif choice == '2':
        print("\n                            WELCOME TO MY BASIC ARITHMATIC CALCULATOR:-")
        print("                                ENTER THE NUMBER YOU WANT TO CALCULATE")
        num1 = float(input("Your first number:   "))
        print("                            ENTER THE NUMBER YOU WANT TO CALCULATE WITH")
        num2 = float(input("Your second number:   "))
        
        print("Choose an operation:")
        print("Add","             -   ","+")
        print("Subtract","    -    "," -")
        print("Multiply","     -    ","*")
        print("Divide","         -   ","/")
        
        operators = input("Choose an operation from +, -, *, /: ")
        
        if operators == '+':
            result = num1 + num2
            print("_________________________________________________")
            print("                             Your Result:", result)
            print("_________________________________________________")
        elif operators == '-':
            result = num1 - num2
            print("_________________________________________________")
            print("                             Your Result:", result)
            print("_________________________________________________")
        elif operators == '*':
            result = num1 * num2
            print("_________________________________________________")
            print("                              Your Result:", result)
            print("_________________________________________________")
        elif operators == '/':
            if num2 != 0:
                result = num1 / num2
                print("_________________________________________________")
                print("                            Your Result:", result)
                print("_________________________________________________")
            else:
                print(" You Cannot Divide By Zero.")
        else:
            print("Invalid operation.")

    elif choice == '3':
        students = []
        attendance = []
        
        while True:
            print("\n                          MAINTAIN YOUR CLASS ATTENDANCE:-")
            print("1. Add a student and mark attendance")
            print("2. View student attendance list")
            print("3. Update student attendance")
            print("4. Go back to main menu")
            
            option = input("Choose an option between(1-4):   ")
            
            if option == '1':
                student = input("Enter student name:   ")
                students.append(student)
                present = input("Present (y/n): ")
                if present.lower() == 'y':
                    attendance.append("Present")
                else:
                    attendance.append("Absent")
                print("Attendance marked.")
                
            elif option == '2':
                print("\nClass Attendance List:  ")
                if not students:  
                    print("No students have been added.")
                else:
                    count = 0
                    for student in students:
                        print(student, "              --               ", attendance[count])
                        count += 1
                    
            elif option == '3':
                if not students:
                    print("No students have been added.")
                else:
                    print("\nClass Attendance List:  ")
                    count = 0
                    for student in students:
                        print(student, "              --               ", attendance[count])
                        count += 1 
                    student_num = int(input("Enter the student number to update attendance: "))
                    if student_num > 0 and student_num <= len(students):
                        present = input("Present (y/n): ")
                        if present.lower() == 'y':
                            attendance[student_num - 1] = "Present"
                        else:
                            attendance[student_num - 1] = "Absent"
                        print("Attendance updated.")
                    else:
                        print("Invalid student number.")
            elif option == '4':
                break
            else:
                print("Invalid option. Please choose between 1 and 4.")
                
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a number between 1 and 4."while True:
    print("\n                                        MAIN MENU")
    print("1. To-Do List")
    print("2. Basic Calculator")
    print("3. Class Attendance")
    print("4. Exit")
    
    choice = input("Choose any one option between(1-4):   ")
    
    if choice == '1':
        tasks = []
        while True:
            print("\n                                    TO-DO LIST:-")
            print("1. Add your task")
            print("2. View your tasks")
            print("3. Delete your task")
            print("4. Update your task")
            print("5. Go back to main menu")
            
            opt = input("Choose any one option between (1-5):   ")
            
            if opt == '1':
                task = input("Enter your task:   ")
                tasks.append(task)
                print("                 YOUR TASK IS ADDED.")
            elif opt == '2':
                print("\n    YOUR TO DO LIST:-")
                if not tasks:
                    print("No tasks have been added.")
                else:
                    count = 1
                    for task in tasks:
                        print("____________________________________")
                        print("               ",count, ".", task)
                        print("____________________________________")
                        count += 1 
            elif opt == '3':
                if not tasks:
                    print("No tasks have been added.")
                else:
                    print("\n    YOUR TO DO LIST:-")
                    count = 1
                    for task in tasks:
                        print("____________________________________")
                        print("               ",count, ".", task)
                        print("____________________________________")
                        count += 1 
                    task_num = int(input("Enter the task number to delete: "))
                    if task_num > 0 and task_num <= len(tasks):
                        del tasks[task_num - 1]
                        print("Task deleted.")
                    else:
                        print("Invalid task number.")
            elif opt == '4':
                if not tasks:
                    print("No tasks have been added.")
                else:
                    print("\n    YOUR TO DO LIST:-")
                    count = 1
                    for task in tasks:
                        print("____________________________________")
                        print("               ",count, ".", task)
                        print("____________________________________")
                        count += 1 
                    task_num = int(input("Enter the task number to update: "))
                    if task_num > 0 and task_num <= len(tasks):
                        task = input("Enter your updated task:   ")
                        tasks[task_num - 1] = task
                        print("Task updated.")
                    else:
                        print("Invalid task number.")
            elif opt == '5':
                break
            else:
                print("Please choose between 1 and 5.")

    elif choice == '2':
        print("\n                            WELCOME TO MY BASIC ARITHMATIC CALCULATOR:-")
        print("                                ENTER THE NUMBER YOU WANT TO CALCULATE")
        num1 = float(input("Your first number:   "))
        print("                            ENTER THE NUMBER YOU WANT TO CALCULATE WITH")
        num2 = float(input("Your second number:   "))
        
        print("Choose an operation:")
        print("Add","             -   ","+")
        print("Subtract","    -    "," -")
        print("Multiply","     -    ","*")
        print("Divide","         -   ","/")
        
        operators = input("Choose an operation from +, -, *, /: ")
        
        if operators == '+':
            result = num1 + num2
            print("_________________________________________________")
            print("                             Your Result:", result)
            print("_________________________________________________")
        elif operators == '-':
            result = num1 - num2
            print("_________________________________________________")
            print("                             Your Result:", result)
            print("_________________________________________________")
        elif operators == '*':
            result = num1 * num2
            print("_________________________________________________")
            print("                              Your Result:", result)
            print("_________________________________________________")
        elif operators == '/':
            if num2 != 0:
                result = num1 / num2
                print("_________________________________________________")
                print("                            Your Result:", result)
                print("_________________________________________________")
            else:
                print(" You Cannot Divide By Zero.")
        else:
            print("Invalid operation.")

    elif choice == '3':
        students = []
        attendance = []
        
        while True:
            print("\n                          MAINTAIN YOUR CLASS ATTENDANCE:-")
            print("1. Add a student and mark attendance")
            print("2. View student attendance list")
            print("3. Update student attendance")
            print("4. Delete student attendance")
            print("5. Go back to main menu")
            
            option = input("Choose an option between(1-5):   ")
            
            if option == '1':
                student = input("Enter student name:   ")
                students.append(student)
                present = input("Present (y/n): ")
                if present.lower() == 'y':
                    attendance.append("Present")
                else:
                    attendance.append("Absent")
                print("Attendance marked.")
                
            elif option == '2':
                print("\nClass Attendance List:  ")
                if not students:  
                    print("No students have been added.")
                else:
                    count = 0
                    for student in students:
                        print(student, "              --               ", attendance[count])
                        count += 1
                    
            elif option == '3':
                if not students:
                    print("No students have been added.")
                else:
                    print("\nClass Attendance List:  ")
                    count = 0
                    for student in students:
                        print(student, "              --               ", attendance[count])
                        count += 1 
                    student_num = int(input("Enter the student number to update attendance: "))
                    if student_num > 0 and student_num <= len(students):
                        present = input("Present (y/n): ")
                        if present.lower() == 'y':
                            attendance[student_num - 1] = "Present"
                        else:
                            attendance[student_num - 1] = "Absent"
                        print("Attendance updated.")
                    else:
                        print("Invalid student number.")
            elif option == '4':
                if not students:
                    print("No students have been added.")
                else:
                    print("\nClass Attendance List:  ")
                    count = 0
                    for student in students:
                        print(student, "              --               ", attendance[count])
                        count += 1 
                    student_num = int(input("Enter the student number to delete attendance: "))
                    if student_num > 0 and student_num <= len(students):
                        del students[student_num - 1]
                        del attendance[student_num - 1]
                        print("Attendance deleted.")
                    else:
                        print("Invalid student number.")
            elif option == '5':
                break
            else:
                print("Invalid option. Please choose between 1 and 5.")
                
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a number between 1 and 4.")