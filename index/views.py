from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

#def index(request):
 #   return HttpResponse('vam')

class IndexView(generic.ListView):
    template_name = 'index/index.html'
    context_object_name = 'humans'

    def get_queryset(self):
        return ['ss','mm']