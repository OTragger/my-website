from unicodedata import category
from django.shortcuts import render
from .models import Project, ProjectImages, Contributor, Category 


# Create your views here.
def projects(request):
    project_list = Project.objects.all()
    return render(request, 'projects/projects.html', {'projects':project_list, 'page_title':'Projects'})


def project_details(request, slug):
    project = Project.objects.get(slug=slug)
    
    #get instances of projectImages
    projectImages = ProjectImages.objects.filter(project=project.id)
    #get a of their thumbs
    thumbs = [i.thumb for i in projectImages]
    
    contributors = ', '.join([str(i) for i in Contributor.objects.filter(project = project.id)])
    category = ', '.join([str(a) for a in Category.objects.filter(project = project.id)])
    
    #this variable is just to simplify the reder code
    objectToSend = {'page_title':project.title,'project':project,'projectImages':thumbs, 'contributors':contributors, 'categories':category}
    
    return render(request, 'projects/project_details.html', objectToSend)