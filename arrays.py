import array
import random

my_array = array.array('i',[10, 5, 3, 4, 5, 2, 1, 7, 4, 6])
for index in range(len(my_array)): 
  my_array[index] = random.randint(1,10)
print("original ", my_array)
  
sum = 0
for index in range(len(my_array) // 2) : 
  item = my_array[index] # 0,1,2, ...
  rev_item = my_array[-1*index - 1] # -1,-2, -3, ...
  sum += item + rev_item
  
  print ("index ", index, "item", item ,"rev_item", rev_item)
  
  temp = item
  my_array[index] = my_array[-1*index - 1]
  my_array[-1*index - 1] = temp
  
print ("sum of elements  is ", sum)
print ("average  is ", sum / len(my_array))
print (my_array)