from django.shortcuts import render
from django.http import HttpResponse
from .forms import PdxForm


def homePageView(request):
    return render(request, 'home.html')


def submitModelsView(request):
    pdx_form = PdxForm()
    context = {
        'pdx_form': pdx_form,
    }
    return render(request, 'submit.html', context)
