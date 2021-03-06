#encoding: utf-8

#from .validForm import valid_form
from django.views.generic import TemplateView, ListView
from .forms import PersonForm, RegisterForm, LoginForm
from django.shortcuts import redirect, render, get_object_or_404, render_to_response
from projects.models import Project, Person
from django.template import RequestContext
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


@login_required
def EditPerson(request):
    person = Person()
    form = PersonForm()

    if request.method == 'POST':
        form = PersonForm(request.POST)

        if form.is_valid():
            person.user = request.user
            person.username = request.POST.get('username')
            person.mail = request.POST.get('usermail')

            person.save()

            return render_to_response('projects/list_projects.html', context_instance=RequestContext(request))

        else:
            context = {'form': form}

        return render_to_response('projects/editPerson.html', context, context_instance=RequestContext(request))

    context = {'form': form}

    return render_to_response('projects/editPerson.html', context, context_instance=RequestContext(request))


@login_required
def ViewPerson(request):
    template_name = 'projects/editPerson.html'
    form = PersonForm()

    try:
        person = request.user
        person_id = person.id

        context = {'usuario': person}

        return render_to_response(template_name, context, context_instance=RequestContext(request))

    except User.DoesNotExist:

        context = {'form': form}

        return render_to_response(template_name, context, context_instance=RequestContext(request))


@login_required
def CreateProject(request):
    if request.method == 'POST':

        proj = Project()

        proj.user = request.user
        proj.name = request.POST.get('name')
        proj.author = request.POST.get('author')
        proj.description = request.POST.get('description')

        is_valid = validForm(proj)

        if not is_valid:

            msg = 'Voçê deve preencher todos os campos deste formulário'
            context = {'msg': msg}

            return render_to_response('projects/create.html', context, context_instance=RequestContext(request))

        else:

            proj.save()
            msg = 'Projeto salvo com sucesso!'
            context = {'msg': msg}

            return render_to_response('projects/tanks.html', context, context_instance=RequestContext(request))

    else:
        return render_to_response('projects/create.html', context_instance=RequestContext(request))


def ListProjects(request):
    template_name = 'projects/list_projects.html'
    projects = Project.objects.all()
    context = {'list_objects': projects}

    return render(request, template_name, context)


def UpdateProject(request, pk):

    project = ""

    if request.user.is_authenticated():
        project = get_object_or_404(Project, pk=pk)
        context = {'project':project}

        if request.user.pk == project.user.pk:

            if request.method == 'POST':

                project.user = request.user
                project.name = request.POST.get('name')
                project.author = request.POST.get('author')
                project.description = request.POST.get('description')

                is_valid = validForm(project)

                if is_valid:

                    project.save()

                    list = Project.objects.all()

                    context_ = {'list_objects': list}

                    return render_to_response('projects/list_projects.html', context_, context_instance=RequestContext(request))

                else:

                    return render_to_response('projects/update_project.html', context, context_instance=RequestContext(request))

            else:

                return render_to_response('projects/update_project.html', context, context_instance=RequestContext(request))

        else:

            list = Project.objects.all()

            context_ = {'list_objects': list}

            return render_to_response('projects/list_projects.html', context_, context_instance=RequestContext(request))

    else:

        list = Project.objects.all()

        context_ = {'list_objects': list}

        return render_to_response('projects/list_projects.html', context_, context_instance=RequestContext(request))


def RemoveProject(request, pk):
    template_name = 'projects/remove_project.html'
    project = get_object_or_404(Project, pk=pk)

    if request.method == 'POST':
        project.delete()

        return redirect('projects_list')

    return render(request, template_name, {'project': project})


def SearchProject(request):
    template_name = 'busca.html'

    search_name = request.GET.get('search')

    s_name = Project.objects.filter(name__contains=search_name)

    if s_name:
        return redirect('projects_list')

    return render_to_response(template_name, s_name)


def Register_user(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password_one = form.cleaned_data['password_one']
            password_two = form.cleaned_data['password_two']

            new_user = User.objects.create_user(username=user, email=email, password=password_one)
            new_user.save()

            msg = "Cadastro realizado com sucesso!"

            context = {'msg':msg}

            return render_to_response('projects/tanks.html', context, context_instance=RequestContext(request))

        else:
            ctx = {'form': form}
            return render_to_response('projects/register.html', ctx, context_instance=RequestContext(request))

    ctx = {'form': form}

    return render_to_response('projects/register.html', ctx, context_instance=RequestContext(request))


def Login_user(request):
    message = ""

    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user_ = authenticate(username=username, password=password)
                if user_ is not None and user_.is_active:
                    login(request, user_)
                    return HttpResponseRedirect('/')

                else:
                    message = "Usuário e/ou Senha incorreta"

        form = LoginForm()
        message = "Favor preencher dados para efetuar o seu login"
        ctx = {'form': form, 'message': message}

        return render_to_response('projects/login.html', ctx, context_instance=RequestContext(request))


def Logout_user(request):
    logout(request)

    return HttpResponseRedirect('/')


def validForm(p):
    name = p.name
    author = p.author
    description = p.description

    is_valid = True

    if not name or not author or not description:

        is_valid = False

        return is_valid

    else:
        return is_valid








