# -*- coding: utf-8 -*-

"""
The library supports validating and formatting post codes for UK.
"""
import re

# Regex from: https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting
POST_CODE_REGEX = '([A-Za-z][A-Ha-hJ-Yj-y]?[0-9][A-Za-z0-9]? [0-9][A-Za-z]{2}|[Gg][Ii][Rr] 0[Aa]{2})'
POST_CODE_REGEX_WITHOUT_SPACE = '([A-Za-z][A-Ha-hJ-Yj-y]?[0-9][A-Za-z0-9]? ?[0-9][A-Za-z]{2}|[Gg][Ii][Rr] ?0[Aa]{2})'

# Compile the regex for code validating
VALID_POST_CODE = re.compile('^{}$'.format(POST_CODE_REGEX), re.I)
VALID_POST_CODE_WITHOUT_SPACE = re.compile('^{}$'.format(POST_CODE_REGEX_WITHOUT_SPACE), re.I)


class ValidationError(Exception):
    """Validation error class."""
    pass


class Postcode:
    """
    Postcode class for validating and formatting post codes
    """

    def __init__(self, code):
        self.code = code

    def get_outward_code(self):
        """
        get outward code method
        :return: outward code of the postcode
        """
        return self.code.split(' ')[0]

    def get_inward_code(self):
        """
        get inward code of postcode
        :return: inward code of the postcode
        """
        return self.code.split(' ')[1]

    @staticmethod
    def is_valid(code: str) -> bool:
        """
        Postcode validation, using REGEX.
        Input: a code as string.
        Output: a boolean.
        """
        return bool(VALID_POST_CODE.match(code)) or bool(VALID_POST_CODE_WITHOUT_SPACE.match(code))

    @staticmethod
    def format(code: str):
        """
        Input: a badly formatted code as string, possibly without spaces.
        Output: a standard formatted code.
        Raises ValidationError, if the code length is invalid.
        """
        # Minimum size is A99AA, 5 letters
        # Maximum size is DN55 1PT, 8 letters
        if len(code) < 5 or len(code) > 8:
            raise ValidationError('Invalid postcode length "{}", must ne between "5" and "8"'.format(len(code)))
        code = code.upper()
        # From start up to the last 3 letters
        out_code = code[:-3].strip()
        # Only the last 3 letters
        inw_code = code[-3:].strip()

        return out_code + ' ' + inw_code

