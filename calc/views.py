from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
def calculate(request):

    if request.method == "POST":
        value = request.POST.get('value_exp')
        ans =  calculation(value)
        response_data = {}
        response_data['val_exp'] = ans
        return HttpResponse(
            json.dumps(response_data),
            content_type="aplication/json"
        )
    else:
        return render(request,'calc.html')


def calculation(expr):
   return safe_eval(expr)

def safe_eval(expr, symbols={}):
   return eval(expr, dict(__builtins__=None), symbols)
