import os


def directory_walker(path):
	""" A function to walk all directories of the 
	    codebase and put all python files into a list
	    parameters: path -> str
	    result: Set(str)
	"""
	try:
		generator = os.walk(path)
		file_path_set = set()

		def dfs(generator, file_path_set):
			"""This nested function will do the actual walking"""

			for root, dirs, files in generator:
				for file in files:
					if is_py_file(file):
						path = os.path.join(root, file)
						file_path_set.add(path)


				
				for directory in dirs:
					if len(dirs) != 0 and directory != ".git":
						path = os.path.join(root, directory)
						new_generator = os.walk(path)
						dfs(new_generator, file_path_set)

			return file_path_set

		python_set = dfs(generator, file_path_set)

		return python_set

	except:
		pass



def is_py_file(file):
	"""A function to filter out non python files """

	file_name, file_extension = os.path.splitext(file)

	return file_extension == ".py"









