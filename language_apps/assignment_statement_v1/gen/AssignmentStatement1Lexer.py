# Generated from D:/AnacondaProjects/iust_compilers_teaching/grammars/AssignmentStatement1.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,14,115,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,1,0,1,0,1,0,1,1,1,1,1,2,1,
        2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,7,5,7,54,8,7,10,7,12,
        7,57,9,7,1,8,4,8,60,8,8,11,8,12,8,61,1,9,4,9,65,8,9,11,9,12,9,66,
        1,9,1,9,5,9,71,8,9,10,9,12,9,74,9,9,1,9,1,9,4,9,78,8,9,11,9,12,9,
        79,3,9,82,8,9,1,10,1,10,1,10,5,10,87,8,10,10,10,12,10,90,9,10,1,
        11,1,11,1,12,1,12,1,13,1,13,1,13,1,13,3,13,100,8,13,1,14,4,14,103,
        8,14,11,14,12,14,104,1,14,1,14,1,15,1,15,1,16,1,16,1,16,3,16,114,
        8,16,1,88,0,17,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,
        11,23,0,25,0,27,0,29,12,31,13,33,14,1,0,3,1,0,48,57,2,0,65,90,97,
        122,3,0,9,9,13,13,32,32,123,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,
        0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,
        17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,
        33,1,0,0,0,1,35,1,0,0,0,3,38,1,0,0,0,5,40,1,0,0,0,7,42,1,0,0,0,9,
        44,1,0,0,0,11,46,1,0,0,0,13,48,1,0,0,0,15,50,1,0,0,0,17,59,1,0,0,
        0,19,81,1,0,0,0,21,83,1,0,0,0,23,91,1,0,0,0,25,93,1,0,0,0,27,99,
        1,0,0,0,29,102,1,0,0,0,31,108,1,0,0,0,33,113,1,0,0,0,35,36,5,58,
        0,0,36,37,5,61,0,0,37,2,1,0,0,0,38,39,5,43,0,0,39,4,1,0,0,0,40,41,
        5,45,0,0,41,6,1,0,0,0,42,43,5,42,0,0,43,8,1,0,0,0,44,45,5,47,0,0,
        45,10,1,0,0,0,46,47,5,40,0,0,47,12,1,0,0,0,48,49,5,41,0,0,49,14,
        1,0,0,0,50,55,3,25,12,0,51,54,3,25,12,0,52,54,3,23,11,0,53,51,1,
        0,0,0,53,52,1,0,0,0,54,57,1,0,0,0,55,53,1,0,0,0,55,56,1,0,0,0,56,
        16,1,0,0,0,57,55,1,0,0,0,58,60,3,23,11,0,59,58,1,0,0,0,60,61,1,0,
        0,0,61,59,1,0,0,0,61,62,1,0,0,0,62,18,1,0,0,0,63,65,3,23,11,0,64,
        63,1,0,0,0,65,66,1,0,0,0,66,64,1,0,0,0,66,67,1,0,0,0,67,68,1,0,0,
        0,68,72,5,46,0,0,69,71,3,23,11,0,70,69,1,0,0,0,71,74,1,0,0,0,72,
        70,1,0,0,0,72,73,1,0,0,0,73,82,1,0,0,0,74,72,1,0,0,0,75,77,5,46,
        0,0,76,78,3,23,11,0,77,76,1,0,0,0,78,79,1,0,0,0,79,77,1,0,0,0,79,
        80,1,0,0,0,80,82,1,0,0,0,81,64,1,0,0,0,81,75,1,0,0,0,82,20,1,0,0,
        0,83,88,5,34,0,0,84,87,3,27,13,0,85,87,9,0,0,0,86,84,1,0,0,0,86,
        85,1,0,0,0,87,90,1,0,0,0,88,89,1,0,0,0,88,86,1,0,0,0,89,22,1,0,0,
        0,90,88,1,0,0,0,91,92,7,0,0,0,92,24,1,0,0,0,93,94,7,1,0,0,94,26,
        1,0,0,0,95,96,5,92,0,0,96,100,5,34,0,0,97,98,5,92,0,0,98,100,5,92,
        0,0,99,95,1,0,0,0,99,97,1,0,0,0,100,28,1,0,0,0,101,103,7,2,0,0,102,
        101,1,0,0,0,103,104,1,0,0,0,104,102,1,0,0,0,104,105,1,0,0,0,105,
        106,1,0,0,0,106,107,6,14,0,0,107,30,1,0,0,0,108,109,5,10,0,0,109,
        32,1,0,0,0,110,111,5,60,0,0,111,114,5,61,0,0,112,114,5,60,0,0,113,
        110,1,0,0,0,113,112,1,0,0,0,114,34,1,0,0,0,13,0,53,55,61,66,72,79,
        81,86,88,99,104,113,1,6,0,0
    ]

class AssignmentStatement1Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    Id = 8
    INT = 9
    FLOAT = 10
    String = 11
    WS = 12
    NEWLINE = 13
    RELOP = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':='", "'+'", "'-'", "'*'", "'/'", "'('", "')'", "'\\n'" ]

    symbolicNames = [ "<INVALID>",
            "Id", "INT", "FLOAT", "String", "WS", "NEWLINE", "RELOP" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "Id", "INT", "FLOAT", "String", "DIGIT", "LETTER", "ESC", 
                  "WS", "NEWLINE", "RELOP" ]

    grammarFileName = "AssignmentStatement1.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


