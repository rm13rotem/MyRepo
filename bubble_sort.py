def swap(arr, i,j):
  temp = arr[i]  
  arr[i]=arr[j]
  arr[j]=temp
  
  return arr

a1 = [1,2,3,4,5,6,7,8]
print (a1)
a1 = swap(a1, 2,3)