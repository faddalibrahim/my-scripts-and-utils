import shutil as s
import psutil as p

def check_disk_usage(disk):
	du = s.disk_usage(disk)
	free = du.free / du.total * 100
	return free > 20

def check_cpu_usage():
	usage = p.cpu_percent(1)
	return usage < 75

if not check_disk_usage("/") or not check_cpu_usage():
	print("ERROR")
else:
	print("Everything is OK")