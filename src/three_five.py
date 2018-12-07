# -*- coding: utf-8 -*-
THREE = 3
FIVE = 5


def three_five(number):
    """
    three_five function takes a number as argument and print the number but for multiples of three print “Three” instead
    of the number and for the multiples of five print “Five”. For numbers which are multiples of both three and five
    print “ThreeFive”
    :param number: integer number to tested in the function
    :return: A string
    """

    # Check if multiples of 3 and 5 then return 'ThreeFive'
    if number % (THREE*FIVE) is 0:
        return 'ThreeFive'

    # Check if multiples of 5 then return 'Five'
    elif number % FIVE is 0:
        return 'Five'

    # Check if multiples of 3 then return 'Three'
    elif number % THREE is 0:
        return 'Three'

    # Return str(number) if none of above conditions passed
    else:
        return str(number)


def exercise_one():
    for number in range(1, 101):
        text = three_five(number)
        print(text)
