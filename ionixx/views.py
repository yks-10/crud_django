from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Todo
from .forms import TodoForm

def index(request):
    context={}
    form=TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form']=form
    return render(request,"ionixx/index.html",context)

def list(request):
    context={}
    context["a"]=Todo.objects.all()
    return render(request, "ionixx/list.html", context)

def detail(request,id):
    context={}
    context["a"]=Todo.objects.get(id=id)
    return render(request, "ionixx/detail.html", context)

def update(request, id):
    context={}
    a= get_object_or_404(Todo, id=id)
    form=TodoForm(request.POST or None, instance=a)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)
    context["form"]=form
    return render(request, "ionixx/update.html", context)


def delete(request, id):
    context={}
    a=get_object_or_404(Todo, id=id)
    if request.method == "POST":
        a.delete()
        return HttpResponseRedirect("")
    return render(request,"ionixx/delete.html",context)

