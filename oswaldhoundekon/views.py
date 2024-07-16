from django.shortcuts import render
from django.http import HttpResponse
from projects.models import Project
from django.core.mail import send_mail

def index(request):
    works = Project.objects.all()[:7]
    return render(request, 'index.html', {'works':works, 'range':range(4), 'page_title':'Home'})


def privacy(request):
    context = {'page_title':'Privacy Policy'}
    return render(request, 'privacy.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        company_name = request.POST['company-name']
        email = request.POST['email']
        service = request.POST['service']
        project_details = request.POST['project-detail']
        
        message = "This is a mail from {}, whose company name is {}. They're requesting a {} service. Here is the project details:\n{}".format(name,company_name,service,project_details)
        send_mail(
            service,
            message,
            email,
            ['oswaldhoundekon@gmail.com']
        )
        context = {'page_title':'Contact','server_response':name}
        return render(request, 'contact.html', context)
    else:
        context = {'page_title':'Contact'}
        return render(request, 'contact.html', context)