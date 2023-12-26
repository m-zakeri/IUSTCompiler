from semesters.spring2021.HW4.gen.Q2Listener import Q2Listener
from semesters.spring2021.HW4.gen.Q2Parser import Q2Parser

class ThreeACListener(Q2Listener):
    def __init__(self):
        self.TempCount = 0
        self.LabelCount = 0


    def CreateTemp(self):
        self.TempCount += 1
        return 'T' + str(self.TempCount)

    def CreateLabel(self):
        self.LabelCount += 1
        return 'L' + str(self.LabelCount)

    def exitEqual_statement(self, ctx: Q2Parser.Equal_statementContext):
        ctx.value_attr = ctx.Identifier().getText() + ' = ' + ctx.expression().getText()
        print(ctx.value_attr)

    def enterWhile_statement(self, ctx: Q2Parser.While_statementContext):
        ctx.value_attr = self.CreateLabel() + ' if' + '!(' + ctx.expression().value_attr + ')' + 'goto' + ctx.statement().value_attr[
                                                                                                          0: 2]
        ctx.statement().value_attr = ctx.statement().value_attr + 'goto'
        ctx.statement().value_attr = self.CreateLabel() + ctx.statement().value_attr

        print(ctx.value_attr)

    def exitOperations_expression(self, ctx: Q2Parser.Operations_expressionContext):
        if ctx.expression(0).type_attr != ctx.expression(1).type_attr:
            print('Semantic error: Cannot operate {0} and {1}'.format(ctx.expression(0).type_attr,
                                                                      ctx.expression(1).type_attr))
            quit(-1)
        else:
            ctx.type_attr = ctx.expression(0).type_attr
            ctx.value_attr = self.CreateTemp()

            print('{0} = {1} {2} {3}'.format(ctx.value_attr, ctx.expression(0).getText(), ctx.OP().getText(),
                                             ctx.expression(1).getText()))

    def exitIf_statement(self, ctx: Q2Parser.If_statementContext):
        ctx.statement(1).value_attr = self.CreateLabel() + ' ' + ctx.statement(1).value_attr
        ctx.value_attr = 'if' + '!(' + ctx.expression().value_attr + ') ' + 'goto ' + ctx.statement(1).value_attr[0: 2]

        print(ctx.value_attr, ctx.statement(1).value_attr)



