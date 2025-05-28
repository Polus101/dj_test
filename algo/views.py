from django.shortcuts import render
from .models import Calc
from .forms import ManagerForm, CalcForm, CalcFilterForm, CalcFilterFormX, CalcSortedForm
# Create your views here.
def new2(request):
    result = ''
    if request.method == 'POST':
        form = ManagerForm(request.POST)
        if form.is_valid():
            form.save()
            result = "Данные успешно добавлены"
        else:
            result = "Неверные данные"

    form = ManagerForm()

    data = {
        'form': form,
        'result': result
    }
    # managers_data = Calc.objects.all()
    return render(request, 'algo/new.html', data)

def new(request):
    result = ''
    if request.method == 'POST':
        form = CalcForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.x = instance.a * 2
            form.save()
            result = "Данные успешно добавлены"
        else:
            result = "Неверные данные"

    form = CalcForm()

    data = {
        'form': form,
        'result': result
    }
    # managers_data = Calc.objects.all()
    return render(request, 'algo/new.html', data)

def view(request):
    calcs = Calc.objects.all()
    return render(request, 'algo/view.html', {'calcs': calcs})

def filters(request):
    calcs = Calc.objects.all()
    form = CalcFilterForm(request.GET)
    form_x = CalcFilterFormX(request.GET)
    form_max_min = CalcSortedForm(request.GET)
    
    
    if form.is_valid():
        if form.cleaned_data['min_value']:
            calcs = calcs.filter(a__gte=form.cleaned_data['min_value'])

    if form_x.is_valid():
        if form_x.cleaned_data['min_value_x']:
            calcs = calcs.filter(x__gte=form_x.cleaned_data['min_value_x'])

    if form_max_min.is_valid():
        if form_max_min.cleaned_data['variant']:
            calcs = calcs.order_by(form_max_min.cleaned_data['variant'])
    #     min_value = form.cleaned_data.get('min_value')
    #     calculations = calculations.filter(input_value__gte=min_value)

    
    return render(request, 'algo/filters.html', {'calcs': calcs, 'form': form, 'form_x': form_x, 'form_max_min': form_max_min})