#request data from URL, sort, and return with information

import requests
file_path = 'data.txt'
with open(file_path, 'r') as file:
	print(file.read())
