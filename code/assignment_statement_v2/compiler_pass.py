"""
ANTLR 4.x listener and visitor implementation for intermediate code generation
"""
__version__ = '0.1.0'
__author__ = 'Morteza'

from code.assignment_statement_v2.gen.AssignmentStatement2Listener import AssignmentStatement2Listener
from code.assignment_statement_v2.gen.AssignmentStatement2Visitor import AssignmentStatement2Visitor

from code.assignment_statement_v2.gen.AssignmentStatement2Parser import AssignmentStatement2Parser


# ----------------------
# Listener pattern
class ThreeAddressCodeGeneratorListener(AssignmentStatement2Listener):
    """
    Type checking and generating three address code (not optimized)
    """

    def __init__(self):
        print('Listener call!')
        self.temp_counter = 0

    def create_temp(self):
        self.temp_counter += 1
        return 'T' + str(self.temp_counter)

    # ------------------
    # Rule number
    def exitNumber_float(self, ctx: AssignmentStatement2Parser.Number_floatContext):
        ctx.type_attr = 'float'
        ctx.value_attr = float(ctx.getText())

    def exitNumber_int(self, ctx: AssignmentStatement2Parser.Number_intContext):
        ctx.type_attr = 'int'
        ctx.value_attr = int(ctx.getText())

    # ------------------
    # Rule factor
    def exitFact_expr(self, ctx: AssignmentStatement2Parser.Fact_exprContext):
        ctx.type_attr = ctx.expr().type_attr
        ctx.value_attr = ctx.expr().value_attr

    def exitFact_id(self, ctx: AssignmentStatement2Parser.Fact_idContext):

        ctx.type_attr = 'string'
        ctx.value_attr = ctx.getText()

    def exitFact_number(self, ctx: AssignmentStatement2Parser.Fact_numberContext):
        ctx.type_attr = ctx.number().type_attr
        ctx.value_attr = ctx.number().value_attr

    # ------------------
    # Rule term
    def exitTerm_fact_mutiply(self, ctx: AssignmentStatement2Parser.Term_fact_mutiplyContext):
        if ctx.term().type_attr != ctx.factor().type_attr:
            print('Semantic error: Cannot multiply {0} and {1}'.format(ctx.term().type_attr, ctx.factor().type_attr))
            quit(-1)
        else:
            if ctx.term().type_attr == 'float':
                ctx.type_attr = 'float'
                ctx.value_attr = ctx.term().value_attr * ctx.factor().value_attr
            elif ctx.term().type_attr == 'int':
                ctx.type_attr = 'int'
                ctx.value_attr = ctx.term().value_attr * ctx.factor().value_attr
            else:
                ctx.type_attr = 'string'
                ctx.value_attr = self.create_temp()
            print('{0} = {1} * {2}'.format(ctx.value_attr, ctx.term().value_attr, ctx.factor().value_attr))

    def exitTerm_fact_divide(self, ctx: AssignmentStatement2Parser.Term_fact_mutiplyContext):
        if ctx.term().type_attr != ctx.factor().type_attr:
            print('Semantic error: Cannot divide {0} and {1}'.format(ctx.term().type_attr, ctx.factor().type_attr))
            quit(-1)
        else:
            if ctx.term().type_attr == 'float':
                ctx.type_attr = 'float'
                ctx.value_attr = ctx.term().value_attr / ctx.factor().value_attr
            elif ctx.term().type_attr == 'int':
                ctx.type_attr = 'int'
                ctx.value_attr = int(ctx.term().value_attr / ctx.factor().value_attr)
            else:
                ctx.type_attr = 'string'
                ctx.value_attr = self.create_temp()
            print('{0} = {1} / {2}'.format(ctx.value_attr, ctx.term().value_attr, ctx.factor().value_attr))

    def exitFactor3(self, ctx: AssignmentStatement2Parser.Factor3Context):
        ctx.type_attr = ctx.factor().type_attr
        ctx.value_attr = ctx.factor().value_attr

    # ------------------
    # Rule expr
    def exitExpr_term_plus(self, ctx: AssignmentStatement2Parser.Expr_term_plusContext):
        if ctx.expr().type_attr != ctx.term().type_attr:
            print('Semantic error: Cannot plus {0} and {1}'.format(ctx.expr().type_attr, ctx.term().type_attr))
            quit(-1)
        else:
            if ctx.term().type_attr == 'float':
                ctx.type_attr = 'float'
                ctx.value_attr = ctx.expr().value_attr + ctx.term().value_attr
            elif ctx.term().type_attr == 'int':
                ctx.type_attr = 'int'
                ctx.value_attr = ctx.expr().value_attr + ctx.term().value_attr
            else:
                ctx.type_attr = 'string'
                ctx.value_attr = self.create_temp()
            print('{0} = {1} + {2}'.format(ctx.value_attr, ctx.expr().value_attr, ctx.term().value_attr))

    def exitExpr_term_minus(self, ctx: AssignmentStatement2Parser.Expr_term_minusContext):
        if ctx.expr().type_attr != ctx.term().type_attr:
            print('Semantic error: Cannot subtract {0} and {1}'.format(ctx.expr().type_attr, ctx.term().type_attr))
            quit(-1)
        else:
            if ctx.term().type_attr == 'float':
                ctx.type_attr = 'float'
                ctx.value_attr = ctx.expr().value_attr - ctx.term().value_attr
            elif ctx.term().type_attr == 'int':
                ctx.type_attr = 'int'
                ctx.value_attr = ctx.expr().value_attr - ctx.term().value_attr
            else:
                ctx.type_attr = 'string'
                ctx.value_attr = self.create_temp()
            print('{0} = {1} - {2}'.format(ctx.value_attr, ctx.expr().value_attr, ctx.term().value_attr))

    def exitTerm4(self, ctx: AssignmentStatement2Parser.Term4Context):
        ctx.type_attr = ctx.term().type_attr
        ctx.value_attr = ctx.term().value_attr

    # ------------------
    # Rule expr
    def exitAssign(self, ctx: AssignmentStatement2Parser.AssignContext):
        ctx.type_attr = ctx.expr().type_attr
        ctx.value_attr = ctx.expr().value_attr
        print('Assign statement: "{0} = {1}"\nAssign type: "{2}"'.format(ctx.ID().getText(), ctx.value_attr,
                                                                         ctx.type_attr))


# -----
# Listener 2
class ThreeAddressCodeGenerator2Listener(AssignmentStatement2Listener):
    """
    Type checking and generating three address code (optimizing number of temporary variables)
    """

    def __init__(self):
        print('Listener2 call!')
        self.temp_counter = 0

    def create_temp(self):
        self.temp_counter += 1
        return 'T' + str(self.temp_counter)

    def remove_temp(self):
        self.temp_counter -= 1

    def get_temp(self):
        return 'T' + str(self.temp_counter)

    @classmethod
    def is_temp(cls, variable):
        if variable[0] == 'T':
            return True
        return False

    # ------------------
    # Rule number
    def exitNumber_float(self, ctx: AssignmentStatement2Parser.Number_floatContext):
        ctx.type_attr = 'float'
        ctx.value_attr = float(ctx.getText())

    def exitNumber_int(self, ctx: AssignmentStatement2Parser.Number_intContext):
        ctx.type_attr = 'int'
        ctx.value_attr = int(ctx.getText())

    # ------------------
    # Rule factor
    def exitFact_expr(self, ctx: AssignmentStatement2Parser.Fact_exprContext):
        ctx.type_attr = ctx.expr().type_attr
        ctx.value_attr = ctx.expr().value_attr

    def exitFact_id(self, ctx: AssignmentStatement2Parser.Fact_idContext):

        ctx.type_attr = 'string'
        ctx.value_attr = ctx.getText()

    def exitFact_number(self, ctx: AssignmentStatement2Parser.Fact_numberContext):
        ctx.type_attr = ctx.number().type_attr
        ctx.value_attr = ctx.number().value_attr

    # ------------------
    # Rule term
    def exitTerm_fact_mutiply(self, ctx: AssignmentStatement2Parser.Term_fact_mutiplyContext):
        if ctx.term().type_attr != ctx.factor().type_attr:
            print('Semantic error: Cannot multiply {0} and {1}'.format(ctx.term().type_attr, ctx.factor().type_attr))
            quit(-1)
        else:
            if ctx.term().type_attr == 'float':
                ctx.type_attr = 'float'
                ctx.value_attr = ctx.term().value_attr * ctx.factor().value_attr
            elif ctx.term().type_attr == 'int':
                ctx.type_attr = 'int'
                ctx.value_attr = ctx.term().value_attr * ctx.factor().value_attr
            else:
                ctx.type_attr = 'string'
                if self.is_temp(ctx.term().value_attr):
                    ctx.value_attr = ctx.term().value_attr
                    if self.is_temp(ctx.factor().value_attr):
                        self.remove_temp()
                elif self.is_temp(ctx.factor().value_attr):
                    ctx.value_attr = ctx.factor().value_attr
                else:
                    ctx.value_attr = self.create_temp()
            print('{0} = {1} * {2}'.format(ctx.value_attr, ctx.term().value_attr, ctx.factor().value_attr))

    def exitTerm_fact_divide(self, ctx: AssignmentStatement2Parser.Term_fact_mutiplyContext):
        if ctx.term().type_attr != ctx.factor().type_attr:
            print('Semantic error: Cannot divide {0} and {1}'.format(ctx.term().type_attr, ctx.factor().type_attr))
            quit(-1)
        else:
            if ctx.term().type_attr == 'float':
                ctx.type_attr = 'float'
                ctx.value_attr = ctx.term().value_attr / ctx.factor().value_attr
            elif ctx.term().type_attr == 'int':
                ctx.type_attr = 'int'
                ctx.value_attr = int(ctx.term().value_attr / ctx.factor().value_attr)
            else:
                ctx.type_attr = 'string'
                if self.is_temp(ctx.term().value_attr):
                    ctx.value_attr = ctx.term().value_attr
                    if self.is_temp(ctx.factor().value_attr):
                        self.remove_temp()
                elif self.is_temp(ctx.factor().value_attr):
                    ctx.value_attr = ctx.factor().value_attr
                else:
                    ctx.value_attr = self.create_temp()
            print('{0} = {1} / {2}'.format(ctx.value_attr, ctx.term().value_attr, ctx.factor().value_attr))

    def exitFactor3(self, ctx: AssignmentStatement2Parser.Factor3Context):
        ctx.type_attr = ctx.factor().type_attr
        ctx.value_attr = ctx.factor().value_attr

    # ------------------
    # Rule expr
    def exitExpr_term_plus(self, ctx: AssignmentStatement2Parser.Expr_term_plusContext):
        if ctx.expr().type_attr != ctx.term().type_attr:
            print('Semantic error: Cannot plus {0} and {1}'.format(ctx.expr().type_attr, ctx.term().type_attr))
            quit(-1)
        else:
            if ctx.term().type_attr == 'float':
                ctx.type_attr = 'float'
                ctx.value_attr = ctx.expr().value_attr + ctx.term().value_attr
            elif ctx.term().type_attr == 'int':
                ctx.type_attr = 'int'
                ctx.value_attr = ctx.expr().value_attr + ctx.term().value_attr
            else:
                ctx.type_attr = 'string'
                if self.is_temp(ctx.expr().value_attr):
                    ctx.value_attr = ctx.expr().value_attr
                    if self.is_temp(ctx.term().value_attr):
                        self.remove_temp()
                elif self.is_temp(ctx.term().value_attr):
                    ctx.value_attr = ctx.term().value_attr
                else:
                    ctx.value_attr = self.create_temp()
            print('{0} = {1} + {2}'.format(ctx.value_attr, ctx.expr().value_attr, ctx.term().value_attr))

    def exitExpr_term_minus(self, ctx: AssignmentStatement2Parser.Expr_term_minusContext):
        if ctx.expr().type_attr != ctx.term().type_attr:
            print('Semantic error: Cannot subtract {0} and {1}'.format(ctx.expr().type_attr, ctx.term().type_attr))
            quit(-1)
        else:
            if ctx.term().type_attr == 'float':
                ctx.type_attr = 'float'
                ctx.value_attr = ctx.expr().value_attr - ctx.term().value_attr
            elif ctx.term().type_attr == 'int':
                ctx.type_attr = 'int'
                ctx.value_attr = ctx.expr().value_attr - ctx.term().value_attr
            else:
                ctx.type_attr = 'string'
                if self.is_temp(ctx.expr().value_attr):
                    ctx.value_attr = ctx.expr().value_attr
                    if self.is_temp(ctx.term().value_attr):
                        self.remove_temp()
                elif self.is_temp(ctx.term().value_attr):
                    ctx.value_attr = ctx.term().value_attr
                else:
                    ctx.value_attr = self.create_temp()
            print('{0} = {1} - {2}'.format(ctx.value_attr, ctx.expr().value_attr, ctx.term().value_attr))

    def exitTerm4(self, ctx: AssignmentStatement2Parser.Term4Context):
        ctx.type_attr = ctx.term().type_attr
        ctx.value_attr = ctx.term().value_attr

    # ------------------
    # Rule expr
    def exitAssign(self, ctx: AssignmentStatement2Parser.AssignContext):
        ctx.type_attr = ctx.expr().type_attr
        ctx.value_attr = ctx.expr().value_attr
        print('Assign statement: "{0} = {1}"\nAssign type: "{2}"'.format(ctx.ID().getText(), ctx.value_attr,
                                                                         ctx.type_attr))


# ------------------------------------------------------------------------
# Visitor pattern
class ThreeAddressCodeGeneratorVisitor(AssignmentStatement2Visitor):
    """
    Type checking and generating three address code (not optimized regarding to the number of temporary variables)
    Utilizing ANTLR 4.x Visitor mechanism
    """

    def __init__(self):
        print('Visitor call!')
        self.temp_counter = 0

    def create_temp(self):
        self.temp_counter += 1
        return 'T' + str(self.temp_counter)

    def visitStart(self, ctx: AssignmentStatement2Parser.StartContext):
        self.visit(tree=ctx.prog())

    def visitProg(self, ctx: AssignmentStatement2Parser.ProgContext):
        if ctx.getChildCount() == 2:
            self.visit(tree=ctx.prog())
        ctx.type_attr, ctx.value_attr = self.visit(tree=ctx.assign())
        return ctx.type_attr, ctx.value_attr

    def visitAssign(self, ctx: AssignmentStatement2Parser.AssignContext):
        ctx.type_attr, ctx.value_attr = self.visit(tree=ctx.expr())
        print('Assign statement: "{0} = {1}"\nAssign type: "{2}"'.format(ctx.ID().getText(), ctx.value_attr,
                                                                         ctx.type_attr))
        return ctx.type_attr, ctx.value_attr

    # ------------------
    # Rule expr
    def visitExpr_term_plus(self, ctx: AssignmentStatement2Parser.Expr_term_plusContext):
        ctx.expr().type_attr, ctx.expr().value_attr = self.visit(tree=ctx.expr())
        ctx.term().type_attr, ctx.term().value_attr = self.visit(tree=ctx.term())
        if ctx.expr().type_attr != ctx.term().type_attr:
            print('Semantic error: Cannot plus {0} and {1}'.format(ctx.expr().type_attr, ctx.term().type_attr))
            quit(-1)
        else:
            if ctx.term().type_attr == 'float':
                ctx.type_attr = 'float'
                ctx.value_attr = ctx.expr().value_attr + ctx.term().value_attr
            elif ctx.term().type_attr == 'int':
                ctx.type_attr = 'int'
                ctx.value_attr = ctx.expr().value_attr + ctx.term().value_attr
            else:
                ctx.type_attr = 'string'
                ctx.value_attr = self.create_temp()
            print('{0} = {1} + {2}'.format(ctx.value_attr, ctx.expr().value_attr, ctx.term().value_attr))
            return ctx.type_attr, ctx.value_attr

    def visitExpr_term_minus(self, ctx: AssignmentStatement2Parser.Expr_term_minusContext):
        ctx.expr().type_attr, ctx.expr().value_attr = self.visit(tree=ctx.expr())
        ctx.term().type_attr, ctx.term().value_attr = self.visit(tree=ctx.term())
        if ctx.expr().type_attr != ctx.term().type_attr:
            print('Semantic error: Cannot plus {0} and {1}'.format(ctx.expr().type_attr, ctx.term().type_attr))
            quit(-1)
        else:
            if ctx.term().type_attr == 'float':
                ctx.type_attr = 'float'
                ctx.value_attr = ctx.expr().value_attr - ctx.term().value_attr
            elif ctx.term().type_attr == 'int':
                ctx.type_attr = 'int'
                ctx.value_attr = ctx.expr().value_attr - ctx.term().value_attr
            else:
                ctx.type_attr = 'string'
                ctx.value_attr = self.create_temp()
            print('{0} = {1} - {2}'.format(ctx.value_attr, ctx.expr().value_attr, ctx.term().value_attr))
            return ctx.type_attr, ctx.value_attr

    def visitTerm4(self, ctx: AssignmentStatement2Parser.Term4Context):
        ctx.type_attr, ctx.value_attr = self.visit(ctx.term())
        return ctx.type_attr, ctx.value_attr

    # ------------------
    # Rule term
    def visitTerm_fact_mutiply(self, ctx: AssignmentStatement2Parser.Term_fact_mutiplyContext):
        ctx.term().type_attr, ctx.term().value_attr = self.visit(tree=ctx.term())
        ctx.factor().type_attr, ctx.factor().value_attr = self.visit(tree=ctx.factor())
        if ctx.term().type_attr != ctx.factor().type_attr:
            print('Semantic error: Cannot multiply {0} and {1}'.format(ctx.term().type_attr, ctx.factor().type_attr))
            quit(-1)
        else:
            if ctx.term().type_attr == 'float':
                ctx.type_attr = 'float'
                ctx.value_attr = ctx.term().value_attr * ctx.factor().value_attr
            elif ctx.term().type_attr == 'int':
                ctx.type_attr = 'int'
                ctx.value_attr = ctx.term().value_attr * ctx.factor().value_attr
            else:
                ctx.type_attr = 'string'
                ctx.value_attr = self.create_temp()
            print('{0} = {1} * {2}'.format(ctx.value_attr, ctx.term().value_attr, ctx.factor().value_attr))
            return ctx.type_attr, ctx.value_attr

    def visitTerm_fact_divide(self, ctx: AssignmentStatement2Parser.Term_fact_divideContext):
        ctx.term().type_attr, ctx.term().value_attr = self.visit(tree=ctx.term())
        ctx.factor().type_attr, ctx.factor().value_attr = self.visit(tree=ctx.factor())
        if ctx.term().type_attr != ctx.factor().type_attr:
            print('Semantic error: Cannot multiply {0} and {1}'.format(ctx.term().type_attr, ctx.factor().type_attr))
            quit(-1)
        else:
            if ctx.term().type_attr == 'float':
                ctx.type_attr = 'float'
                ctx.value_attr = ctx.term().value_attr / ctx.factor().value_attr
            elif ctx.term().type_attr == 'int':
                ctx.type_attr = 'int'
                ctx.value_attr = int(ctx.term().value_attr / ctx.factor().value_attr)
            else:
                ctx.type_attr = 'string'
                ctx.value_attr = self.create_temp()
            print('{0} = {1} / {2}'.format(ctx.value_attr, ctx.term().value_attr, ctx.factor().value_attr))
            return ctx.type_attr, ctx.value_attr

    def visitFactor3(self, ctx: AssignmentStatement2Parser.Factor3Context):
        ctx.type_attr, ctx.value_attr = self.visit(tree=ctx.factor())
        return ctx.type_attr, ctx.value_attr

    # ------------------
    # Rule factor
    def visitFact_expr(self, ctx: AssignmentStatement2Parser.Fact_exprContext):
        return self.visit(tree=ctx.expr())

    def visitFact_id(self, ctx: AssignmentStatement2Parser.Fact_idContext):
        return 'string', ctx.ID().getText()

    def visitFact_number(self, ctx: AssignmentStatement2Parser.Fact_numberContext):
        return self.visit(tree=ctx.number())

    # ------------------
    # Rule number
    def visitNumber_float(self, ctx: AssignmentStatement2Parser.Number_floatContext):
        return 'float', float(ctx.FLOAT().getText())

    def visitNumber_int(self, ctx: AssignmentStatement2Parser.Number_intContext):
        return 'int', int(ctx.INT().getText())


# Visitor pattern 2
class ThreeAddressCodeGenerator2Visitor(AssignmentStatement2Visitor):
    """
    Type checking and generating three address code (optimizing number of temporary variables)
    Utilizing ANTLR 4.x Visitor mechanism
    """

    def __init__(self):
        print('Visitor2 call!')
        self.temp_counter = 0

    def create_temp(self):
        self.temp_counter += 1
        return 'T' + str(self.temp_counter)

    def remove_temp(self):
        self.temp_counter -= 1

    def get_temp(self):
        return 'T' + str(self.temp_counter)

    @classmethod
    def is_temp(cls, variable):
        if variable[0] == 'T':
            return True
        return False

    def visitStart(self, ctx: AssignmentStatement2Parser.StartContext):
        self.visit(tree=ctx.prog())

    def visitProg(self, ctx: AssignmentStatement2Parser.ProgContext):
        if ctx.getChildCount() == 2:
            self.visit(tree=ctx.prog())
        ctx.type_attr, ctx.value_attr = self.visit(tree=ctx.assign())
        return ctx.type_attr, ctx.value_attr

    def visitAssign(self, ctx: AssignmentStatement2Parser.AssignContext):
        ctx.type_attr, ctx.value_attr = self.visit(tree=ctx.expr())
        print('Assign statement: "{0} = {1}"\nAssign type: "{2}"'.format(ctx.ID().getText(), ctx.value_attr,
                                                                         ctx.type_attr))
        return ctx.type_attr, ctx.value_attr

    # ------------------
    # Rule expr
    def visitExpr_term_plus(self, ctx: AssignmentStatement2Parser.Expr_term_plusContext):
        ctx.expr().type_attr, ctx.expr().value_attr = self.visit(tree=ctx.expr())
        ctx.term().type_attr, ctx.term().value_attr = self.visit(tree=ctx.term())
        if ctx.expr().type_attr != ctx.term().type_attr:
            print('Semantic error: Cannot plus {0} and {1}'.format(ctx.expr().type_attr, ctx.term().type_attr))
            quit(-1)
        else:
            if ctx.term().type_attr == 'float':
                ctx.type_attr = 'float'
                ctx.value_attr = ctx.expr().value_attr + ctx.term().value_attr
            elif ctx.term().type_attr == 'int':
                ctx.type_attr = 'int'
                ctx.value_attr = ctx.expr().value_attr + ctx.term().value_attr
            else:
                ctx.type_attr = 'string'
                if self.is_temp(ctx.expr().value_attr):
                    ctx.value_attr = ctx.expr().value_attr
                    if self.is_temp(ctx.term().value_attr):
                        self.remove_temp()
                elif self.is_temp(ctx.term().value_attr):
                    ctx.value_attr = ctx.term().value_attr
                else:
                    ctx.value_attr = self.create_temp()
            print('{0} = {1} + {2}'.format(ctx.value_attr, ctx.expr().value_attr, ctx.term().value_attr))
            return ctx.type_attr, ctx.value_attr

    def visitExpr_term_minus(self, ctx: AssignmentStatement2Parser.Expr_term_minusContext):
        ctx.expr().type_attr, ctx.expr().value_attr = self.visit(tree=ctx.expr())
        ctx.term().type_attr, ctx.term().value_attr = self.visit(tree=ctx.term())
        if ctx.expr().type_attr != ctx.term().type_attr:
            print('Semantic error: Cannot plus {0} and {1}'.format(ctx.expr().type_attr, ctx.term().type_attr))
            quit(-1)
        else:
            if ctx.term().type_attr == 'float':
                ctx.type_attr = 'float'
                ctx.value_attr = ctx.expr().value_attr - ctx.term().value_attr
            elif ctx.term().type_attr == 'int':
                ctx.type_attr = 'int'
                ctx.value_attr = ctx.expr().value_attr - ctx.term().value_attr
            else:
                ctx.type_attr = 'string'
                if self.is_temp(ctx.expr().value_attr):
                    ctx.value_attr = ctx.expr().value_attr
                    if self.is_temp(ctx.term().value_attr):
                        self.remove_temp()
                elif self.is_temp(ctx.term().value_attr):
                    ctx.value_attr = ctx.term().value_attr
                else:
                    ctx.value_attr = self.create_temp()
            print('{0} = {1} - {2}'.format(ctx.value_attr, ctx.expr().value_attr, ctx.term().value_attr))
            return ctx.type_attr, ctx.value_attr

    def visitTerm4(self, ctx: AssignmentStatement2Parser.Term4Context):
        ctx.type_attr, ctx.value_attr = self.visit(ctx.term())
        return ctx.type_attr, ctx.value_attr

    # ------------------
    # Rule term
    def visitTerm_fact_mutiply(self, ctx: AssignmentStatement2Parser.Term_fact_mutiplyContext):
        ctx.term().type_attr, ctx.term().value_attr = self.visit(tree=ctx.term())
        ctx.factor().type_attr, ctx.factor().value_attr = self.visit(tree=ctx.factor())
        if ctx.term().type_attr != ctx.factor().type_attr:
            print('Semantic error: Cannot multiply {0} and {1}'.format(ctx.term().type_attr, ctx.factor().type_attr))
            quit(-1)
        else:
            if ctx.term().type_attr == 'float':
                ctx.type_attr = 'float'
                ctx.value_attr = ctx.term().value_attr * ctx.factor().value_attr
            elif ctx.term().type_attr == 'int':
                ctx.type_attr = 'int'
                ctx.value_attr = ctx.term().value_attr * ctx.factor().value_attr
            else:
                ctx.type_attr = 'string'
                if self.is_temp(ctx.term().value_attr):
                    ctx.value_attr = ctx.term().value_attr
                    if self.is_temp(ctx.factor().value_attr):
                        self.remove_temp()
                elif self.is_temp(ctx.factor().value_attr):
                    ctx.value_attr = ctx.factor().value_attr
                else:
                    ctx.value_attr = self.create_temp()
            print('{0} = {1} * {2}'.format(ctx.value_attr, ctx.term().value_attr, ctx.factor().value_attr))
            return ctx.type_attr, ctx.value_attr

    def visitTerm_fact_divide(self, ctx: AssignmentStatement2Parser.Term_fact_divideContext):
        ctx.term().type_attr, ctx.term().value_attr = self.visit(tree=ctx.term())
        ctx.factor().type_attr, ctx.factor().value_attr = self.visit(tree=ctx.factor())
        if ctx.term().type_attr != ctx.factor().type_attr:
            print('Semantic error: Cannot multiply {0} and {1}'.format(ctx.term().type_attr, ctx.factor().type_attr))
            quit(-1)
        else:
            if ctx.term().type_attr == 'float':
                ctx.type_attr = 'float'
                ctx.value_attr = ctx.term().value_attr / ctx.factor().value_attr
            elif ctx.term().type_attr == 'int':
                ctx.type_attr = 'int'
                ctx.value_attr = int(ctx.term().value_attr / ctx.factor().value_attr)
            else:
                ctx.type_attr = 'string'
                if self.is_temp(ctx.term().value_attr):
                    ctx.value_attr = ctx.term().value_attr
                    if self.is_temp(ctx.factor().value_attr):
                        self.remove_temp()
                elif self.is_temp(ctx.factor().value_attr):
                    ctx.value_attr = ctx.factor().value_attr
                else:
                    ctx.value_attr = self.create_temp()
            print('{0} = {1} / {2}'.format(ctx.value_attr, ctx.term().value_attr, ctx.factor().value_attr))
            return ctx.type_attr, ctx.value_attr

    def visitFactor3(self, ctx: AssignmentStatement2Parser.Factor3Context):
        ctx.type_attr, ctx.value_attr = self.visit(tree=ctx.factor())
        return ctx.type_attr, ctx.value_attr

    # ------------------
    # Rule factor
    def visitFact_expr(self, ctx: AssignmentStatement2Parser.Fact_exprContext):
        return self.visit(tree=ctx.expr())

    def visitFact_id(self, ctx: AssignmentStatement2Parser.Fact_idContext):
        return 'string', ctx.ID().getText()

    def visitFact_number(self, ctx: AssignmentStatement2Parser.Fact_numberContext):
        return self.visit(tree=ctx.number())

    # ------------------
    # Rule number
    def visitNumber_float(self, ctx: AssignmentStatement2Parser.Number_floatContext):
        return 'float', float(ctx.FLOAT().getText())

    def visitNumber_int(self, ctx: AssignmentStatement2Parser.Number_intContext):
        return 'int', int(ctx.INT().getText())
