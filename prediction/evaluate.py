import codecs
import re
import argparse
from random import randint


def main():
    
    # initialize argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', '-t', help='input file')
    parser.add_argument('--predicted','-p', help='predicted file')
    args = parser.parse_args()

    test_values = []

    test_file = codecs.open(args.test,"r", 'utf-8', errors = 'ignore')
    predicted_file = codecs.open(args.predicted,"r", 'utf-8', errors = 'ignore')

    for line in test_file:
        test_values.append(float(re.split(r'\s',line.rstrip())[0]))

    sum_error_square = 0.0
    count = 0
    for line in predicted_file:
        p_value = float(re.split(r'\s',line.rstrip())[0])
        sum_error_square += pow(test_values[count]-p_value, 2)
        count += 1

    avg_sum_error_square = sum_error_square/count
    standard_error = pow(avg_sum_error_square, 0.5)

    print("Error :"+ str(standard_error))



#boilerplate for main
if __name__ == '__main__':
    main()