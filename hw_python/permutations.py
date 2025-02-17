for i in range(5):
  digit1 = i + 1
  for j in range(5):
    digit2 = j + 1
    if (digit1 != digit2):
        for k in range(5):
          digit3 = k + 1
          if (digit1 !=  digit3 and digit2 != digit3):
            for l in range(5):
              digit4 = l + 1
              if (digit1 !=  digit4 and digit2 !=  digit4 and digit3 != digit4):
                for m in range(5):
                  digit5 = m + 1
                  if (digit1 !=  digit5 and digit2 !=  digit5 
                      and digit3 != digit5 and digit4 != digit5):
                    print (digit1,digit2,digit3,digit4,digit5)
              
         
