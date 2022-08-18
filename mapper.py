from walker import directory_walker


path = "C:\\Users\\abreham\\Desktop\\Django_projects\\asynchronous"
# path = input("Please enter path:")


path_set = directory_walker(path)

def main():

	for file_path in path_set:
		backward_map = map_imported_modules(file_path)
		make_tree(backward_map)






def map_imported_modules(file_path):
	"""Read the initial lines of a python file 
	   to determine which module were imported
	   parameter: file_path -> file object
	   return: a mapping between given module and imported ones  -> dictionay
	"""
	
	with open(file_path) as file:
		sentinel = True
		module_map = {}
		while sentinel:
			line_string = file.readline()
			string_list = line_string.split()
			if string_list[0] == "from":


		# print(file_path, "::",  first_line)




def make_tree(backward_map):
	"""Build the tree connection of a single node """

	pass