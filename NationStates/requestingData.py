import re
import requests

file_path = r'C:\Users\Eklavya\Documents\CodeVS\NationStates\data.txt'
try:
    with open(file_path, 'r') as file:
        if (content := file.read()):
            print("Content Successfully Read")
            
            # Find all numbers that follow a hashtag
            numbers = re.findall(r'#(\d+)', content)
            
#            # Print the extracted numbers
 #           print(numbers)
except FileNotFoundError:
    print(f'Error: The file at {file_path} was not found.')
except Exception as e:
    print(f'An error occurred: {e}')
