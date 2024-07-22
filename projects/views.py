from unicodedata import category
from django.shortcuts import render
from .models import *


# Create your views here.
def projects(request):
    project_list = Project.objects.all().order_by('?')
    categories_list = Category.objects.all()

    context = {'projects':project_list, 'page_title':'Projects', 'categories':categories_list}
    return render(request, 'projects/projects.html', context)


def project_details(request, slug):
    project = Project.objects.get(slug=slug)
    all_projects = Project.objects.all()
    next_project = None
    previous_project = None
    #defining next and previous projects
    #if this is not he last project in the data set (this is for the next project)
    if not project.id == all_projects[len(all_projects)-1].id:
        next_project = all_projects[list(all_projects).index(project) + 1]
        
    #if this not the first project of the data set
    if not project.id == all_projects[0].id:
        previous_project = all_projects[list(all_projects).index(project) - 1]
    
    
    #get instances of projectImages
    projectImages = ProjectImages.objects.filter(project=project.id).order_by('?')
    #get a of their thumbs
    thumbs = [i.thumb for i in projectImages]
    
    contributors = Contributor.objects.filter(project = project.id)
    #contribs = ', '.join([str(i) for i in Contributor.objects.filter(project = project.id)])
    category = ', '.join([str(a) for a in Category.objects.filter(project = project.id)])
    tags = ', '.join([str(a) for a in Tag.objects.filter(project = project.id)])
    
    #this variable is just to simplify the reder code
    context = {
        'page_title':project.title,
        'project':project,
        'projectImages':thumbs, 
        'contributors':contributors, 
        'categories':category,
        'tags':tags,
    }
    
    if next_project is not None:
        context['next_project'] = next_project
    if previous_project is not None:
        context['previous_project'] = previous_project
    
    return render(request, 'projects/project_details.html', context)