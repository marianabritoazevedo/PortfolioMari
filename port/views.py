from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.urls import reverse
from .models import Port
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
    posts = Port.objects.all()
    '''page = request.GET.get('page',1)
    paginator = Paginator(posts,3)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)'''
    context = {
        'posts': posts,
    }
    template_name = 'port/portfolio.html'
    return render(request, template_name, context)

def details(request, slug):
    post = get_object_or_404(Port, slug=slug)
    template_name = 'port/details.html'
    context = {
        'post': post
    }
    return render(request, template_name, context)

def search(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        submitbutton = request.GET.get('submit')
        if query is not None:
            lookups = Q(title__icontains=query) | Q(tecnologias__icontains=query)
            results = Port.objects.filter(lookups).distinct()
            context = {
                'results': results,
                'submitbutton': submitbutton,
            }
            return render(request, 'port/search.html', context)
        else:
            return render(request, 'port/search.html')
    else:
        return render(request, 'port/search.html')