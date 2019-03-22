from django.shortcuts import render
from django.contrib import messages

from About.models import About
from Work.models import Work
from Contact.form import ContactForm
from Skill.models import MySkill


# Create your views here.
def home_view(request, *args, **kwargs):
    obj = About.objects.all()
    context = {
        'object': obj
    }
    return render(request, "home.html", context)


def work_view(request):
    obj = Work.objects.all()
    context = {
        'object': obj
    }
    return render(request, "work.html", context)


def contact_view(request, *args, **kwargs):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        if form.save():
            messages.success(request, "Thanks for Contacting Me")
            form = ContactForm()
        else:
            messages.error(request, "An error occurred.. Try again")

    context = {
        'form': form
    }
    return render(request, "contact.html", context)


def skill_view(request, *args, **kwargs):
    obj = MySkill.objects.all()
    context = {
        'object': obj
    }
    return render(request, "skill.html", context)