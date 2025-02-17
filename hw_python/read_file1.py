import os

# Step 1: Retrieve the file path from the environment variable
path = os.getenv('fileName')
print (path)
file_contents = ""

# Step 2: Check if the environment variable is set
if path:
    try:
        # Open the file and read its contents
        with open(path, 'r') as file:
            file_contents = file.read()
        

        # Step 3: Print or use the contents
        print(file_contents)

    except FileNotFoundError:
        print(f"File not found: {path}")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
else:
    print("Environment variable fileName is not set.")

if (file_contents == ""):
  print ("empty file found")
else:
  words_in_line = file_contents.split(" ")
  if (len(words_in_line) != 2):
    print ("two parameters in line")
  else :
    for i in range(int(words_in_line[1])):
      print(words_in_line[0])