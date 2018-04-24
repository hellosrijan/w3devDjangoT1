from django.shortcuts import render, redirect
from accounts.form import RegistrationForm, EditProfileForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='SignIn')
def accounts(request):
    return render(request, 'accounts/Profile.html')


def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/MyAccount/SignnIn ')
    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'accounts/SignUp.html', args)


@login_required(login_url='SignIn')
def view_profile(request):
    args = {'user': request.user}
    return render(request, 'accounts/Profile.html', args)


@login_required(login_url='SignIn')
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/MyAccount/Profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/EditProfile.html', args)


@login_required(login_url='SignIn')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/MyAccount/Profile')
        else:
            return redirect('/MyAccount/ChangePassword')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'accounts/ChangePassword.html', args)
