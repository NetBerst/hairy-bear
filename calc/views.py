from django.shortcuts import render
from django import forms
from django.http import HttpResponse

class ExpresForm(forms.Form):
    artem = forms.CharField(label="Ввидите ваше выражение",max_length=20,widget=forms.Textarea)

# Create your views here.
def calculate(request):

    if request.method == "POST":
        form = ExpresForm(request.POST)
        if form.is_valid():
            ans =  calculation(form.cleaned_data['artem'])

            return HttpResponse("Ответ: %s " % ans)

    else:
        form = ExpresForm().as_p()

    return render(request,'name.html',{'form':form})


def calculation(expr):
   return safe_eval(expr)

def safe_eval(expr, symbols={}):
   return eval(expr, dict(__builtins__=None), symbols)
