from datetime import datetime

from django.core.mail import send_mail

from zayavka.forms import zayavkaFromSaitForm
from zayavka.models import zayavka


def main(request):
    if request.POST:
        form = zayavkaFromSaitForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.date_sozd = datetime.now()
            post.kanal_pr = 'Заявка с сайта'
            post.status = 'Новая заявка'
            ss = 'От ' + post.name_kl +' тел.'+str(post.tel)
            send_mail('Поступила новая заявка на сайт', ss , 'zhem-otchet@mail.ru',
                      ['sawf@rambler.ru'], fail_silently=False, html_message=ss)
            post.save()
    else:
        form = zayavkaFromSaitForm()
    return {'tn3': zayavka.objects.filter(status='Новая заявка').count(), 'allform':form}
