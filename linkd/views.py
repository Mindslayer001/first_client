from django.shortcuts import render,HttpResponse
from linkd.models import LinkData as ld

def home(request):
    link_fetcher = ld.objects.get(id=1)
    context = {'zoom':link_fetcher.zoomlink}
    return render(request, 'linkd/_base.html', context)
