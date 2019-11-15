from django.shortcuts import render
from django.views.generic import ListView

#from django.views.decorators.csrf import csrf_protect
#from django.utils.decorators import method_decorator
#method_decorator(csrf_protect)


def handle_page_not_found(request, exception):
    return render(request, 'frontend/404.html', {})

def google08f29c7b03e739ef(request):
    return render(request, 'frontend/google08f29c7b03e739ef.html', {})

# Create your views here.
class FrontWebPage(ListView):
    template_name = 'frontend/index.html'

    def get_queryset(self):
        return 0

    #def get(self, request, format=None):
    #    return JsonResponse({'hi':'hello'})

    #def post(self, request, format=None):
    #    dic1 = dict(request.POST.dict())
    #    print(dic1)

    #    text = 'Mail from ' + dic1['name'] + ' ' + dic1['email'] + '\n\n\n' + dic1['message']

    #    send_mail(
    #        dic1['subject'],
    #        text,
    #        dic1['email'],
    #        ['chenapodatechnologies@gmail.com'],
    #        fail_silently=False,
    #    )
        #email = EmailMessage(dic1['subject'], dic1['message'], to=['def@domain.com'])
        #email.send()
    #    return HttpResponse('Message Sent! Thanks for writing to us')

