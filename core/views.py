from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from .forms import ContactMessagePortugues, ContactMessageIngles
from django.http import HttpResponseRedirect
from .models import SobreMim, FormacaoAcademica, FormacaoComplementar, FormacaoProfissional, CardPortfolio

# Create your views here.
def index(request):
    template_name = 'core/index.html'

    show_script = False
    sobremim = SobreMim.objects.last()
    form_academica = FormacaoAcademica.objects.all()
    form_profissional = FormacaoProfissional.objects.all()
    form_complementar = FormacaoComplementar.objects.all()
    card_port = CardPortfolio.objects.all()
    context = {}

    if request.method == 'POST' and 'button-port' in request.POST:
        form_port = ContactMessagePortugues(request.POST)
        if form_port.is_valid():
            context['is_valid'] = True
            form_port.send_mail_portugues()
            form_port = ContactMessagePortugues()
            show_script = True
    else:
        form_port = ContactMessagePortugues()

    if request.method == 'POST' and 'button-ing' in request.POST:
        form_ing = ContactMessageIngles(request.POST)
        if form_ing.is_valid():
            context['is_valid'] = True
            form_ing.send_mail_ingles()
            form_ing = ContactMessageIngles()
            show_script = True
    else:
        form_ing = ContactMessageIngles()
    context = {
        'form_port': form_port,
        'form_ing': form_ing,
        'sobremim': sobremim,
        'form_academica': form_academica,
        'form_profissional': form_profissional, 
        'form_complementar': form_complementar,
        'card_port': card_port,
        'show_script': show_script,
    }
    return render(request, template_name, context)

def set_language(request):
    response = HttpResponseRedirect('/')
    if request.method == 'POST':
        language = request.POST.get('language')
        if language:
            if language != settings.LANGUAGE_CODE and [lang for lang in settings.LANGUAGES if lang[0] == language]:
                redirect_path = f'/{language}/'
            elif language == settings.LANGUAGE_CODE:
                redirect_path = '/'
            else:
                return response
            from django.utils import translation
            translation.activate(language)
            response = HttpResponseRedirect(redirect_path)
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    return response
