from django.shortcuts import render
from .models import Member
from django.http import HttpResponse
# from django.template import loader

def blog(request):
#   template = loader.get_template('index.html')
#   return HttpResponse(template.render())
    return render(request, 'index.html')
def display(request):
    members=Member.objects.all()
    context={'members':members}
    return render(request, 'member.html', context)