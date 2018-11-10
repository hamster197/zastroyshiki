from zayavka.models import zayavka


def main(request):
    return {'tn3': zayavka.objects.filter(status='Новая заявка').count()}
