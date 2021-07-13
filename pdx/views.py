from django.shortcuts import render, redirect, get_object_or_404
from .forms import PdxForm
from .filters import PdxFilter
from .models import Pdx


def homepage(request):
    return render(request, 'home.html')


def model_submitted(request):
    return render(request, 'model_submitted.html')


def submit_model(request):
    if request.method == 'POST':
        pdx_form = PdxForm(request.POST)
        if pdx_form.is_valid():
            pdx_form.save()
            return redirect('model_submitted.html', permanent=True)
    else:
        pdx_form = PdxForm()

    context = {
        'pdx_form': pdx_form,
    }
    return render(request, 'submit.html', context)


def pdx_list(request, **kwargs):
    data = Pdx.objects.all()
    data_filter = PdxFilter(request.GET, queryset=data)

    context = {
        'data': data_filter,
    }
    return render(request, 'data.html', context)


def pdx_detail(request, pk):
    data = Pdx.objects.all()
    detail = get_object_or_404(data, pk=pk)

    context = {
        'detail': detail,
    }
    return render(request, 'model_detail.html', context)
