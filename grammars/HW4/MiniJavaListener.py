from gen.MiniJavaParserListener import MiniJavaParserListener
from gen.MiniJavaParser import MiniJavaParser
import queue
from AST import AST

class MiniJavaListener(MiniJavaParserListener):
    def __init__(self):
        self.ast = AST()
        self.q = queue.Queue()



    # def exitExpression0(self, ctx:MiniJavaParser.Expression0Context):
    #     value = ctx.ADD() | ctx.SUB() | ctx.MUL() | ctx.LT() | ctx.AND()
    #     self.ast.make_node(value,None,None)

    # def exitIdentifier(self, ctx:MiniJavaParser.IdentifierContext):
    #     self.ast.add_child()


