# Initialize empty lists to store student names and grades
student_names = []
student_grades = []
# Infinite loop to keep the program running
while True:
    # Display menu options
    print("\nStudent Data Management System")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Remove Student")
    print("6. Calculate Average Grade")
    print("7. Display Students Above Threshold")
    print("8. Exit")
    
    # Take user's choice as input
    choice = input("Enter your choice: ")
    
    if choice == '1':
        # Add Student
        name = input("Enter student name: ")
        grade = float(input("Enter student grade: "))
        student_names.append(name)
        student_grades.append(grade)
        print(f"Student {name} added successfully.")
    
    elif choice == '2':
        # Display All Students
        if len(student_names) == 0:
            print("No students in the list.")
        else:
            print("\nStudent List:")
            for i in range(len(student_names)):
                print(f"Name: {student_names[i]}, Grade: {student_grades[i]}")
    
    elif choice == '3':
        # Search Student
        name = input("Enter student name to search: ")
        found = False
        for i in range(len(student_names)):
            if student_names[i].lower() == name.lower():
                print(f"Student found: Name: {student_names[i]}, Grade: {student_grades[i]}")
                found = True
                break
        if not found:
            print("Student not found.")
    
    elif choice == '4':
        # Update Student
        name = input("Enter student name to update: ")
        found = False
        for i in range(len(student_names)):
            if student_names[i].lower() == name.lower():
                new_name = input("Enter new name (press enter to skip): ")
                new_grade = input("Enter new grade (press enter to skip): ")
                if new_name:
                    student_names[i] = new_name
                if new_grade:
                    student_grades[i] = float(new_grade)
                print(f"Student {name} updated successfully.")
                found = True
                break
        if not found:
            print("Student not found.")
    
    elif choice == '5':
        # Remove Student
        name = input("Enter student name to remove: ")
        found = False
        for i in range(len(student_names)):
            if student_names[i].lower() == name.lower():
                del student_names[i]
                del student_grades[i]
                print(f"Student {name} removed successfully.")
                found = True
                break
        if not found:
            print("Student not found.")
    
    elif choice == '6':
        # Calculate Average Grade
        if len(student_grades) == 0:
            print("No students to calculate average grade.")
        else:
            total_grade = sum(student_grades)
            average = total_grade / len(student_grades)
            print(f"Average Grade: {average:.2f}")
    
    elif choice == '7':
        # Display Students Above Threshold
        threshold = float(input("Enter grade threshold: "))
        found = False
        for i in range(len(student_names)):
            if student_grades[i] > threshold:
                print(f"Name: {student_names[i]}, Grade: {student_grades[i]}")
                found = True
        if not found:
            print("No students found with grades above the threshold.")
    
    elif choice == '8':
        # Exit the program
        print("Exiting the program.")
        break
    
    else:
        print("Invalid choice. Please try again.")
