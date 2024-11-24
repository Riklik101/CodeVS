import re
import os
import requests

# Construct the file path relative to the script's location
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'data.txt')

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
else:
    try:
        issue = input("Enter the issue number: ")
        issue_num = int(issue)
        if issue_num in numbers_dict:
            print(f'Issue {issue_num}: {numbers_dict[issue_num]}')
        else:
            print(f'Issue number {issue_num} not found.')
    except ValueError:
        print("Invalid input. Please enter a valid issue number.")