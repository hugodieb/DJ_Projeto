#encoding: utf-8

from django.views.generic import TemplateView, ListView
from .forms import ProjectForm
from django.shortcuts import redirect, render, get_object_or_404
from .models import Project

class CreateProjectView(TemplateView):

	template_name = 'projects/create.html'

	def get_context_data(self, **Kwargs):
		context = super(CreateProjectView, self).get_context_data(**Kwargs)
		context['form'] = ProjectForm(self.request.POST or None)

		return context

	def post(self, request):
		context = self.get_context_data()
		form = context['form']

		if form.is_valid():
			form.save()
			return redirect('home')

		return self.render_to_response(context)

class ListProjects(ListView):

	template_name = 'projects/list_projects.html'
	model = Project
	context_object_name = 'list_projects'

def UpdateProject(request, pk):
	template_name = 'projects/update_project.html'
	
	project = get_object_or_404(Project, pk=pk)
	form = ProjectForm(request.POST or None, instance=project)

	if form.is_valid():
		form.save()
		return redirect('projects_list')

	return render(request, template_name, {'form':form})

def RemoveProject(request, pk):
	template_name = 'projects/remove_project.html'
	project = get_object_or_404(Project, pk=pk)

	if request.method=='POST':
		project.delete()

		return redirect('projects_list')

	return render(request, template_name, {'project':project})

def SearchProject(request):

	template_name = 'busca.html'

	search_name = request.GET.get('search')

	s_name = Project.objects.filter(name__contains=search_name)

	if s_name:

		return redirect('projects_list')


	return render_to_response(template_name, s_name)

	


