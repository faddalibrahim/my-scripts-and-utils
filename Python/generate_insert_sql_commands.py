#!/usr/bin/env python

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
	with open("sql_l.txt","w") as sql:
		for line in data:
			sql.write(f"insert into {table} values({line})\n")




data = getData()


if data != None:
	sqlise(data)