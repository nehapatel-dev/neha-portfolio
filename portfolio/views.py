from django.shortcuts import render
from .models import Project 
from django.core.mail import send_mail

# Create your views here.


def index(request):
    return render(request, 'portfolio/index.html')
def about(request):
    return render(request, 'portfolio/about.html')   
def skills(request):
    return render(request , 'portfolio/skills.html')  
def project(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/project.html', {
        'projects': projects
    })    
def education(request):
    return render(request, 'portfolio/education.html')   
def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        send_mail(
            subject=f"Portfolio Message from {name}",
            message=f"Email: {email}\n\nMessage:\n{message}",
            from_email="ptl.neha786@gmail.com",
            recipient_list=["ptl.neha786@gmail.com"],
            fail_silently=False
        )

        return render(request, "portfolio/contact.html", {"success": True})

    return render(request, "portfolio/contact.html")
