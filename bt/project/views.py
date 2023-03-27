from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .forms import *
from .models import *

# Create your views here.
class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = 'project/project_create.html'
    success_url = '/project/projectlist'

    def form_valid(self, form):
        return super().form_valid(form)
    
class ProjectListView(ListView):
    model = Project
    template_name = 'project/project_list.html'
    context_object_name = 'projectlist'

    def get_queryset(self):
        return super().get_queryset()

class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = 'project/project_create.html'
    success_url = '/project/projectlist'

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project/project_detail.html'
    context_object_name = 'projectdetail'

    def get(self, request, *args, **kwargs):
        team = ProjectTeam.objects.filter(project_id = self.kwargs['pk'])
        return render(request, self.template_name, {'projectdetail': self.get_object(), 'team':team})
    
class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'project/project_delete.html'
    success_url = '/project/projectlist'
    context_object_name = 'projectdelete'

    # def get(self, request, *args, **kwargs):
    #     return self.delete(request, *args, **kwargs)
    
    # success_url = 'project/projectlist'
    
class ProjectTeamCreateView(CreateView):
    model = ProjectTeam
    form_class = ProjectTeamCreationForm
    template_name = 'project/projectteam_create.html'
    success_url = '/project/projectteamlist'

    def form_valid(self, form):
        return super().form_valid(form)
    
class ProjectTeamListView(ListView):
    model = ProjectTeam
    template_name = 'project/projectteam_list.html'
    context_object_name = 'projectteamlist'

    def get_queryset(self):
        return super().get_queryset()