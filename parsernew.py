import csv
import argparse


def read_registry(filename):
    reader = csv.DictReader(filename, delimiter=",")
    registry = []
    for row in reader:
        registry.append(row)
    return registry


def write_device_files(device_files):
    for registry in device_files:
        with open(registry[0]['volttron device name'] + ".csv", "w+") as f:
            writer = csv.DictWriter(f, delimiter=",",
                                    fieldnames=registry[0].keys())
            writer.writeheader()
            for row in registry:
                writer.writerow(row)


def create_device_files(devices, points):
    device_files = []
    for device in devices:
        device_registry = []
        for point in points:
            device_registry.append(dict(point, **device))
        device_files.append(device_registry)
    return device_files


def main(args):
    devices = read_registry(args.c_f_1)
    points = read_registry(args.c_f_2)
    device_files = create_device_files(devices, points)
    write_device_files(device_files)


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("c_f_1", type=argparse.FileType('r'),
                            help="I/P devices.csv")
    arg_parser.add_argument("c_f_2", type=argparse.FileType('r'),
                            help="I/P pointlist.csv")
    args = arg_parser.parse_args()
    main(args)
