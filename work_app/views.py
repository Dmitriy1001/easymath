from math import gcd
from functools import reduce

from django.contrib import messages
from django.http import Http404
from django.shortcuts import render, redirect


from .forms import MathForm
from .equations_data import equations, equations_detail


def index(request):
    return render(request, 'work_app/index.html')


def equations_list(request):
    return render(request, 'work_app/equations_list.html', {'equations': equations})


def equation_detail(request, equation_slug):
    try:
        name, equation = equations_detail[equation_slug]
    except KeyError:
        raise Http404('Рівняння не знайдено')
    if request.method == 'POST':
        form = MathForm(request.POST)
        if form.is_valid():
            numbers = map(int, form.cleaned_data['numbers'].split())
            messages.success(request, eval(equation)(numbers))
            return redirect('equation_detail', equation_slug)
    else:
        form = MathForm()
    return render(request, 'work_app/equation_detail.html', {'form': form, 'name': name})
