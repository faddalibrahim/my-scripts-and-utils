#!/usr/bin/env python

"""
This script generates lines of sql code for insert operations
A txt file containing the lines of data to be inserted is required
Plus a table to be inserted into

the getData() functions reads the txt data file and returns a list of the data
this is then passed into the sqlise() function to generate the sql code

if the txt data file contains this data:
	1232021,"C090904","John Dramani Mahama","male","2000-06-13","NDC",0
	1232022,"C090904","Nana Addo-Danquah Akuffo Addo","male","2000-06-13","NPP",0
	1232023,"C090904","Nana Konadu Agyeman-Rawlings","female","2000-06-13","NDP",0
	1232024,"C090904","Ayariga Moses","male","2000-06-13","PNC",0

and the table name entered is Presidents

ths output file generated will contain this:
	insert into Presidents values(1232021,"C090904","John Dramani Mahama","male","2000-06-13","NDC",0)
	insert into Presidents values(1232022,"C090904","Nana Addo-Danquah Akuffo Addo","male","2000-06-13","NPP",0)
	insert into Presidents values(1232023,"C090904","Nana Konadu Agyeman-Rawlings","female","2000-06-13","NDP",0)
	insert into Presidents values(1232024,"C090904","Ayariga Moses","male","2000-06-13","PNC",0)


NB: this script can be easily modified to work with csv files. Feel free to modify it however you want.


#TODO : check for empty data files to avoid generating an empty output
	convert into bash
	modify to work with csv files
	Look at how to incorporate os.path.exists()

"""

file_path = input("file path: ")

while file_path.strip() == 0:
	file_path = input("file path: ")

table = input("table name: ")

while table.strip() == 0:
	table = input("table name: ")



def getData(file=file_path):
	try:
		with open(file) as data_file:
			data = [line.strip() for line in data_file]
		return data
	except FileNotFoundError as e:
		print(f"The file, {file_path}, doesn't exist")
		return
	except Exception as e:
		print("Something went wrong")
		return


def sqlise(data):
	"""
	the sql.txt is the output file. the file will be generated in the same directory as where this script file is
	you can change the directory to any other. something like to your desktop or anywhere
	"""
	with open("sql.txt","w") as sql:
		for line in data:
			sql.write(f"insert into {table} values({line})\n")




data = getData()


if data != None:
	sqlise(data)
