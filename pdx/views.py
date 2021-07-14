from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.http import Http404

from .forms import PdxForm
from .filters import PdxFilter
from .models import Pdx
from .serializers import PdxSerializer


def homepage_view(request):
    return render(request, 'home.html')


def model_submitted_view(request):
    return render(request, 'model_submitted.html')


def submit_model_view(request):
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


def pdx_list_view(request, **kwargs):
    data = Pdx.objects.all()
    data_filter = PdxFilter(request.GET, queryset=data)
    data_list = data_filter.qs

    paginator = Paginator(data_list, 15)
    page_number = request.GET.get('page')

    try:
        data_list = paginator.page(page_number)
    except PageNotAnInteger:
        data_list = paginator.page(1)
    except EmptyPage:
        data_list = paginator.page(page_number.num_pages)

    context = {
        'data_filter': data_filter,
        'data_list': data_list,
    }
    return render(request, 'data.html', context)


def pdx_detail_view(request, model_id):
    try:
        detail = Pdx.objects.get(model_id=model_id)  # model_id is the primary key
    except Pdx.DoesNotExist:
        raise Http404('Pdx model does not exist.')

    context = {
        'detail': detail,
    }
    return render(request, 'model_detail.html', context)
