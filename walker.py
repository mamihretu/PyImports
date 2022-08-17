import os






path = "C:\\Users\\abreham\\Desktop\\Django_projects\\asynchronous"

generator = os.walk(path)
# print(next(generator))

file_set = set()

def directory_walker(generator, file_set):
	""" A function to walk all directories of the 
	    codebase and put all python files into a list
	"""

	for root, dirs, files in generator:
		# print(dirs, ":", files)
		for file in files:
			file_set.add(file)

		
		for directory in dirs:
			if len(dirs) != 0 and directory != ".git":
				# print(directory.upper(), ":>",  files)
				path = os.path.join(root, directory)
				print(path)
				new_generator = os.walk(path)
				directory_walker(new_generator, file_set)



	return file_set


print(directory_walker(generator, file_set))





