from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import User
from .form import UserForm

# Create your views here.
def index(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'user/index.html', context)

def user_add_submition(request):
    if(request.method == "POST"):
        form = UserForm(request.POST)

        print(" name {0}".format(request.POST.get('name')))
        

        if(form.is_valid()):
            form.print_user()

            name_input = request.POST.get('name')
            old_input = request.POST.get('old')
            number_input = request.POST.get('number')
            user_data = User(name=name_input, old=old_input, number=number_input)
            user_data.save()

            return redirect('index')

        else:
            return redirect('user-input')
def user_input(request):
    return render(request, 'user/user_input.html')

def user_edit(request, id):
    user_data = User.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'user/user_edit.html',  {'user': user_data})
    
def user_edit_submition(request, id):
    user_data = User.objects.get(id=id)
    user_data.name = request.POST.get('name')
    user_data.old = request.POST.get('old')
    user_data.number = request.POST.get('number')
    user_data.save()
    return redirect('index')

def user_delete(request, id):
    user_data = User.objects.get(id=id)
    user_data.delete()
    return redirect('index')