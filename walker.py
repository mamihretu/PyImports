
import os


def directory_walker(path):
	""" A function to walk all directories of the 
	    codebase and put all python files into a list
	"""
	try:
		generator = os.walk(path)
		file_set = set()

		def dfs(generator, file_set):
			"""This nested function will do the actual walking"""

			for root, dirs, files in generator:
				for file in files:
					file_set.add(file)

				
				for directory in dirs:
					if len(dirs) != 0 and directory != ".git":
						path = os.path.join(root, directory)
						new_generator = os.walk(path)
						dfs(new_generator, file_set)


			return file_set

		return dfs(generator, file_set)

	except:
		pass








