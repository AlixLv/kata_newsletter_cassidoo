
import re

# Initialize the string 
string = "Welcome to sparkbyexamples"
print("Original string:",string)

# Using regex
# Remove multiple characters from the string
characters_to_remove = ['e', 'm', 's', 'W', ' ']
pattern = '[' +  ''.join(characters_to_remove) +  ']'
result = re.sub(pattern, '', string) 
print("The string after removing multiple characters:",result)