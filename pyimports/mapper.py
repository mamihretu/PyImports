from walker import directory_walker
import networkx as nx








def make_graph(path, library_name):
	

	file_dict = directory_walker(path)
	pre_pended_file_dict = pre_pend_file_chain(file_dict, library_name)
	module_map_list = map_all_modules(pre_pended_file_dict)
	G = nx.DiGraph()
	G.add_edges_from(module_map_list)

	return G


def pre_pend_file_chain(file_dict, library_name):
	""" prepend file chain, so that two files in a different directories are not confused"""

	for file_path in file_dict:
		chain = file_path.split("\\")
		main_library_index = chain.index(library_name)
		remaining_chain = chain[main_library_index + 1:]
		chained_name = '.'.join(remaining_chain)
		chained_stripped_name = chained_name.rstrip(".py")
		file_dict[file_path] = chained_stripped_name

	return file_dict

def map_all_modules(file_dict):
	"""Loop through all files to build a mapping between all modules and their dependancies
	   parameter -> file_dict : dictionary
	   result ->  (file_name, imported_module): a list of tuples 
	"""	

	module_map_list = []
	for file_path in file_dict:
		file_name = file_dict[file_path]
		with open(file_path) as file_object:
			sentinel = True
			empty_count = 0
			
			while sentinel:
				try:
					line_string = file_object.readline()
					string_list = line_string.split()

					if empty_count == 10:
						sentinel = False

					if len(string_list) > 0 and (string_list[0] == "import" or string_list[0] == "from"):
						if string_list[1] == ".":
							imported_module = string_list[3]

						imported_module = string_list[1]
						module_map_list.append((file_name, imported_module))

					elif len(string_list) == 0:
						empty_count += 1

				except:
					pass

	return module_map_list








			




