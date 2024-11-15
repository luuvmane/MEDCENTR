from django.views.generic import TemplateView
from main.utils import get_random_choice
from services.models import Service
from speciality.models import Speciality
from users.models import Doctor
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings


def contacts_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Отправка письма
        send_mail(
            f'Сообщение от {name}',
            message,
            email,
            [settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
        )
        return HttpResponseRedirect(reverse('main:contacts'))

    return render(request, 'main/contacts.html')


def about_view(request):
    return render(request, 'main/about.html')


class IndexView(TemplateView):
    """
    Класс для главной страницы сайта.
    """

    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        """
        Метод для вывода информации на главную страницу.
        """

        context_data = super().get_context_data(**kwargs)
        context_data['speciality_list'] = Speciality.objects.all()
        context_data['doctors'] = get_random_choice(Doctor.objects.all())
        context_data['service_list'] = get_random_choice(Service.objects.all())

        return context_data
