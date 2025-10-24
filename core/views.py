from django.shortcuts import render
from django.http import JsonResponse
from antlr4 import *
from minilang.MiniLangLexer import MiniLangLexer
from minilang.MiniLangParser import MiniLangParser
from minilang.MiniLangVisitorImpl import MiniLangVisitorImpl

def evaluate_expression(input_expr):
    input_stream = InputStream(input_expr)
    lexer = MiniLangLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MiniLangParser(token_stream)
    tree = parser.expr()
    visitor = MiniLangVisitorImpl()
    result = visitor.visit(tree)
    return result

def index(request):
    return render(request, 'core/index.html')

def calcular(request):
    if request.method == 'POST':
        x = int(request.POST.get('x', 0))
        y = int(request.POST.get('y', 0))
        z = (x * y) + 10
        nuevo_x = x + 1
        return JsonResponse({'z': z, 'x_mas_uno': nuevo_x})
    return JsonResponse({'error': 'Método no permitido'}, status=405)
