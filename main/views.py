from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render
from django.template.loader import get_template
from .forms import ContactForm
from .models import Slider
from catalog.models import Category


def index(request):
    prod = Category.objects.all()
    slide = Slider.objects.all()

    return render(request, 'main/index.html', {
        'slide_list': slide,
        'prod_list': prod
    })


def catalog(request):
    return render(request, 'catalog/category_list.html')


def portfolio(request):
    return render(request, 'main/portfolio.html')


def calc(request):
    context = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_message(form.cleaned_data['name'], form.cleaned_data['email'], form.cleaned_data['phone'])
            context = {'success': 1}
    else:
        form = ContactForm()
    context['form'] = form
    return render(request, 'main/calc.html', context=context,)


def send_message(name, email, phone):
    text = get_template('main/message.html')
    html = get_template('main/message.html')
    context = {'name': name, 'email': email, 'phone': phone}
    subject = 'сообщение от пользователя'
    from_email = 'pasukov.e@yandex.ru'
    text_content = text.render(context)
    html_content = html.render(context)

    msg = EmailMultiAlternatives(subject, text_content, from_email, ['pasukov.e@yandex.ru'])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()

