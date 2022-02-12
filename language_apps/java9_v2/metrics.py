"""
The `metrics` module implements the computation of different source code and design metrics for Java language


"""

__version__ = '0.1.0'
__author__ = 'Morteza'

from antlr4 import *
from language_apps.java9_v2.gen.Java9_v2Parser import Java9_v2Parser
from language_apps.java9_v2.gen.Java9_v2Listener import Java9_v2Listener


class DesignMetrics(Java9_v2Listener):
    """
    Computing number of classes in a project
    """
    def __init__(self):
        self.__dsc = 0  # design size in classes

    @property
    def get_design_size(self):
        return self.__dsc

    def enterNormalClassDeclaration(self, ctx: Java9_v2Parser.NormalClassDeclarationContext):
        self.__dsc += 1


class DesignMetrics2(Java9_v2Listener):
    """
    Computing number of private attributes in a class, `class_name`
    """
    def __init__(self, class_name):
        self.__number_of_private_attr = 0  # design size in classes
        self.__class_name = class_name
        self.__is_enter_class = False

    @property
    def get_number_of_private_attr(self):
        return self.__number_of_private_attr

    def enterNormalClassDeclaration(self, ctx: Java9_v2Parser.NormalClassDeclarationContext):
        if ctx.identifier().Identifier().getText() == self.__class_name:
            self.__is_enter_class = True

    def exitNormalClassDeclaration(self, ctx: Java9_v2Parser.NormalClassDeclarationContext):
        if ctx.identifier().Identifier().getText() == self.__class_name and self.__is_enter_class:
            self.__is_enter_class = False

    def enterFieldDeclaration(self, ctx: Java9_v2Parser.FieldDeclarationContext):
        if self.__is_enter_class and ctx.fieldModifier(0).getText() == 'private':
            print(ctx.fieldModifier(0).getText())
            self.__number_of_private_attr += 1
