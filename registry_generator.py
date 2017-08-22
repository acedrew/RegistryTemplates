import csv
import argparse

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument(
           "c_f_1", type=argparse.FileType('r'), help="I/P devices.csv")
arg_parser.add_argument(
           "c_f_2", type=argparse.FileType('r'), help="I/P pointlist.csv")
args = arg_parser.parse_args()

reader = csv.DictReader(args.c_f_1, delimiter=",")
r2=csv.DictReader(args.c_f_2, delimiter=",")
files = []
points = []
pointnumber=0

for line in r2:
	points.append(line)
	pointnumber=pointnumber+1

for row in reader:
	files.append(row)
	for item in files:
		result_list=[]
		for d1 in files:
			merged_dict=d1.copy()
			result_list.append(merged_dict.copy())
			for d2 in points:
				merged_dict.update(d2)
				result_list.append(merged_dict.copy())
	opfile=open("main_registry.csv","w+")
	writer=csv.DictWriter(opfile,delimiter=",",fieldnames=files[0].keys()+points[0].keys())
	writer.writeheader()
	for row in result_list:
			writer.writerow(row)
	opfile.close()

