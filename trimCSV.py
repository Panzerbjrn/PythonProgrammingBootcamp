#!/usr/bin/python
import csv
import sys

# Target csv
file = sys.argv[1]
# Column to remove columns after
remove_from = int(sys.argv[2])

with open(file, "r") as csv_in, open(file[:-4] + "_trimmed.csv", "w") as csv_out:
    reader = csv.reader(csv_in)
    writer = csv.writer(csv_out, lineterminator='\n')
    for row in reader:
        writer.writerow(row[:remove_from])