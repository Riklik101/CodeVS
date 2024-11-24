import re
import requests

file_path = r'C:\Users\Eklavya\Documents\CodeVS\NationStates\data.txt'
try:
    with open(file_path, 'r') as file:
        if (content := file.read()):
            print("Content Successfully Read")
            
            # Find all numbers that follow a hashtag and their corresponding choices
            matches = re.findall(r'#(\d+)\s*(.*?)\s*(?=#\d+|$)', content, re.DOTALL)
            
            # Create a dictionary from the matches
            numbers_dict = {int(num): choice.strip() for num, choice in matches}

except FileNotFoundError:
    print(f'Error: The file at {file_path} was not found.')
except Exception as e:
    print(f'An error occurred: {e}')
issue = input("Enter the issue number: ") #add sql injection prevention in the future
if (issue_num := int(issue)) in numbers_dict:
    print(f'Issue {issue_num}: {numbers_dict[issue_num]}')