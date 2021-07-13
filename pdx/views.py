from django.shortcuts import render, redirect
from .forms import PdxForm
from .models import Pdx


def homePageView(request):
    return render(request, 'home.html')


def modelSubmittedView(request):
    return render(request, 'model_submitted.html')


def submitModelsView(request):
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


def dataView(request, **kwargs):
    data = Pdx.objects.all()

    context = {
        'data': data,
    }
    return render(request, 'data.html', context)


def dataDetailView(request, pk):
    detail = Pdx.objects.filter(pk=pk)

    context = {
        'detail': detail,
    }
    return render(request, 'data_detail.html', context)
