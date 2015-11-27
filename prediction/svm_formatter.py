#this is to convert a file into svm format
#usage python3 svm_formatter.py --train/test input_file dictionary_file output_file

import codecs
import csv
import argparse
from random import randint


def main():
    
    # initialize argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', '-i', help='input file')
    parser.add_argument('--train','-o', help='train file')
    parser.add_argument('--test', '-p', help='test file')
    args = parser.parse_args()


    #open output file
    train_file = codecs.open(args.train, 'w', 'utf-8', errors = 'ignore')
    test_file = codecs.open(args.test,'w','utf-8', errors='ignore')


    with open(args.input) as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:
            svm_line = row[0]+"\t"
            count = 1
            for element in row[1:]:
                if element.strip() == 'NULL':
                    element = "0"
                svm_line += str(count) + ":" + str(element.strip())+"\t"
                count += 1
            if randint(0,9) <=7:
                train_file.write(svm_line.rstrip()+'\n')
            else:
                test_file.write(svm_line.rstrip()+'\n')

    train_file.close()
    test_file.close()

#boilerplate for main
if __name__ == '__main__':
    main()