def is_password_valid(pass_text):
  abc = "abcdefghijklmnopqrstuvwxyz"
  symbol = "!@#$%^&*()_+- "
  digits = "1234567890"
    
  is_digit_inside = False
  is_lower_inside = False
  is_upper_inside = False
  is_symbol_inside = False
  
  for ch in pass_text:    
      if (p):
          is_lower_inside = True 
          
      for u in abc.upper():
        if (p  == u):
          is_upper_inside = True
          
      for s in symbol:
        if (p == s):  
          is_symbol_inside = True
          
      for d in  digits:
        if (p == d):
          is_digit_inside = True
      
      if (is_lower_inside == False) : 
        print ("no lower letter inside ")
      if (is_upper_inside == False) : 
        print ("no upper letter inside ")
      if (is_symbol_inside == False) : 
        print ("no symbol letter inside ")
      if (is_digit_inside == False) : 
        print ("no digit letter inside ")
      
      return  is_lower_inside and is_upper_inside and is_digit_inside and is_symbol_inside
              
      
pass_example = input("password >>")      
print ("Valid password = ", is_password_valid(pass_example))
    
  
