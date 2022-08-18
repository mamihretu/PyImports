





from walker import directory_walker

path = "C:\\Users\\abreham\\Desktop\\Django_projects\\asynchronous"

sett = directory_walker(path)

for path in sett:
	print(path)