from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import User
from .forms import ManagerRegisterForm, DeveloperRegisterForm, TeamLeaderRegisterForm, TesterRegisterForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required

# Create your views here.
class ManagerRegisterView(CreateView):
    model = User
    form_class = ManagerRegisterForm
    template_name = 'user/managerregister.html'
    success_url = 'index'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'manager'
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
    
class DeveloperRegisterView(CreateView):
    model = User
    form_class = DeveloperRegisterForm
    template_name = 'user/developerregister.html'
    success_url = 'index'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'developer'
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
    
class TeamLeaderRegisterView(CreateView):
    model = User
    form_class = TeamLeaderRegisterForm
    template_name = 'user/teamleaderregister.html'
    success_url = 'index'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teamleader'
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
    
class TesterRegisterView(CreateView):
    model = User
    form_class = TesterRegisterForm
    template_name = 'user/testerregister.html'
    success_url = 'index'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'tester'
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
    
class UserLoginView(LoginView):
    template_name = 'user/login.html'

    def get_redirect_url(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_manager:
                return '/user/index/'
            if self.request.user.is_developer:
                return '/user/index/'
            if self.request.user.is_teamleader:
                return '/user/index/'
            else:
                return '/user/index/'     
            
class UserLogoutView(LogoutView):
    def get_redirect_url(self):
        return '/user/login'

@login_required(login_url='/user/login/')
def indexView(request):
    return render(request, 'home/index.html')      
