import argparse

__version__ = '2.0'


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--number', required=True, type=int, help='number to perform calculation')
    parser.add_argument('--name', required=True, help='name to print')
    parser.add_argument('--age', required=True, type=int, help='age to determine the formality of discourse')
    args = vars(parser.parse_args())
    print("My name is {}. I am {} years old. I want to have {} children.".format(args['name'], args['age'], args['number']))

