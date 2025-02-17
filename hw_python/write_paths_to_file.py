import os

# Open the file in read mode
values = os.environ['path']
values_array = values.split(';')
with open('a.txt', "w") as file:
    # write all lines of the file
    for p in values_array : 
      file.write(p + "\n")
      
values = os.environ['USER']
print (values)
values_array = values.split(';')
with open('b.txt', "w") as file:
    # write all lines of the file
    for p in values_array : 
      file.write(p + "\n")
        
