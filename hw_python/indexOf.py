#for indexLine in range (3): 
line = 'name:"Tel Aviv"'
colon_index = line.find(":")
my_property = line[0:colon_index]
my_value = line[colon_index + 1:]
my_value = my_value.replace("\"", "")
print (my_property, " equals ", my_value )
