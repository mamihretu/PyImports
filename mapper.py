from walker import directory_walker


def map_all_modules(file_dict):
	"""Loop through all files to build a mapping between all modules and their dependancies
	   parameter -> file_dict : dictionary
	   result ->  a list of {file : list} dictionaries
	"""	

	map_list = []
	for file_path in file_dict:
		file_name = file_dict[file_path]
		dependancy_map = read_imported_modules(file_path, file_name)
		if dependancy_map:
			map_list.append(dependancy_map)
		else:
			pass

	return map_list


def read_imported_modules(file_path, file_name):
	"""Read the initial lines of a python file 
	   to determine which module were imported
	   parameter -> file_path : str
	                file_name : str
	   result ->  a mapping between given module and imported ones : dictionay
	"""
	
	with open(file_path) as file_object:
		sentinel = True
		empty_count = 0
		module_map = {file_name : []}
		while sentinel:
			try:
				line_string = file_object.readline()
				string_list = line_string.split()

				if empty_count == 10:
					sentinel = False

				if len(string_list) > 0 and (string_list[0] == "import" or string_list[0] == "from"):
					imported_module = string_list[1]
					module_map[file_name].append(imported_module)

				elif len(string_list) == 0:
					empty_count += 1
			except:
				pass


		return module_map

def main():
	"""Build the tree connection of a single node """

	# path = "C:\\Users\\abreham\\Desktop\\Django_projects\\asynchronous"
	path = "C:\\Users\\abreham\\Desktop\\Environment\\django_environment\\Lib\\site-packages\\django"
	# path = input("Please enter path:")

	file_dict = directory_walker(path)
	library_name = "django"
	pre_pended_file_dict = pre_pend_file_chain(file_dict, library_name)

	map_list = map_all_modules(pre_pended_file_dict)

	for mapping in map_list:
		print(mapping)
		print()


def pre_pend_file_chain(file_dict, library_name):
	""" prepend file chain"""

	for file_path in file_dict:
		chain = file_path.split("\\")
		main_library_index = chain.index(library_name)
		remaining_chain = chain[main_library_index + 1:]
		chained_name = '.'.join(remaining_chain)
		file_dict[file_path] = chained_name

	return file_dict




main()



