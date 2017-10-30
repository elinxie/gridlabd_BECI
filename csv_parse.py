import sys, csv
import numpy as np

def value_to_complex(val):
    return complex(val[0:-1] + 'j')

def print_csv(my_csv, column_name, value_bar=complex(0)):
    with open(my_csv) as csvfile:
        csv_reader = csv.reader(csvfile)
        fieldnames = []
        for row in csv_reader:
            if (len(row) > 1 and fieldnames == []):
                fieldnames = row
                break
        if column_name in fieldnames:
            csv_dictreader = csv.DictReader(csvfile,fieldnames)
            for row in csv_dictreader:
                row_value = value_to_complex(row[column_name])
                if np.abs(row_value) > np.abs(value_bar):
                    print(row[fieldnames[0]], row[column_name])

def main(argv):
    if len(argv) > 3:
        print("running on " + argv[1])
        print_csv(argv[1], argv[2], complex(argv[3]))
    elif len(argv) > 2:
        print_csv(argv[1], argv[2])
    else:
        print("""to use, please provide the name of the csv file, the name of the column of that file you want to examine
            For example, you can run in terminal
                        python csv_parse.py test.csv length 30
                            or in a python file 
                        import csv_parse
                        ...
                        csv_parse(test.csv, length, 30)
            where 'test.csv' is the csv file you want to examine, 'length' is the first string in the column that you want to examine,
            and '30' is the complex number that you want to check in the column 'length'. If any row has a value larger
            than '30' in column 'length', then the file prints the first row and the the value in column 'length' """)

if __name__ == "__main__":
    main(sys.argv)