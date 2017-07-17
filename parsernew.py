import csv
import argparse

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument(
           "c_f_1", type=argparse.FileType('r'), help="I/P devices.csv")
arg_parser.add_argument(
           "c_f_2", type=argparse.FileType('r'), help="I/P pointlist.csv")
args = arg_parser.parse_args()

reader = csv.DictReader(args.c_f_1, delimiter=",")
devices = []
for row in reader:
    devices.append(row)

reader = csv.DictReader(args.c_f_2, delimiter=",")
points = []
for row in reader:
    points.append(row)

device_files = []
for device in devices:
    device_registry = []
    for point in points:
        device_registry.append(dict(point, **device))
    device_files.append(device_registry)

for registry in device_files:
    with open(registry[0]['volttron device name'] + ".csv", "w+") as f:
        writer = csv.DictWriter(
                 f, delimiter=",", fieldnames=registry[0].keys())
        writer.writeheader()
        for row in registry:
            writer.writerow(row)







