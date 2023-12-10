from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.decorators import login_required
from .models import ProfileModel
from .forms import SignUpForm,UserUpdateForm,ProfileUpdateForm,UserRoleForm

# Create your views here.
def sign_up(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users-login')
    else:
        form = SignUpForm
    context = {
        'form':form,
    }
    return render(request, 'users/sign_up.html', context)

@login_required
def profile(request):
    if request.method=='POST':
        u_form = UserUpdateForm(request.POST or None, instance = request.user)
        p_form = ProfileUpdateForm(request.POST or None,request.FILES or None,instance=request.user.profilemodel)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('users-profile')
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profilemodel)
    context = {
        'u_form':u_form,
        'p_form':p_form,

    }

    return render (request, 'users/profile.html',context)

@login_required

def manage_users(request):
    users = ProfileModel.objects.all()

    context = {
        'users': users,
    }

    return render(request,'users/list.html',context)
  
@login_required
def manage_users(request):
    users = ProfileModel.objects.all()

    if request.method == 'POST':
        form = UserRoleForm(request.POST)
        if form.is_valid():
            # Process the form data and update user roles
            for user in users:
                user.role = form.cleaned_data['user_role']
                user.save()
            # Redirect to the same page or another page as needed
            return redirect('manage-users')
    else:
        # Initialize the form with the current user roles
        initial_values = {'user_role': [(user.role, user.role) for user in users]}
        form = UserRoleForm(initial=initial_values)
        print(initial_values)

    context = {
        'users': users,
        'form': form,
    }

    return render(request, 'users/list.html', context)