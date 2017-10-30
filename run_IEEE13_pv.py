import csv_parse as cparse
import os
import sys
def main(argv):
    os.system("gridlabd -o IEEE13_pv1.xml -v IEEE13_pv1.glm >> output.txt")
    csv_files =['voltage{0}_pv.csv'.format(l) for l in ['A', 'B', 'C']]
    meter = 'm680'
    for c in csv_files:
        print(c)
        cparse.print_csv(c, meter, complex('2640'))

if __name__ == "__main__":
    main(sys.argv)
