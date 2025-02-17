sum_grades = 0
number_of_students = int(input("How many students in this class "))
number_of_students_passed = 0
  
for index in range(number_of_students):
  #print(index)
  grade = int(input("enter grade {0}: ".format(index)))
  if (grade >= 60):
    sum_grades += grade
    number_of_students_passed

print ("The average of passing grades is ", sum_grades / number_of_students_passed)