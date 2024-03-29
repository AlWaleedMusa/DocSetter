#!/usr/bin/python3
import sys
import re
import os


def main():
	"""
	Start of the program with checking of command line input is correct
	"""

	if len(sys.argv) != 2:
		print("Usage: <Script_name> <Module_name>")
		# sys.exit("Help: <Script_name> -h or --help (NOT READY YET)")   # <------ maybe will add

	# Validate the function name passed from the command line
	module = sys.argv[1]

	if function_module_validate(module):
		function_name = module[2:-3]
		module_name = module
		txt_name = re.sub(r"\.py", ".txt", module)

		# create a copy of the blueprint using the function name passed and module name
		ready_to_write = make_doc(function_name, module_name)

		# write the new lines to a <file.txt> ready to edit
		write_doc(ready_to_write, txt_name)


def write_doc(new_lines, txt_filename):
	"""
	a function that write a list of lines to a new .txt file

	Args:
		new_lines (list): list of new fixed lines ready to write
		txt_filename (str): text file to write to

	Return:
		Nothing, Will Create a new "tests" dir if not there and a new .txt ready to edit
	"""

	# checking if tests dir is created or not and cd into it
	if os.path.exists("tests"):
		os.chdir("tests")
	else:
		os.mkdir("tests")
		os.chdir("tests")
	

	with open(txt_filename, "a") as file:
		file.writelines(new_lines)


def make_doc(function_name, module_name):
	"""
	a function that take a valid function name and a module name and
	use a blueprint to make a docstring bpprint ready to fill with the 
	needed tests

	Args:
		function_name (str): function name to use
		module_name (str): file name used to import the function

	Return:
		a list of all new lines ready to write
	"""
	new_lines = []
	with open ("./DocSetter/blueprint.txt") as file:
		lines = file.readlines()
		for line in lines:
			line = re.sub(r"<function_name>", function_name, line)
			line = re.sub(r"<file_name>", module_name[:-3], line)
			new_lines.append(line)
	return new_lines


def function_module_validate(module):
	"""
	a function that take two strings from command line and check if its a valid
	function name and a valid module name

	Args:
		module (str): string passed to validate module name

	Return:
		True if its a valid name

	Raise:
		ValueError: if names is inValid
	"""
	module_ok = 0
	if module:
		module_name = re.search(r"\.py$", module)
		if module_name:
			module_ok = 1
		else:
			raise ValueError("Please provide a Valid Module name")

	if module_ok:
		return True


if __name__ == "__main__":
	main()
