def dtob_tail_GPT(deci, bin_string):
    """
    [Tail Recursion] decimal to binary
    deci: 十進位整數
    bin_string: 目前累積好的二進位字串
    """
    if deci == 0:
        if bin_string == '':
            return '0'
        return bin_string

    remainder = deci % 2
    bin_string = str(remainder) + bin_string
    return dtob_tail_GPT(deci // 2, bin_string)


deci_value = int(input('Enter an integer: '))
print('Binary =', dtob_tail_GPT(deci_value, ''))

from decimal import Decimal

def dtob_tail(deci, bin_string):
    '''[Tail Recursion] for decimal-to-binary transformation'''
    deci = Decimal(deci)

    if deci == 0:
        return bin_string
    else:
        bin_string = str(deci % Decimal(2)) + bin_string
        deci = deci // Decimal(2)
        return dtob_tail(deci, bin_string)


deci_value = input('Enter an integer: ')
bin_string = ''

print('\n', dtob_tail.__doc__)
print('Decimal({0}) = '.format(deci_value), end='')
result = dtob_tail(deci_value, bin_string)
print('Binary({})'.format(result))

dtob_tail_GPT(deci_value, bin_string)
dtob_tail(deci_value, bin_string)