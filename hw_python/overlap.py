def max_overlap(arr1,arr2):
  counter = 0
  
  for index1 in range(len(arr1)): # 0,1,..,7
    for index2 in range(len(arr2)): # 0, ..,5
      
      if (arr1[index1] == arr2[index2] and index1 != index2):
        counter +=1
  
  return counter

# positive arrays
array1 = [1,2, 8,5,8,8, 10 , 23]
#print (len(array1)) #8
array2 = [1,5,5,9, 222, 344]
#print (len(array2)) #6
count_digits = max_overlap(array1, array2)
print (count_digits)
count_digits = max_overlap(array2, array1)
print (count_digits)
