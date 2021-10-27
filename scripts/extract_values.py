import argparse
import os
import traceback
import pandas as pd
from tqdm import tqdm

import csv
import glob
import json


def main(db_path, verbose=False):
    # gets the name of the directory where the script is, to allow
    # executing the script from anywhere.
    directory = os.path.dirname(os.path.realpath(__file__))

    #DATABASE IMPORT TO REDIS
    csv_files = [f for f in glob.glob(os.path.join(db_path, "*.csv"))]
    csv_files.sort()
    tables = {}  # the dictionary of all the tables, in pandas representation.
    values = {}  # the dictionary of all the values taken by all the columns.

    for csv_file in tqdm(csv_files):
        #Read CSV File
        try:
            csvfile = open(csv_file, newline='')
            csvreader = csv.reader(csvfile, delimiter=',')

            first_row = True
            lines = []  # build a list of all the lines.
            for row in csvreader:
                if first_row == True:
                    headers = row
                    headers[0] = headers[0][1:]  # isolate the columns names.
                    first_row = False
                else:
                    lines.append(row)

            csvfile.close()
            tables[csv_file] = pd.DataFrame(lines, columns=headers)  # create the pd representation.
        except:
            print(traceback.format_exc())

    # fill the values dictionary with the content of the colums,
    # by accumulating the values inside the proper field.
    for table_name in tables:
        for column in tables[table_name].columns:
            if column not in values:  # make sure the column has been seen.
                values[column] = []
            values[column] += list(tables[table_name][column])  # push the values.

    # remove all redundant values to have sets.
    for column in values:
        values[column] = list(set(values[column]))

    # write the results inside a log file.
    with open("values.log", "w") as log_file:
        print("values are being written inside 'values.log'...", end=' ')
        json.dump(values, log_file, indent=4)
        print("done")

if __name__ == "__main__":
    # create a parser to change behaviour from outside.
    parser = argparse.ArgumentParser()
    parser.add_argument("tables", type=str, nargs=1,
            help="the location of the tables, from the execution location (is required).")
    parser.add_argument('-v', "--verbose", default=False, action="store_true",
            help="turns on verbose (defaults to False).")

    args = parser.parse_args()

    #EXECUTION PARAMETERS
    verbose = args.verbose
    db_path = args.tables[0]

    # the actual redis database generation.
    main(db_path, verbose=verbose)
