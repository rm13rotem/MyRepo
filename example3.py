first_grade = int(input("enter grade 1:"))
second_grade = int(input("enter grade 2:"))
average = (second_grade + first_grade) / 2;

print ("average = ", average)
if (average > 80):
  print ("excelent")
elif (average >= 60):
  print ("passed") 
else:
  print ("failed")
