"""
The main module of IUST Compiler project.

Refer to `language_apps` package to find classroom code snippets.

"""
import re


class Main:
    """Welcome to Compiler course
    This file contains the main script for all code snippets
    """

    @classmethod
    def print_welcome(cls, name) -> None:
        """
        Print welcome message
        :param name:
        :return:
        """
        print(f'Welcome to our dragon course {name}.')

    def tokenize_name(self, method_name):
        method_name = 'getSdfsdfsdtudentNsdfdsfumber'

        identifier_parts = list()
        # First: split based-on CamelCase
        matches = re.finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', method_name)
        camel_cases = [m.group(0) for m in matches]

        # Second: split based-on underscore character '_'
        for case in camel_cases:
            case = case.lower()
            case = case.split('_')
            identifier_parts.extend(case)

        print(f'Method name tokens {camel_cases}.')


# Main driver
if __name__ == '__main__':
    Main.print_welcome('IUST-COMPILER')
