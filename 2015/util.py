

def test_function():
	print("hello world")

def get_file_as_single_string(file_name):

	with open(file_name) as f:
		content = f.read()
	
	return content 

def get_file_as_list_of_strings(file_name):

	with open(file_name) as f:
		content = f.readlines()

	return content