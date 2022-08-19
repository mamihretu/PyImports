import os





def directory_walker(path):
	""" A function to walk all directories of the 
	    codebase and put all python files into a list
	    parameters -> path : str
	    result -> dictionary of path to file mapping 
	"""
	try:
		generator = os.walk(path)
		file_dict = {}
		directory_path_set = set()
		directory_path_set.add(path)

		def dfs(generator, file_dict):
			"""This function will do the actual walking
			   parameters -> generator: generator object( generator[0] = root, generator[1] = list(dirs), generator[2] = list(files)) 
			              -> file_dict: empty dictionary object
			   result -> dictionary of path to file mapping 
			"""

			for root, dirs, files in generator:

				for file in files:               # Add path to file mapping to file_dict
					if is_py_file(file):
						path = os.path.join(root, file)
						file_dict[path] = file 


				for directory in dirs:           # List files and directories of one directory
					if len(dirs) != 0 and directory != ".git":
						path = os.path.join(root, directory)
						if path not in directory_path_set:
							directory_path_set.add(path)
							new_generator = os.walk(path)
							dfs(new_generator, file_dict)

			return file_dict	

		return dfs(generator, file_dict)

	except:
		pass





def is_py_file(file):
	"""A function to filter out non python files """

	file_name, file_extension = os.path.splitext(file)

	return file_extension == ".py"









