def merge_array(array1, array2):
  index1 = 0
  index2 = 0
  result = []
  while ((index1 < len(array1)) or (index2 < len(array2))):
    if (index1 >= len(array1)):
      result.append(array2[index2])
      index2 += 1
    elif (index2 >= len(array2)):
      result.append(array1[index1])
      index1 += 1
    elif (array1[index1] > array2[index2]):
      result.append(array2[index2])
      index2 += 1
    else:
      result.append(array1[index1])
      index1 += 1
  return result
 
array1 = [1,2,5,6,7]
array2 = [3,4,7,8,9,111]
print(merge_array(array1, array2))