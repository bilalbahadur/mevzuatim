import os
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from proje.models import Mansets, Sample
from django.shortcuts import render, get_object_or_404, redirect
from .models import Mansets, Sample, Comment
from .forms import CommentForm
# Create your views here.


def index(request):

     context = dict()
     context ['Mansets'] = Mansets.objects.all()
     context['samples']= Sample.objects.all()

     return render(request, 'index.html', context)
    

def redirect_hakkimizda(request):
     
     return render(request, 'hakkimizda.html')

def redirect_mansetler(request):
     context = dict()
     context ['Mansets'] = Mansets.objects.all()
     return render(request, 'mansetler.html', context)

def redirect_blog(request):
     
     context= dict()

     context['samples']= Sample.objects.all()

     return render(request, 'blog.html', context)

def redirect_iletisim(request):
     
     return render(request, 'iletisim.html')


def redirect_manset_detail(request, manset_id):
    manset = get_object_or_404(Mansets, id=manset_id)  # Burada 'Manset' model adını kullanıyoruz
    context = {
        'manset': manset,
    }
    return render(request, 'manset_detail.html', context)




def redirect_manset_detail(request, manset_id):
    manset = get_object_or_404(Mansets, id=manset_id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = manset
            comment.save()
            return redirect('redirect_manset_detail', manset_id=manset.id)
    else:
        form = CommentForm()

    context = {
        'manset': manset,
        'form': form,
    }
    return render(request, 'manset_detail.html', context)