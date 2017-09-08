"""

Binary conversion to/from Decimal

"""

def decimal_to_binary(integer):
    """
    Integer 11 has binary representation '1011'.
    To check, '1011' => 2^(4-1) + 2^(2-1) + 2^(1-1) = 8 + 2 + 1 = 11.

    1.  11 / 2 = 5 remainder 1.  Hence, the right-most binary digit is '1'.
    2.   5 / 2 = 2 remainder 1.  Hence, left-append '1' to obtain '11'.
    3.   2 / 2 = 1 remainder 0.  Hence, left-append '0' to obtain '011'.
    4.   1 is left, so left-append '1' to obtain '1011'.
    """
    if integer < 0:
        return None
    elif integer == 0:
        return integer
    else:
        string = ''
        while integer / 2 > 0:
            string = str(integer % 2) + string
            integer = integer / 2
        string = '1' + string
        return int(string)

def decimal_to_binary_recursive(integer):
    if integer < 2:
        return str(integer % 2)
    return decimal_to_binary_recursive(integer / 2) + str(integer % 2)


def binary_to_decimal(binary):
    """
    Again, integer 11 has binary representation '1011'.

    1.  Right-most digit '1' contributes +1 = +2^k where k = 0
    2.  Next digit '1' contributes +2 = +2^k where k = 1
    3.  Next digit '0' contributes nothing
    4.  Last digit '1' contributes +8 = +2^k where k = 3
    """
    string = str(binary)
    num_digits = len(string)
    integer = 0
    for k in range(num_digits):
        digit = string[num_digits - k - 1]
	if digit == '1':
            integer += 2 ** k
    return integer



if __name__ == '__main__':
    binary_numbers = [decimal_to_binary(i) for i in range(15)]
    print binary_numbers
    print [binary_to_decimal(i) for i in binary_numbers]
