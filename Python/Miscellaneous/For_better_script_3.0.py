import argparse

__version__ = "3.0"


def calculation(number):
    if number > 100:
        return number**2
    else:
        return number**number


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--number', required=True, type=int, help='number to perform calculation')
    values = parser.parse_args()
    user_number = values.number
    calculation_result = calculation(user_number)
    print(calculation_result)