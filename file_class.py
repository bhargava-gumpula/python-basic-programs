import os
import sys

class File:
	def __init__(self, name):
		self.size = 0
		self.name = name
		self.filePath = "/Users/bhargavagumpula/work/python-basic-programs/self.name"
		self.type = os.system("file %s" % (self.name))
		self.file_extention = os.path.splitext(self.filePath)[1]
		self.file_extention = self.file_extention.lstrip(".")
		print(self.file_extention)
		if self.file_extention == "txt":
			self.type = "Text File"
		else:
			self.type = "Unknown"
		self.lines = 0
		self.words = 0
		

		file = open(self.name, "r")
		file_content = file.read()
		for char in file_content:
			self.size += 1
			if char == " ":
				self.words += 1
		for line in file:
			line = line	
	def remove(self):
		os.remove(self.name)
		print("Removed")
	
	def show(self):	
		print("Name : %s\nSize : %s\nType : %s\nLines : %s\nWords : %s" % (str(self.name), str(self.size), str(self.type), str(self.lines), str(self.words)))
	
	def __str__(self):
		print(self.file_content)

file = File(sys.argv[1])
file.show()
