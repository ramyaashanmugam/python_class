print("hello world")

marks_student1 = 88
marks_student2 = 77
marks_student3 = 54

# Calculate the average marks
total_marks = marks_student1 + marks_student2 + marks_student3
tota_students= len([marks_student1,marks_student2,marks_student3])
average_marks = total_marks / tota_students

# Determine the grade based on the average marks
grade = (
	(average_marks >= 80) * 'A' +
	(average_marks >= 60) * (average_marks < 80) * 'B' +
	(average_marks >= 40) * (average_marks < 60) * 'C' +
	(average_marks < 40) * 'D'
)


# Print the average marks and grade
print("Average Marks:",int(int(average_marks * 100) / 100))
#print("Grade:", grade)

print("grade:",(average_marks >= 80)*'A' + 
      (average_marks >= 60) * (average_marks < 80) * 'B' +
      (average_marks >= 40) * (average_marks < 60) * 'C' +
      (average_marks < 40) * 'D')

print((marks_student1 >= marks_student2) * (marks_student1 >= marks_student3) *marks_student1 +
       (marks_student2 >= marks_student1)*(marks_student2 >= marks_student3)* marks_student2 +
       (marks_student3 >= marks_student1) * (marks_student3 >= marks_student2) * marks_student3 )

'''
# Finding the highest mark
highest = (marks_student1 * (marks_student1 >= marks_student2) * (marks_student1 >= marks_student3) +
           marks_student2 * (marks_student2 >= marks_student1) * (marks_student2 >= marks_student3) +
           marks_student3 * (marks_student3 >= marks_student1) * (marks_student3 >= marks_student2))

# Finding the lowest mark
lowest = (marks_student1 * (marks_student1 <= marks_student2) * (marks_student1 <= marks_student3) +
          marks_student2 * (marks_student2 <= marks_student1) * (marks_student2 <= marks_student3) +
          marks_student3 * (marks_student3 <= marks_student1) * (marks_student3 <= marks_student2))


# Print results
print("Highest Mark:", highest)
print("Lowest Mark:", lowest)
'''