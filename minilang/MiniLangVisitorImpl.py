from .MiniLangVisitor import MiniLangVisitor
from .MiniLangParser import MiniLangParser

class MiniLangVisitorImpl(MiniLangVisitor):
    def __init__(self):
        self.memory = {}

    def visitProgram(self, ctx: MiniLangParser.ProgramContext):
        for stmt in ctx.statement():
            self.visit(stmt)
        return None

    def visitAssign(self, ctx: MiniLangParser.AssignContext):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[var_name] = value
        return value

    def visitPrint(self, ctx: MiniLangParser.PrintContext):
        value = self.visit(ctx.expr())
        print(value)
        return value

    def visitExpr(self, ctx: MiniLangParser.ExprContext):
        
        if ctx.op:
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            op = ctx.op.text
            if op == '+':
                return left + right
            elif op == '-':
                return left - right
            elif op == '*':
                return left * right
            elif op == '/':
                if right == 0:
                    raise ValueError("División por cero")
                return left / right

        if ctx.INT():
            return int(ctx.INT().getText())

        if ctx.ID():
            var_name = ctx.ID().getText()
            if var_name not in self.memory:
                raise NameError(f"Variable '{var_name}' no definida")
            return self.memory[var_name]

        if ctx.expr():
            return self.visit(ctx.expr(0))

        return None
