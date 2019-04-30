import sys
import getopt


ERROR_STRING = 'invalid input'


NUMBERS = {
    1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
    10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
    17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
    60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'
}

THOUSANDS = {
    1: 'thousand', 2: 'million', 3: 'billion', 4: 'trillion'
}

OPERATIONS = {
    '+': 'plus', '-': 'minus', '*': 'multiplication', '/': 'division', '=': 'equals'
}


def convert(s):
    result = list()

    def _n2w(number):
        try:
            return NUMBERS[number]
        except KeyError:
            if number < 100:
                return '{} {}'.format(NUMBERS[number - number % 10], NUMBERS[number % 10])
            if number % 100:
                return '{} hundred {}'.format(NUMBERS[number // 100], _n2w(number % 100))
            return '{} hundred'.format(NUMBERS[number // 100])

    if s == '0':
        return 'zero'

    if len(s) > 15:
        return ERROR_STRING

    iterations = len(s) // 3  # calculate the number of triples in string
    if len(s) % 3:
        iterations += 1

    for i in range(0, iterations):
        symbols = int(s[(i+1)*-3:i*-3 if i else None])  # slice three symbols one by one
        if symbols:
            if i:  # when i equals zero, we process the last three characters i.e not thousands
                result.append(THOUSANDS[i])
            result.append(_n2w(symbols))

    return ' '.join(result[::-1])


def humanize(s):
    tokens = list()

    number = ''
    operations_nearby_flag = True

    for symbol in s:
        if symbol.isdigit():
            number += symbol
        elif number:
            tokens.append(convert(number))
            number = ''
            operations_nearby_flag = False

        if not symbol.isdigit():
            if symbol in OPERATIONS:
                if operations_nearby_flag:
                    return ERROR_STRING

                tokens.append(OPERATIONS[symbol])
                operations_nearby_flag = True

            elif symbol != ' ':
                return ERROR_STRING

    if number:
        tokens.append(convert(number))

    return ' '.join(tokens)


if __name__ == '__main__':
    string = "3 + 7 = 10"

    try:
        opts, args = getopt.getopt(sys.argv[1:], "s:")
    except getopt.GetoptError:
        print('humanize.py -s "string"')
        sys.exit()

    for opt, arg in opts:
        if opt == "-s":
            string = arg
        else:
            assert False, "Unknown option"

    print(humanize(string))
