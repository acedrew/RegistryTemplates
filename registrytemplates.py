import csv


ipfile1 = open('Devices.csv',"r")
reader = csv.DictReader(ipfile1, delimiter=",")
devices = []
for row in reader:
	devices.append(row)

ipfile2 = open('Pointlist.csv',"r")
reader=csv.DictReader(ipfile2)
points = []
for row in reader:
	points.append(row)

device_files = []
for device in devices:
	device_registry = []
	for point in points:
		device_registry.append(dict(point, **device))
	device_files.append(device_registry)

print(device_files)
for registry in device_files:
	with open(registry[0]['volttron device name'] + ".csv", "w+") as f:
		writer = csv.DictWriter(f, delimiter=",", fieldnames=registry[0].keys())
		writer.writeheader()
		for row in registry:
			writer.writerow(row)

#for line in r2:
#	points.append(line)
#	pointnumber=pointnumber+1
#
#for row in reader:
#	files.append(row)
#	for item in files:
#		#merged=([item]*pointnumber+points)
#		#print merged
#		result_list=[]
#		for d1 in files:
#			merged_dict=d1.copy()
#			for d2 in points:
#				merged_dict.update(d2)
#				result_list.append(merged_dict.copy())
#	opfile=open(row["volttron device name"]+".csv","w+")
#	writer=csv.DictWriter(opfile, delimiter=",", fieldnames=list(files[0].keys()) + list(points[0].keys()))
#	writer.writeheader()
#	for row in result_list:
#			writer.writerow(row)
#	opfile.close()
