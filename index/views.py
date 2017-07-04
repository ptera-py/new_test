from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate

from .models import menu_item

def index(request):
    l = []
    o = menu_item()
    o.name = 'Registration'
    o.ref = 'registration'
    l.append(o)
    c = menu_item()
    c.name = 'Login'
    c.ref = 'login'
    l.append(c)
    latest_question_list = l
    k = request.user.username
    context = {'start_menu': latest_question_list, 'm': k}
    return render(request, 'index/index.html', context)

#class IndexView(generic.ListView):
 #   template_name = 'index/index.html'
  #  context_object_name = 'start_menu'
#
 #   def get_queryset(self):
  #      return menu_item.objects.all()


#Registr
class RegisterFormView(generic.edit.FormView):
    form_class = UserCreationForm
    success_url = '/index/login/'
    template_name = 'index/register.html/'

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

#Auth
class LoginFormView(generic.edit.FormView):
    form_class = AuthenticationForm
    success_url = '/index/'
    template_name = 'index/login.html/'

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

#logout
class LogoutView(generic.base.View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/index/')
