"""
The main module of IUST Compiler project.

This module do not contains any code.
Please refer to `language_apps` package to find classroom code snippets.

"""


class Main():
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
        print(f'Welcome to our deragon course {name}.')


# Main driver
if __name__ == '__main__':
    Main.print_welcome('COMPILER')
