import array

array1 = array.array("i", [1,1,11,3,1])
# alternative form - array1 = [1,1,11,3,1]

item = int(input("which number is being counted?"))
counter = 0

for current_index in [0,1,2,3,4]:
  if (array1[current_index] == item) : 
    counter +=1
 
 
print(item, " appears ", counter, " times")   
