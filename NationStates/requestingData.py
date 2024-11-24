#request data from URL, sort, and return with information

import requests

file_path = r'C:\Users\Eklavya\Documents\CodeVS\NationStates\data.txt'
try:
    with open(file_path, 'r') as file:
        if (content := file.read()):
            print(content)
except FileNotFoundError:
    print(f'Error: The file at {file_path} was not found.')
except Exception as e:
    print(f'An error occurred: {e}')
