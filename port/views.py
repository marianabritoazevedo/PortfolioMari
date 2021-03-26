from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.urls import reverse
from .models import Port, Certificado, PortfolioOK, CertificadoOK
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
    posts = PortfolioOK.objects.all().order_by('-published_date')
    page = request.GET.get('page', 1)
    paginator = Paginator(posts,6)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        'posts': posts,
    }
    template_name = 'port/portfolio.html'
    return render(request, template_name, context)

def details(request, slug):
    post = get_object_or_404(PortfolioOK, slug=slug)
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
            lookups = Q(titulo_port__icontains=query) | Q(tecnologias__icontains=query) | Q(titulo_ing__icontains=query) | Q(texto_port__icontains=query) | Q(texto_ing__icontains=query) 
            results = PortfolioOK.objects.filter(lookups).distinct()
            context = {
                'results': results,
                'submitbutton': submitbutton,
            }
            return render(request, 'port/search.html', context)
        else:
            return render(request, 'port/search.html')
    else:
        return render(request, 'port/search.html')

def certificado(request):
    template_name = 'port/certificado.html'
    certificados = CertificadoOK.objects.all().order_by('-published_date')
    page = request.GET.get('page', 1)
    paginator = Paginator(certificados,6)
    try:
        certificados = paginator.page(page)
    except PageNotAnInteger:
        certificados = paginator.page(1)
    except EmptyPage:
        certificados = paginator.page(paginator.num_pages)
    context = {
        'certificados': certificados,
    }
    return render(request, template_name, context)

def certificado_details(request, slug):
    certificado = get_object_or_404(CertificadoOK, slug=slug)
    template_name = 'port/certificado_details.html'
    context = {
        'certificado': certificado,
    }
    return render(request, template_name, context)

def search_certificado(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        submitbutton = request.GET.get('submit')
        if query is not None:
            lookups = Q(titulo_port__icontains=query) | Q(titulo_ing__icontains=query) | Q(descricao_port__icontains=query) | Q(descricao_ing__icontains=query) 
            results = CertificadoOK.objects.filter(lookups).distinct()
            context = {
                'results': results,
                'submitbutton': submitbutton,
            }
            return render(request, 'port/search-certificado.html', context)
        else:
            return render(request, 'port/search-certificado.html')
    else:
        return render(request, 'port/search-certificado.html')
