from django.shortcuts import render

def indexInicio(request):
    return render(request, 'InicioApp/indexinicio.html')

