from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    if request.method == 'GET':
        inputan_search = request.GET.get('search')
        if inputan_search is not None:
            lowongan = Lowongan.objects.filter(posisi__contains=inputan_search)
            perusahaan = Lowongan.objects.filter(perusahaan__nama__contains=inputan_search)
            
            return render(request, 'search_result.html', {'inputan_search':inputan_search,'lowongan': lowongan, 'perusahaan': perusahaan})
    perusahaan_show = Lowongan.objects.order_by('-id')[:5]
    
    return render(request,'home.html', {'perusahaan_show': perusahaan_show})

def search(request):
    if request.method == 'GET':
        inputan_search = request.GET.get('search')
        if inputan_search is not None:
            lowongan = Lowongan.objects.filter(posisi__contains=inputan_search)
            perusahaan = Lowongan.objects.filter(perusahaan__nama__contains=inputan_search)
            
            jumlah_lowongan = Lowongan.objects.filter(posisi__contains=inputan_search).count()
            return render(request, 'search_result.html', {'perusahaan': perusahaan, 'inputan_search':inputan_search, 'lowongan': lowongan, 'jumlah_lowongan': jumlah_lowongan})
    return render(request, 'search_result.html')

def detail(request, id_lowongan):
    lowongan = Lowongan.objects.get(id = id_lowongan)
    if request.method == 'GET':
        inputan_search = request.GET.get('search')
        if inputan_search is not None:
            lowongan = Lowongan.objects.filter(posisi__contains=inputan_search)
            perusahaan = Lowongan.objects.filter(perusahaan__nama__contains=inputan_search)
            
            return render(request, 'search_result.html', {'inputan_search':inputan_search,'lowongan': lowongan})
    return render(request, 'detail.html', {'lowongan': lowongan})

def Detail(request):
        return render(request, 'detail.html')
