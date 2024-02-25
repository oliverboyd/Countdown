from django.http import JsonResponse
from django.shortcuts import render
from django.utils.safestring import mark_safe
from .countdown import *

def home(request):
    if request.is_ajax():
        number1 = int(request.GET.get('number1'))
        number2 = int(request.GET.get('number2'))
        number3 = int(request.GET.get('number3'))
        number4 = int(request.GET.get('number4'))
        number5 = int(request.GET.get('number5'))
        number6 = int(request.GET.get('number6'))
        target = int(request.GET.get('target'))
        shortest = request.GET.get('shortest')
        array = [number1,number2,number3,number4,number5,number6]
        if shortest == "true":
            result = mark_safe(print_out(filter_equiv(filter_redundant(filter_duplicates(min_only(countdown(target,array)))))))
        elif shortest == "false":
            result = mark_safe(print_out(filter_redundant2(filter_equiv(filter_redundant(filter_duplicates(countdown(target,array)))))))
        else:
            raise TypeError("Only boolean values are allowed")
        return JsonResponse({'result': result })
    return render(request, 'home.html')

def print_out(array):
    string = ""
    if array == "Impossible":
        string = "<br>Impossible"
        return string
    elif array == "Trivial":
        string = "<br>Trivial"
        return string
    else:
        i=0
        L=len(array)
        if L == 1:
            string = "<br><b>One solution</b><br><br>"
            
        else:
            string += "<br><b>" + str(L) + " Solutions</b><br>"
        for i in range(0,L):
            Lin = len(array[i])
            if L>1:
                string += "<br><b>Solution " + str(i + 1) + ":</b><br>"
            for j in range(0,Lin):
                x = array[i][j][0]
                y = array[i][j][1]
                if x > y:
                    string = string + str(array[i][j][0]) + " " + array[i][j][2] + " " + str(array[i][j][1]) + " = " + str(array[i][j][3]) + "<br>"
                else: 
                    string = string + str(array[i][j][1]) + " " + array[i][j][2] + " " + str(array[i][j][0]) + " = " + str(array[i][j][3]) + "<br>"
    return string