import os


def rename_files():
	target_path = "./prank/prank"

	file_list = os.listdir(target_path)

	start_path = os.getcwd()
	os.chdir(target_path)

	for file_name in file_list:
		new_name = file_name.translate(None, "0123456789")
		os.rename(file_name, new_name)
		print ("Rename file " + file_name + " to " + new_name)

	os.chdir(start_path)

rename_files()